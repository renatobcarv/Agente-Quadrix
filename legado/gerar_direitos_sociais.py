# -*- coding: utf-8 -*-
"""Material DENSO (apostila) — Dia 5: Direito Constitucional, direitos sociais
(arts. 6º a 11) + bloco de Português (pontuação e crase). Teoria em prosa +
35 questões (15 C/E + 20 A-E) com gabarito comentado. Segue docs/prompt-mestre.md.
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(_HERE)
OUTDIR = os.path.join(_REPO, "materiais", "dia05-direitos-sociais")
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "Dia5_Direitos_Sociais.html")

QCE = [
    ("O transporte é direito social expressamente previsto no art. 6º da Constituição.",
     "C", "Correto. O transporte foi incluído no rol do art. 6º pela EC 90/2015. Moradia (EC 26/2000) e alimentação (EC 64/2010) também são inclusões posteriores."),
    ("A licença à gestante, sem prejuízo do emprego e do salário, tem duração de noventa dias.",
     "E", "Errado. A CF fixa 120 dias (inciso XVIII do art. 7º). A troca do número (90, 180) é a armadilha típica."),
    ("O salário mínimo é fixado por estado, conforme o custo de vida de cada região.",
     "E", "Errado. O salário mínimo é fixado em lei e nacionalmente unificado (art. 7º, IV). O piso regional, por lei complementar, é coisa distinta."),
    ("A remuneração do serviço extraordinário é superior à do normal em, no mínimo, cinquenta por cento.",
     "C", "Correto. É a literalidade do art. 7º, XVI: hora extra com acréscimo mínimo de 50%."),
    ("É proibido qualquer trabalho aos menores de dezoito anos.",
     "E", "Errado. Proíbe-se o trabalho a menores de 16, salvo aprendiz a partir dos 14. Os 18 anos referem-se à vedação do trabalho noturno, perigoso ou insalubre (art. 7º, XXXIII)."),
    ("Vigora a unicidade sindical: é vedada a criação de mais de um sindicato na mesma base territorial.",
     "C", "Correto. O art. 8º, II, consagra a unicidade, sendo a base territorial não inferior a um município."),
    ("Compete ao sindicato, e não aos trabalhadores, decidir sobre a oportunidade de exercer a greve.",
     "E", "Errado. O art. 9º atribui aos próprios trabalhadores a decisão sobre a oportunidade de exercer a greve e os interesses a defender."),
    ("As férias anuais são remuneradas com, pelo menos, um terço a mais do que o salário normal.",
     "C", "Correto. Literalidade do art. 7º, XVII. Dizer “metade” ou “o dobro” seria o erro."),
    ("O décimo terceiro salário tem como base de cálculo a metade da remuneração do mês de dezembro.",
     "E", "Errado. O 13º tem por base a remuneração integral ou o valor da aposentadoria (art. 7º, VIII)."),
    ("Ninguém é obrigado a filiar-se ou a manter-se filiado a sindicato.",
     "C", "Correto. É a liberdade de filiação sindical (art. 8º, V)."),
    ("A proteção da relação de emprego contra despedida arbitrária é automática, independentemente de lei.",
     "E", "Errado. O art. 7º, I, remete a proteção a lei complementar, que preverá indenização compensatória, entre outros direitos."),
    ("O aviso prévio é proporcional ao tempo de serviço, sendo, no mínimo, de trinta dias.",
     "C", "Correto. Art. 7º, XXI: aviso prévio proporcional, com piso de 30 dias."),
    ("A assistência gratuita em creches e pré-escolas é assegurada aos filhos dos trabalhadores até os seis anos de idade.",
     "E", "Errado. O art. 7º, XXV, assegura creche e pré-escola do nascimento até os 5 anos de idade."),
    ("Nas empresas de mais de duzentos empregados, é assegurada a eleição de um representante dos trabalhadores.",
     "C", "Correto. É o art. 11 da Constituição. Trocar 200 por 100 ou 500 é a pegadinha."),
    ("A participação nos lucros ou resultados integra a remuneração do empregado para todos os efeitos.",
     "E", "Errado. O art. 7º, XI, prevê a participação nos lucros desvinculada da remuneração."),
]

QME = [
    ("Art. 6º", "Assinale a opção que apresenta um direito social expressamente previsto no art. 6º.",
     ["o transporte", "o pleno emprego", "o saneamento básico", "o acesso à internet", "o crédito popular"],
     0, "Gabarito A: o transporte integra o rol (EC 90/2015). ✗B, ✗C, ✗D, ✗E: pleno emprego, saneamento, internet e crédito popular não constam do art. 6º."),
    ("Art. 7º — gestante", "A licença à gestante, sem prejuízo do emprego e do salário, tem a duração de",
     ["sessenta dias.", "cento e vinte dias.", "noventa dias.", "cento e oitenta dias.", "trinta dias."],
     1, "Gabarito B: 120 dias (art. 7º, XVIII). ✗A, ✗C, ✗D, ✗E: os demais números são trocas-armadilha."),
    ("Art. 7º — hora extra", "A remuneração do serviço extraordinário deve ser superior à do normal, no mínimo, em",
     ["vinte por cento.", "trinta por cento.", "cinquenta por cento.", "cem por cento.", "setenta por cento."],
     2, "Gabarito C: acréscimo mínimo de 50% (art. 7º, XVI). ✗A, ✗B, ✗D, ✗E: percentuais incorretos."),
    ("Art. 7º — jornada", "A duração do trabalho normal, salvo negociação, não deve ser superior a",
     ["seis horas diárias e quarenta e quatro semanais.", "oito horas diárias e quarenta e oito semanais.", "dez horas diárias e quarenta e quatro semanais.", "oito horas diárias e quarenta e quatro semanais.", "doze horas diárias e trinta e seis semanais."],
     3, "Gabarito D: 8h diárias e 44h semanais (art. 7º, XIII). ✗A: 6h é o turno ininterrupto de revezamento. ✗B: não são 48 semanais. ✗C, ✗E: números incorretos."),
    ("Art. 7º — idade", "Quanto à idade para o trabalho, é proibido o trabalho a menores de",
     ["quatorze anos, sem exceção.", "dezoito anos em qualquer atividade.", "doze anos, salvo aprendiz.", "dezesseis anos, salvo aprendiz a partir dos doze.", "dezesseis anos, salvo na condição de aprendiz, a partir dos quatorze."],
     4, "Gabarito E: proibido a menores de 16, salvo aprendiz a partir dos 14 (art. 7º, XXXIII). ✗B: os 18 anos referem-se ao trabalho noturno/perigoso/insalubre. ✗A, ✗C, ✗D: idades trocadas."),
    ("Art. 8º — sindical", "Acerca da organização sindical, assinale a opção correta.",
     ["É vedada a criação de mais de um sindicato na mesma base territorial, não inferior a um município.", "Vigora a pluralidade sindical na mesma base territorial.", "É permitida a interferência do Poder Público para garantir a ordem.", "A filiação ao sindicato da categoria é obrigatória.", "O aposentado filiado não pode votar nem ser votado."],
     0, "Gabarito A: unicidade sindical (art. 8º, II). ✗B: não é pluralidade. ✗C: é vedada a interferência do Poder Público. ✗D: a filiação é livre. ✗E: o aposentado filiado vota e é votado."),
    ("Art. 9º — greve", "A respeito do direito de greve, assinale a opção correta.",
     ["Depende de autorização prévia do Ministério do Trabalho.", "Compete aos trabalhadores decidir sobre a oportunidade de exercê-lo e os interesses a defender.", "Compete exclusivamente ao sindicato deflagrar o movimento.", "É vedado a todos os trabalhadores da iniciativa privada.", "É proibido em qualquer atividade essencial."],
     1, "Gabarito B: são os trabalhadores que decidem (art. 9º). ✗A: não depende de autorização. ✗C: a decisão é dos trabalhadores, não só do sindicato. ✗D: a greve é assegurada. ✗E: nas essenciais a lei regula o atendimento das necessidades inadiáveis, não há proibição absoluta."),
    ("Art. 7º — férias", "As férias anuais remuneradas são asseguradas com o pagamento de",
     ["pelo menos um terço a mais do que o salário normal.", "pelo menos a metade a mais do que o salário normal.", "valor igual ao salário normal, sem acréscimo.", "pelo menos o dobro do salário normal.", "pelo menos dois terços a mais do que o salário normal."],
     0, "Gabarito A: salário + no mínimo 1/3 (art. 7º, XVII). ✗B, ✗D, ✗E: frações incorretas. ✗C: há acréscimo obrigatório."),
    ("Art. 7º — aviso prévio", "O aviso prévio, proporcional ao tempo de serviço, é assegurado com duração",
     ["fixa de quinze dias.", "mínima de trinta dias, nos termos da lei.", "máxima de trinta dias.", "fixa de sessenta dias.", "definida só em convenção coletiva, sem piso legal."],
     1, "Gabarito B: proporcional, com mínimo de 30 dias (art. 7º, XXI). ✗A, ✗C, ✗D: prazos incorretos. ✗E: há piso constitucional."),
    ("Art. 7º — 13º", "O décimo terceiro salário tem como base de cálculo",
     ["metade da remuneração de dezembro.", "o valor de um salário mínimo.", "a remuneração integral ou o valor da aposentadoria.", "apenas o salário-base, sem adicionais.", "a média dos seis últimos salários."],
     2, "Gabarito C: remuneração integral ou valor da aposentadoria (art. 7º, VIII). ✗A, ✗B, ✗D, ✗E: bases de cálculo incorretas."),
    ("Art. 11", "É assegurada a eleição de um representante dos trabalhadores nas empresas com",
     ["mais de duzentos empregados.", "mais de cinquenta empregados.", "mais de cem empregados.", "mais de quinhentos empregados.", "qualquer número de empregados."],
     0, "Gabarito A: mais de 200 empregados (art. 11). ✗B, ✗C, ✗D: números incorretos. ✗E: há limite mínimo."),
    ("Art. 7º — despedida", "A proteção da relação de emprego contra despedida arbitrária, conforme o art. 7º, I,",
     ["é automática e independe de regulamentação.", "depende de lei complementar, que preverá indenização compensatória.", "foi disciplinada por medida provisória.", "aplica-se só a servidores estatutários.", "vigora só para contratos por prazo determinado."],
     1, "Gabarito B: depende de lei complementar. ✗A: não é automática. ✗C: não foi por MP. ✗D, ✗E: não há essa restrição."),
    ("Art. 7º — menor", "É vedado o trabalho noturno, perigoso ou insalubre aos",
     ["maiores de dezesseis e menores de dezoito anos apenas.", "menores de quatorze anos.", "menores de dezoito anos.", "menores de dezesseis anos, salvo aprendiz.", "menores de vinte e um anos."],
     2, "Gabarito C: a vedação alcança todos os menores de 18 anos (art. 7º, XXXIII). ✗A: não se limita à faixa 16–18. ✗B, ✗D, ✗E: idades incorretas."),
    ("Art. 8º — filiação", "Sobre a filiação sindical, a Constituição estabelece que",
     ["todo trabalhador é obrigado a filiar-se ao sindicato da categoria.", "a filiação depende de autorização do empregador.", "só trabalhadores na ativa podem filiar-se.", "ninguém será obrigado a filiar-se ou a manter-se filiado.", "a desfiliação depende de autorização judicial."],
     3, "Gabarito D: filiação livre (art. 8º, V). ✗A: não é obrigatória. ✗B: não depende do empregador. ✗C: aposentado também se filia. ✗E: a desfiliação é livre."),
    ("Art. 7º — creche", "A assistência gratuita em creches e pré-escolas é assegurada do nascimento até os",
     ["três anos.", "quatro anos.", "seis anos.", "sete anos.", "cinco anos."],
     4, "Gabarito E: até os 5 anos de idade (art. 7º, XXV). ✗A, ✗B, ✗C, ✗D: idades incorretas."),
    ("Art. 7º — lucros", "A participação nos lucros ou resultados da empresa é",
     ["desvinculada da remuneração, conforme definido em lei.", "integrante da remuneração para todos os efeitos.", "obrigatória apenas para estatais.", "calculada sempre em um salário mínimo.", "vedada nas empresas privadas."],
     0, "Gabarito A: desvinculada da remuneração (art. 7º, XI). ✗B: justamente não integra a remuneração. ✗C, ✗D, ✗E: afirmações sem respaldo no texto."),
    ("Art. 7º — salário mínimo", "Quanto ao salário mínimo, o art. 7º estabelece que ele é",
     ["fixado por decreto e diferenciado por estado.", "fixado em lei, nacionalmente unificado, vedada a vinculação para qualquer fim.", "passível de vinculação como índice.", "reajustado a critério do empregador.", "destinado a atender só o trabalhador, excluída a família."],
     1, "Gabarito B: fixado em lei, nacionalmente unificado, vedada a vinculação (art. 7º, IV), atendendo trabalhador e família. ✗A: não é por decreto nem por estado. ✗C: a vinculação é vedada. ✗D: há reajustes legais. ✗E: alcança a família."),
    ("Art. 7º — irredutibilidade", "A irredutibilidade do salário comporta exceção quando houver",
     ["determinação unilateral do empregador.", "autorização verbal do empregado.", "convenção ou acordo coletivo de trabalho.", "ordem do Ministério do Trabalho.", "previsão em regulamento interno."],
     2, "Gabarito C: a redução só por convenção ou acordo coletivo (art. 7º, VI). ✗A, ✗B, ✗D, ✗E: nenhum desses autoriza a redução salarial."),
    ("Art. 6º — emendas", "Assinale o direito social incluído no art. 6º por emenda posterior a 1988.",
     ["a saúde", "a educação", "a previdência social", "o transporte", "o trabalho"],
     3, "Gabarito D: o transporte foi incluído pela EC 90/2015. ✗A, ✗B, ✗C, ✗E: saúde, educação, previdência e trabalho constam do texto original."),
    ("Art. 9º — greve", "Sobre a greve em atividades essenciais, é correto afirmar que",
     ["a greve é totalmente proibida nessas atividades.", "o sindicato é obrigado a manter 100% dos serviços.", "o Ministério do Trabalho decide sobre a greve.", "a greve dispensa qualquer comunicação prévia.", "a lei definirá os serviços essenciais e o atendimento das necessidades inadiáveis da comunidade."],
     4, "Gabarito E: a lei define os serviços essenciais e assegura o atendimento das necessidades inadiáveis (art. 9º, §1º). ✗A: não há proibição total. ✗B: não se exige 100%. ✗C: a decisão é dos trabalhadores. ✗D: há deveres de comunicação."),
]

# ---- bloco Português: pontuação e crase (teoria) ----
CRASE = [
    ("Quando OCORRE", "Diante de palavra feminina que exige artigo “a” + preposição “a”. Ex.: “Refiro-me à diretora.”"),
    ("Locuções femininas", "À tarde, à noite, à vista, às vezes, à medida que, à moda de. Ex.: “Saímos à noite.”"),
    ("Horas determinadas", "“Cheguei às oito horas.” (a + as horas)."),
    ("NÃO ocorre — palavra masculina", "“Andar a pé”, “a cavalo”, “a respeito de” (palavra masculina não tem artigo “a”)."),
    ("NÃO ocorre — verbo", "Antes de verbo não há crase: “Estou disposto a ajudar.”"),
    ("NÃO ocorre — pronomes", "Antes de “você”, “essa/esta”, “ela”: “Refiro-me a você / a esta questão.”"),
]

CSS = """
@page { size:A4; margin:13mm 13mm 15mm 13mm; }
* { box-sizing:border-box; }
body { font-family:'Segoe UI','Helvetica Neue',Arial,sans-serif; color:#1d2733; font-size:11px; line-height:1.6; margin:0; orphans:3; widows:3; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
h1,h2,h3,h4 { margin:0; font-weight:700; }
p { margin:0 0 7px; text-align:justify; orphans:3; widows:3; }
.cover { height:250mm; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; background:linear-gradient(135deg,#7a0c1c 0%,#b3122a 55%,#8e1020 100%); color:#fff; border-radius:6px; page-break-after:always; padding:0 24mm; }
.cover .kicker { letter-spacing:4px; font-size:12px; opacity:.85; font-weight:600; }
.cover h1 { font-size:44px; line-height:1.05; margin:10px 0 6px; }
.cover .sub { font-size:15px; font-weight:400; opacity:.95; max-width:140mm; }
.cover .rule { width:70px; height:4px; background:#ffd27a; margin:22px 0; border-radius:2px; }
.cover .meta { font-size:12.5px; opacity:.9; line-height:1.7; }
.cover .badge { margin-top:26px; background:rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.4); padding:9px 18px; border-radius:40px; font-size:13px; font-weight:600; }
.section-title { font-size:17px; color:#b3122a; border-bottom:3px solid #b3122a; padding-bottom:4px; margin:16px 0 9px; page-break-after:avoid; }
.section-title:first-of-type { margin-top:4px; }
.subhead { font-size:12.5px; color:#7a0c1c; font-weight:700; margin:11px 0 4px; border-left:4px solid #b3122a; padding-left:8px; page-break-after:avoid; }
.box2 { display:grid; grid-template-columns:1fr 1fr; gap:9px; margin:7px 0; }
.callout { border-radius:7px; padding:9px 12px; page-break-inside:avoid; margin:6px 0; }
.c-banca { background:#eef4ff; border-left:4px solid #2b6cb0; }
.c-peg { background:#fff5f5; border-left:4px solid #c0392b; }
.c-mnem { background:#fff8e6; border-left:4px solid #d4a017; }
.c-key { background:#eefaf1; border-left:4px solid #1f9d57; }
.callout h4 { font-size:10.5px; margin-bottom:4px; text-transform:uppercase; letter-spacing:.4px; }
.c-banca h4 { color:#2b6cb0; } .c-peg h4 { color:#c0392b; } .c-mnem h4 { color:#a07400; } .c-key h4 { color:#1f9d57; }
.callout ul { margin:3px 0 0; padding-left:15px; } .callout li { margin:2.5px 0; }
table { width:100%; border-collapse:collapse; margin:7px 0; font-size:9.8px; page-break-inside:avoid; }
th { background:#7a0c1c; color:#fff; text-align:left; padding:6px 8px; }
td { border:1px solid #e2e6ee; padding:6px 8px; vertical-align:top; }
tr:nth-child(even) td { background:#fbf6f7; }
td .rn { font-weight:700; color:#b3122a; }
.qbox { border:1px solid #e2e6ee; border-radius:8px; padding:9px 12px; margin:0 0 8px; page-break-inside:avoid; }
.qbox .qn { color:#b3122a; font-weight:700; }
.qbox .tema { display:inline-block; background:#eef0f5; color:#56627a; font-size:8.2px; font-weight:700; text-transform:uppercase; letter-spacing:.4px; padding:2px 7px; border-radius:20px; margin-left:6px; }
.qbox ol { margin:5px 0 0; padding-left:0; list-style:none; counter-reset:opt; }
.qbox ol li { counter-increment:opt; margin:2.5px 0; padding-left:20px; position:relative; }
.qbox ol li::before { content:counter(opt,upper-alpha)")"; position:absolute; left:0; top:0; font-weight:700; color:#56627a; }
.ce { margin-top:5px; font-size:10px; color:#56627a; font-weight:700; }
.gab-item { border-bottom:1px solid #eef0f4; padding:6px 0; page-break-inside:avoid; }
.gab-item .n { font-weight:700; color:#7a0c1c; }
.gab-item .resp { font-weight:700; }
.gab-c { color:#1f9d57; } .gab-e { color:#c0392b; }
.pagebreak { page-break-before:always; }
.lead { font-size:11px; color:#33414f; }
"""

crase_rows = "".join(f"<tr><td><span class='rn'>{t}</span></td><td>{d}</td></tr>" for (t, d) in CRASE)
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
  <h1>Direitos<br>Sociais</h1>
  <div class="rule"></div>
  <div class="sub">Arts. 6º a 11 da CF/88 — apostila, bloco de pontuação e crase e 35 questões com gabarito comentado</div>
  <div class="meta" style="margin-top:26px;">Concurso <b>Sedes/DF</b> · Banca <b>Quadrix</b> · 2026<br>Técnico Administrativo (Cargo 202)</div>
  <div class="badge">Dia 5 · 35 questões para fazer agora</div>
</div>

<h2 class="section-title">1. Por que os direitos sociais derrubam o candidato</h2>
<p>Os arts. 6º a 11 formam a parte mais “decoreba” do Direito Constitucional, e é exatamente aí que a Quadrix monta suas armadilhas. Como banca de literalidade, ela cobra <b>números</b> (120 dias de licença, um terço de férias, 50% da hora extra, as idades de 16, 14 e 18 anos, os 200 empregados) e <b>listas</b> (o rol do art. 6º), trocando um único elemento para criar o erro. Quem fixa os números e entende a lógica de cada direito acerta com tranquilidade; quem leu por cima cai na troca. Este material organiza esse conteúdo artigo por artigo, com destaque para os pontos que a banca mais altera.</p>

<h2 class="section-title">2. Art. 6º — o rol dos direitos sociais</h2>
<p>O art. 6º enumera os direitos sociais: <b>educação, saúde, alimentação, trabalho, moradia, transporte, lazer, segurança, previdência social, proteção à maternidade e à infância e assistência aos desamparados</b>. Três deles foram acrescentados por emenda ao longo do tempo, e isso é cobrado: a <b>moradia</b> entrou pela EC 26/2000, a <b>alimentação</b> pela EC 64/2010 e o <b>transporte</b> pela EC 90/2015 — este último, por ser o mais recente, é o mais perguntado. A pegadinha clássica insere no rol um direito que não está lá (“pleno emprego”, “saneamento”, “acesso à internet”) ou retira um que está. Decorar a lista evita o erro.</p>

<h2 class="section-title">3. Art. 7º — os direitos dos trabalhadores</h2>
<p>É o artigo de onde sai a maioria das questões, porque concentra os números. O <b>salário mínimo</b> é fixado em lei, <b>nacionalmente unificado</b> (um único valor para todo o país), capaz de atender às necessidades do trabalhador <b>e de sua família</b>, sendo <b>vedada a sua vinculação para qualquer fim</b> — ou seja, ele não pode servir de índice. A <b>jornada</b> normal não excede <b>8 horas diárias e 44 semanais</b>, reduzindo-se a <b>6 horas</b> nos turnos ininterruptos de revezamento, salvo negociação coletiva. As <b>férias</b> são pagas com, no mínimo, <b>um terço a mais</b> que o salário; o <b>13º salário</b> tem por base a <b>remuneração integral</b>; o serviço extraordinário (hora extra) é remunerado com acréscimo de, no mínimo, <b>50%</b>; e o <b>aviso prévio</b> é proporcional ao tempo de serviço, com piso de <b>30 dias</b>.</p>
<p>Quanto à proteção da pessoa, a <b>licença à gestante</b> dura <b>120 dias</b>, sem prejuízo do emprego e do salário, enquanto a <b>licença-paternidade</b> é fixada “nos termos da lei” (a CF não define o número de dias). Sobre a <b>idade</b>, é proibido o trabalho a menores de <b>16</b> anos, salvo na condição de <b>aprendiz a partir dos 14</b>; e é vedado o trabalho noturno, perigoso ou insalubre aos menores de <b>18</b>. Há ainda garantias importantes: o <b>FGTS</b>, o <b>seguro-desemprego</b>, a <b>irredutibilidade salarial</b> (salvo convenção ou acordo coletivo), a proteção contra <b>despedida arbitrária</b> (que depende de <b>lei complementar</b>), a <b>participação nos lucros desvinculada da remuneração</b> e a assistência gratuita em <b>creches e pré-escolas até os 5 anos</b>.</p>
<div class="callout c-mnem"><h4>Os números de ouro do art. 7º</h4><b>120</b> dias (gestante) · <b>+1/3</b> (férias) · <b>+50%</b> (hora extra) · <b>8h/44h</b> (jornada) · <b>6h</b> (revezamento) · <b>16/14/18</b> (idade) · <b>30</b> dias (aviso prévio) · <b>5</b> anos (creche).</div>

<h2 class="section-title">4. Arts. 8º a 11 — sindicato, greve e representação</h2>
<p>O art. 8º garante a <b>liberdade sindical</b>, mas com uma limitação importante: vigora a <b>unicidade sindical</b> — é vedada a criação de mais de um sindicato representativo da mesma categoria na mesma <b>base territorial</b>, que não pode ser inferior a um município. É <b>vedada a interferência</b> do Poder Público na organização sindical, e <b>ninguém é obrigado</b> a filiar-se ou a manter-se filiado; o aposentado filiado pode votar e ser votado. O art. 9º assegura o <b>direito de greve</b>, competindo aos próprios <b>trabalhadores</b> decidir sobre a oportunidade de exercê-lo e os interesses a defender; nos serviços essenciais, a <b>lei</b> define o atendimento das necessidades inadiáveis da comunidade. Por fim, o art. 11 assegura, nas empresas de <b>mais de 200 empregados</b>, a eleição de um <b>representante dos trabalhadores</b> para o entendimento direto com os empregadores.</p>
<div class="callout c-banca"><h4>Como a Quadrix cobra os direitos sociais</h4>
  <ul>
    <li>Troca de número: “licença de 90 dias”, “hora extra de 20%”, “representante acima de 100 empregados”.</li>
    <li>Troca de regra: “pluralidade sindical”, “o sindicato decide a greve”, “salário mínimo por estado”.</li>
    <li>Item falso no rol do art. 6º (insere “pleno emprego” ou “internet”).</li>
  </ul></div>

<h2 class="section-title pagebreak">5. Bloco de Português — pontuação e crase</h2>
<p>Encerrando o dia, uma síntese do bloco de Língua Portuguesa previsto para hoje. A <b>crase</b> é a fusão de dois “a”: a preposição “a” com o artigo feminino “a” (ou com o “a” inicial dos pronomes “aquele/aquilo”). O teste mais seguro é a <b>troca por palavra masculina</b>: se, ao substituir o termo feminino por um masculino, surgir “ao”, há crase (“Refiro-me à diretora” → “ao diretor”); se surgir apenas “o”, não há. A tabela resume os casos de ocorrência e de proibição.</p>
<table>
  <thead><tr><th style="width:32%">Situação</th><th>Regra e exemplo</th></tr></thead>
  <tbody>{crase_rows}</tbody>
</table>
<p>Quanto à <b>pontuação</b>, três usos são os mais cobrados. A <b>vírgula</b> separa termos de mesma função (enumerações), isola o adjunto adverbial deslocado, o aposto, o vocativo e a oração subordinada adjetiva <b>explicativa</b> — mas <b>nunca</b> separa o sujeito do seu verbo nem o verbo do seu complemento. O <b>ponto e vírgula</b> separa orações longas ou itens de uma enumeração já pontuada por vírgulas. Os <b>dois-pontos</b> introduzem uma enumeração, uma explicação ou uma fala. A pegadinha mais comum coloca uma vírgula indevida entre o sujeito e o verbo (“Os candidatos aprovados, receberão o cargo” — errado).</p>
<div class="callout c-peg"><h4>Pegadinhas de pontuação e crase</h4>
  <ul>
    <li>Vírgula separando sujeito e verbo — sempre errada.</li>
    <li>Crase antes de verbo (“disposto à ajudar”) e antes de pronome (“à você”) — proibida.</li>
    <li>“à medida que” (proporção) ≠ “na medida em que” (causa) — não confunda.</li>
  </ul></div>

<h2 class="section-title pagebreak">6. 35 questões para fazer agora</h2>
<p class="lead">Resolva sem olhar o gabarito. <b>Itens 1 a 15:</b> julgue como CERTO ou ERRADO. <b>Itens 16 a 35:</b> múltipla escolha (A–E). O gabarito comentado está na seção 7.</p>
<p class="subhead">Parte I — Julgue os itens (Certo / Errado)</p>
{ce_html}
<p class="subhead">Parte II — Múltipla escolha (A–E)</p>
{me_html}

<h2 class="section-title pagebreak">7. Gabarito comentado</h2>
<p class="lead">Cada item traz a resposta e a explicação: por que a correta está certa e, nas de múltipla escolha, qual elemento torna cada alternativa errada.</p>
{gab_html}

</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("HTML gerado:", OUT, "| C/E:", len(QCE), "| A-E:", len(QME), "| total:", len(QCE)+len(QME))
