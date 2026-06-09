---
name: quadrix
description: >
  Analisar, resolver, revisar e GERAR questões de concurso no estilo da banca
  Instituto Quadrix (padrão 2025, conselhos profissionais). Use quando o usuário
  pedir para resolver/comentar questões da Quadrix, revisar gabarito, treinar para
  prova Quadrix, ou gerar uma prova/simulado em PDF no layout da banca.
---

# SKILL — Banca Quadrix (resolver · revisar · gerar)

Esta skill condensa os padrões mapeados em `provasquadrix.md` (64 provas + 10 gabaritos
Quadrix 2025) em um procedimento operacional. **Consulte `provasquadrix.md` para a
evidência detalhada e exemplos reais.**

## Quando usar
- Resolver uma ou mais questões da Quadrix com justificativa.
- Revisar/auditar uma questão e seu gabarito (achar ambiguidade, risco de anulação).
- Treinar o usuário explicando a "pegadinha" de cada questão.
- **Gerar um simulado/prova em PDF visualmente fiel à Quadrix** (ver §4).

## Fatos da banca que governam tudo (memorize)
1. **Formato:** múltipla escolha, **5 alternativas (A–E), uma única correta**. Sem certo/errado puro, sem somatório.
2. **O comando quase sempre pede a CORRETA** ("assinale a opção correta", "é correto afirmar"). "incorreta/exceto/que não" são raros — quando aparecem, são o ponto da pegadinha.
3. **Estrutura:** Conhecimentos Básicos → Complementares → Específicos, numeração contínua (40 questões no padrão; 50 no CRA‑SP).
4. **Distratores erram por palavra absoluta/restritiva:** apenas, somente, sempre, nunca, todos, qualquer, vedado, salvo, dispensa‑se, temporário/definitivo, pode/deve.
5. **Nível superior = caso hipotético** ("Uma empresa Ltda. … Com base nessa situação hipotética, assinale…").
6. **Variante "julgue os itens I, II, III"** resolvida dentro das 5 alternativas (Somente o item…/Todos/Nenhum).
7. **Gabarito é balanceado**; nas específicas costuma **ciclar A→B→C→D→E**. Não existe "letra mais provável".

---

## 1. Como identificar o tipo de questão
Classifique antes de resolver:

| Sinal no enunciado | Tipo | Estratégia |
|---|---|---|
| "assinale a opção correta / é correto afirmar" | **única correta** | valide cada alternativa como V/F; sobra 1 verdadeira |
| "incorreta / que não / exceto" | **única incorreta** | **circule a negação**; 4 são verdadeiras, marque a falsa |
| "julgue os itens" + I/II/III | **itens combinados** | avalie I, II, III isoladamente; depois escolha a letra |
| "assinale a opção que apresenta [o valor/o termo/o nome]" | **objetiva/definição** | calcule ou recupere o termo exato |
| "Com base nessa situação hipotética" | **caso aplicado** | leia o caso todo, aplique a regra, só então leia alternativas |
| texto‑base "questões de X a Y" | **interpretação** | leia o texto antes; resposta tem de se sustentar no texto |

## 2. Como tratar as pegadinhas (8 mecânicas)
Ao avaliar cada alternativa, rode esta varredura (detalhe e exemplos em `provasquadrix.md` §2):
1. **Palavra absoluta indevida** — apenas/somente/sempre/nunca/todos/qualquer/vedado tornam falsa uma frase quase certa. *Pegadinha nº 1.*
2. **Quase‑certa** — frase 90% correta com **um** detalhe trocado (número, prazo, %, órgão, artigo).
3. **Inversão de conceitos** — causa/efeito, físico/lógico (MAC/IP), RAM/disco, definição/exemplo.
4. **Troca de instituto/regime** — improbidade×ética; RPP×RPNP; temporário×definitivo; PPA×LDO×LOA.
5. **Fora de escopo** — alternativa verdadeira que **não responde** ao comando (vantagem quando se pediu desvantagem).
6. **A mais longa/ressalvada** (nível superior) — a correta tende a ser completa e cautelosa; confirme cada ressalva.
7. **Lei/artigo plausível porém errado** — número citado pode estar corrompido ou o artigo não diz aquilo.
8. **Atualidade com fato trocado** — local/data/número/relação geopolítica invertidos.

> Regra de ouro: **uma única palavra decide a alternativa.** Leia palavra por palavra os qualificadores.

## 3. Como estruturar a resposta correta (formato de saída ao resolver)
Para cada questão, produza:

