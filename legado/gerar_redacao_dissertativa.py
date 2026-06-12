# -*- coding: utf-8 -*-
"""Material DENSO (apostila): Redação Dissertativo-Argumentativa para concurso (Quadrix).
Segue o Prompt Mestre (docs/prompt-mestre.md): prosa explicativa, exemplos por extenso,
2 modelos nota máxima comentados, técnicas, banco de repertório e roteiro de estudo.
SEM page-break por seção. Gera HTML (render via Chrome).
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(_HERE)
OUTDIR = os.path.join(_REPO, "materiais", "dia12-redacao-dissertativa")
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "Dia12_Redacao_Dissertativa.html")

MODELO = [
    {"rotulo": "Introdução",
     "texto": ("A Constituição Federal de 1988 inaugurou um novo paradigma ao reconhecer a "
        "<span class='rep'>assistência social como direito do cidadão e dever do Estado</span>, "
        "independentemente de contribuição. <span class='con'>Não obstante</span> esse avanço normativo, "
        "a efetivação plena desse direito ainda esbarra em obstáculos estruturais. <span class='con'>Desse modo</span>, "
        "<span class='tese'>a redução das desigualdades sociais no Brasil depende tanto do fortalecimento dos serviços "
        "socioassistenciais quanto da superação da cultura assistencialista que historicamente marcou o país.</span>"),
     "analise": [
        ("Contextualização", "Abre com um fato histórico-normativo (a CF/88) — repertório que situa o tema sem rodeios e já mostra conhecimento."),
        ("Problematização", "‘Não obstante esse avanço… esbarra em obstáculos’ cria a tensão entre o que a lei promete e o que a realidade entrega."),
        ("Tese (o coração do texto)", "A última frase toma posição e anuncia os DOIS eixos: (1) fortalecer serviços e (2) superar o assistencialismo. Cada eixo vira um parágrafo."),
     ]},
    {"rotulo": "Desenvolvimento 1",
     "texto": ("<span class='con'>Em primeiro lugar</span>, o fortalecimento da rede de proteção social mostra-se "
        "imprescindível. O <span class='rep'>Sistema Único de Assistência Social (SUAS)</span>, ao organizar serviços "
        "como os ofertados nos Centros de Referência de Assistência Social (CRAS), aproxima o Estado das famílias em "
        "situação de vulnerabilidade. <span class='con'>Segundo dados do IBGE</span>, milhões de brasileiros vivem abaixo "
        "da linha da pobreza, o que evidencia a relevância de equipamentos públicos capilarizados. <span class='con'>Assim</span>, "
        "investir em infraestrutura e em equipes técnicas qualificadas é condição para que a assistência deixe de ser promessa e se torne prática."),
     "analise": [
        ("Tópico frasal", "A 1ª frase anuncia o argumento (fortalecer a rede). Tudo no parágrafo serve a ela — unidade temática."),
        ("Repertório produtivo", "SUAS, CRAS e dados do IBGE não são enfeite: cada citação sustenta o argumento."),
        ("Fechamento", "‘Assim, investir… é condição’ arremata o raciocínio antes de passar ao próximo parágrafo."),
     ]},
    {"rotulo": "Desenvolvimento 2",
     "texto": ("<span class='con'>Ademais</span>, é preciso romper com a lógica do assistencialismo, que reduz o "
        "beneficiário à condição de mero receptor de favores. <span class='con'>Conforme o economista Amartya Sen</span>, "
        "<span class='rep'>o desenvolvimento deve ser compreendido como a ampliação das liberdades e das capacidades dos "
        "indivíduos</span>. <span class='con'>Nessa perspectiva</span>, programas de transferência de renda só cumprem seu "
        "papel quando articulados a ações de educação, qualificação profissional e geração de emprego, promovendo a autonomia e a emancipação dos cidadãos."),
     "analise": [
        ("Progressão", "‘Ademais’ marca um SEGUNDO argumento, diferente do primeiro: o texto avança em vez de repetir."),
        ("Repertório de autoridade", "Cita Amartya Sen com pertinência (liberdades e capacidades), ancorando o argumento da autonomia."),
        ("Aprofundamento", "Liga a transferência de renda à educação e ao trabalho — raciocínio próprio, não senso comum."),
     ]},
    {"rotulo": "Conclusão",
     "texto": ("<span class='con'>Portanto</span>, a assistência social só se concretizará como direito quando o Estado "
        "conjugar a ampliação dos serviços à promoção da autonomia dos beneficiários. <span class='con'>Para tanto</span>, "
        "<span class='rep'>é fundamental que o poder público, em parceria com a sociedade civil, amplie o financiamento do SUAS "
        "e invista na formação continuada dos servidores</span>, garantindo, dessa forma, que a proteção social seja, de fato, "
        "um instrumento de justiça e de redução das desigualdades."),
     "analise": [
        ("Retomada da tese", "Retoma os DOIS eixos da introdução (serviços + autonomia). Fecha o círculo aberto no começo."),
        ("Proposta concreta", "Aponta agente + ação + meio: poder público e sociedade civil ampliam financiamento e formação."),
        ("Fecho de impacto", "‘instrumento de justiça e de redução das desigualdades’ encerra retomando o tema, sem abrir assunto novo."),
     ]},
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

ARGUMENTOS = [
    ("Argumento de autoridade", "Apoia-se em lei, autor ou instituição reconhecida.", "“Conforme o art. 6º da Constituição, a assistência social é direito de todos…”"),
    ("Argumento por dados", "Usa estatística para dimensionar o problema.", "“Segundo o IBGE, milhões de brasileiros vivem abaixo da linha da pobreza…”"),
    ("Argumento por exemplificação", "Cita um caso ou programa concreto.", "“Programas como o de transferência de renda demonstram que…”"),
    ("Causa e consequência", "Mostra o encadeamento entre fatos.", "“A ausência de fiscalização gera a perpetuação do trabalho infantil…”"),
    ("Comparação / contraste", "Confronta épocas, grupos ou países.", "“Enquanto países desenvolvidos universalizaram a creche, o Brasil ainda…”"),
]

REPERTORIO = [
    ("CF/1988, art. 1º, III", "Dignidade da pessoa humana — fundamento da República.", "Qualquer tema de direitos e cidadania."),
    ("CF/1988, art. 3º", "Objetivos: erradicar a pobreza e reduzir desigualdades.", "Desigualdade social, pobreza, inclusão."),
    ("CF/1988, art. 6º", "Rol dos direitos sociais (educação, saúde, assistência…).", "Saúde, educação, moradia, assistência."),
    ("LOAS / SUAS — Lei 8.742/1993", "Organiza a assistência social como política pública.", "Assistência social, vulnerabilidade, SUAS."),
    ("ECA — Lei 8.069/1990", "Proteção integral à criança e ao adolescente.", "Infância, trabalho infantil, evasão escolar."),
    ("Estatuto do Idoso — Lei 10.741/2003", "Proteção integral à pessoa idosa.", "Envelhecimento, etarismo, cuidado."),
    ("Lei Maria da Penha — 11.340/2006", "Enfrentamento à violência doméstica e familiar.", "Violência de gênero, proteção à mulher."),
    ("Amartya Sen — Desenvolvimento como Liberdade", "Desenvolvimento = ampliação de liberdades e capacidades.", "Autonomia, emancipação, pobreza."),
    ("Norberto Bobbio — A Era dos Direitos", "O desafio não é fundamentar, mas efetivar direitos.", "Distância entre lei e realidade."),
    ("ONU — Agenda 2030 (ODS)", "Metas globais de redução da desigualdade e da fome.", "Pobreza, fome, desigualdade, sustentabilidade."),
]

ERROS = [
    ("Fugir do tema", "Escrever sobre algo próximo, mas não exatamente o que foi pedido — o erro que mais zera.",
     "Tema: ‘desafios da assistência social’. O candidato disserta sobre ‘pobreza no mundo’ em geral.",
     "Sublinhe as palavras-chave do comando e amarre cada parágrafo a elas."),
    ("Não tomar posição", "Introdução que ‘apresenta o assunto’ sem defender nada — sem tese não há argumentação.",
     "‘A assistência social é um tema muito importante e polêmico na atualidade.’",
     "Feche a introdução com tese que toma posição e anuncia os dois argumentos."),
    ("Senso comum / achismo", "Trocar repertório por frases prontas e vazias, que nada comprovam.",
     "‘Desde os primórdios da humanidade, todos sabem que a desigualdade é ruim.’",
     "Use repertório legítimo: uma lei, um dado, um autor."),
    ("1ª pessoa e informalidade", "A dissertação de concurso é impessoal e formal; gírias e ‘eu acho’ derrubam a língua.",
     "‘Eu acho que a gente precisa ajudar mais os pobres, né?’",
     "Use 3ª pessoa e registro formal: ‘É necessário que o Estado amplie a proteção social’."),
    ("Parágrafo sem unidade", "Misturar dois argumentos no mesmo parágrafo, perdendo o foco e a progressão.",
     "Um parágrafo que fala, ao mesmo tempo, de financiamento, educação e cultura.",
     "Um argumento por parágrafo, anunciado no tópico frasal."),
    ("Conclusão com tema novo", "Trazer no fim um argumento inédito que não foi desenvolvido — quebra a coerência.",
     "Concluir falando, pela 1ª vez, em ‘reforma tributária’, ausente no texto.",
     "A conclusão retoma o que já foi dito e propõe encaminhamento; nada de novidade."),
]


def render_modelo(m):
    analise = "".join(f"<div class='an-item'><span class='an-tag'>{t}</span> {d}</div>" for (t, d) in m["analise"])
    return (f"<div class='modelo-bloco'><div class='modelo-rotulo'>{m['rotulo']}</div>"
            f"<div class='modelo-grid'><div class='modelo-texto'>{m['texto']}</div>"
            f"<div class='modelo-analise'>{analise}</div></div></div>")


conectivos_rows = "".join(f"<tr><td><span class='rn'>{r}</span></td><td>{l}</td></tr>" for (r, l) in CONECTIVOS)
arg_rows = "".join(f"<tr><td><b>{n}</b></td><td>{d}</td><td><span class='er-c'>{e}</span></td></tr>" for (n, d, e) in ARGUMENTOS)
rep_rows = "".join(f"<tr><td><span class='rn'>{f}</span></td><td>{o}</td><td>{u}</td></tr>" for (f, o, u) in REPERTORIO)
erros_rows = "".join(f"<tr><td><b>{t}</b><br><span class='er-d'>{d}</span></td><td><span class='er-x'>✗ {ex}</span></td><td><span class='er-c'>✓ {c}</span></td></tr>" for (t, d, ex, c) in ERROS)
modelo_html = "".join(render_modelo(m) for m in MODELO)

CSS = """
@page { size:A4; margin:13mm 13mm 15mm 13mm; }
* { box-sizing:border-box; }
body { font-family:'Segoe UI','Helvetica Neue',Arial,sans-serif; color:#1d2733; font-size:11px; line-height:1.6; margin:0; orphans:3; widows:3; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
h1,h2,h3,h4 { margin:0; font-weight:700; }
p { margin:0 0 7px; text-align:justify; orphans:3; widows:3; }
.cover { height:250mm; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; background:linear-gradient(135deg,#064e3b 0%,#047857 55%,#065f46 100%); color:#fff; border-radius:6px; page-break-after:always; padding:0 24mm; }
.cover .kicker { letter-spacing:4px; font-size:12px; opacity:.85; font-weight:600; }
.cover h1 { font-size:43px; line-height:1.05; margin:10px 0 6px; }
.cover .sub { font-size:15px; font-weight:400; opacity:.95; max-width:140mm; }
.cover .rule { width:70px; height:4px; background:#ffd27a; margin:22px 0; border-radius:2px; }
.cover .meta { font-size:12.5px; opacity:.9; line-height:1.7; }
.cover .badge { margin-top:26px; background:rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.4); padding:9px 18px; border-radius:40px; font-size:13px; font-weight:600; }
.section-title { font-size:17px; color:#047857; border-bottom:3px solid #047857; padding-bottom:4px; margin:16px 0 9px; page-break-after:avoid; }
.section-title:first-of-type { margin-top:4px; }
.subhead { font-size:12.5px; color:#065f46; font-weight:700; margin:11px 0 4px; border-left:4px solid #047857; padding-left:8px; page-break-after:avoid; }
.example { background:#f3faf7; border:1px solid #cfeede; border-left:4px solid #047857; border-radius:6px; padding:8px 11px; margin:6px 0; page-break-inside:avoid; }
.example .lbl { display:inline-block; background:#047857; color:#fff; font-size:8px; font-weight:700; text-transform:uppercase; letter-spacing:.5px; padding:2px 8px; border-radius:10px; margin-bottom:4px; }
.example p { margin:0 0 5px; font-size:10.6px; line-height:1.6; }
.example p:last-child { margin-bottom:0; }
.example .txt { font-style:italic; color:#21303a; }
.note-inline { color:#0e7490; font-style:normal; font-weight:600; }
.box2 { display:grid; grid-template-columns:1fr 1fr; gap:9px; margin:7px 0; }
.callout { border-radius:7px; padding:9px 12px; page-break-inside:avoid; margin:6px 0; }
.c-key { background:#eefaf1; border-left:4px solid #047857; }
.c-why { background:#fff5f5; border-left:4px solid #c0392b; }
.c-tip { background:#eef9f7; border-left:4px solid #0e7490; }
.c-mnem { background:#fff8e6; border-left:4px solid #d4a017; }
.callout h4 { font-size:10.5px; margin-bottom:4px; text-transform:uppercase; letter-spacing:.4px; }
.c-key h4 { color:#047857; } .c-why h4 { color:#c0392b; } .c-tip h4 { color:#0e7490; } .c-mnem h4 { color:#a07400; }
.callout ul { margin:3px 0 0; padding-left:15px; } .callout li { margin:2.5px 0; }
table { width:100%; border-collapse:collapse; margin:7px 0; font-size:9.9px; page-break-inside:avoid; }
th { background:#064e3b; color:#fff; text-align:left; padding:6px 8px; }
td { border:1px solid #e2e6ee; padding:6px 8px; vertical-align:top; }
tr:nth-child(even) td { background:#f5faf8; }
td .rn { font-weight:700; color:#047857; }
.er-d { font-size:9px; color:#5a6573; } .er-x { color:#b3271e; } .er-c { color:#1f7a4d; }
.legenda { display:flex; gap:12px; flex-wrap:wrap; font-size:9px; margin:5px 0 9px; }
.legenda span { padding:2px 8px; border-radius:4px; font-weight:700; }
.lg-tese { background:#fde68a; color:#7c5e00; } .lg-con { background:#dbeafe; color:#1e40af; } .lg-rep { background:#dcfce7; color:#166534; }
.modelo-bloco { border:1px solid #d9e2dd; border-radius:9px; margin:0 0 9px; overflow:hidden; page-break-inside:avoid; }
.modelo-rotulo { background:#047857; color:#fff; font-weight:700; font-size:10px; text-transform:uppercase; letter-spacing:.5px; padding:4px 11px; }
.modelo-grid { display:grid; grid-template-columns:1.32fr 1fr; }
.modelo-texto { padding:10px 12px; font-size:10.3px; line-height:1.66; text-align:justify; border-right:1px solid #eef0f4; }
.modelo-analise { padding:9px 11px; background:#fafbfd; }
.an-item { font-size:8.9px; line-height:1.45; margin-bottom:6px; color:#46536a; }
.an-tag { display:inline-block; background:#047857; color:#fff; font-weight:700; font-size:7.8px; text-transform:uppercase; letter-spacing:.3px; padding:1px 6px; border-radius:10px; margin-bottom:2px; }
.tese { background:#fde68a; border-radius:3px; padding:0 2px; font-weight:600; }
.con { background:#dbeafe; border-radius:3px; padding:0 2px; }
.rep { background:#dcfce7; border-radius:3px; padding:0 2px; }
.passo { counter-reset:step; margin-top:4px; }
.passo .p { position:relative; padding-left:30px; margin-bottom:7px; font-size:10.5px; text-align:justify; }
.passo .p::before { counter-increment:step; content:counter(step); position:absolute; left:0; top:-1px; width:21px; height:21px; background:#047857; color:#fff; border-radius:50%; text-align:center; line-height:21px; font-weight:700; font-size:11px; }
.pagebreak { page-break-before:always; }
"""

HTML = f"""<!DOCTYPE html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body>

<div class="cover">
  <div class="kicker">REDAÇÃO</div>
  <h1>Dissertativo-<br>Argumentativa</h1>
  <div class="rule"></div>
  <div class="sub">Apostila completa: teoria, técnicas, banco de repertório, como estudar e DOIS modelos nota máxima comentados</div>
  <div class="meta" style="margin-top:26px;">Concurso <b>Sedes/DF</b> · Banca <b>Quadrix</b> · 2026<br>Técnico Administrativo (Cargo 202)</div>
  <div class="badge">Dia 12 · Estrutura da redação</div>
</div>

<h2 class="section-title">1. O que é a redação de concurso e o que a banca cobra</h2>
<p>A redação exigida em concursos como os da Quadrix é a <b>dissertativo-argumentativa</b>. Dissertar é expor ideias de forma organizada sobre um assunto; argumentar é defender um <b>ponto de vista</b> com razões que o sustentem. Reunindo as duas coisas, o que se pede é um texto em que você assume uma posição clara diante de um tema e a comprova com argumentos consistentes, em linguagem formal e impessoal. Não se trata de narrar uma história, de descrever algo nem de simplesmente opinar: trata-se de <b>convencer</b> o leitor pelo raciocínio.</p>
<p>O comando da prova costuma ter três partes que você precisa ler com atenção: o <b>tema</b> (a frase que delimita exatamente o assunto), os <b>textos motivadores</b> (uma pequena coletânea que serve de estímulo — e da qual você não pode copiar trechos) e as <b>instruções</b> (número de linhas, se há título, o gênero). O erro mais grave e mais comum nasce justamente aqui: o candidato lê o tema por cima, escreve sobre um assunto parecido e <b>foge ao tema</b> — falha que zera ou reduz drasticamente a nota. Por isso, antes de qualquer palavra, sublinhe as palavras-chave do comando e mantenha o texto inteiro amarrado a elas.</p>
<p>Nos concursos da área social, como o da Sedes/DF, os temas tendem a girar em torno de <b>políticas públicas, cidadania, assistência social, desigualdade, serviço público e direitos fundamentais</b>. Vale, portanto, ter na manga um repertório voltado a esses assuntos — algo que este material organiza mais adiante, num banco pronto para memorizar. A correção, em regra, distribui a nota em quatro grandes eixos.</p>
<div class="box2">
  <div class="callout c-key"><h4>Os 4 critérios de correção</h4>
    <ul>
      <li><b>Conteúdo / abordagem do tema:</b> atendeu exatamente ao pedido e defendeu uma tese clara? É o item de maior peso.</li>
      <li><b>Estrutura textual:</b> introdução, desenvolvimento e conclusão bem delimitados, com parágrafos organizados?</li>
      <li><b>Coesão e coerência:</b> as ideias se ligam por conectivos adequados e progridem com lógica?</li>
      <li><b>Domínio da norma culta:</b> ortografia, acentuação, concordância, regência, pontuação e crase.</li>
    </ul></div>
  <div class="callout c-why"><h4>O que mais derruba a nota</h4>
    <ul>
      <li><b>Fuga ao tema</b> — releia o comando e sublinhe as palavras-chave.</li>
      <li><b>Ausência de tese</b> — texto que "fala sobre" sem tomar posição.</li>
      <li><b>Senso comum</b> — sem repertório, o argumento não se sustenta.</li>
      <li><b>Erros de norma culta</b> — cada deslize custa pontos.</li>
      <li><b>Desrespeito ao número de linhas</b> — abaixo do mínimo, penaliza.</li>
    </ul></div>
</div>

<h2 class="section-title">2. Como dissecar o tema e construir a tese</h2>
<p>Antes de escrever, é preciso decompor o tema. Esse planejamento de poucos minutos é o que separa a redação que flui da redação que trava na metade. O processo tem quatro passos: identificar o núcleo do tema, levantar ideias (causas, consequências, soluções), escolher os dois eixos mais férteis e transformá-los em tese. Veja o processo aplicado a um tema real.</p>
<div class="example">
  <span class="lbl">Exemplo resolvido — dissecando o tema</span>
  <p><b>Tema:</b> "A persistência do trabalho infantil no Brasil".</p>
  <p><b>1) Núcleo:</b> não basta falar de "trabalho infantil"; o comando pede explicar por que ele <b>ainda persiste</b>. O foco é a causa e a permanência do problema.</p>
  <p><b>2) Levantamento:</b> causas — vulnerabilidade econômica das famílias, evasão escolar, naturalização cultural, fiscalização insuficiente; consequências — perda da infância, perpetuação da pobreza.</p>
  <p><b>3) Escolha de 2 eixos</b> que rendam um parágrafo cada: (a) a <b>vulnerabilidade socioeconômica</b> que empurra a criança ao trabalho; (b) a <b>falha do Estado</b> na fiscalização e na garantia da escola.</p>
  <p><b>4) Tese:</b> "<span class='txt'>A superação do trabalho infantil no Brasil depende tanto do enfrentamento da vulnerabilidade econômica das famílias quanto do fortalecimento da fiscalização e da escola pública.</span>"</p>
</div>
<div class="callout c-mnem"><h4>Mnemônico — N.I.E.T.</h4><b>N</b>úcleo do tema → <b>I</b>deias (causas/consequências) → <b>E</b>scolha de 2 eixos → <b>T</b>ese. Decore essa ordem: ela cabe em 3 minutos de rascunho e evita a fuga ao tema.</div>

<h2 class="section-title">3. A arquitetura do texto: quatro parágrafos</h2>
<p>O modelo mais seguro para concurso tem <b>quatro parágrafos</b>: uma introdução, dois de desenvolvimento e uma conclusão. Essa arquitetura organiza o raciocínio, garante equilíbrio entre as partes e facilita a vida do corretor, que encontra rapidamente a tese, os argumentos e o fechamento. Entender a função de cada parágrafo importa mais do que decorar a forma.</p>
<p class="subhead">Parágrafo 1 — Introdução</p>
<p>Tem duas tarefas: <b>apresentar o tema</b> (uma ou duas frases de contexto) e <b>fechar com a tese</b>, anunciando os dois argumentos que serão desenvolvidos. É a bússola do texto: depois de lê-la, o corretor já sabe o que você defende e por quê. Tem de três a cinco linhas e termina, sempre, com uma posição assumida.</p>
<p class="subhead">Parágrafos 2 e 3 — Desenvolvimento</p>
<p>Cada um defende <b>um único argumento</b>, na ordem anunciada na tese. A receita: <b>tópico frasal</b> (anuncia o argumento) + <b>argumentação com repertório</b> (lei, dado, autor, fato) + <b>frase de fechamento</b>. O segredo é a <b>progressão</b>: o segundo parágrafo traz um argumento diferente do primeiro, não a mesma ideia reescrita.</p>
<p class="subhead">Parágrafo 4 — Conclusão</p>
<p><b>Retoma a tese</b> e os dois argumentos de forma sintética e apresenta um <b>encaminhamento</b> — uma proposta indicando quem deve agir, o que deve ser feito e com que finalidade. Não traz argumento novo nem termina com pergunta.</p>
<table>
  <thead><tr><th style="width:16%">Parágrafo</th><th style="width:30%">Função</th><th>O que não pode faltar</th></tr></thead>
  <tbody>
    <tr><td><span class="rn">1. Introdução</span></td><td>Apresentar o tema e firmar a tese.</td><td>Contextualização + tese com os 2 eixos anunciados.</td></tr>
    <tr><td><span class="rn">2. Desenv. 1</span></td><td>Defender o 1º argumento.</td><td>Tópico frasal + repertório + fechamento.</td></tr>
    <tr><td><span class="rn">3. Desenv. 2</span></td><td>Defender o 2º argumento (progressão).</td><td>Argumento diferente, com novo repertório.</td></tr>
    <tr><td><span class="rn">4. Conclusão</span></td><td>Retomar a tese e propor solução.</td><td>Síntese + proposta (agente + ação + finalidade).</td></tr>
  </tbody>
</table>

<h2 class="section-title">4. A introdução em três modelos completos</h2>
<p>Há três maneiras eficientes de abrir a introdução, e todas terminam do mesmo jeito: com a tese. A <b>tese</b> segue uma fórmula simples — declarar o que você defende e anunciar, na mesma frase, os dois eixos: <i>"X depende tanto de [argumento 1] quanto de [argumento 2]"</i>. Veja três introduções completas sobre o mesmo tema, cada uma com uma estratégia de abertura.</p>
<p style="margin-bottom:3px;"><span class="note-inline">Tema dos exemplos:</span> "Os desafios da proteção social da pessoa idosa no Brasil".</p>
<div class="example"><span class="lbl">Abertura por repertório legal/histórico</span>
  <p class="txt">O Estatuto do Idoso (Lei nº 10.741/2003) consolidou, no ordenamento brasileiro, a proteção integral à pessoa idosa, reconhecendo-a como sujeito pleno de direitos. Apesar desse marco, o envelhecimento acelerado da população expõe a fragilidade das políticas voltadas a esse grupo. Diante disso, a efetiva proteção social do idoso depende tanto da ampliação dos serviços de cuidado quanto do combate ao etarismo enraizado na sociedade.</p></div>
<div class="example"><span class="lbl">Abertura por contexto + problema</span>
  <p class="txt">O Brasil envelhece em ritmo mais veloz do que constrói as estruturas necessárias para acolher seus idosos. Embora a Constituição assegure a essa população amparo e dignidade, a realidade revela dificuldade de acesso à saúde, abandono e invisibilidade social. Nesse cenário, garantir a proteção do idoso exige medidas que aliem o cuidado público à mudança cultural.</p></div>
<div class="example"><span class="lbl">Abertura por conceito/definição</span>
  <p class="txt">Envelhecer com dignidade é mais do que prolongar a vida: é assegurar autonomia, cuidado e participação social. No Brasil, contudo, essa concepção ainda esbarra na escassez de serviços e no preconceito etário. Por isso, a proteção social do idoso constitui desafio que envolve, ao mesmo tempo, o fortalecimento das políticas de cuidado e a superação do etarismo.</p></div>
<div class="callout c-tip"><h4>Repare</h4>As três mudam o início, mas terminam igual: com uma <b>tese</b> que toma posição e anuncia <b>dois eixos</b> (serviços de cuidado + combate ao etarismo). Esses eixos serão, exatamente, os dois parágrafos de desenvolvimento.</div>

<h2 class="section-title">5. O desenvolvimento: tipos de argumento e repertório</h2>
<p>É no desenvolvimento que a redação ganha ou perde força. Cada parágrafo precisa de um argumento bem delimitado e de <b>repertório produtivo</b> — uma informação externa usada para comprovar o que se afirma. Existem cinco tipos de argumento que você pode combinar; dominá-los dá variedade ao texto e evita a repetição do mesmo recurso.</p>
<table>
  <thead><tr><th style="width:24%">Tipo de argumento</th><th style="width:34%">Como funciona</th><th>Exemplo de uso</th></tr></thead>
  <tbody>{arg_rows}</tbody>
</table>
<p>Qualquer que seja o tipo, o parágrafo segue a mesma estrutura interna. Veja um parágrafo de desenvolvimento completo, sobre o tema do idoso, com a dissecação de suas três partes.</p>
<div class="example"><span class="lbl">Parágrafo de desenvolvimento (modelo)</span>
  <p class="txt"><b>Em primeiro lugar, a ampliação dos serviços de cuidado é condição para a proteção do idoso.</b> Equipamentos como os Centros de Convivência e os serviços de proteção do SUAS oferecem acompanhamento e combatem o isolamento social, um dos principais fatores de adoecimento na velhice. Segundo o IBGE, a população com mais de 60 anos deve praticamente dobrar nas próximas décadas, o que torna urgente o investimento em infraestrutura e em profissionais capacitados. <b>Dessa forma, sem uma rede de cuidado robusta, o direito à proteção permanece apenas no papel.</b></p></div>
<div class="box2">
  <div class="callout c-key"><h4>As três partes do parágrafo</h4>
    <ul>
      <li><b>Tópico frasal</b> (início, em negrito): anuncia o argumento.</li>
      <li><b>Argumentação + repertório</b> (meio): SUAS e dado do IBGE sustentam a ideia.</li>
      <li><b>Fechamento</b> (fim, em negrito): conclui o raciocínio do parágrafo.</li>
    </ul></div>
  <div class="callout c-why"><h4>Erros a evitar no desenvolvimento</h4>
    <ul>
      <li>Jogar o repertório sem conectá-lo ("Amartya Sen é famoso." — e daí?).</li>
      <li>Trazer dois argumentos no mesmo parágrafo, perdendo a unidade.</li>
      <li>Encher linhas com repetição em vez de aprofundar a ideia.</li>
    </ul></div>
</div>

<h2 class="section-title">6. A conclusão e a proposta de encaminhamento</h2>
<p>A conclusão começa com um conectivo conclusivo (<b>Portanto</b>, <b>Dessa forma</b>, <b>Diante do exposto</b>), retoma a tese e os dois argumentos em poucas palavras e termina com uma <b>proposta de encaminhamento</b>. Uma boa proposta responde a quatro perguntas: <b>quem</b> deve agir (agente), <b>o que</b> deve ser feito (ação), <b>como</b> (meio) e <b>para quê</b> (finalidade). Quanto mais concreta, melhor.</p>
<div class="example"><span class="lbl">Conclusão com proposta detalhada</span>
  <p class="txt">Portanto, a proteção social do idoso só se efetivará quando o poder público unir a ampliação dos serviços de cuidado ao enfrentamento do etarismo. Para isso, é necessário que os governos, em parceria com a sociedade civil, ampliem a rede de Centros de Convivência e promovam campanhas educativas de valorização da pessoa idosa, a fim de assegurar-lhe uma velhice digna.</p></div>
<div class="example"><span class="lbl">Conclusão mais sintética (também válida)</span>
  <p class="txt">Diante do exposto, garantir dignidade ao idoso exige tanto investimento em cuidado quanto mudança de mentalidade. Cabe ao Estado, ao lado da sociedade, fortalecer os serviços de proteção e combater o preconceito etário, de modo que envelhecer deixe de ser sinônimo de abandono.</p></div>
<div class="callout c-why"><h4>Na conclusão, nunca</h4>
  <ul>
    <li>Apresentar argumento novo não desenvolvido no texto.</li>
    <li>Terminar com pergunta retórica ou frase vaga ("é preciso refletir").</li>
    <li>Copiar a introdução palavra por palavra — retome com outras palavras.</li>
  </ul></div>

<h2 class="section-title">7. Coesão: os conectivos que ligam o texto</h2>
<p>Coesão é a amarração entre frases e parágrafos, e é critério de correção. O conectivo certo guia o leitor e mostra domínio da norma; o errado (usar "portanto" onde caberia "porque") compromete o sentido. Tenha um repertório por função e evite repetir sempre os mesmos ("e", "mas", "então").</p>
<table><thead><tr><th style="width:24%">Função no texto</th><th>Conectivos para usar</th></tr></thead><tbody>{conectivos_rows}</tbody></table>
<p>Além dos conectivos, a coesão se faz com a <b>retomada</b> de termos por pronomes e sinônimos (em vez de repetir a mesma palavra) e com a <b>progressão</b> — cada parágrafo acrescenta algo, nunca gira em torno do mesmo ponto.</p>

<h2 class="section-title">8. Banco de repertório para a área social</h2>
<p>Repertório se prepara <b>antes</b> da prova. Decore um conjunto de "coringas" — leis, autores e dados que servem a vários temas — e treine encaixá-los. A tabela abaixo reúne os mais versáteis para os temas que costumam cair em concursos da área social. Em provas, prefira citar a fonte de forma segura; para números específicos, confira a fonte atual antes de afirmar. <span class="note-inline">[CONFERIR FONTE ATUAL]</span> para estatísticas exatas.</p>
<table>
  <thead><tr><th style="width:30%">Repertório coringa</th><th style="width:38%">O que diz</th><th>Onde encaixa</th></tr></thead>
  <tbody>{rep_rows}</tbody>
</table>
<div class="callout c-mnem"><h4>Como usar o banco</h4>Escolha <b>2 a 3 repertórios por tema</b> e distribua um por parágrafo. Nunca cite por citar: sempre explique, em uma frase, a relação do repertório com o argumento que está defendendo.</div>

<h2 class="section-title">9. Como estudar e treinar a redação</h2>
<p>Redação não se aprende lendo teoria — aprende-se <b>escrevendo e corrigindo</b>. O cronograma reserva dias específicos para escrever uma redação; aproveite-os com método. Uma rotina eficiente combina produção, correção e construção de repertório, em ciclos curtos e constantes.</p>
<div class="box2">
  <div class="callout c-key"><h4>Rotina semanal sugerida</h4>
    <ul>
      <li><b>Escreva 1 redação completa</b> no tempo real da prova (cronometre ~1h a 1h30).</li>
      <li><b>Deixe descansar um dia</b> e corrija com o checklist final deste material, como se fosse o corretor.</li>
      <li><b>Treino de tese:</b> pegue 5 temas e escreva só introdução + tese, 10 minutos cada. É o que mais combate a fuga ao tema.</li>
      <li><b>Dissecação:</b> leia 1 redação nota máxima e marque tese, repertório e conectivos.</li>
    </ul></div>
  <div class="callout c-tip"><h4>O que treinar em paralelo</h4>
    <ul>
      <li><b>Banco de repertório:</b> memorize 8 a 10 coringas da tabela da seção 8.</li>
      <li><b>Gramática dos erros recorrentes:</b> use os dias de Português (crase, concordância, regência, pontuação).</li>
      <li><b>Letra e linhas:</b> treine caber a estrutura no número de linhas com letra legível.</li>
      <li><b>Atualidades da área:</b> acompanhe temas de assistência social e serviço público.</li>
    </ul></div>
</div>

<h2 class="section-title">10. Os erros que mais derrubam a nota</h2>
<p>Conhecer o erro é metade do caminho para evitá-lo. A tabela reúne as falhas mais frequentes, com um exemplo do que <span class="er-x">não fazer</span> e a <span class="er-c">forma correta</span>.</p>
<table><thead><tr><th style="width:24%">Erro</th><th style="width:38%">Exemplo do erro</th><th>Como corrigir</th></tr></thead><tbody>{erros_rows}</tbody></table>

<h2 class="section-title pagebreak">11. Modelo NOTA MÁXIMA &#8470;1 — comentado</h2>
<p>A teoria aplicada. À esquerda, o texto; à direita, a análise de <b>por que cada parágrafo funciona</b>. Os destaques marcam os elementos-chave.</p>
<p style="margin-bottom:4px;"><span class="note-inline">Tema:</span> "A efetivação da assistência social como instrumento de redução das desigualdades no Brasil".</p>
<div class="legenda"><span class="lg-tese">tese</span><span class="lg-con">conectivos</span><span class="lg-rep">repertório</span></div>
{modelo_html}
<div class="callout c-key"><h4>Por que essa redação tira nota máxima</h4>
  <ul>
    <li><b>Tese clara</b> na introdução, com dois eixos que organizam todo o texto.</li>
    <li><b>Cada parágrafo</b> defende um argumento, com repertório produtivo (CF/88, SUAS, IBGE, Amartya Sen) ligado à ideia.</li>
    <li><b>Progressão real:</b> o D2 avança para a ideia de autonomia, sem repetir o D1.</li>
    <li><b>Conclusão</b> retoma os dois eixos e propõe encaminhamento concreto.</li>
    <li><b>Coesão</b> impecável e <b>norma culta</b> sem deslizes.</li>
  </ul></div>

<h2 class="section-title">12. Modelo NOTA MÁXIMA &#8470;2 — serviço público</h2>
<p>Um segundo modelo, sobre tema típico para o cargo, mostra que a <b>mesma estrutura</b> se adapta a qualquer assunto. Leia notando a tese ao fim da introdução, o repertório em cada desenvolvimento e a proposta na conclusão.</p>
<p style="margin-bottom:4px;"><span class="note-inline">Tema:</span> "A importância da qualidade no atendimento ao público nos órgãos da Administração".</p>
<div class="example"><span class="lbl">Introdução</span>
  <p class="txt">A Constituição de 1988 erigiu a eficiência a princípio da Administração Pública (art. 37), vinculando o serviço estatal à satisfação do cidadão. Todavia, filas, descaso e burocracia ainda marcam a relação entre o poder público e a população. Desse modo, aprimorar a qualidade do atendimento depende tanto da capacitação contínua dos servidores quanto da modernização tecnológica dos órgãos públicos.</p></div>
<div class="example"><span class="lbl">Desenvolvimento 1 — capacitação</span>
  <p class="txt">Inicialmente, a formação dos servidores é decisiva para um atendimento de qualidade. Um agente preparado compreende que sua função é servir ao cidadão, tratando-o com urbanidade e eficiência — deveres previstos nos estatutos funcionais. A ausência de capacitação, por outro lado, gera atendimentos hostis e decisões equivocadas, que minam a confiança na Administração. Assim, investir em treinamento permanente é transformar o servidor em instrumento efetivo do interesse público.</p></div>
<div class="example"><span class="lbl">Desenvolvimento 2 — modernização</span>
  <p class="txt">Ademais, a modernização tecnológica é igualmente indispensável. A digitalização de serviços, os canais de autoatendimento e os sistemas integrados reduzem filas e encurtam prazos, materializando o princípio da eficiência. A Lei nº 14.129/2021, que institui o Governo Digital, evidencia esse caminho ao estimular a prestação digital de serviços públicos. Dessa forma, aliar tecnologia à simplificação de processos devolve ao cidadão tempo e dignidade.</p></div>
<div class="example"><span class="lbl">Conclusão</span>
  <p class="txt">Portanto, a qualidade do atendimento público só se concretiza quando capacitação e tecnologia caminham juntas. Para tanto, cabe à Administração, em parceria com as escolas de governo, promover a formação continuada dos servidores e ampliar a oferta de serviços digitais, a fim de que o atendimento ao cidadão seja, de fato, expressão de respeito e de eficiência.</p></div>
<div class="callout c-key"><h4>O que se repete dos dois modelos (a fórmula)</h4>
  <ul>
    <li>Introdução com repertório + problema + <b>tese de dois eixos</b>.</li>
    <li>Dois desenvolvimentos, cada um com tópico frasal, repertório (art. 37; Lei 14.129/2021) e fechamento.</li>
    <li>Conclusão que retoma os eixos e traz <b>proposta com agente, ação e finalidade</b>.</li>
  </ul></div>

<h2 class="section-title">13. Passo a passo na hora da prova + checklist</h2>
<p>Com estrutura e técnica em mãos, siga este roteiro. Os primeiros minutos de planejamento valem mais do que parecem: é o rascunho da tese que evita a fuga ao tema e a falta de argumentos.</p>
<div class="passo">
  <div class="p"><b>Leia o comando e sublinhe as palavras-chave.</b> Defina, com exatidão, o que a banca pede. (2 a 3 min)</div>
  <div class="p"><b>Disseque o tema com o N.I.E.T.</b> (núcleo → ideias → 2 eixos → tese). Só comece a escrever com a tese pronta.</div>
  <div class="p"><b>Liste o repertório</b> de cada parágrafo: uma lei, um dado, um autor ou um fato por argumento.</div>
  <div class="p"><b>Escreva a introdução:</b> contexto + tese com os dois eixos anunciados.</div>
  <div class="p"><b>Escreva os dois desenvolvimentos:</b> tópico frasal → argumentação com repertório → fechamento.</div>
  <div class="p"><b>Escreva a conclusão:</b> retome a tese e proponha o encaminhamento (agente + ação + meio + finalidade).</div>
  <div class="p"><b>Revise</b> concordância, regência, crase, pontuação, repetições e o número de linhas. (3 a 5 min)</div>
</div>
<div class="callout c-tip"><h4>Checklist final — confira antes de entregar</h4>
  <ul>
    <li>☐ A introdução tem tese clara, com posicionamento e dois eixos anunciados.</li>
    <li>☐ Cada desenvolvimento defende um argumento, com repertório produtivo.</li>
    <li>☐ A conclusão retoma a tese e traz proposta de encaminhamento.</li>
    <li>☐ Texto em 3ª pessoa, formal, sem gíria nem "eu acho".</li>
    <li>☐ Conectivos variados ligando frases e parágrafos.</li>
    <li>☐ Norma culta revisada e número de linhas dentro do limite.</li>
  </ul></div>

</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("HTML gerado (denso, ampliado):", OUT)
