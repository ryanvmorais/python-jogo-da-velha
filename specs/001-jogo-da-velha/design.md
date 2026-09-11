---
feature: Jogo da Velha (Tic Tac Toe) via terminal
status: concluído
data: 2026-09-11
relacionado:
  - 001-jogo-da-velha/requirements.md
origem: engenharia reversa
---

# 001 — Jogo da Velha — design

## Visão geral da abordagem

Um único módulo (`main.py`) com uma classe (`JogoDaVelha`) que guarda o
estado de uma partida (o tabuleiro 3x3 e o status final) e expõe um método
por responsabilidade (limpar tela, exibir tabuleiro, reiniciar, verificar
vitória/empate, ler jogada do usuário, sortear jogada da máquina). Uma
função `main()` no nível do módulo orquestra o loop de partidas e o prompt
de replay, e é o único ponto que lê/imprime diretamente no terminal fora da
classe.

Não há camadas (persistência, rede, UI gráfica) — é intencional: o projeto
é didático e o objetivo é que o fluxo caiba na cabeça em uma leitura.

## Layout de módulos

```
main.py            # classe do jogo + função main() (ponto de entrada)
tests/test_main.py # suíte pytest
```

## Modelo de dados

`JogoDaVelha` (não é um dataclass/pydantic — é um objeto com estado
mutável, o ponto pedagógico central da POO nesta spec):

- `tabuleiro: list[list[str]]` — matriz 3x3, cada posição é `" "` (vazia),
  `"X"` ou `"O"`.
- `status_final: str` — `""` (partida em andamento), `"X"`, `"O"` ou
  `"Empate"`.

## Componentes

### `JogoDaVelha.limpar_tela`

Detecta o SO via `os.name` (`"nt"` = Windows) e roda `cls`/`clear` via
`os.system`. Efeito de terminal, sem retorno.

### `JogoDaVelha.exibir_tabuleiro`

Limpa a tela e imprime o tabuleiro atual: uma linha em branco, as três
linhas do tabuleiro (posições separadas por `|`) intercaladas por um
separador entre elas, e uma linha em branco final.

### `JogoDaVelha.reiniciar_jogo`

Recria `tabuleiro` como uma matriz 3x3 de espaços vazios e zera
`status_final`. Chamado pelo `__init__` (primeira partida) e pelo loop de
replay em `main()`.

### `JogoDaVelha.verificar_vitoria_ou_empate`

Para cada jogador ("X" depois "O"), testa as 3 linhas, 3 colunas e 2
diagonais; a primeira combinação completa define `status_final` e encerra a
checagem. Se nenhuma combinação venceu e não há posição vazia, `status_final`
vira `"Empate"`.

### `JogoDaVelha.jogada_do_usuario`

Loop de leitura: pede linha e coluna, converte para `int`, valida o
intervalo 0-2 e se a posição está livre. Repete em caso de `ValueError`
(entrada não numérica), coordenada fora do intervalo, ou posição ocupada —
nunca deixa uma exceção subir.

### `JogoDaVelha.jogada_da_maquina`

Sai cedo se `status_final` já foi definido (o usuário acabou de vencer).
Calcula as posições livres do tabuleiro e sorteia uma com
`random.choice`; se não houver posição livre, não faz nada.

### `main()`

Loop externo (uma partida por iteração): enquanto não há `status_final`,
alterna jogada do usuário e da máquina, verificando vitória/empate após
cada uma. Ao terminar, exibe o tabuleiro final e a mensagem de resultado, e
pergunta se o usuário quer jogar de novo (`s`/qualquer outra coisa).

## Interfaces

Nenhuma — programa de terminal sem rede, arquivo ou API. A única "interface"
é o protocolo de entrada/saída via `input()`/`print()`, documentado nos
requisitos funcionais.

## ADRs

### ADR-1 — `os.system` em vez de `subprocess.run(..., shell=True)`

**Decisão.** `limpar_tela` usa `os.system(comando)` com uma string fixa
(`"cls"` ou `"clear"`).

**Alternativas.** (a) `subprocess.run(comando, shell=True)` — a versão
original antes desta modernização. (b) uma lib de terceiros (`colorama`,
`rich`) com função de limpar tela embutida.