```
QUESTÃO N — [disciplina/tema] — [tipo identificado]
Comando: pede a opção CORRETA / INCORRETA.
Gabarito: (LETRA).
Por quê (a correta): <regra legal/técnica que a sustenta — cite lei/artigo/CPC/conceito>.
Por que as outras caem:
  (A) ... — <mecânica da pegadinha + o termo exato que a torna falsa>
  (B) ...
  ... (todas as demais)
Pegadinha‑chave: <a armadilha central, ex.: "apenas" indevido / inversão MAC↔IP>.
Risco de anulação: <baixo/médio/alto + motivo, se houver ambiguidade>.
```
- **Sempre cite o dispositivo** (Lei nº, artigo, CPC, princípio) que fundamenta a correta e que derruba cada distrator.
- Se a questão for de cálculo, **mostre o cálculo** passo a passo.
- Se identificar ambiguidade real (duas alternativas defensáveis), **diga "passível de recurso/anulação"** — a banca anula esse perfil de questão (vide `provasquadrix.md` §4.3).

## 4. Como GERAR uma prova/simulado em PDF (fiel à Quadrix)
Use o gerador `gerar_prova_quadrix.py` (nesta pasta). Ele já replica o layout da banca:
cabeçalho com conselho + `Quadrix | 2025`, caixa de instrução, faixa **PROVA OBJETIVA**,
faixas de seção (**CONHECIMENTOS BÁSICOS/COMPLEMENTARES/ESPECÍFICOS**), duas colunas
justificadas, rótulo **QUESTÃO N** em caixa arredondada com ícone, e **gabarito em página
separada** ao final.

### 4.1 Regras de fidelidade (obrigatórias)
- **5 alternativas (A–E)**, uma correta. Numeração contínua.
- **Estrutura:** Básicos (1–15) → Complementares (16–20) → Específicos (21–40). (Ou 1–20/21–30/31–50 para 50 questões.)
- **Distribuição de conteúdo** conforme `provasquadrix.md` §3 (Português+Mat/RLM+Informática nos básicos; kit de leis no complementar; legislação do conselho + área no específico).
- **Dificuldade** crescente: básicos diretos; específicos de nível superior em **caso hipotético** longo.
- **Distratores** construídos com as 8 mecânicas do §2 — cada alternativa errada deve errar por um motivo nomeável (palavra absoluta, número trocado, inversão…).
- **Gabarito ciclando A→B→C→D→E** nas específicas (anti‑clustering da banca).
- **Fonte:** sans‑serif tipo Calibri/Carlito (a Quadrix **não** usa serifada). O gerador usa Calibri do Windows; se o usuário insistir em serifada, é um desvio do original — avise.
- **Cabeçalho:** nome do conselho à esquerda (maiúsculas, cinza), `Quadrix | 2025` à direita; instrução‑padrão idêntica à real.

### 4.2 Como rodar
```bash
python gerar_prova_quadrix.py exemplo_prova.json saida.pdf
```
O JSON descreve metadados + blocos + questões (esquema documentado no topo do script e em `exemplo_prova.json`). Para um pedido novo, **gere o conteúdo das questões seguindo §§1–3**, escreva o JSON e rode o script.

### 4.3 Checklist final antes de entregar o PDF
- [ ] 40 (ou 50) questões, A–E, numeração contínua, 3 blocos na ordem certa.
- [ ] Cada distrator tem motivo nomeável; nenhuma questão com 2 corretas defensáveis.
- [ ] Gabarito ciclado nas específicas; nenhuma letra dominante.
- [ ] Cabeçalho, faixas e caixa de instrução presentes; fonte sans‑serif.
- [ ] Gabarito em **página separada** ao final, com divisão por blocos.
- [ ] Atualidades coerentes com o ano‑alvo do simulado.

---

## 5. Erros a evitar (auto‑revisão da skill)
- Não invente que a Quadrix usa certo/errado estilo Cebraspe — **ela não usa**.
- Não diga "a letra C é a mais provável" — o gabarito é balanceado.
- Não entregue justificativa sem citar o dispositivo/regra.
- Ao gerar prova, não deixe distrator "obviamente absurdo" em todas as alternativas — a banca faz distratores **plausíveis**.
- Não use fonte serifada alegando ser o padrão Quadrix.

*Fonte de verdade desta skill: `provasquadrix.md` (análise de 64 provas + 10 gabaritos Quadrix 2025).*
