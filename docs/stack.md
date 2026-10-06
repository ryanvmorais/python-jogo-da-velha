# A stack, e por quê

Cada tecnologia que sustenta o Jogo da Velha: o que faz, por que foi
escolhida contra a alternativa, e os conceitos que valem a pena estudar
primeiro se forem novos para você.

Não é exaustivo — o grafo completo de versões do grupo de desenvolvimento está
travado no `uv.lock`. Este doc é o mapa: a *forma* do projeto e o raciocínio
por trás de cada peça.

O projeto é um único programa: um script de terminal, sem dependências de
runtime (só a biblioteca padrão do Python), com um grupo de ferramentas de
qualidade por fora.

```
main.py  ──►  biblioteca padrão do Python (random, os)
```

---

## Linguagem e empacotamento

### Python 3.12+

A única linguagem do projeto. 3.12 é o piso porque é a versão mínima usada nos
outros projetos do Ryan (`site-ryan-morais`, `webvigil`, `pedra-papel-tesoura`)
— manter o mesmo piso evita "funciona num projeto e não no outro" por causa de
sintaxe.

**Por que esta:** o projeto é puramente didático (lógica, matrizes, POO) —
qualquer linguagem serviria, mas Python tem a sintaxe mais direta para quem
está aprendendo esses conceitos por trás de um jogo de terminal.

**Estudar:** classes e `self`, matriz como lista de listas (`tabuleiro[i][j]`),
`random.choice`, type hints modernos (`list[list[str]]`),
`if __name__ == "__main__"`.

### uv

O gerenciador de pacotes e ambientes virtuais do Python (da Astral, o time do
Ruff). Substitui `pip` + `venv` manual. `uv sync` instala o grupo de
desenvolvimento a partir do `uv.lock`; `uv run <comando>` executa dentro do
ambiente sem precisar ativá-lo.

**Por que esta:** o projeto não tem dependência de runtime (só stdlib), mas as
ferramentas de qualidade (ruff, black, mypy, pytest) precisam de um ambiente
isolado e reprodutível. `uv` é uma ordem de magnitude mais rápido que
`pip`/`venv`, usa o `pyproject.toml` padrão (PEP 621) e gera um lockfile real
(`uv.lock`) — o mesmo gerenciador usado nos outros projetos Python do Ryan.

**Estudar:** `uv sync`, `uv run <comando>`, `uv add --dev <pacote>`, `uv lock`,
a diferença entre `[project.dependencies]` (runtime, vazio aqui) e
`[dependency-groups] dev` (ferramentas).

---

## Ferramentas de qualidade

### Ruff

O linter — substitui Flake8 + isort + pyupgrade num binário só, quase
instantâneo. Aqui verifica erros óbvios (`F`), estilo `pycodestyle` (`E`/`W`),
ordena imports (`I`) e sugere sintaxe moderna (`UP`).

**Por que esta:** é o linter padrão em todos os projetos Python do Ryan; um só
comando (`ruff check .`) substitui o que antes precisava de 3-4 ferramentas
separadas.

**Estudar:** `uv run ruff check .`, `uv run ruff check --fix .` (corrige o que
for seguro), a tabela `select` no `pyproject.toml` (cada letra é uma família
de regra).

### Black

O formatador — sem configuração para discutir (mesma filosofia do `gofmt`).
Reescreve o arquivo no estilo canônico do Black; ninguém revisa espaçamento em
code review.

**Por que esta:** padrão de-facto do ecossistema Python; usado sem exceção nos
outros projetos do Ryan.

**Estudar:** `uv run black .` (reformata), `uv run black --check .` (só
verifica, usado no CI).

### Mypy

O verificador de tipos estáticos, em modo `strict`. Lê as anotações de tipo
(`-> None`, `list[list[str]]`) e garante que elas sejam consistentes antes
mesmo de rodar o código.

**Por que esta:** o projeto é pequeno, mas tipar tudo desde o início é a
prática que os outros projetos do Ryan seguem — evita o hábito de "só ligo o
mypy quando o projeto crescer" (nunca liga).

**Estudar:** sintaxe `list[X]` (não `List`), `-> None` explícito em método que
não retorna nada, `uv run mypy`.

### pytest

O executor de testes. `tests/test_main.py` cobre a lógica do jogo
(`verificar_vitoria_ou_empate`, validação de entrada, sorteio da máquina) sem
depender de um terminal real.

**Por que esta:** padrão de-facto de testes em Python; a fixture
`monkeypatch` (nativa do pytest) é o que permite simular `input()` e
`random.choice` sem I/O real — essencial para testar um jogo de terminal.

**Estudar:** `@pytest.fixture`, `@pytest.mark.parametrize` (testar várias
linhas/colunas/diagonais sem repetir código), `monkeypatch.setattr`
(substituir `input`/`random.choice` durante o teste), `capsys` (capturar o
que foi impresso no terminal).

---

## Peças menores

| Peça | Papel |
|---|---|
| `random.choice` (stdlib) | sorteia a posição livre da jogada da máquina |
| `os.system` (stdlib) | limpa o terminal (`cls` no Windows, `clear` no Unix/Mac) |
| `sys.stdout.reconfigure` (stdlib) | força UTF-8 na saída, evitando `UnicodeEncodeError` com stdout redirecionado no Windows |

---

## O que deliberadamente não está na stack

- **Qualquer dependência de runtime** — o jogo inteiro cabe na biblioteca
  padrão; adicionar uma lib externa só para isso seria peso sem ganho
  pedagógico.
- **Um framework de CLI (Typer/Click)** — o menu tem duas perguntas por
  jogada (linha e coluna) e uma de replay; `input()` puro já ensina o
  conceito sem introduzir uma dependência nova.
- **`subprocess`** — a limpeza de tela usa `os.system(comando)` com uma
  string fixa (`"cls"`/`"clear"`, nunca entrada do usuário);
  `subprocess.run(..., shell=True)` faria o mesmo com mais código e é o
  padrão que ferramentas de segurança sinalizam por hábito (mesmo sem risco
  real aqui).
