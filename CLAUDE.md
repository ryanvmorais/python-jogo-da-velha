# CLAUDE.md

Este arquivo orienta o Claude Code (claude.ai/code) ao trabalhar neste
repositório.

## Visão geral do projeto

Jogo da Velha (Tic Tac Toe) em Python, via terminal — material de estudo
para prática de lógica de programação, matrizes e Orientação a Objetos. Um
único arquivo (`main.py`), sem dependência de runtime (só a biblioteca
padrão). Repositório pessoal/educacional, público no GitHub.

## Comandos comuns

```bash
# Sincronizar o ambiente (.venv) a partir do uv.lock
uv sync

# Rodar o jogo
uv run main.py

# Rodar a suíte de testes
uv run pytest

# Rodar um teste específico
uv run pytest tests/test_main.py::test_verificar_vitoria_detecta_linha_completa -v

# Lint, formatação e tipos (nesta ordem)
uv run ruff check .          # lint (substitui flake8 + isort)
uv run ruff check --fix .    # corrige automaticamente o que for seguro
uv run black .               # formatação
uv run mypy                  # tipos (arquivos em [tool.mypy] files)

# Gerenciar dependências de desenvolvimento (não há dependências de runtime)
uv add --dev <pacote>
uv remove --dev <pacote>
uv lock --upgrade-package <pacote>
```

## Arquitetura

```
main.py              # classe JogoDaVelha + função main() (ponto de entrada)
tests/test_main.py   # suíte pytest (20 casos)
docs/stack.md         # o que cada peça da stack faz e por quê
specs/                # spec-driven development (ver specs/README.md)
  001-jogo-da-velha/
iniciar_jogo.bat      # atalho Windows: uv run main.py (fallback: python main.py)
iniciar_jogo.sh       # atalho Linux/macOS: uv run main.py (fallback: python3 main.py)
pyproject.toml        # gerenciado por uv — sem deps de runtime, grupo dev com
                       # ruff/black/mypy/pytest
uv.lock               # lock do grupo dev — nunca editar à mão
.github/
  workflows/ci.yml    # ruff -> black --check -> mypy -> pytest, em push/PR
  dependabot.yml      # PRs semanais de atualização (uv + github-actions)
```

### `JogoDaVelha` (em `main.py`)

Guarda o estado de uma partida: o tabuleiro (`tabuleiro: list[list[str]]`,
matriz 3x3) e o resultado (`status_final`). Um método por responsabilidade —
`limpar_tela`, `exibir_tabuleiro`, `reiniciar_jogo`,
`verificar_vitoria_ou_empate` (varre linhas/colunas/diagonais),
`jogada_do_usuario` (lê e valida `input()`), `jogada_da_maquina`
(`random.choice` entre as posições livres). `main()` orquestra o loop de
partidas e o prompt de replay. Detalhamento completo (RF-NN, ADRs) em
[`specs/001-jogo-da-velha/`](specs/001-jogo-da-velha/requirements.md).

## Convenções

- **Idioma do código:** português — projeto pessoal/educacional (regra do
  `CLAUDE.md` global: "Pessoal solo → Português"). Exceções: keywords da
  linguagem, termos técnicos universais (`int`, `str`, `bool`).
- **Estilo de construção de arquivos** (docstrings, type hints, comentários,
  réguas de seção): ver a skill `/estilo-arquivos` — não repetido aqui.

## Qualidade e automação

Sequência do portão, sempre nesta ordem: `ruff check .` → `black --check .`
→ `mypy` → `pytest`. O `.github/workflows/ci.yml` roda exatamente essa
sequência (Python 3.12 e 3.13) em todo push na `main` e em todo PR — um
check verde no PR significa o mesmo que um clone limpo passando.

Sem hooks de `.claude/` neste projeto (repositório pequeno demais para
justificar automação por evento); rode o portão manualmente antes de
commitar.

## Spec-driven development

Specs em `specs/NNN-nome/` (`requirements.md` → `design.md` → `tasks.md`),
conduzidas pela skill `/spec`. A spec `001-jogo-da-velha` foi escrita por
**engenharia reversa** (o jogo já estava pronto) e é o padrão-ouro de
formato para specs futuras neste repositório — ver
[`specs/README.md`](specs/README.md).

Ao fim de cada sessão: `/atualizar-docs` e depois `/fechar-sessao` (agrupa
as mudanças, commita em Conventional Commits numa branch, dá push, abre/
atualiza o PR — para antes do merge).

## Gestão de dependências (uv)

O projeto **não tem dependência de runtime** — só a biblioteca padrão do
Python. O `uv` gerencia apenas o grupo `dev` (`ruff`, `black`, `mypy`,
`pytest`), travado em `uv.lock`. Commite `pyproject.toml` **e** `uv.lock`
juntos; nunca edite o lock à mão.

> **Cuidado:** `iniciar_jogo.bat`/`.sh` preferem `uv run main.py`, mas caem
> para `python`/`python3 main.py` puro se o `uv` não estiver instalado — é
> assim que alguém sem `uv` (o público educacional do README) ainda consegue
> rodar o jogo.
