"""Testes para main.py.

Estratégia de isolamento: `limpar_tela` é sempre mockada (chama `os.system`,
efeito de terminal irrelevante para a lógica testada). `input()` é mockado via
`monkeypatch.setattr("builtins.input", ...)` para simular a digitação do
usuário sem bloquear a suíte. `random.choice` é mockado quando o teste precisa
de uma jogada determinística da máquina.
"""

from __future__ import annotations

import random
from collections.abc import Iterator

import pytest

from main import JogoDaVelha

pytestmark = pytest.mark.usefixtures("_sem_tela")


@pytest.fixture
def _sem_tela(monkeypatch: pytest.MonkeyPatch) -> None:
    """Substitui a limpeza de tela por um no-op em toda a suíte."""
    monkeypatch.setattr(JogoDaVelha, "limpar_tela", lambda self: None)


@pytest.fixture
def jogo() -> JogoDaVelha:
    """Retorna:
    JogoDaVelha: Instância nova, com o tabuleiro vazio.
    """
    return JogoDaVelha()


def _digitar(monkeypatch: pytest.MonkeyPatch, *respostas: str) -> Iterator[str]:
    """Simula uma sequência de respostas do usuário no `input()`.

    Args:
        monkeypatch (pytest.MonkeyPatch): Fixture de monkeypatch do teste.
        *respostas (str): Respostas a devolver, uma por chamada de `input()`.

    Returns:
        Iterator[str]: O iterador usado internamente (raramente precisa ser
            inspecionado pelo teste).
    """
    valores = iter(respostas)
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(valores))
    return valores


def _tabuleiro_vazio() -> list[list[str]]:
    """Retorna:
    list[list[str]]: Matriz 3x3 nova, preenchida só com espaços.
    """
    return [[" " for _ in range(3)] for _ in range(3)]


# ---------------------------------------------------------------------------
# __init__ / reiniciar_jogo
# ---------------------------------------------------------------------------


def test_init_comeca_com_tabuleiro_vazio(jogo: JogoDaVelha) -> None:
    assert jogo.tabuleiro == _tabuleiro_vazio()
    assert jogo.status_final == ""


def test_reiniciar_jogo_zera_tabuleiro_e_status(jogo: JogoDaVelha) -> None:
    jogo.tabuleiro[0][0] = "X"
    jogo.status_final = "X"

    jogo.reiniciar_jogo()

    assert jogo.tabuleiro == _tabuleiro_vazio()
    assert jogo.status_final == ""


# ---------------------------------------------------------------------------
# verificar_vitoria_ou_empate
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("linha", [0, 1, 2])
def test_verificar_vitoria_detecta_linha_completa(
    jogo: JogoDaVelha, linha: int
) -> None:
    jogo.tabuleiro[linha] = ["X", "X", "X"]

    jogo.verificar_vitoria_ou_empate()

    assert jogo.status_final == "X"


@pytest.mark.parametrize("coluna", [0, 1, 2])
def test_verificar_vitoria_detecta_coluna_completa(
    jogo: JogoDaVelha, coluna: int
) -> None:
    for linha in range(3):
        jogo.tabuleiro[linha][coluna] = "O"

    jogo.verificar_vitoria_ou_empate()

    assert jogo.status_final == "O"


def test_verificar_vitoria_detecta_diagonal_principal(jogo: JogoDaVelha) -> None:
    jogo.tabuleiro[0][0] = jogo.tabuleiro[1][1] = jogo.tabuleiro[2][2] = "X"

    jogo.verificar_vitoria_ou_empate()

    assert jogo.status_final == "X"


def test_verificar_vitoria_detecta_diagonal_secundaria(jogo: JogoDaVelha) -> None:
    jogo.tabuleiro[0][2] = jogo.tabuleiro[1][1] = jogo.tabuleiro[2][0] = "O"

    jogo.verificar_vitoria_ou_empate()

    assert jogo.status_final == "O"


def test_verificar_vitoria_tabuleiro_vazio_nao_declara_vencedor(
    jogo: JogoDaVelha,
) -> None:
    jogo.verificar_vitoria_ou_empate()

    assert jogo.status_final == ""


def test_verificar_vitoria_tabuleiro_cheio_sem_vencedor_e_empate(
    jogo: JogoDaVelha,
) -> None:
    jogo.tabuleiro = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"],
    ]

    jogo.verificar_vitoria_ou_empate()

    assert jogo.status_final == "Empate"


# ---------------------------------------------------------------------------
# jogada_do_usuario
# ---------------------------------------------------------------------------


def test_jogada_do_usuario_aceita_posicao_livre(
    jogo: JogoDaVelha, monkeypatch: pytest.MonkeyPatch
) -> None:
    _digitar(monkeypatch, "1", "1")
    jogo.jogada_do_usuario()
    assert jogo.tabuleiro[1][1] == "X"


def test_jogada_do_usuario_repete_apos_coordenada_fora_do_limite(
    jogo: JogoDaVelha, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Coordenada fora de 0-2 não deve travar: o loop pede de novo até validar."""
    _digitar(monkeypatch, "5", "0", "0", "0")
    jogo.jogada_do_usuario()
    assert jogo.tabuleiro[0][0] == "X"


def test_jogada_do_usuario_repete_apos_posicao_ocupada(
    jogo: JogoDaVelha, monkeypatch: pytest.MonkeyPatch
) -> None:
    jogo.tabuleiro[0][0] = "O"
    _digitar(monkeypatch, "0", "0", "1", "2")
    jogo.jogada_do_usuario()
    assert jogo.tabuleiro[1][2] == "X"
    assert jogo.tabuleiro[0][0] == "O"


def test_jogada_do_usuario_repete_apos_entrada_nao_numerica(
    jogo: JogoDaVelha, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Letra digitada no lugar do número não deve travar (ValueError tratado)."""
    _digitar(monkeypatch, "abc", "2", "2", "2")
    jogo.jogada_do_usuario()
    assert jogo.tabuleiro[2][2] == "X"


# ---------------------------------------------------------------------------
# jogada_da_maquina
# ---------------------------------------------------------------------------


def test_jogada_da_maquina_ocupa_posicao_livre_sorteada(
    jogo: JogoDaVelha, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(random, "choice", lambda _posicoes: (1, 1))
    jogo.jogada_da_maquina()
    assert jogo.tabuleiro[1][1] == "O"


def test_jogada_da_maquina_nao_joga_se_ja_houver_vencedor(jogo: JogoDaVelha) -> None:
    jogo.status_final = "X"

    jogo.jogada_da_maquina()

    assert jogo.tabuleiro == _tabuleiro_vazio()


def test_jogada_da_maquina_nao_joga_com_tabuleiro_cheio(jogo: JogoDaVelha) -> None:
    jogo.tabuleiro = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
    tabuleiro_antes = [linha.copy() for linha in jogo.tabuleiro]

    jogo.jogada_da_maquina()

    assert jogo.tabuleiro == tabuleiro_antes


# ---------------------------------------------------------------------------
# exibir_tabuleiro
# ---------------------------------------------------------------------------


def test_exibir_tabuleiro_mostra_as_jogadas_atuais(
    jogo: JogoDaVelha, capsys: pytest.CaptureFixture[str]
) -> None:
    jogo.tabuleiro[0][0] = "X"
    jogo.tabuleiro[1][1] = "O"

    jogo.exibir_tabuleiro()

    saida = capsys.readouterr().out
    assert "X" in saida
    assert "O" in saida