**Porquê.** `comando` nunca é entrada do usuário — é sempre um literal fixo
escolhido por `os.name`. `os.system` faz exatamente o mesmo com uma linha
mais simples e sem o `shell=True` que ferramentas de análise estática
sinalizam por hábito (mesmo sem risco real aqui, o sinal de alerta some).
Descartar (b): manter zero dependência de runtime é um objetivo explícito
(RNF-01).

**Trade-off.** `os.system` é levemente menos flexível que `subprocess`
(não captura stdout/stderr) — irrelevante aqui, pois o efeito desejado é só
o side-effect no terminal.

### ADR-2 — Extrair `main()` em vez de código solto em `if __name__ == "__main__"`

**Decisão.** O loop do jogo vive numa função `main()`, chamada pelo guard
`if __name__ == "__main__"`.

**Alternativas.** (a) manter o loop diretamente no bloco do guard (como
estava antes da modernização).

**Porquê.** Uma função nomeada é importável e documentável (docstring); o
guard vira uma linha só. Não muda o comportamento em nada.

**Trade-off.** Nenhum relevante — é reorganização pura.

### ADR-3 — `exibir_tabuleiro` monta as linhas num loop, não em 5 `print` repetidos

**Decisão.** `exibir_tabuleiro` itera `self.tabuleiro` com `enumerate` e
imprime cada linha (e o separador entre elas), em vez de 5 chamadas
`print(...)` com os 9 índices `tabuleiro[i][j]` escritos à mão.

**Alternativas.** (a) manter as 5 chamadas `print` originais, uma por linha
de tabuleiro/separador (como estava). (b) montar a string inteira com
`" | ".join(...)` e um único `print`.

**Porquê.** A versão original, depois de ganhar type hints e passar pelo
Black, estourava o limite de 88 colunas em 3 das 5 linhas (os f-strings com
9 índices literais são longos). Descartar (a): quebrar manualmente essas
linhas deixava o código menos legível que um loop. Descartar (b): o
`join` numa linha só é mais denso e menos óbvio para quem está aprendendo
que o loop explícito com `enumerate`. A saída impressa é idêntica à
original — confirmado rodando o jogo manualmente antes e depois da mudança.

**Trade-off.** Nenhum relevante — mesmo comportamento, só reorganização do
código-fonte.

### ADR-4 — Reconfigurar `sys.stdout` para UTF-8 no import

**Decisão.** `main.py` chama `sys.stdout.reconfigure(encoding="utf-8",
errors="replace")` no nível do módulo, se o atributo existir.

**Alternativas.** (a) não fazer nada (comportamento original). (b) remover os
emojis das mensagens.

**Porquê.** No Windows, quando `stdout` não está preso a um console UTF-8
(saída redirecionada para arquivo, pipe, ou alguns executores de CI), o
Python cai para a codepage do sistema (`cp1252`) e todo `print()` com emoji
lança `UnicodeEncodeError` — confirmado ao rodar `main.py` com a entrada via
pipe durante esta modernização (o `⚠️` da mensagem de entrada inválida
disparava o crash). Descartar (a): é a causa raiz do crash. Descartar (b):
os emojis são parte da voz didática/calorosa do projeto (RF-01, RF-03);
removê-los é perda maior que o custo de uma linha de configuração.

**Trade-off.** `errors="replace"` troca um caractere não suportado por `?`
em vez de crashar — aceitável, pois a única saída que perderia fidelidade é
um terminal exótico que também não suporta UTF-8.

## Impacto no código existente

Esta spec documenta a versão já modernizada de `main.py` (type hints, `uv`,
suíte de testes). Não há código legado para migrar — é a spec fundadora do
projeto.

## Estratégia de testes

Unitária, sem integração (não há rede nem arquivo). `limpar_tela` é sempre
mockada nos testes (evita side-effect de terminal); `input()` é mockado via
`monkeypatch.setattr("builtins.input", ...)` para simular sequências de
digitação, inclusive as inválidas que o loop de validação precisa absorver;
`random.choice` é mockado quando o teste precisa de uma jogada determinística
da máquina. Ver `tests/test_main.py` e a seção "Testes" de
`requirements.md`.
