# -*- coding: utf-8 -*-
"""Material DENSO (apostila) — Dia 8: Direito Constitucional, Organizacao do Estado
e Administracao Publica (arts. 18-44). Teoria + lei seca comentada + 35 questoes
(15 C/E + 20 A-E) com gabarito comentado. Segue docs/prompt-mestre.md.
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(_HERE)
OUTDIR = os.path.join(_REPO, "materiais", "dia08-organizacao-estado")
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "Dia8_Organizacao_Estado.html")

QCE = [
    ("A Republica Federativa do Brasil é formada pela Uniao, pelos Estados, pelo Distrito Federal e pelos Municipios.",
     "C", "Literalidade do art. 1º. Os quatro entes federados sao os unicos."),
    ("O Distrito Federal é equiparado aos Estados para fins de divisao de competencias.",
     "E", "Errado. O DF tem regime juridico proprio; nao é puro Estado nem puro Municipio. Troca tipica."),
    ("Cada Estado tem liberdade para organizar sua Administracao conforme entender conveniente.",
     "E", "Errado. Os Estados devem seguir o padrao federal (art. 25, parágrafo 1º). Nao há liberdade irrestrita."),
    ("A competencia legislativa concorrente significa que Uniao e Estados legislam sobre o mesmo assunto, mas a lei estadual prevalece.",
     "E", "Errado. Sobre o mesmo assunto sim, mas a Uniao fixa normas gerais; a lei estadual fica restrita (art. 24, parágrafo 2º)."),
    ("O Municipio é pessoa juridica de direito publico interno, competente para gerir seus interesses locais.",
     "C", "Correto. Art. 1º, parágrafo unico. O Municipio tem autonomia (receita, administracao, legislacao)."),
    ("A Uniao pode intervir em Estado ou Municipio sem decisao judicial previa.",
     "E", "Errado. A intervencao depende de requisitos e, em regra, de autorizacao judicial (arts. 34-36)."),
    ("Os Poderes da Uniao sao os três: Legislativo, Executivo e Judiciario.",
     "C", "Correto. Art. 2º. Separacao entre poderes."),
    ("O Congresso Nacional é composto apenas pela Camara dos Deputados.",
     "E", "Errado. Congresso Nacional = Camara dos Deputados + Senado Federal (art. 28, parágrafo 4º)."),
    ("A Camara dos Deputados tem 513 membros, exceto em anos de eleicao.",
     "E", "Errado. Sao sempre 513 deputados, independentemente de eleicao (art. 45, parágrafo 1º). Numero fixo."),
    ("O Senado tem 3 senadores por Estado, totalizando 81 senadores.",
     "C", "Correto. 3 x 27 (26 Estados + 1 DF) = 81 (art. 46, parágrafo 1º)."),
    ("A aprovacao de lei complementar exige quorum de maioria absoluta.",
     "C", "Correto. Lei complementar pede quorum mais exigente (maioria absoluta) que lei ordinaria."),
    ("Decreto-lei e medida provisoria sao a mesma coisa.",
     "E", "Errado. Decreto-lei nao existe mais (abolido em 1988). Medida provisoria é o instrumento moderno."),
    ("Medida provisoria perde eficacia automaticamente se nao for votada em 60 dias.",
     "C", "Correto. MP tem validade de 60 dias, podendo ser prorrogada uma vez por mais 60 (art. 62, parágrafo 3º)."),
    ("O veto presidencial pode ser derrubado por maioria absoluta do Congresso.",
     "E", "Errado. Derruba-se veto com maioria de 2/5 dos deputados e senadores (art. 66, parágrafo 4º)."),
    ("O Presidente da Republica é simultaneamente Chefe de Estado e Chefe de Governo.",
     "C", "Correto. Sistema presidencialista: Presidente acumula os dois papéis (art. 76)."),
]

QME = [
    ("Federacao", "A Republica Federativa do Brasil é constituída por",
     ["apenas a Uniao e os Estados, excluídos Distrito Federal e Municipios.",
      "Uniao, Estados, Distrito Federal e Municipios.",
      "Uniao e Municipios, sendo os Estados territoriais administrativos.",
      "28 Estados, sendo o DF assimilado a um Estado.",
      "Uniao e Estados em regime de soberania compartilhada com Municipios autonomos."],
     1, "Gabarito B: os quatro entes federados (art. 1º). A: exclui entes constituintes. C, D, E: conceituacoes erradas."),
    ("Competencia", "A competencia legislativa concorrente entre Uniao e Estados sobre a mesma matéria significa que",
     ["ambas tem liberdade legislativa total; a posterior prevalece.",
      "a lei estadual prevalece sempre sobre a federal.",
      "a Uniao fixa normas gerais e o Estado pode complementar, respeitando as normas gerais.",
      "apenas a Uniao legisla; o Estado executa.",
      "a lei municipal absorve ambas as competencias."],
     2, "Gabarito C: Uniao fixa normas gerais; Estado legisla em caráter complementar (art. 24, parágrafo 2º). A, B: falta a hierarquia. D, E: incorretos."),
    ("Municipio", "Quanto a autonomia municipal, é correto afirmar que o Municipio",
     ["nao é pessoa juridica; é meramente divisao administrativa do Estado.",
      "é pessoa juridica com autonomia em matéria de receita, administracao e legislacao de interesse local.",
      "tem a mesma competencia legislativa que o Estado.",
      "pode legislar sobre matéria de competencia privativa da Uniao.",
      "nao pode cobrar tributos, pois essa funcao é exclusiva do Estado."],
     1, "Gabarito B: autonomia em receita, administracao e legislacao local (art. 30). A: é sim pessoa juridica. C, D: competencias restritas. E: pode cobrar tributos."),
    ("Intervencao", "A intervencao federal em Estado ou Municipio",
     ["pode ocorrer por decisao unilateral do Presidente, sem outras exigencias.",
      "está autorizada apenas em caso de guerra externa.",
      "pode ocorrer, conforme requisitos legais, e geralmente requer decisao judicial (em certos casos).",
      "nunca é possível, pois viola o princípio federativo.",
      "cabe exclusivamente ao Congresso, sem Presidente."],
     2, "Gabarito C: intervencao é possível, respeitando requisitos e, em muitos casos, com decisao judicial (arts. 34-36). A: nao é unilateral. B: nao se limita a guerra. D: é possível. E: Presidente e Congresso intervem."),
    ("Camara", "A Camara dos Deputados é composta por",
     ["um numero variavel conforme a populacao de cada Estado.",
      "numero maximo de 513 deputados, distribuído proporcionalmente entre os Estados.",
      "513 deputados, sendo o numero fixado constitucionalmente.",
      "mais de 600 membros, um para cada municipio.",
      "numero definido a cada legislatura pelo Congresso."],
     2, "Gabarito C: 513 deputados, numero fixo (art. 45, parágrafo 1º). A: a distribuicao é proporcional, mas o total é fixo. B: maximo é impreciso. D, E: incorretos."),
    ("Senado", "O Senado Federal é composto por",
     ["um senador por Estado, totalizando 27.",
      "dois senadores por Estado, totalizando 54.",
      "três senadores por Estado, totalizando 81 (incluindo o DF).",
      "numero variavel conforme a populacao estadual.",
      "85 membros, incluindo senadores eleitos a cada 4 anos."],
     2, "Gabarito C: 3 senadores por Estado, 27 unidades = 81 (art. 46, parágrafo 1º). A, B, D, E: numeros errados."),
    ("Lei complementar", "A lei complementar, em comparacao com a lei ordinaria,",
     ["é inferior hierarquicamente, pois exige menos votos.",
      "é superior e exige quorum de maioria absoluta para aprovacao.",
      "é identica a lei ordinaria, apenas com nome diferente.",
      "nunca pode revogar lei ordinaria.",
      "é aprovada apenas pelo Senado, nao pela Camara."],
     1, "Gabarito B: lei complementar é superior e pede maioria absoluta (art. 69). A: é superior. C, D, E: incorretos."),
    ("Medida provisoria", "A medida provisoria, segundo a CF, tem vigencia de",
     ["indefinida, até ser votada pelo Congresso.",
      "120 dias, renovaveis até uma vez (total de 240 dias).",
      "60 dias, podendo ser prorrogada uma unica vez por mais 60 dias.",
      "30 dias, improrrogavel.",
      "tempo definido pelo Presidente, sem limite constitucional."],
     2, "Gabarito C: 60 dias + prorrogacao de 60 dias (maximo) (art. 62, parágrafo 3º). A: é limitada. B: 120 é total, nao por parcela. D, E: incorretos."),
    ("Veto", "O veto presidencial a lei aprovada pelo Congresso",
     ["é absoluto: o Congresso nao pode derruba-lo.",
      "pode ser derrubado por maioria simples do Congresso.",
      "pode ser derrubado por maioria de 2/5 dos deputados e senadores.",
      "depende de aprovacao do Supremo Tribunal Federal.",
      "é automaticamente derrubado se nao votado em 30 dias."],
     2, "Gabarito C: maioria de 2/5 dos membros de cada Casa (art. 66, parágrafo 4º). A: nao é absoluto. B: exige 2/5, nao maioria simples. D, E: incorretos."),
    ("Chefe de Estado", "No sistema presidencialista brasileiro, o Presidente da Republica é",
     ["apenas Chefe de Governo; outro oficial é Chefe de Estado.",
      "Chefe de Estado, mas nao Chefe de Governo.",
      "simultaneamente Chefe de Estado e Chefe de Governo.",
      "representante do Legislativo no Executivo.",
      "subordinado ao Congresso Nacional."],
     2, "Gabarito C: Presidente acumula ambas as funcoes (art. 76). A, B: nao há separacao. D, E: incorretos."),
    ("Separacao de poderes", "O princípio da separacao de poderes significa que",
     ["um Poder nao pode nunca interferir em outro.",
      "cada Poder é independente, mas há sistema de freios e contrapesos.",
      "o Legislativo é superior aos outros dois.",
      "o Executivo executa leis do Legislativo sem discussao.",
      "nao há qualquer limite ao Poder Judiciario."],
     1, "Gabarito B: independencia + sistema de checks and balances (art. 2º). A: há interferencia legitima. C, D, E: conceituacoes erradas."),
    ("Distrito Federal", "O Distrito Federal, no ordenamento constitucional,",
     ["é equiparado totalmente a um Estado.",
      "é equiparado totalmente a um Municipio.",
      "tem regime juridico proprio, nao sendo puro Estado nem puro Municipio.",
      "nao é ente da federacao.",
      "pode ser suprimido por lei complementar."],
     2, "Gabarito C: regime juridico singular do DF (art. 32). A, B: nao é equiparavel. D: é ente federado. E: a supressao seria inconstitucional."),
    ("Princípios federativos", "Sao clausulas petreas que nao podem sequer ser emendadas",
     ["apenas a separacao de poderes.",
      "a divisao do Brasil em Estados, Municipios e DF, a forma federativa de Estado, o voto direto e universal, e o sistema presidencialista.",
      "qualquer artigo da Constituicao.",
      "apenas o rol de direitos fundamentais.",
      "nenhuma, pois a Constituicao é totalmente flexível."],
     1, "Gabarito B: os incisos do art. 60, parágrafo 4º, definem clausulas petreas (federalismo, forma, voto, sistema). A, C, D, E: incorretos."),
    ("Competencia exclusiva", "A competencia legislativa exclusiva da Uniao refere-se a materias como",
     ["educacao, saude e previdencia social.",
      "codigo penal, codigo de processo penal e direito bancario.",
      "zoneamento urbano, transito e taxas municipais.",
      "direito trabalhista, que é competencia exclusiva do Estado.",
      "materias que so o Municipio pode legislar."],
     1, "Gabarito B: codigo penal, processo penal, direito bancario sao competencia privativa da Uniao (art. 22). A, C: sao concorrentes ou municipais. D, E: incorretos."),
    ("Autonomia administrativa", "A autonomia administrativa que a Constituicao garante aos entes federados significa",
     ["liberdade para cumprir ou descumprir a Constituicao Federal.",
      "capacidade de auto-organizacao respeitando a CF, legislacao federal aplicavel e a propria legislacao.",
      "poder de revogar leis federais conforme a vontade local.",
      "inexistencia de qualquer controle de constitucionalidade sobre leis estaduais.",
      "independencia absoluta sem qualquer limite legal."],
     1, "Gabarito B: autonomia é relativa, vinculada a CF e as leis federais (art. 25). A, C, D, E: autonomia nao é absoluta."),
    ("Reparticao de competencias", "Na reparticao de competencias constitucionais, uma matéria que é privativa (exclusiva) da Uniao",
     ["pode ser delegada ao Estado por lei federal.",
      "nao pode ser delegada; é indelegavel.",
      "pode ser assumida por qualquer Estado que assim decidir.",
      "exige aprovacao do Senado Federal para ser exercida.",
      "depende de decisao do Supremo Tribunal Federal."],
     0, "Gabarito A: lei federal pode autorizar delegacao de competencia privativa (art. 22, parágrafo unico). B: pode ser delegada. C, D, E: incorretos."),
]

CSS = """
@page { size:A4; margin:13mm 13mm 15mm 13mm; }
* { box-sizing:border-box; }
body { font-family:'Segoe UI','Helvetica Neue',Arial,sans-serif; color:#1d2733; font-size:11px; line-height:1.6; margin:0; orphans:3; widows:3; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
h1,h2,h3,h4 { margin:0; font-weight:700; }
p { margin:0 0 7px; text-align:justify; orphans:3; widows:3; }
.cover { height:250mm; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; background:linear-gradient(135deg,#8b0000 0%,#dc143c 55%,#a00020 100%); color:#fff; border-radius:6px; page-break-after:always; padding:0 24mm; }
.cover .kicker { letter-spacing:4px; font-size:12px; opacity:.85; font-weight:600; }
.cover h1 { font-size:43px; line-height:1.06; margin:10px 0 6px; }
.cover .sub { font-size:15px; font-weight:400; opacity:.95; max-width:140mm; }
.cover .rule { width:70px; height:4px; background:#ffd27a; margin:22px 0; border-radius:2px; }
.cover .meta { font-size:12.5px; opacity:.9; line-height:1.7; }
.cover .badge { margin-top:26px; background:rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.4); padding:9px 18px; border-radius:40px; font-size:13px; font-weight:600; }
.section-title { font-size:17px; color:#dc143c; border-bottom:3px solid #dc143c; padding-bottom:4px; margin:16px 0 9px; page-break-after:avoid; }
.section-title:first-of-type { margin-top:4px; }
.subhead { font-size:12.5px; color:#8b0000; font-weight:700; margin:11px 0 4px; border-left:4px solid #dc143c; padding-left:8px; page-break-after:avoid; }
.box2 { display:grid; grid-template-columns:1fr 1fr; gap:9px; margin:7px 0; }
.callout { border-radius:7px; padding:9px 12px; page-break-inside:avoid; margin:6px 0; }
.c-banca { background:#eef4ff; border-left:4px solid #2b6cb0; }
.c-peg { background:#fff5f5; border-left:4px solid #c0392b; }
.c-key { background:#eefaf1; border-left:4px solid #1f9d57; }
.callout h4 { font-size:10.5px; margin-bottom:4px; text-transform:uppercase; letter-spacing:.4px; }
.c-banca h4 { color:#2b6cb0; } .c-peg h4 { color:#c0392b; } .c-key h4 { color:#1f9d57; }
.callout ul { margin:3px 0 0; padding-left:15px; } .callout li { margin:2.5px 0; }
table { width:100%; border-collapse:collapse; margin:7px 0; font-size:9.8px; page-break-inside:avoid; }
th { background:#8b0000; color:#fff; text-align:left; padding:6px 8px; }
td { border:1px solid #e2e6ee; padding:6px 8px; vertical-align:top; }
tr:nth-child(even) td { background:#fbf6f7; }
td .rn { font-weight:700; color:#dc143c; }
.qbox { border:1px solid #e2e6ee; border-radius:8px; padding:9px 12px; margin:0 0 8px; page-break-inside:avoid; }
.qbox .qn { color:#dc143c; font-weight:700; }
.qbox .tema { display:inline-block; background:#eef0f5; color:#56627a; font-size:8.2px; font-weight:700; text-transform:uppercase; letter-spacing:.4px; padding:2px 7px; border-radius:20px; margin-left:6px; }
.qbox ol { margin:5px 0 0; padding-left:0; list-style:none; counter-reset:opt; }
.qbox ol li { counter-increment:opt; margin:2.5px 0; padding-left:20px; position:relative; }
.qbox ol li::before { content:counter(opt,upper-alpha)")"; position:absolute; left:0; top:0; font-weight:700; color:#56627a; }
.ce { margin-top:5px; font-size:10px; color:#56627a; font-weight:700; }
.gab-item { border-bottom:1px solid #eef0f4; padding:6px 0; page-break-inside:avoid; }
.gab-item .n { font-weight:700; color:#8b0000; }
.gab-item .resp { font-weight:700; }
.gab-c { color:#1f9d57; } .gab-e { color:#c0392b; }
.pagebreak { page-break-before:always; }
.lead { font-size:11px; color:#33414f; }
"""

ce_html = ""
for i, (af, _g, _c) in enumerate(QCE, 1):
    ce_html += (f'<div class="qbox"><span class="qn">{i}.</span> {af}'
                f'<div class="ce">(&nbsp;&nbsp;) Certo&nbsp;&nbsp;&nbsp;(&nbsp;&nbsp;) Errado</div></div>')
me_html = ""
for k, (tema, enun, opts, ok, com) in enumerate(QME, 16):
    lis = "".join(f"<li>{o}</li>" for o in opts)
    me_html += (f'<div class="qbox"><span class="qn">{k}.</span> {enun}'
                f'<span class="tema">{tema}</span><ol>{lis}</ol></div>')
gab_html = ""
for i, (af, g, c) in enumerate(QCE, 1):
    cls = "gab-c" if g == "C" else "gab-e"
    rot = "CERTO" if g == "C" else "ERRADO"
    gab_html += f'<div class="gab-item"><span class="n">{i}.</span> <span class="resp {cls}">{rot}</span> — {c}</div>'
for k, (tema, enun, opts, ok, com) in enumerate(QME, 16):
    gab_html += f'<div class="gab-item"><span class="n">{k}.</span> {com}</div>'

HTML = f"""<!DOCTYPE html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body>

<div class="cover">
  <div class="kicker">DIREITO CONSTITUCIONAL</div>
  <h1>Organizacao<br>do Estado</h1>
  <div class="rule"></div>
  <div class="sub">Federacao, divisao de poderes, competencias e Administracao Publica — apostila, lei seca comentada e 35 questoes com gabarito comentado</div>
  <div class="meta" style="margin-top:26px;">Concurso <b>Sedes/DF</b> · Banca <b>Quadrix</b> · 2026<br>Tecnico Administrativo (Cargo 202)</div>
  <div class="badge">Dia 8 · 35 questoes para fazer agora</div>
</div>

<h2 class="section-title">1. A Federacao brasileira</h2>
<p>O Brasil é uma <b>Republica Federativa</b> formada pela Uniao, Estados, Distrito Federal e Municipios (art. 1º). Cada um é <b>pessoa juridica de direito publico interno</b> com autonomia relativa. A federacao é <b>indissolúvel</b> (nao se pode sair dela) e clausula petrea (inviolavel até por emenda). Ha <b>26 Estados + DF = 27 unidades</b>. Cada ente tem competencia legislativa, administrativa e tributaria proprias, mas sempre dentro da Constituicao Federal. A <b>Uniao</b> representa o Brasil internacionalmente; os <b>Estados</b> tem poderes residuais (tudo o que nao foi atribuído a Uniao); o <b>DF</b> tem regime especial (nao é puro Estado nem Municipio); os <b>Municipios</b> cuidam de interesse local.</p>

<h2 class="section-title">2. Separacao de poderes (art. 2º)</h2>
<p>Sao <b>três</b> os Poderes: <b>Legislativo, Executivo e Judiciario</b>, independentes e harmonicos. Nem um pode deixar de existir, e ha um sistema de <b>freios e contrapesos</b> (checks and balances). O Legislativo faz leis; o Executivo administra; o Judiciario julga. Mas nao há isolamento hermetico: o Presidente veta lei do Legislativo, o Legislativo derruba veto do Presidente, o Judiciario analisa constitucionalidade de atos dos outros Poderes.</p>

<h2 class="section-title">3. Competencias legislativas</h2>
<p>A CF distribui o poder de legislar de três formas. A <b>competencia privativa (ou exclusiva)</b> é so de um ente (art. 22 para Uniao). A <b>competencia concorrente</b> (art. 24) é de dois ou mais: Uniao fixa <b>normas gerais</b>, e o Estado/DF <b>complementa</b>, respeitando as normas. A <b>competencia residual</b> (art. 25, parágrafo 1º) é dos Estados: tudo o que nao foi atribuído a Uniao. Lei federal pode <b>delegar</b> competencia privativa da Uniao aos Estados (art. 22, parágrafo unico).</p>
<div class="callout c-banca"><h4>Como a Quadrix cobra competencias</h4>
  <ul>
    <li>Trocar "Estado legisla livremente" por "Estado complementa normas gerais da Uniao".</li>
    <li>Confundir competencia concorrente (ambos legislam) com exclusiva (so um).</li>
    <li>Afirmar que Estado pode delegar; quem delega é a Uniao, por lei.</li>
  </ul></div>

<h2 class="section-title">4. O Congresso Nacional (arts. 44-91)</h2>
<p>É bicameral: <b>Camara dos Deputados + Senado Federal</b>. A <b>Camara</b> tem <b>513 deputados</b> (numero <b>fixo</b>, nao variavel), distribuidos proporcionalmente entre os Estados (art. 45, parágrafo 1º). O <b>Senado</b> tem <b>3 senadores por Estado + 3 pelo DF = 81 senadores</b> (art. 46, parágrafo 1º). Ambas as Casas votam leis. Ha quorum minimo (maioria dos membros presentes) para lei ordinaria e maioria absoluta para lei complementar. O veto presidencial a lei derruba-se com <b>maioria de 2/5 dos deputados e 2/5 dos senadores</b>, em sessao conjunta (art. 66, parágrafo 4º).</p>

<h2 class="section-title">5. O Presidente da Republica (arts. 76-91)</h2>
<p>É <b>Chefe de Estado e Chefe de Governo</b> (sistema presidencialista). Tem mandato de <b>4 anos</b>, é <b>reelegivél uma vez</b> (maximo 8 anos). Exerce funcao executiva (administra), legislativa (sanciona/veta leis, edita medidas provisorias) e simbolica (representa o Brasil). Pode editar <b>medidas provisorias</b> (art. 62), que tem validade de <b>60 dias</b>, prorrogaveis por mais <b>60 dias</b> (maximo 120), e devem ser convertidas em lei ou caducam. Nao pode legislar sobre direito penal, processual penal, organizacao judiciaria, regime dos servidores publicos (nem sob MPs).</p>

<h2 class="section-title">6. Lei ordinaria, lei complementar, decreto-lei e MP</h2>
<p><b>Lei ordinaria</b>: aprovada por maioria simples (maioria dos presentes, se houver quorum de metade dos membros + 1). <b>Lei complementar</b>: exige maioria absoluta (metade dos membros + 1 de cada Casa). Lei complementar é superior e so pode ser alterada por outra lei complementar. <b>Decreto-lei</b> foi abolido em 1988. <b>Medida provisoria (MP):</b> ato do Presidente com forca de lei, para casos de urgencia e relevancia, valida por 60 dias, prorrogavel uma vez por mais 60. Se nao votada em 120 dias, caduca e volta ao status quo anterior (art. 62).</p>

<h2 class="section-title">7. Intervencao nos entes federados (arts. 34-36)</h2>
<p>A Uniao pode intervir em Estado ou Municipio em casos de <b>requisitos específicos</b> (art. 34): manutencao da ordem publica, defesa da lei, integridade do patrimonio publico, cumprimento de ordem judicial, etc. A intervencao deve ser <b>decretada pelo Presidente</b>, em alguns casos com consentimento do Congresso. Ha <b>intervencao federal</b> (da Uniao em Estado) e <b>estadual</b> (do Estado em Municipio). Ambas requerem <b>lei</b> que defina o prazo e a amplitude. Essa é uma excecao ao federalismo; por isso tem requisitos rigorosos.</p>

<h2 class="section-title pagebreak">8. 35 questoes para fazer agora</h2>
<p class="lead">Resolva sem olhar o gabarito. <b>Itens 1 a 15:</b> julgue como CERTO ou ERRADO. <b>Itens 16 a 35:</b> multipla escolha (A–E). O gabarito comentado está na secao 9.</p>
<p class="subhead">Parte I — Julgue os itens (Certo / Errado)</p>
{ce_html}
<p class="subhead">Parte II — Multipla escolha (A–E)</p>
{me_html}

<h2 class="section-title pagebreak">9. Gabarito comentado</h2>
<p class="lead">Cada item traz a resposta e a explicacao: por que a correta está certa e, nas de multipla escolha, qual elemento torna cada alternativa errada.</p>
{gab_html}

</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("HTML gerado:", OUT, "| C/E:", len(QCE), "| A-E:", len(QME), "| total:", len(QCE)+len(QME))
