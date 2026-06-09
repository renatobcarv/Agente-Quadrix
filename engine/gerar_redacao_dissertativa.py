# -*- coding: utf-8 -*-
"""Material de estudo DENSO (estilo apostila): Redação Dissertativo-Argumentativa.
Texto corrido + exemplos escritos por extenso + modelo NOTA MÁXIMA comentado.
SEM quebra de página por seção: o conteúdo flui e preenche a folha.
Gera HTML (render via Chrome).
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(_HERE)
OUTDIR = os.path.join(_REPO, "materiais", "dia12-redacao-dissertativa")
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "Dia12_Redacao_Dissertativa.html")

# ===== MODELO NOTA MÁXIMA comentado =====
MODELO = [
    {
        "rotulo": "Introdução",
        "texto": (
            "A Constituição Federal de 1988 inaugurou um novo paradigma ao reconhecer a "
            "<span class='rep'>assistência social como direito do cidadão e dever do Estado</span>, "
            "independentemente de contribuição. <span class='con'>Não obstante</span> esse avanço "
            "normativo, a efetivação plena desse direito ainda esbarra em obstáculos estruturais. "
            "<span class='con'>Desse modo</span>, <span class='tese'>a redução das desigualdades "
            "sociais no Brasil depende tanto do fortalecimento dos serviços socioassistenciais quanto "
            "da superação da cultura assistencialista que historicamente marcou o país.</span>"
        ),
        "analise": [
            ("Contextualização", "Abre com um fato histórico-normativo (a CF/88) — repertório que situa o tema sem rodeios e já demonstra conhecimento."),
            ("Problematização", "‘Não obstante esse avanço… esbarra em obstáculos’ cria a tensão entre o que a lei promete e o que a realidade entrega: é isso que justifica o texto existir."),
            ("Tese (o coração da redação)", "A última frase apresenta a tese e anuncia os DOIS eixos que serão defendidos: (1) fortalecer os serviços e (2) superar o assistencialismo. Cada eixo vira um parágrafo de desenvolvimento."),
        ],
    },
    {
        "rotulo": "Desenvolvimento 1",
        "texto": (
            "<span class='con'>Em primeiro lugar</span>, o fortalecimento da rede de proteção social "
            "mostra-se imprescindível. O <span class='rep'>Sistema Único de Assistência Social (SUAS)</span>, "
            "ao organizar serviços como os ofertados nos Centros de Referência de Assistência Social (CRAS), "
            "aproxima o Estado das famílias em situação de vulnerabilidade. "
            "<span class='con'>Segundo dados do IBGE</span>, milhões de brasileiros vivem abaixo da linha "
            "da pobreza, o que evidencia a relevância de equipamentos públicos capilarizados. "
            "<span class='con'>Assim</span>, investir em infraestrutura e em equipes técnicas qualificadas "
            "é condição para que a assistência deixe de ser promessa e se torne prática."
        ),
        "analise": [
            ("Tópico frasal", "A 1ª frase anuncia o argumento do parágrafo (fortalecer a rede). Tudo o que vem depois serve a essa ideia — parágrafo com unidade."),
            ("Repertório produtivo", "Cita o SUAS e os CRAS (conhecimento da própria área do concurso) e dados do IBGE. Não é enfeite: cada citação sustenta o argumento."),
            ("Frase de fechamento", "‘Assim, investir… é condição’ arremata o parágrafo retomando e concluindo o raciocínio antes de passar ao próximo."),
        ],
    },
    {
        "rotulo": "Desenvolvimento 2",
        "texto": (
            "<span class='con'>Ademais</span>, é preciso romper com a lógica do assistencialismo, que "
            "reduz o beneficiário à condição de mero receptor de favores. "
            "<span class='con'>Conforme o economista Amartya Sen</span>, "
            "<span class='rep'>o desenvolvimento deve ser compreendido como a ampliação das liberdades e "
            "das capacidades dos indivíduos</span>. <span class='con'>Nessa perspectiva</span>, programas "
            "de transferência de renda só cumprem seu papel quando articulados a ações de educação, "
            "qualificação profissional e geração de emprego, promovendo a autonomia e a emancipação dos cidadãos."
        ),
        "analise": [
            ("Progressão (não repete o D1)", "‘Ademais’ marca um SEGUNDO argumento, distinto do primeiro: o texto avança em vez de repetir a mesma ideia com outras palavras."),
            ("Repertório de autoridade", "Cita Amartya Sen com pertinência (liberdades e capacidades), elevando o nível do texto e ancorando o argumento da autonomia."),
            ("Aprofundamento", "Liga a transferência de renda à educação e ao trabalho, mostrando raciocínio próprio em vez de senso comum."),
        ],
    },
    {
        "rotulo": "Conclusão",
        "texto": (
            "<span class='con'>Portanto</span>, a assistência social só se concretizará como direito quando "
            "o Estado conjugar a ampliação dos serviços à promoção da autonomia dos beneficiários. "
            "<span class='con'>Para tanto</span>, <span class='rep'>é fundamental que o poder público, em "
            "parceria com a sociedade civil, amplie o financiamento do SUAS e invista na formação continuada "
            "dos servidores</span>, garantindo, dessa forma, que a proteção social seja, de fato, um "
            "instrumento de justiça e de redução das desigualdades."
        ),
        "analise": [
            ("Retomada da tese", "‘Conjugar a ampliação dos serviços à promoção da autonomia’ retoma os DOIS eixos da introdução. O texto fecha o círculo que abriu."),
            ("Proposta concreta", "Aponta agente + ação + meio: poder público e sociedade civil ampliam o financiamento e a formação. Encaminhamento real, não frase vaga."),
            ("Fecho de impacto", "‘instrumento de justiça e de redução das desigualdades’ encerra retomando o tema com elegância e sem abrir assunto novo."),
        ],
    },
]

CONECTIVOS = [
    ("Introduzir / iniciar", "Inicialmente; Em primeiro lugar; Diante disso; Nesse contexto; A princípio"),
    ("Adicionar argumento", "Ademais; Além disso; Outrossim; Soma-se a isso; Não só… mas também; Igualmente"),
    ("Opor / contrastar", "Todavia; Contudo; Entretanto; Não obstante; Em contrapartida; Por outro lado"),
    ("Causa / justificar", "Visto que; Uma vez que; Posto que; Em razão de; Tendo em vista que; Porquanto"),
    ("Consequência", "Por conseguinte; De modo que; Logo; Como resultado; Por isso"),
    ("Exemplificar / citar", "A título de exemplo; Segundo; Conforme; De acordo com; Como afirma; Nas palavras de"),
    ("Concluir", "Portanto; Dessa forma; Em síntese; Diante do exposto; Por fim; Assim sendo"),
]

ERROS = [
    ("Fugir do tema",
     "Escrever sobre algo próximo, mas não exatamente o que foi pedido — o erro que mais zera a redação.",
     "Tema: ‘os desafios da assistência social’. O candidato disserta genericamente sobre ‘pobreza no mundo’.",
     "Antes de escrever, sublinhe as palavras-chave do comando e mantenha cada parágrafo amarrado a elas."),
    ("Não tomar posição",
     "Introdução que ‘apresenta o assunto’ mas não defende nada. Sem tese, não há dissertação argumentativa.",
     "‘A assistência social é um tema muito importante e polêmico na sociedade atual.’ (não diz o que você defende)",
     "Feche a introdução com uma tese que tome posição e anuncie os dois argumentos."),
    ("Senso comum / achismo",
     "Trocar repertório por frases prontas e vazias, que não comprovam nada.",
     "‘Desde os primórdios da humanidade, todos sabem que a desigualdade é ruim.’",
     "Substitua por repertório legítimo: uma lei (CF/88, SUAS), um dado (IBGE), um autor (Amartya Sen)."),
    ("Primeira pessoa e informalidade",
     "A dissertação de concurso é impessoal e formal. Gírias, ‘eu acho’ e ‘a gente’ derrubam a nota de língua.",
     "‘Eu acho que a gente precisa ajudar mais os pobres, né?’",
     "Use a 3ª pessoa e o registro formal: ‘É necessário que o Estado amplie a proteção social’."),
    ("Parágrafo sem unidade",
     "Misturar dois argumentos no mesmo parágrafo, deixando o texto confuso e sem progressão.",
     "Um parágrafo que fala, ao mesmo tempo, de financiamento, de educação e de cultura, sem foco.",
     "Um argumento por parágrafo, anunciado no tópico frasal e desenvolvido até o fim."),
    ("Conclusão que abre tema novo",
     "Trazer, no último parágrafo, um argumento inédito que não foi desenvolvido — quebra a coerência.",
     "Concluir falando, pela primeira vez, em ‘reforma tributária’, que não apareceu no texto.",
     "A conclusão retoma o que já foi dito e propõe um encaminhamento; nada de novidade."),
]


def render_modelo(m):
    analise = "".join(
        f"<div class='an-item'><span class='an-tag'>{t}</span> {d}</div>" for (t, d) in m["analise"]
    )
    return f"""
    <div class="modelo-bloco">
      <div class="modelo-rotulo">{m['rotulo']}</div>
      <div class="modelo-grid">
        <div class="modelo-texto">{m['texto']}</div>
        <div class="modelo-analise">{analise}</div>
      </div>
    </div>"""


conectivos_rows = "".join(
    f"<tr><td><span class='rn'>{rel}</span></td><td>{lst}</td></tr>" for (rel, lst) in CONECTIVOS
)
erros_rows = "".join(
    f"<tr><td><b>{t}</b><br><span class='er-d'>{d}</span></td>"
    f"<td><span class='er-x'>✗ {ex}</span></td>"
    f"<td><span class='er-c'>✓ {c}</span></td></tr>"
    for (t, d, ex, c) in ERROS
)
modelo_html = "".join(render_modelo(m) for m in MODELO)

CSS = """
@page { size:A4; margin:13mm 13mm 15mm 13mm; }
* { box-sizing:border-box; }
body { font-family:'Segoe UI','Helvetica Neue',Arial,sans-serif; color:#1d2733; font-size:10.7px; line-height:1.62; margin:0;
  -webkit-print-color-adjust:exact; print-color-adjust:exact; }
