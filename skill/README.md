# Kit Quadrix — como usar num chat normal

Este kit reúne tudo o que a Claude precisa para **analisar, resolver, revisar e gerar
provas no estilo do Instituto Quadrix (padrão 2025)**. Você pode usá‑lo em qualquer
conversa normal (Claude.ai, app ou Claude Code), sem precisar reanalisar as provas.

## Arquivos do kit
| Arquivo | Onde está | Para quê |
|---|---|---|
| `SKILLQUADRIX.md` | `skill/` | A "skill": instruções operacionais (como classificar, resolver, revisar e gerar). |
| `padroes-da-banca.md` | `docs/` | A referência técnica com os padrões mapeados e exemplos reais. |
| `gerar_prova_quadrix.py` | `engine/` | Gera o PDF no layout da Quadrix (rode no seu computador). |
| `gerar_material_html.py` | `engine/` | Gera material de estudo em HTML/CSS (render via Chrome). |
| `exemplo_prova.json` | `engine/` | Modelo de entrada do gerador (esquema documentado). |

## Como fazer pedidos num chat normal

**1) Abra uma conversa nova** e anexe (ou cole o conteúdo de) `skill/SKILLQUADRIX.md` e
`docs/padroes-da-banca.md`. Se for gerar PDF, anexe também `engine/gerar_prova_quadrix.py` e
`engine/exemplo_prova.json`.

**2) Diga à Claude para usar a skill.** Exemplos de pedido que funcionam bem:

- **Resolver uma questão:**
  > "Use a skill Quadrix. Resolva esta questão e explique a pegadinha: [cole a questão e as alternativas A–E]."

- **Resolver uma prova inteira / corrigir:**
  > "Seguindo a skill Quadrix, dê o gabarito comentado destas 10 questões, citando o dispositivo legal de cada uma e por que cada distrator cai."

- **Treinar / explicar padrões:**
  > "Com base na referência Quadrix, me explique as 8 mecânicas de pegadinha com um exemplo de cada."

- **Gerar um simulado em PDF:**
  > "Use a skill Quadrix para criar um simulado de **Contador – CORE** com 40 questões (15 básicas, 5 complementares, 20 específicas), nível e distratores no padrão da banca. Escreva o JSON e me explique como rodar o `gerar_prova_quadrix.py`."

- **Gerar de um cargo/conselho específico:**
  > "Monte um simulado de **Assistente Administrativo – CRB** no padrão Quadrix, com gabarito ciclando A→E nas específicas."

**3) Para gerar o PDF**, salve o JSON que a Claude produzir e rode no seu computador:
```bash
python engine/gerar_prova_quadrix.py minha_prova.json simulado.pdf
```
Requisitos: Python 3 + `reportlab` (instale com `pip install reportlab`). No Windows,
o gerador usa a fonte Calibri automaticamente (sans‑serif, como a banca).

## Dica
Se quiser, peça à Claude para **já entregar o JSON pronto** e até para **rodar o
gerador** caso ela tenha acesso ao terminal (como no Claude Code). Num chat web sem
terminal, ela escreve o JSON e você roda o comando localmente.
