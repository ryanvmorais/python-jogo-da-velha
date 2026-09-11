# Specs — Jogo da Velha

Este projeto usa spec-driven development: cada feature é documentada em
`specs/NNN-nome/` como três arquivos Markdown agnósticos de ferramenta —
`requirements.md` (o quê/porquê), `design.md` (como) e `tasks.md` (quebra
executável e rastreável). O fluxo de 4 fases (`requirements → design → tasks
→ implementação`), com portão de aprovação humana em cada uma, é conduzido
pela skill `/spec`.

## Convenções

- **Numeração:** `NNN` sequencial de 3 dígitos (`001`, `002`, ...), nome
  curto em kebab-case.
- **Frontmatter** (idêntico nos três arquivos de uma spec):
  ```yaml
  ---
  feature: <título legível>
  status: rascunho | aprovado | em andamento | concluído
  data: AAAA-MM-DD
  relacionado:
    - NNN-outra/requirements.md
  origem: concepção | engenharia reversa
  ---
  ```
- **Critério de aceite:** Given/When/Then, um `### RF-NN` (heading, linkável)
  por requisito funcional; `### RNF-NN` para não funcional.
- **Rastreabilidade:** toda tarefa em `tasks.md` cita o(s) requisito(s) e/ou
  ADR que satisfaz (`— RF-01, ADR-2`); a última tarefa de cada etapa é o
  portão de qualidade, com o resultado real anotado ao executar.
- **Idioma:** português — projeto pessoal/educacional (ver `CLAUDE.md`).

## Workflow

```
requirements.md (rascunho) --[aprovação]--> (aprovado)
        |
        v
design.md (aprovado) --[aprovação]--> status dos requirements avança
        |
        v
tasks.md (aprovado) --[aprovação]--> em andamento
        |
        v
implementação, tarefa a tarefa --[portão de qualidade]--> concluído
```

Comandos da skill `/spec`: `nova <nome>` (abre requirements) · `design`
(projeta) · `tasks` (quebra) · `implementar` (executa) · `status` (panorama
de todas as specs).

## Índice / Roadmap

| Spec | Escopo | Status |
|---|---|---|
| [001-jogo-da-velha](001-jogo-da-velha/requirements.md) | O jogo completo: jogadas em matriz 3x3, vitória/empate, replay, limpeza de tela multiplataforma | concluído |

## Notas de manutenção

Nenhuma pegadinha registrada ainda — projeto pequeno, sem invariante frágil
conhecido. Ao adicionar uma feature nova (ex.: placar acumulado, IA que
bloqueia, cores no terminal — ver "Atividade para praticar" no `README.md`),
abra uma spec nova em vez de estender `001` diretamente.

Use `001-jogo-da-velha/` como padrão de formato para as próximas specs deste
repositório.
