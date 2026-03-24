![Jogo da Velha em Python - Lógica de Programação e Matrizes](https://github.com/ryanvmorais/python-jogo-da-velha/blob/main/assets/jogo-da-velha-python-logica-programacao.png?raw=true)

# ❌⭕ Jogo da Velha em Python | Exercício de Lógica de Programação

Este repositório contém um **Jogo da Velha (Tic Tac Toe)** desenvolvido em Python, projetado especificamente como um material de estudo para desenvolvedores iniciantes. O foco principal é a aplicação prática de **fundamentos da programação** e manipulação de matrizes no terminal.

### 🎯 Objetivo do Projeto:
Demonstrar a aplicação de **estruturas de repetição**, **estruturas condicionais** e **Programação Orientada a Objetos (POO)** em Python. É um projeto prático perfeito para estudantes que desejam consolidar o raciocínio lógico por trás da construção de sistemas.

---

### 📚 O que você vai aprender com este projeto?
Este exercício foi estruturado para consolidar conceitos essenciais de algoritmos:

*   **Estruturas de Repetição:** Controle de turnos e verificação de vitória (Loops `while` e `for`).
*   **Estruturas Condicionais:** Validação de jogadas e regras do jogo (`if/elif/else`).
*   **Manipulação de Matrizes:** Como gerenciar dados usando índices `[linha][coluna]`.
*   **POO (Orientada a Objetos):** Organização de código modular, limpo e reutilizável.
*   **Interação Multiplataforma com o SO:** Uso do módulo `subprocess` em conjunto com `os.name` para detectar o sistema operacional em tempo real e executar o comando de limpeza de tela correto (`cls` no Windows ou `clear` em sistemas Unix/Mac).

---
### 🧠 Guia de Implementação: A Lógica por trás do Código
Para quem está começando, o maior desafio não é a sintaxe, mas a **montagem do raciocínio**. Confira o passo a passo da construção deste jogo:
1. **Abstração e Modelagem:** Imagine o tabuleiro como uma matriz 3x3. No Python, usamos uma **lista de listas** para representar isso, permitindo acessar cada quadrado através de coordenadas como `tabuleiro[0][1]`.
2. **UX e Fluxo de Jogo:** O jogo funciona em ciclos. O usuário interage via terminal, o sistema valida a jogada e utiliza o módulo `subprocess` para limpar a tela, criando a sensação de um aplicativo dinâmico e organizado.
3. **Arquitetura com POO:** Utilizamos **Programação Orientada a Objetos (POO)** para para organizar o código. A classe `JogoDaVelha` centraliza toda a lógica e armazena o "estado" da partida (quem venceu, de quem é a vez e como está o tabuleiro).
4. **Inicialização:** Todo início (ou reinício) de partida limpa as variáveis de controle e gera um novo tabuleiro preenchido apenas com espaços vazios (`' '`).
5. **Algoritmo de Vitória:** Desenvolvemos uma lógica matemática que varre as **8 possibilidades de vitória**: 3 linhas, 3 colunas e 2 diagonais. Se três símbolos iguais forem detectados em sequência, o jogo identifica o vencedor.
6. **O "Game Loop":** O coração do projeto é um loop `while True`. Ele coordena a orquestra: `desenha o tabuleiro` -> `processa jogada do usuário` -> `verifica vitória` -> `processa jogada aleatória da máquina` -> `verifica vitória` -> `repete`.
7. **Tratamento de Erros:**  Implementamos blocos `try/except` para que o programa não quebre caso o usuário digite algo inesperado (como letras em vez de números), garantindo uma experiência estável.

---

### 🛠️ Tecnologias e Ferramentas:
Para garantir a melhor experiência de aprendizado e a execução correta de todos os recursos (como a limpeza de tela automática), o projeto utiliza as seguintes tecnologias:


| Ferramenta | Descrição | Badge |
| :--- | :--- | :--- |
| **Python 3** | Linguagem principal utilizada no desenvolvimento do algoritmo. | ![Linguagem Python](https://img.shields.io/badge/-Python-3776AB%3Fstyle%3Dflat%26logo%3Dpython?logo=python&logoColor=3776AB&logoSize=flat&color=F0F0F0) |
| **Terminal** | Interface onde o jogo é executado e processa as entradas do usuário. | ![Terminal](https://img.shields.io/badge/Terminal-241F31?style=flat&logo=gnometerminal&logoColor=241F31&color=F0F0F0) |
| **VS Code / PyCharm** | IDEs recomendadas para edição, depuração e refatoração do arquivo `main.py`. | ![PyCharm](https://img.shields.io/badge/PyCharm-pycharm?style=flat&logo=pycharm&logoColor=000000&color=F0F0F0) |

---

### ✅ Requisitos Mínimos:

Para garantir que o jogo funcione corretamente, certifique-se de ter os seguintes itens instalados:

- **Python 3.10 ou superior:** O código utiliza recursos modernos da linguagem.
- **VS Code / PyCharm (Opcional):** Recomendado para abrir e editar o arquivo `main.py` com suporte total a refatoração e depuração.

> **Dica:** Para verificar sua versão do Python, digite `python --version` no seu terminal.

---

### ⚙️ Como Executar o Projeto:
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/ryanvmorais/python-jogo-da-velha.git
   ``` 
2. **Execute o script:**
- Navegue até a **pasta do projeto** e utilize o comando abaixo no seu terminal (CMD, PowerShell ou Terminal do VS Code/PyCharm):
   ```bash
   python main.py
   ```
> **Nota:** O jogo detectará automaticamente se você está no `Windows`, `Linux` ou `macOS` para gerenciar a limpeza da tela.
---

### 📋 Atividade para praticar:

Para exercitar o que aprendeu, tente modificar o código e implementar estas novas funcionalidades:

1. **🏆 Placar:** Crie variáveis para armazenar e exibir um contador de vitórias acumuladas.
2. **🤖 Modo Single Player:** Tente fazer a máquina bloquear suas jogadas em vez de apenas jogar aleatoriamente.
3. **🎨 Cores no Terminal:** Utilize a biblioteca `colorama` para colorir o **"X"** de vermelho e o **"O"** de azul.

---

### 💡 Ficou com alguma dúvida ou tem sugestões?

Aprender algo novo tem seus desafios, mas estou aqui para caminharmos juntos! Se você encontrou algum erro, teve dificuldade em rodar o jogo ou pensou em uma funcionalidade incrível para adicionar:

*   **Abra uma [Issue](https://github.com/ryanvmorais/python-jogo-da-velha/issues):** Clique no link e descreva sua dúvida ou sugestão. É a melhor forma de trocarmos conhecimento e ajudarmos outras pessoas que tenham a mesma dúvida!
*   **Me mande um E-mail:** Se preferir algo mais privado, pode me escrever em [**contato@ryanmorais.com.br**](mailto:contato@ryanmorais.com.br).

Ficarei muito feliz em ver seu progresso e receber seu feedback para melhorar cada vez mais nossos materiais de estudo! 🤝

---

### ⚖️ Licença

Este projeto está sob a **Licença MIT**. Isso significa que você pode usar, copiar e modificar o código à vontade, inclusive para seus próprios projetos, desde que mantenha os créditos originais. Para mais detalhes, consulte o arquivo [LICENSE](LICENSE).
