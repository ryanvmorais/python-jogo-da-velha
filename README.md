![Jogo da Velha em Python: captura real do terminal com uma partida vencida por X](assets/jogo-da-velha-python-terminal.svg)

# ⭕ Jogo da Velha em Python | Exercício de Lógica de Programação

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![deps](https://img.shields.io/badge/deps-uv-DE5FE9)
[![CI](https://github.com/ryanvmorais/python-jogo-da-velha/actions/workflows/ci.yml/badge.svg)](https://github.com/ryanvmorais/python-jogo-da-velha/actions/workflows/ci.yml)
![Lint](https://img.shields.io/badge/lint-ruff-261230)
![Format](https://img.shields.io/badge/style-black-000000)
![Types](https://img.shields.io/badge/types-mypy%20strict-2A6DB2)
![License](https://img.shields.io/badge/license-MIT-green)

Este repositório contém um **Jogo da Velha (Tic Tac Toe) em Python**, projetado como material de estudo para desenvolvedores iniciantes. O foco principal é a aplicação prática de **fundamentos da programação** e manipulação de matrizes no terminal.

### 🎯 Objetivo do Projeto:

Demonstrar a aplicação de **estruturas de repetição**, **estruturas condicionais** e **Programação Orientada a Objetos (POO)** em Python. É um projeto prático perfeito para estudantes que desejam consolidar o raciocínio lógico por trás da construção de sistemas.

---

### 📚 O que você vai aprender com este projeto?

Este exercício foi estruturado para consolidar conceitos essenciais de algoritmos:

- **Estruturas de Repetição:** controle de turnos e verificação de vitória (loops `while` e `for`).
- **Estruturas Condicionais:** validação de jogadas e regras do jogo (`if/elif/else`).
- **Manipulação de Matrizes:** como gerenciar dados usando índices `[linha][coluna]`.
- **POO (Orientada a Objetos):** organização de código modular, limpo e reutilizável.
- **Interação Multiplataforma com o SO:** uso do módulo `os` (`os.system` em conjunto com `os.name`) para detectar o sistema operacional em tempo real e executar o comando de limpeza de tela correto (`cls` no Windows ou `clear` em sistemas Unix/Mac).

---

### 🧠 Guia de Implementação (A Lógica por trás do Código):

Para quem está começando, o maior desafio não é a sintaxe, mas a **montagem do raciocínio**. Confira o passo a passo da construção deste jogo:

1. **Abstração e Modelagem:** imagine o tabuleiro como uma matriz 3x3. No Python, usamos uma **lista de listas** para representar isso, permitindo acessar cada quadrado através de coordenadas como `tabuleiro[0][1]`.
2. **UX e Fluxo de Jogo:** o jogo funciona em ciclos. O usuário interage via terminal, o sistema valida a jogada e utiliza `os.system` para limpar a tela, criando a sensação de um aplicativo dinâmico e organizado.
3. **Arquitetura com POO:** utilizamos **Programação Orientada a Objetos (POO)** para organizar o código. A classe `JogoDaVelha` centraliza toda a lógica e armazena o "estado" da partida (quem venceu, de quem é a vez e como está o tabuleiro).
4. **Inicialização:** todo início (ou reinício) de partida limpa as variáveis de controle e gera um novo tabuleiro preenchido apenas com espaços vazios (`' '`).
5. **Algoritmo de Vitória:** desenvolvemos uma lógica matemática que varre as **8 possibilidades de vitória**: 3 linhas, 3 colunas e 2 diagonais. Se três símbolos iguais forem detectados em sequência, o jogo identifica o vencedor.
6. **O "Game Loop":** o coração do projeto é a função `main()`. Ela coordena a orquestra: `desenha o tabuleiro` -> `processa jogada do usuário` -> `verifica vitória` -> `processa jogada aleatória da máquina` -> `verifica vitória` -> `repete`.
7. **Tratamento de Erros:** implementamos blocos `try/except` para que o programa não quebre caso o usuário digite algo inesperado (como letras em vez de números), garantindo uma experiência estável.

---

### 🛠️ Tecnologias e Ferramentas:

Para garantir a melhor experiência de aprendizado, o projeto utiliza as seguintes tecnologias:

| Ferramenta | Descrição |
| :--- | :--- |
| **Python 3.12+** | Linguagem principal do projeto. O jogo usa só a biblioteca padrão, sem dependências externas. |
| **uv** | Gerenciador de dependências e ambientes virtuais: cria o ambiente e roda o jogo com um único comando. |
| **Terminal** | Interface onde o jogo roda e recebe as jogadas do usuário (CMD, PowerShell ou o terminal do VS Code/PyCharm). |

As ferramentas de qualidade (Ruff, Black, Mypy e Pytest) estão em [Qualidade e testes](#qualidade-e-testes). Para o porquê de cada escolha, veja [docs/stack.md](docs/stack.md).

---

### ⚙️ Como rodar o projeto localmente:

**Pré-requisitos:** [Python 3.12+](https://www.python.org/downloads/) e [uv](https://docs.astral.sh/uv/getting-started/installation/). Para conferir, rode `python --version` e `uv --version`.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/ryanvmorais/python-jogo-da-velha.git
    cd python-jogo-da-velha
    ```
2.  **Execute o jogo:** no terminal (CMD, PowerShell ou o do VS Code/PyCharm), dentro da pasta do projeto. O `uv` cria o ambiente virtual sozinho na primeira execução.
    ```bash
    uv run main.py
    ```
3.  **Prefere dois cliques? Use o atalho:** no Windows, abra o `iniciar_jogo.bat`; no Linux/macOS, execute o `iniciar_jogo.sh` no terminal. Os scripts detectam se você tem `uv` (preferido) ou `python`/`python3` instalado antes de iniciar a partida.

> ⚠️ **Nota:** sem o `uv`, `python main.py` funciona igual, porque o jogo não tem nenhuma dependência externa. O jogo também detecta se você está no Windows, Linux ou macOS para limpar a tela do jeito certo.

---

### Qualidade e testes

O projeto tem uma suíte de testes automatizados (`pytest`) e um portão de qualidade que roda no CI a cada push e a cada PR:

```bash
uv sync                 # instala as dependências de desenvolvimento
uv run ruff check .     # lint + ordem de imports
uv run black --check .  # formatação
uv run mypy             # checagem de tipos
uv run pytest           # testes
```

Para o mapa de cada tecnologia da stack (o que é, por que foi escolhida, o que estudar), veja [docs/stack.md](docs/stack.md). Para o comportamento esperado do jogo e o histórico de decisões, veja [specs/](specs/). Para o detalhamento de arquitetura e convenções, veja [CLAUDE.md](CLAUDE.md).

---

### 📋 Atividades para praticar (Desafios de Evolução):

Para exercitar o que aprendeu, tente modificar o código e implementar estas novas funcionalidades:

1. **🏆 Placar Acumulado:** crie um contador que não zere ao reiniciar uma partida. Implemente variáveis de controle (ex.: `vitorias_x` e `vitorias_o`) que persistam enquanto o programa estiver aberto: toda vez que um vencedor for detectado, atualize o placar e exiba-o no próximo turno.
   - **O Aprendizado:** diferenciar variáveis que controlam a **rodada** das que controlam o **histórico do jogador**, mantendo dados consistentes em aplicações com vários ciclos de execução.
2. **🤖 Modo Single Player:** faça a máquina bloquear suas jogadas em vez de apenas jogar aleatoriamente.
   - **O Aprendizado:** transformar uma regra de estratégia ("se o adversário está para ganhar, bloqueie") em condições sobre as 8 linhas de vitória que você já varre no código.
3. **🎨 Cores no Terminal:** use a biblioteca `colorama` para colorir o **"X"** de vermelho e o **"O"** de azul.
   - **O Aprendizado:** instalar uma dependência externa com `uv add` e usá-la sem quebrar o resto do programa.

---

### 🧭 Continue praticando:

Este projeto faz parte de uma trilha de exercícios de lógica de programação em Python. Depois deste, experimente:

- **[Jogo da Cobrinha em Python](https://github.com/ryanvmorais/python-jogo-da-cobrinha):** listas dinâmicas e game loop com `curses`.
- **[Portfólio Dinâmico com Django](https://github.com/ryanvmorais/django-fullstack-portfolio):** o primeiro passo fora do terminal, com segurança avançada e otimização de consultas.

Veja todos os projetos e vídeos do canal em [aprenda-com-ryan-morais](https://github.com/ryanvmorais/aprenda-com-ryan-morais).

---

### 💡 Ficou com alguma dúvida ou tem sugestões?

Aprender algo novo tem seus desafios, mas estou aqui para caminharmos juntos! Se você encontrou algum erro, teve dificuldade em rodar o jogo ou pensou numa melhoria que tornaria este material ainda mais didático:

- **Abra uma [Issue](https://github.com/ryanvmorais/python-jogo-da-velha/issues):** descreva sua dúvida ou sugestão. É a melhor forma de trocarmos conhecimento e ajudarmos outras pessoas que tenham a mesma dúvida.
- **Contribua com código:** quer propor uma melhoria? Veja o passo a passo no [CONTRIBUTING.md](CONTRIBUTING.md).
- **Me mande um e-mail:** se preferir algo mais privado, escreva para [**contato@ryanmorais.com.br**](mailto:contato@ryanmorais.com.br).

Ficarei muito feliz em ver seu progresso e receber seu feedback para melhorar cada vez mais nossos materiais de estudo! 🤝

---

### ⚖️ Licença

Este projeto está sob a **Licença MIT**. Isso significa que você pode usar, copiar e modificar o código à vontade, inclusive nos seus projetos. Para mais detalhes, consulte o arquivo [LICENSE](LICENSE).
