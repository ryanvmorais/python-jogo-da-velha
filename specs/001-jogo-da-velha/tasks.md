---
feature: Jogo da Velha (Tic Tac Toe) via terminal
status: concluído
data: 2026-09-11
relacionado:
  - 001-jogo-da-velha/requirements.md
  - 001-jogo-da-velha/design.md
origem: engenharia reversa
---

# 001 — Jogo da Velha — Tasks

## Etapa 0 — Jogo original (histórico, pré-modernização)

- [x] `main.py`: classe `JogoDaVelha` com tabuleiro 3x3 e status final.
      — RF-01, RF-02, RF-03
- [x] `main.py`: loop principal com pergunta de replay. — RF-05
- [x] `main.py`: limpeza de tela multiplataforma (`cls`/`clear` via
      `subprocess.run(..., shell=True)`). — RF-06
- [x] `iniciar_jogo.bat` / `iniciar_jogo.sh`: scripts de atalho por SO
      (já apontavam corretamente para `main.py`).
- [x] Portão de qualidade. — verificação manual (sem suíte automatizada
      nesta etapa).

## Etapa 1 — Modernização (uv, tipos, testes)

- [x] `main.py`: adiciona type hints em toda assinatura (`-> None` explícito,
      `list[list[str]]`) e `from __future__ import annotations`.
- [x] `main.py`: extrai `limpar_tela` como método próprio (antes embutido em
      `exibir_tabuleiro`). — ADR-1
- [x] `main.py`: troca `subprocess.run(comando, shell=True)` por
      `os.system(comando)`. — ADR-1
- [x] `main.py`: extrai o loop do `if __name__ == "__main__"` para uma função
      `main() -> None`. — ADR-2
- [x] `main.py`: reescreve `exibir_tabuleiro` com um loop sobre as linhas do
      tabuleiro, em vez de 5 `print` com índices literais (necessário após
      os type hints empurrarem 3 linhas para além do limite de 88 colunas do
      Black). — ADR-3
- [x] `main.py`: reconfigura `sys.stdout` para UTF-8 no import, corrigindo um
      `UnicodeEncodeError` real ao rodar com stdout redirecionado no Windows
      (achado ao fazer o smoke test manual desta modernização, no `⚠️` da
      mensagem de entrada inválida). — ADR-4
- [x] `pyproject.toml`: cria manifesto gerenciado por `uv` — sem dependência
      de runtime, grupo `dev` com `ruff`, `black`, `mypy`, `pytest`. — RNF-01
- [x] Remove `requirements.txt` (substituído pelo `pyproject.toml` +
      `uv.lock`).
- [x] `tests/test_main.py`: suíte pytest cobrindo RF-01 a RF-04 (20 casos,
      parametrizados onde fazia sentido). — RF-01, RF-02, RF-03, RF-04
- [x] `iniciar_jogo.bat` / `iniciar_jogo.sh`: passa a preferir
      `uv run main.py`, com fallback para `python`/`python3` puro.
- [x] Portão de qualidade. — `ruff check .`, `black --check .`, `mypy` e
      `pytest` (20 passed) verdes.

## Etapa 2 — Documentação e CI

- [x] `docs/stack.md`: mapa da stack (Python, uv, ruff, black, mypy, pytest).
- [x] `specs/001-jogo-da-velha/`: esta spec, por engenharia reversa.
- [x] `.github/dependabot.yml`: atualização semanal de `uv` +
      `github-actions`.
- [x] `.github/workflows/ci.yml`: job `qualidade` (`ruff` → `black --check`
      → `mypy` → `pytest`) em Python 3.12 e 3.13.
- [x] `CLAUDE.md`: orientação de projeto para sessões futuras.
- [x] `README.md` / `CONTRIBUTING.md`: atualizados para `uv` (em vez de
      `pip`) e para a suíte de testes.
- [x] `.gitignore`: adiciona os caches de `ruff`/`mypy`/`pytest`.
- [x] Portão de qualidade. — `ruff check .`, `black --check .`, `mypy` e
      `pytest` (20 passed) verdes; CI local equivalente ao workflow.
