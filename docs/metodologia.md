# Metodologia — como um bom material de concurso deve ensinar

> Documento-guia do **Agente Quadrix**. Todo material gerado deve seguir estes princípios.

## O erro mais comum

A maioria dos PDFs de estudo ensina como uma **faculdade**: discussão, interpretação aberta, teoria pela teoria. Mas a prova não cobra isso. A prova cobra **reconhecimento de padrão sob pressão de tempo**.

> Concurso não recompensa quem leu mais. Recompensa quem:
> reconhece padrões mais rápido · interpreta melhor · erra menos sob pressão · revisa com eficiência.

O objetivo de um material não é *informar* — é **transformar informação em acerto**.

---

## As 7 funções de um material forte

1. **Abertura estratégica** — abre explicando _por que aquele tema derruba candidato_ e o que realmente importa. O aluno entra sabendo onde focar.
2. **Explicação em camadas** — primeiro a lógica (o porquê), depois a regra, depois a exceção. Nunca joga a regra seca isolada.
3. **Ensinar pelo erro** — mostra o erro típico como ferramenta pedagógica: "é aqui que a maioria marca errado, e por quê".
4. **Exemplos da banca, não genéricos** — o exemplo imita o jeito que a Quadrix escreve, não um caso de manual.
5. **Pegadinha integrada** — a armadilha é ensinada _junto_ com o conteúdo, não num quadro separado no fim.
6. **Design cognitivo** — cor e layout viram memória visual. Padrão consistente: 🔴 pegadinha · 🟢 macete · 🔵 explicação.
7. **Revisão eficiente** — macetes curtos e gabarito claro permitem revisar rápido na véspera.

---

## Estrutura ideal de uma página/seção

1. **Título do tema** + (se questão) número e assunto.
2. **Lei seca** em destaque (caixa), com o texto exato.
3. **O que significa** — a tradução em linguagem direta, com a lógica.
4. **Exemplo concreto** — uma situação que torna a regra tangível.
5. **Pegadinha Quadrix** — como a banca tenta te derrubar nesse ponto.
6. **Macete** — gancho de memória de uma linha.

Para questões comentadas, acrescente:
- **Enunciado realista** (no estilo da banca).
- **5 alternativas** com distratores plausíveis (não óbvios).
- **Gabarito + comentário** explicando a _estratégia de resolução_, não só a letra certa.

---

## Gatilhos de escrita da banca (decore)

| Gatilho | Como a banca usa | Como você deve ler |
|---|---|---|
| **VEDADO** | "X é vedado" | Se é vedado, alternativa que diz "permitido" é falsa |
| **SALVO / EXCETO** | "proíbe X, salvo Y" | Existe exceção; alternativa que a ignora está errada |
| **APENAS / SOMENTE / INDEPENDENTEMENTE** | condição ou gratuidade exata | Confira se a condição foi respeitada |
| **SEMPRE / NUNCA / ABSOLUTO** | "funciona assim sempre" | Quase sempre falso — procure a exceção |
| **Troca lei↔decreto** | "decreto pode obrigar" | Obrigação ao particular só nasce de **lei** formal |

---

## Regras de qualidade do design

- **Sem espaço morto.** Conteúdo flui em cards que não quebram no meio (`break-inside: avoid`). Nada de meia página em branco.
- **Densidade alta, legível.** Mais conteúdo por página, sem virar muro de texto — use cards, grids de 2 colunas e listas.
- **Gabarito equilibrado.** As respostas corretas se distribuem entre A–E, como numa prova real (nunca "quase tudo B").
- **Acentuação correta.** Por isso o motor principal é HTML/CSS renderizado por navegador — controle tipográfico real.

---

## Por que HTML/CSS → Chrome (e não só reportlab)

`reportlab` é uma biblioteca de **fluxo de texto**: empilha parágrafos e deixa buracos ao quebrar página. Serve para **imitar o caderno oficial** da banca (layout fixo), e é isso que `gerar_prova_quadrix.py` faz.

Para **material de estudo bonito**, HTML + CSS dá controle real de layout (cards, caixas coloridas, colunas, tipografia) e o navegador distribui o conteúdo sem espaço morto. Por isso `gerar_material_html.py` escreve HTML e o Chrome converte em PDF.
