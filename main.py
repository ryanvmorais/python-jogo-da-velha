"""Jogo da Velha (Tic Tac Toe) via terminal — projeto educacional de POO.

Material de estudo para prática de lógica de programação, matrizes e
Orientação a Objetos em Python puro (sem dependências externas).

ESTRUTURA DO CÓDIGO (BASEADA EM CLASSE):
1. INICIALIZAÇÃO (__init__): Onde o tabuleiro 'limpo' é criado.
2. INTERFACE (exibir_tabuleiro): Como o jogo aparece no terminal (limpeza de
   tela e grid).
3. REGRAS DE VITÓRIA (verificar_vitoria_ou_empate): A lógica matemática que
   analisa linhas, colunas e diagonais.
4. AGENTES (usuário vs máquina): As funções que gerenciam as jogadas de cada
   um.
5. LOOP PRINCIPAL (main): O controle da partida e a opção de jogar novamente
   (Replay).
"""

from __future__ import annotations

import os
import random
import sys

# No Windows, stdout sem console UTF-8 (saída redirecionada/pipe, alguns
# executores de CI) cai para cp1252 e quebra os emojis abaixo com
# UnicodeEncodeError; reconfigurar para UTF-8 evita o crash em qualquer ambiente.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


class JogoDaVelha:
    """Motor do jogo: guarda o tabuleiro 3x3 e o status da partida."""

    def __init__(self) -> None:
        self.reiniciar_jogo()

    def limpar_tela(self) -> None:
        """Limpa o terminal, detectando o sistema operacional automaticamente."""
        # 'nt' é o identificador interno para Windows.
        comando = "cls" if os.name == "nt" else "clear"
        os.system(comando)

    def exibir_tabuleiro(self) -> None:
        """Redesenha a tela: limpa o console e imprime o grid 3x3 atual."""
        self.limpar_tela()

        print()
        for i, linha in enumerate(self.tabuleiro):
            print(f" {linha[0]} | {linha[1]} | {linha[2]}")
            if i < 2:
                print("-----------")
        print()

    def reiniciar_jogo(self) -> None:
        """Zera o tabuleiro (matriz 3x3 de espaços vazios) e o status final."""
        self.tabuleiro: list[list[str]] = [[" " for _ in range(3)] for _ in range(3)]
        self.status_final: str = ""  # Pode ser 'X', 'O' ou 'Empate'

    def verificar_vitoria_ou_empate(self) -> None:
        """Testa as condições de vitória (linhas, colunas, diagonais) e empate."""
        for jogador in ["X", "O"]:
            # Verifica Linhas e Colunas
            for i in range(3):
                if all(self.tabuleiro[i][j] == jogador for j in range(3)) or all(
                    self.tabuleiro[j][i] == jogador for j in range(3)
                ):
                    self.status_final = jogador
                    return

            # Verifica Diagonais
            if (
                self.tabuleiro[0][0]
                == self.tabuleiro[1][1]
                == self.tabuleiro[2][2]
                == jogador
            ) or (
                self.tabuleiro[0][2]
                == self.tabuleiro[1][1]
                == self.tabuleiro[2][0]
                == jogador
            ):
                self.status_final = jogador
                return

        # Verifica se não há mais espaços vazios (Empate)
        if not any(" " in linha for linha in self.tabuleiro):
            self.status_final = "Empate"

    def jogada_do_usuario(self) -> None:
        """Lê a jogada do usuário pelo teclado, validando até receber uma
        posição livre dentro do tabuleiro."""
        while True:
            try:
                print("Sua vez (X)!")
                linha = int(input("Digite a linha (0, 1 ou 2): "))
                coluna = int(input("Digite a coluna (0, 1 ou 2): "))

                if linha in range(3) and coluna in range(3):
                    if self.tabuleiro[linha][coluna] == " ":
                        self.tabuleiro[linha][coluna] = "X"
                        break
                    print("❌ Essa posição já está ocupada! Tente outra.")
                else:
                    print("⚠️ Coordenada fora do limite! Escolha entre 0 e 2.")
            except ValueError:
                print("⚠️ Entrada inválida! Digite apenas números inteiros.")

    def jogada_da_maquina(self) -> None:
        """Sorteia uma posição livre no tabuleiro para a jogada da máquina."""
        # A máquina só joga se o usuário ainda não tiver vencido
        if self.status_final != "":
            return

        # Identifica todas as posições livres no tabuleiro
        posicoes_livres = [
            (linha, coluna)
            for linha in range(3)
            for coluna in range(3)
            if self.tabuleiro[linha][coluna] == " "
        ]

        if posicoes_livres:
            linha, coluna = random.choice(posicoes_livres)
            self.tabuleiro[linha][coluna] = "O"


def main() -> None:
    """Roda o loop principal: joga partidas até o usuário decidir encerrar."""
    jogo = JogoDaVelha()

    while True:
        # Loop principal da partida ativa
        while jogo.status_final == "":
            jogo.exibir_tabuleiro()
            jogo.jogada_do_usuario()
            jogo.verificar_vitoria_ou_empate()

            if jogo.status_final == "":
                jogo.jogada_da_maquina()
                jogo.verificar_vitoria_ou_empate()

        # Tela de encerramento da partida
        jogo.exibir_tabuleiro()
        if jogo.status_final == "Empate":
            print("⚖️ Deu Velha! O jogo terminou empatado.")
        else:
            print(f"🎉 Fim de jogo! O vencedor foi: {jogo.status_final}")

        # Opção de Replay
        pergunta = input("\nDeseja jogar novamente? (s/n): ").lower()
        if pergunta == "s":
            jogo.reiniciar_jogo()
        else:
            print("Até a próxima! 👋")
            break


if __name__ == "__main__":
    main()