h1,h2,h3,h4 { margin:0; font-weight:700; }
p { margin:0 0 7px; text-align:justify; }
.cover { height:250mm; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;
  background:linear-gradient(135deg,#064e3b 0%,#047857 55%,#065f46 100%); color:#fff; border-radius:6px; page-break-after:always; padding:0 24mm; }
.cover .kicker { letter-spacing:4px; font-size:12px; opacity:.85; font-weight:600; }
.cover h1 { font-size:43px; line-height:1.05; margin:10px 0 6px; }
.cover .sub { font-size:15px; font-weight:400; opacity:.95; max-width:135mm; }
.cover .rule { width:70px; height:4px; background:#ffd27a; margin:22px 0; border-radius:2px; }
.cover .meta { font-size:12.5px; opacity:.9; line-height:1.7; }
.cover .badge { margin-top:26px; background:rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.4); padding:9px 18px; border-radius:40px; font-size:13px; font-weight:600; }
/* títulos de seção fluem, NÃO quebram página */
.section-title { font-size:17px; color:#047857; border-bottom:3px solid #047857; padding-bottom:4px; margin:16px 0 9px; page-break-after:avoid; }
.section-title:first-of-type { margin-top:4px; }
.subhead { font-size:12.5px; color:#065f46; font-weight:700; margin:11px 0 4px; border-left:4px solid #047857; padding-left:8px; page-break-after:avoid; }
.lead { font-size:11px; color:#33414f; }
/* exemplos escritos por extenso */
.example { background:#f3faf7; border:1px solid #cfeede; border-left:4px solid #047857; border-radius:6px; padding:8px 11px; margin:6px 0; page-break-inside:avoid; }
.example .lbl { display:inline-block; background:#047857; color:#fff; font-size:8px; font-weight:700; text-transform:uppercase; letter-spacing:.5px; padding:2px 8px; border-radius:10px; margin-bottom:4px; }
.example p { margin:0; font-size:10.3px; line-height:1.6; }
.example .txt { font-style:italic; color:#21303a; }
.note-inline { color:#0e7490; font-style:normal; font-weight:600; }
/* boxes */
.box2 { display:grid; grid-template-columns:1fr 1fr; gap:9px; margin:7px 0; }
.callout { border-radius:7px; padding:9px 12px; page-break-inside:avoid; }
.c-key { background:#eefaf1; border-left:4px solid #047857; }
.c-why { background:#fff5f5; border-left:4px solid #c0392b; }
.c-tip { background:#eef9f7; border-left:4px solid #0e7490; }
.callout h4 { font-size:10.5px; margin-bottom:4px; text-transform:uppercase; letter-spacing:.4px; }
.c-key h4 { color:#047857; } .c-why h4 { color:#c0392b; } .c-tip h4 { color:#0e7490; }
.callout ul { margin:3px 0 0; padding-left:15px; } .callout li { margin:2.5px 0; }
/* tabelas */
table { width:100%; border-collapse:collapse; margin:7px 0; font-size:9.8px; page-break-inside:avoid; }
th { background:#064e3b; color:#fff; text-align:left; padding:6px 8px; }
td { border:1px solid #e2e6ee; padding:6px 8px; vertical-align:top; }
tr:nth-child(even) td { background:#f5faf8; }
td .rn { font-weight:700; color:#047857; }
.er-d { font-size:9px; color:#5a6573; } .er-x { color:#b3271e; } .er-c { color:#1f7a4d; }
/* modelo comentado */
.legenda { display:flex; gap:12px; flex-wrap:wrap; font-size:9px; margin:5px 0 9px; }
.legenda span { padding:2px 8px; border-radius:4px; font-weight:700; }
.lg-tese { background:#fde68a; color:#7c5e00; } .lg-con { background:#dbeafe; color:#1e40af; } .lg-rep { background:#dcfce7; color:#166534; }
.modelo-bloco { border:1px solid #d9e2dd; border-radius:9px; margin:0 0 9px; overflow:hidden; page-break-inside:avoid; }
.modelo-rotulo { background:#047857; color:#fff; font-weight:700; font-size:10px; text-transform:uppercase; letter-spacing:.5px; padding:4px 11px; }
.modelo-grid { display:grid; grid-template-columns:1.32fr 1fr; }
.modelo-texto { padding:10px 12px; font-size:10.2px; line-height:1.66; text-align:justify; border-right:1px solid #eef0f4; }
.modelo-analise { padding:9px 11px; background:#fafbfd; }
.an-item { font-size:8.9px; line-height:1.45; margin-bottom:6px; color:#46536a; }
.an-tag { display:inline-block; background:#047857; color:#fff; font-weight:700; font-size:7.8px; text-transform:uppercase; letter-spacing:.3px; padding:1px 6px; border-radius:10px; margin-bottom:2px; }
.tese { background:#fde68a; border-radius:3px; padding:0 2px; font-weight:600; }
.con { background:#dbeafe; border-radius:3px; padding:0 2px; }
.rep { background:#dcfce7; border-radius:3px; padding:0 2px; }
.passo { counter-reset:step; margin-top:4px; }
.passo .p { position:relative; padding-left:30px; margin-bottom:7px; font-size:10.3px; text-align:justify; }
.passo .p::before { counter-increment:step; content:counter(step); position:absolute; left:0; top:-1px; width:21px; height:21px; background:#047857; color:#fff; border-radius:50%; text-align:center; line-height:21px; font-weight:700; font-size:11px; }
.pagebreak { page-break-before:always; }
"""

HTML = f"""<!DOCTYPE html>
<html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head>
<body>

<div class="cover">
  <div class="kicker">REDAÇÃO</div>
  <h1>Dissertativo-<br>Argumentativa</h1>
  <div class="rule"></div>
  <div class="sub">Apostila completa: teoria, técnicas, exemplos por extenso e um modelo NOTA MÁXIMA comentado parágrafo a parágrafo</div>
  <div class="meta" style="margin-top:26px;">Concurso <b>Sedes/DF</b> · Banca <b>Quadrix</b> · 2026<br>Técnico Administrativo (Cargo 202)</div>
  <div class="badge">Dia 12 · Estrutura da redação</div>
</div>

<h2 class="section-title">1. O que é a redação de concurso e o que a banca cobra</h2>
<p>A redação exigida em concursos como os da Quadrix é a <b>dissertativo-argumentativa</b>. Dissertar é expor ideias de forma organizada sobre um assunto; argumentar é defender um <b>ponto de vista</b> com razões que o sustentem. Reunindo as duas coisas, o que se pede é um texto em que você assume uma posição clara diante de um tema e a comprova com argumentos consistentes, em linguagem formal e impessoal. Não se trata de narrar uma história, de descrever algo nem de simplesmente opinar: trata-se de <b>convencer</b> o leitor por meio do raciocínio.</p>
<p>O comando da prova costuma ter três partes que você precisa ler com atenção: o <b>tema</b> (a frase que delimita exatamente o assunto), os <b>textos motivadores</b> (uma pequena coletânea que serve de estímulo — e da qual você não pode copiar trechos) e as <b>instruções</b> (número de linhas, se há título, o gênero). O erro mais grave e mais comum nasce justamente aqui: o candidato lê o tema por cima, escreve sobre um assunto parecido e <b>foge ao tema</b> — falha que zera ou reduz drasticamente a nota. Por isso, antes de qualquer palavra, sublinhe as palavras-chave do comando e mantenha o texto inteiro amarrado a elas.</p>
<p>Nos concursos da área social, como o da Sedes/DF, os temas tendem a girar em torno de <b>políticas públicas, cidadania, assistência social, desigualdade, serviço público e direitos fundamentais</b>. Vale, portanto, ter na manga um repertório voltado a esses assuntos: dispositivos da Constituição de 1988, o SUAS, dados do IBGE/IPEA e pensadores que tratam de justiça social. A correção, em regra, distribui a nota em quatro grandes eixos, descritos a seguir.</p>

<div class="box2">
  <div class="callout c-key">
    <h4>Os 4 critérios de correção</h4>
    <ul>
      <li><b>Conteúdo / abordagem do tema:</b> você atendeu exatamente ao que foi pedido e defendeu uma tese clara? É o item de maior peso.</li>
      <li><b>Estrutura textual:</b> há introdução, desenvolvimento e conclusão bem delimitados, com parágrafos organizados?</li>
      <li><b>Coesão e coerência:</b> as ideias se ligam por conectivos adequados e progridem com lógica, sem contradição nem repetição?</li>
      <li><b>Domínio da norma culta:</b> ortografia, acentuação, concordância, regência, pontuação e crase corretas.</li>
    </ul>
  </div>
  <div class="callout c-why">
    <h4>O que mais derruba a nota</h4>
    <ul>
      <li><b>Fuga ao tema</b> — releia o comando e sublinhe as palavras-chave antes de começar.</li>
      <li><b>Ausência de tese</b> — um texto que "fala sobre" o assunto sem tomar posição não argumenta.</li>
      <li><b>Senso comum e achismo</b> — sem repertório, o argumento não se sustenta.</li>
      <li><b>Erros de norma culta</b> — cada deslize de gramática custa pontos no eixo de língua.</li>
      <li><b>Desrespeito ao número de linhas</b> — abaixo do mínimo, penaliza; muito acima, idem.</li>
    </ul>
  </div>
</div>

<h2 class="section-title">2. A arquitetura do texto: quatro parágrafos</h2>
<p>O modelo mais seguro para concurso tem <b>quatro parágrafos</b>: uma introdução, dois parágrafos de desenvolvimento e uma conclusão. Essa arquitetura não é uma camisa de força arbitrária — ela organiza o raciocínio, garante equilíbrio entre as partes e facilita a vida do corretor, que encontra rapidamente a tese, os argumentos e o fechamento. Entender a função de cada parágrafo é mais importante do que decorar a forma.</p>

<p class="subhead">Parágrafo 1 — Introdução</p>
<p>A introdução tem duas tarefas: <b>apresentar o tema</b> (em uma ou duas frases que o contextualizem) e <b>fechar com a tese</b>, isto é, com o seu ponto de vista, já anunciando os dois argumentos que serão desenvolvidos. É a bússola do texto: depois de lê-la, o corretor já sabe o que você vai defender e por quê. Uma introdução típica tem de três a cinco linhas e termina, obrigatoriamente, com uma posição assumida.</p>

<p class="subhead">Parágrafos 2 e 3 — Desenvolvimento</p>
<p>Cada parágrafo de desenvolvimento defende <b>um único argumento</b>, na ordem em que foi anunciado na tese. A receita de cada um é a mesma: começa com um <b>tópico frasal</b> (a frase que anuncia o argumento), avança com a <b>argumentação apoiada em repertório</b> (uma lei, um dado, um autor, um fato) e termina com uma <b>frase de fechamento</b> que amarra a ideia. O segredo é a <b>progressão</b>: o segundo parágrafo precisa trazer um argumento diferente do primeiro, e não repeti-lo com outras palavras.</p>

<p class="subhead">Parágrafo 4 — Conclusão</p>
<p>A conclusão <b>retoma a tese</b> e os dois argumentos de forma sintética e apresenta um <b>encaminhamento</b> — uma proposta que indique quem deve agir, o que deve ser feito e com que finalidade. Ela não traz argumento novo nem termina com pergunta: seu papel é fechar, com firmeza, o círculo aberto na introdução.</p>

<table>
  <thead><tr><th style="width:16%">Parágrafo</th><th style="width:30%">Função</th><th>O que não pode faltar</th></tr></thead>
  <tbody>
    <tr><td><span class="rn">1. Introdução</span></td><td>Apresentar o tema e firmar a tese.</td><td>Contextualização + tese com os 2 eixos anunciados.</td></tr>
    <tr><td><span class="rn">2. Desenv. 1</span></td><td>Defender o 1º argumento.</td><td>Tópico frasal + repertório + fechamento.</td></tr>
    <tr><td><span class="rn">3. Desenv. 2</span></td><td>Defender o 2º argumento (progressão).</td><td>Argumento diferente do anterior, com novo repertório.</td></tr>
    <tr><td><span class="rn">4. Conclusão</span></td><td>Retomar a tese e propor solução.</td><td>Síntese dos eixos + proposta (agente + ação + finalidade).</td></tr>
  </tbody>
</table>

<h2 class="section-title">3. A introdução e a construção da tese</h2>
<p>A introdução vale muito porque é a primeira impressão e porque ali mora a tese. Há três maneiras eficientes de começá-la, e todas terminam do mesmo jeito: com o seu posicionamento. A <b>tese</b> segue uma fórmula simples e poderosa — declarar o que você defende e, na mesma frase, anunciar os dois eixos que vai desenvolver, no modelo: <i>"X depende tanto de [argumento 1] quanto de [argumento 2]"</i>. Quando a tese anuncia os dois argumentos, os parágrafos de desenvolvimento já estão definidos. Veja, abaixo, três introduções completas sobre o mesmo tema, cada uma usando uma estratégia de abertura diferente.</p>
<p style="margin-bottom:3px;"><span class="note-inline">Tema dos exemplos:</span> "Os desafios da proteção social da pessoa idosa no Brasil".</p>

<div class="example">
  <span class="lbl">Abertura por repertório legal/histórico</span>
  <p class="txt">O Estatuto do Idoso (Lei nº 10.741/2003) consolidou, no ordenamento brasileiro, a proteção integral à pessoa idosa, reconhecendo-a como sujeito pleno de direitos. Apesar desse marco, o envelhecimento acelerado da população expõe a fragilidade das políticas voltadas a esse grupo. Diante disso, a efetiva proteção social do idoso depende tanto da ampliação dos serviços de cuidado quanto do combate ao etarismo enraizado na sociedade.</p>
</div>
<div class="example">
  <span class="lbl">Abertura por contexto + problema</span>
  <p class="txt">O Brasil envelhece em ritmo mais veloz do que constrói as estruturas necessárias para acolher seus idosos. Embora a Constituição assegure a essa população amparo e dignidade, a realidade revela dificuldade de acesso à saúde, abandono e invisibilidade social. Nesse cenário, garantir a proteção do idoso exige medidas que aliem o cuidado público à mudança cultural.</p>
</div>
<div class="example">
  <span class="lbl">Abertura por conceito/definição</span>
  <p class="txt">Envelhecer com dignidade é mais do que prolongar a vida: é assegurar autonomia, cuidado e participação social. No Brasil, contudo, essa concepção ainda esbarra na escassez de serviços e no preconceito etário. Por isso, a proteção social do idoso constitui desafio que envolve, ao mesmo tempo, o fortalecimento das políticas de cuidado e a superação do etarismo.</p>
</div>
<div class="callout c-tip"><h4>Repare</h4>As três introduções mudam o início, mas terminam igual: com uma <b>tese</b> que toma posição e anuncia <b>dois eixos</b> (serviços de cuidado + combate ao etarismo). Esses dois eixos serão, exatamente, os dois parágrafos de desenvolvimento.</div>

<h2 class="section-title">4. O desenvolvimento: argumento sustentado por repertório</h2>
<p>É no desenvolvimento que a redação ganha ou perde força. Cada parágrafo deve conter um argumento bem delimitado e, sobretudo, <b>repertório produtivo</b> — uma informação externa (lei, dado, autor, fato) usada para comprovar o que se afirma. Repertório não é enfeite: citar um autor sem explicar sua relação com o tema não pontua. Os quatro tipos de repertório mais úteis para os temas da área social estão na tabela a seguir.</p>
<table>
  <thead><tr><th style="width:20%">Tipo de repertório</th><th style="width:40%">Exemplos para usar</th><th>Como empregar</th></tr></thead>
  <tbody>
    <tr><td><b>Legal / normativo</b></td><td>CF/88; SUAS (Lei 8.742/93); Estatuto do Idoso; ECA</td><td>"A Constituição de 1988 assegura…", ligando o direito ao argumento.</td></tr>
    <tr><td><b>Dados / estatística</b></td><td>IBGE; IPEA; PNAD; ONU</td><td>"Segundo o IBGE, …", para dimensionar o problema.</td></tr>
    <tr><td><b>Pensadores / autores</b></td><td>Amartya Sen (liberdades); Norberto Bobbio (direitos); Milton Santos (território)</td><td>"Conforme Amartya Sen, …", para fundamentar o raciocínio.</td></tr>
    <tr><td><b>Fato histórico / atualidade</b></td><td>Redemocratização; criação do SUAS; programas sociais</td><td>Para mostrar evolução ou contraste entre promessa e realidade.</td></tr>
  </tbody>
</table>
<p>Veja, abaixo, um parágrafo de desenvolvimento completo, escrito sobre o tema da proteção ao idoso, e a dissecação de suas três partes.</p>
<div class="example">
  <span class="lbl">Parágrafo de desenvolvimento (modelo)</span>
  <p class="txt"><b>Em primeiro lugar, a ampliação dos serviços de cuidado é condição para a proteção do idoso.</b> Equipamentos como os Centros de Convivência e os serviços de proteção do SUAS oferecem acompanhamento e combatem o isolamento social, um dos principais fatores de adoecimento na velhice. Segundo o IBGE, a população com mais de 60 anos deve praticamente dobrar nas próximas décadas, o que torna urgente o investimento em infraestrutura e em profissionais capacitados. <b>Dessa forma, sem uma rede de cuidado robusta, o direito à proteção permanece apenas no papel.</b></p>
</div>
<div class="box2">
  <div class="callout c-key"><h4>As três partes do parágrafo</h4>
    <ul>
      <li><b>Tópico frasal</b> (em negrito, início): anuncia o argumento.</li>
      <li><b>Argumentação + repertório</b> (meio): SUAS e dado do IBGE sustentam a ideia.</li>
      <li><b>Fechamento</b> (em negrito, fim): conclui o raciocínio do parágrafo.</li>
    </ul>
  </div>
  <div class="callout c-why"><h4>Erro a evitar no desenvolvimento</h4>
    <ul>
      <li>Jogar o repertório sem conectá-lo ao argumento ("Amartya Sen é um economista famoso." — e daí?).</li>
      <li>Trazer dois argumentos no mesmo parágrafo, perdendo a unidade.</li>
      <li>Encher linhas com repetição em vez de aprofundar a ideia.</li>
    </ul>
  </div>
</div>

<h2 class="section-title">5. A conclusão e a proposta de encaminhamento</h2>
<p>A conclusão começa com um conectivo conclusivo (<b>Portanto</b>, <b>Dessa forma</b>, <b>Diante do exposto</b>), retoma a tese e os dois argumentos em poucas palavras e termina com uma <b>proposta de encaminhamento</b>. Uma boa proposta responde a quatro perguntas: <b>quem</b> deve agir (o agente — poder público, sociedade civil, escolas), <b>o que</b> deve ser feito (a ação), <b>como</b> ou <b>por meio de quê</b> (o meio) e <b>para quê</b> (a finalidade). Quanto mais concreta, melhor. Abaixo, duas conclusões possíveis para o tema do idoso.</p>
<div class="example">
  <span class="lbl">Conclusão com proposta detalhada</span>
  <p class="txt">Portanto, a proteção social do idoso só se efetivará quando o poder público unir a ampliação dos serviços de cuidado ao enfrentamento do etarismo. Para isso, é necessário que os governos, em parceria com a sociedade civil, ampliem a rede de Centros de Convivência e promovam campanhas educativas de valorização da pessoa idosa, a fim de assegurar-lhe uma velhice digna.</p>
</div>
<div class="example">
  <span class="lbl">Conclusão mais sintética (também válida)</span>
  <p class="txt">Diante do exposto, garantir dignidade ao idoso exige tanto investimento em cuidado quanto mudança de mentalidade. Cabe ao Estado, ao lado da sociedade, fortalecer os serviços de proteção e combater o preconceito etário, de modo que envelhecer deixe de ser sinônimo de abandono.</p>
</div>
<div class="callout c-why"><h4>Na conclusão, nunca</h4>
  <ul>
    <li>Apresentar um argumento novo que não foi desenvolvido no texto.</li>
    <li>Terminar com pergunta retórica ou com frase vaga ("é preciso refletir sobre isso").</li>
    <li>Copiar a introdução palavra por palavra — retome com outras palavras.</li>
  </ul>
</div>

<h2 class="section-title">6. Coesão: os conectivos que ligam o texto</h2>
<p>Coesão é a amarração entre frases e parágrafos, e é um dos critérios de correção. O conectivo certo guia o leitor e mostra domínio da norma; o conectivo errado (usar "portanto" onde caberia "porque", por exemplo) compromete o sentido. Tenha à mão um repertório de conectivos organizados por função e evite repetir sempre os mesmos ("e", "mas", "então"). A tabela abaixo reúne os mais úteis para a redação.</p>
<table><thead><tr><th style="width:24%">Função no texto</th><th>Conectivos para usar</th></tr></thead><tbody>{conectivos_rows}</tbody></table>
<p>Além dos conectivos, a coesão se faz com a <b>retomada</b> de termos por pronomes e sinônimos (em vez de repetir a mesma palavra) e com a <b>progressão</b> das ideias — cada parágrafo deve acrescentar algo, nunca girar em torno do mesmo ponto.</p>

<h2 class="section-title">7. Os erros que mais derrubam a nota</h2>
<p>Conhecer o erro é metade do caminho para evitá-lo. A tabela a seguir reúne as falhas mais frequentes, com um exemplo do que <span class="er-x">não fazer</span> e a <span class="er-c">forma correta</span>.</p>
<table>
  <thead><tr><th style="width:24%">Erro</th><th style="width:38%">Exemplo do erro</th><th>Como corrigir</th></tr></thead>
  <tbody>{erros_rows}</tbody>
</table>

<h2 class="section-title pagebreak">8. Modelo NOTA MÁXIMA — comentado parágrafo a parágrafo</h2>
<p>Agora, a teoria aplicada. A redação abaixo seria avaliada com nota máxima. À esquerda está o texto; à direita, a análise que explica <b>por que cada parágrafo funciona</b>. Os destaques mostram os elementos-chave.</p>
<p style="margin-bottom:4px;"><span class="note-inline">Tema:</span> "A efetivação da assistência social como instrumento de redução das desigualdades no Brasil".</p>
<div class="legenda">
  <span class="lg-tese">tese</span>
  <span class="lg-con">conectivos / operadores</span>
  <span class="lg-rep">repertório</span>
</div>
{modelo_html}
<div class="callout c-key"><h4>Por que essa redação tira nota máxima</h4>
  <ul>
    <li><b>Tese clara</b> na introdução, com dois eixos que organizam todo o texto.</li>
    <li><b>Cada parágrafo</b> defende um argumento, com repertório produtivo (CF/88, SUAS, IBGE, Amartya Sen) ligado à ideia.</li>
    <li><b>Progressão real:</b> o segundo desenvolvimento avança para a ideia de autonomia, sem repetir o primeiro.</li>
    <li><b>Conclusão</b> retoma os dois eixos e propõe encaminhamento concreto (agente + ação + finalidade).</li>
    <li><b>Coesão</b> impecável (Não obstante, Desse modo, Ademais, Portanto) e <b>norma culta</b> sem deslizes.</li>
  </ul>
</div>

<h2 class="section-title">9. Passo a passo para escrever a sua redação</h2>
<p>Com a estrutura e as técnicas em mãos, siga este roteiro na hora da prova. Os primeiros minutos de planejamento valem mais do que parecem: é o rascunho mental da tese que evita a fuga ao tema e a falta de argumentos.</p>
<div class="passo">
  <div class="p"><b>Leia o comando e sublinhe as palavras-chave.</b> Defina, com exatidão, o que a banca pede. Sem isso, todo o resto pode ir por água abaixo. (2 a 3 minutos)</div>
  <div class="p"><b>Defina sua tese e os dois argumentos</b> num rascunho de três linhas. Só comece a escrever quando souber o que vai defender e com quais dois eixos.</div>
  <div class="p"><b>Liste o repertório</b> de cada parágrafo: uma lei, um dado, um autor ou um fato para cada argumento.</div>
  <div class="p"><b>Escreva a introdução:</b> uma ou duas frases de contexto e, ao final, a tese com os dois eixos anunciados.</div>
  <div class="p"><b>Escreva os dois desenvolvimentos:</b> tópico frasal → argumentação com repertório → frase de fechamento. Um argumento por parágrafo.</div>
  <div class="p"><b>Escreva a conclusão:</b> retome a tese e proponha o encaminhamento (agente + ação + meio + finalidade).</div>
  <div class="p"><b>Revise</b> concordância, regência, crase, pontuação, repetições e o número de linhas. Essa releitura final recupera pontos preciosos. (3 a 5 minutos)</div>
</div>
<div class="callout c-tip"><h4>Checklist final — confira antes de entregar</h4>
  <ul>
    <li>☐ A introdução tem tese clara, com posicionamento e dois eixos anunciados.</li>
    <li>☐ Cada parágrafo de desenvolvimento defende um argumento, com repertório produtivo.</li>
    <li>☐ A conclusão retoma a tese e traz proposta de encaminhamento.</li>
    <li>☐ O texto está em 3ª pessoa, formal, sem gíria nem "eu acho".</li>
    <li>☐ Há conectivos variados ligando frases e parágrafos.</li>
    <li>☐ A norma culta foi revisada e o número de linhas respeita o limite.</li>
  </ul>
</div>

</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("HTML gerado (denso):", OUT)
