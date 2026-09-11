---
feature: Jogo da Velha (Tic Tac Toe) via terminal
status: concluído
data: 2026-09-11
relacionado: []
origem: engenharia reversa
---

# 001 — Jogo da Velha

## Contexto e problema

Este repositório é material de estudo: um jogo de terminal que exercita
lógica de programação, manipulação de matrizes (lista de listas) e
Orientação a Objetos, sem depender de nada além da biblioteca padrão do
Python. O jogo já existe e funciona (`main.py`); esta spec documenta
retroativamente o comportamento implementado, para servir de referência
formal e de modelo para futuras mudanças.

## Objetivos

- Jogar partidas de velha (usuário X vs. máquina O) num tabuleiro 3x3 no
  terminal.
- Detectar vitória (linha, coluna ou diagonal) ou empate a cada jogada.
- Validar toda entrada do usuário sem travar o programa.
- Funcionar em Windows, Linux e macOS sem alteração de código.

## Não objetivos

- Modo multiplayer (dois jogadores humanos).
- Placar acumulado entre partidas (proposto como exercício no README, não
  implementado).
- Máquina com estratégia (bloquear o usuário) — a jogada é aleatória entre as
  posições livres.
- Interface gráfica ou web.

## Personas

- **Aprendiz de Python**: quer ler o código e entender como uma classe,
  `self`, uma matriz 3x3 (lista de listas) e um loop de jogo se encaixam.
- **Jogador casual**: só quer abrir o jogo (com duplo clique ou um comando) e
  jogar algumas partidas no terminal.

## Requisitos funcionais

### RF-01 — Escolher uma posição por linha e coluna

- **Given** o tabuleiro está visível e é a vez do usuário (X)
  **When** o usuário digita uma linha e uma coluna entre 0 e 2 apontando
  para uma posição vazia
  **Then** a posição recebe "X" e o jogo segue para a checagem de vitória.
- **Given** o usuário digita uma linha ou coluna fora do intervalo 0-2
  **When** a entrada é validada
  **Then** uma mensagem de erro é exibida e o jogo pede a jogada novamente,
  sem encerrar.
- **Given** o usuário aponta para uma posição já ocupada
  **When** a jogada é validada
  **Then** uma mensagem de erro é exibida e o jogo pede a jogada novamente.
- **Given** o usuário digita algo que não é um número (ex.: `abc`)
  **When** a conversão para inteiro falha
  **Then** uma mensagem de erro é exibida (sem stack trace) e o jogo pede a
  jogada novamente.

### RF-02 — Sortear a jogada da máquina

- **Given** uma partida em andamento sem vencedor ainda
  **When** chega a vez da máquina jogar
  **Then** uma posição livre do tabuleiro é sorteada uniformemente e
  recebe "O".
- **Given** o usuário já venceu na própria jogada
  **When** o turno chegaria à máquina
  **Then** a máquina não joga (a partida já terminou).
- **Given** não há posições livres no tabuleiro
  **When** a máquina tentaria jogar
  **Then** nenhuma jogada é feita (o tabuleiro permanece igual).

### RF-03 — Determinar vitória ou empate

- **Given** um jogador (X ou O) completa uma linha, coluna ou diagonal
  **When** o tabuleiro é analisado após a jogada
  **Then** esse jogador é declarado vencedor e a partida termina.
- **Given** todas as posições do tabuleiro estão preenchidas e nenhum
  jogador completou uma linha, coluna ou diagonal
  **When** o tabuleiro é analisado
  **Then** o resultado é "Empate".

### RF-04 — Exibir o tabuleiro

- **Given** uma jogada (do usuário ou da máquina) acabou de acontecer
  **When** a tela é redesenhada
  **Then** o console é limpo e o grid 3x3 atual é impresso, com as posições
  separadas por `|` e as linhas por um separador.

### RF-05 — Jogar novamente ou encerrar

- **Given** uma partida terminou (vitória ou empate)
  **When** o usuário responde `s` à pergunta de replay
  **Then** o tabuleiro é reiniciado e uma nova partida começa.
- **Given** uma partida terminou
  **When** o usuário responde algo diferente de `s`
  **Then** uma mensagem de despedida é exibida e o programa termina.

### RF-06 — Limpar a tela entre jogadas

- **Given** o sistema operacional é Windows
  **When** a tela precisa ser limpa
  **Then** o comando `cls` é executado.
- **Given** o sistema operacional é Linux ou macOS
  **When** a tela precisa ser limpa
  **Then** o comando `clear` é executado.

## Requisitos não funcionais

### RNF-01 — Sem dependências externas

O jogo deve rodar com Python puro (biblioteca padrão), sem exigir
`pip install` de nenhum pacote em tempo de execução.

### RNF-02 — Portabilidade

O mesmo `main.py` deve funcionar sem alteração em Windows, Linux e macOS
(scripts de atalho separados por sistema cobrem só a conveniência de
inicialização, não a lógica do jogo).

### RNF-03 — Feedback nunca deixa o usuário travado

Nenhuma entrada inválida (coordenada fora do intervalo, posição ocupada,
texto não numérico) pode lançar uma exceção não tratada — o jogo sempre pede
a jogada de novo.

### RNF-04 — Saída não crasha por codificação

A impressão no terminal (incluindo os emojis das mensagens de status) não
pode lançar `UnicodeEncodeError`, mesmo quando `stdout` não está preso a um
console UTF-8 (saída redirecionada para arquivo, pipe, ou executor de CI).

## Perguntas em aberto

Nenhuma — feature pequena e já finalizada; ver "Atividade para praticar" no
`README.md` para extensões futuras propostas (placar acumulado, máquina que
bloqueia, cores no terminal).

## Testes

### RF-01, RF-02, RF-03 — Lógica pura do jogo

`tests/test_main.py` cobre `verificar_vitoria_ou_empate` para linha, coluna,
as duas diagonais, tabuleiro vazio e tabuleiro cheio sem vencedor
(parametrizado onde fazia sentido); `jogada_do_usuario` com entrada
válida/fora do intervalo/posição ocupada/não numérica (via `monkeypatch` em
`input`); e `jogada_da_maquina` com `random.choice` mockado, incluindo os
casos de guarda (vencedor já definido, tabuleiro cheio).

### RF-04 — Exibição

`tests/test_main.py` verifica, via `capsys`, que `exibir_tabuleiro` mostra
as jogadas atuais do tabuleiro.

### RF-05, RF-06 — Loop principal e limpeza de tela

Não têm teste automatizado direto: `main()` é um loop interativo até
`input()` sem timeout embutido, e `limpar_tela()` chama `os.system` (efeito
de terminal, não de retorno). Cobertos por verificação manual ao rodar o
jogo (inclusive com entrada via pipe, para expor o crash de codificação
corrigido no ADR-4 de `design.md`); `limpar_tela` é mockada nos testes acima
para isolar a lógica.
