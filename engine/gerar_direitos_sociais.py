# -*- coding: utf-8 -*-
"""Material de estudo: Direito Constitucional - Direitos Sociais (arts. 6 a 11 da CF/88).
Teoria em cards + 20 questoes comentadas (distratores equilibrados, gabarito A-E).
Gera HTML profissional (render via Chrome).
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(_HERE)
OUTDIR = os.path.join(_REPO, "materiais", "dia05-direitos-sociais")
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "Dia5_Direitos_Sociais.html")

CARDS = [
    ("Art. 6º — O rol dos direitos sociais",
     "São direitos sociais: <b>educação, saúde, alimentação, trabalho, moradia, transporte, lazer, segurança, previdência social, proteção à maternidade e à infância e assistência aos desamparados</b>.",
     "Lembre das emendas: <b>moradia</b> (EC 26/2000), <b>alimentação</b> (EC 64/2010) e <b>transporte</b> (EC 90/2015) foram incluídos depois.",
     "A banca inventa um direito que NÃO está no rol (ex.: ‘emprego’, ‘internet’) ou retira um que está (ex.: tira ‘transporte’). Decore os 11.",
     "‘Transporte’ é o mais novo (2015) e o mais cobrado por ser recente."),

    ("Art. 7º — Salário mínimo",
     "O salário mínimo é <b>fixado em lei, nacionalmente unificado</b>, capaz de atender às necessidades vitais básicas do trabalhador e de sua família, com reajustes que lhe preservem o poder aquisitivo; é <b>vedada sua vinculação para qualquer fim</b>.",
     "‘Nacionalmente unificado’ = um único valor para todo o país (não é por estado). O piso regional é outra coisa, criado por lei complementar.",
     "Trocar ‘nacionalmente unificado’ por ‘fixado por estado’; ou dizer que pode ser usado como indexador (é vedada a vinculação).",
     "Mínimo = único no país + não serve de índice."),

    ("Art. 7º — Jornada de trabalho",
     "Duração do trabalho normal <b>não superior a 8 horas diárias e 44 semanais</b>; jornada de <b>6 horas</b> para turnos ininterruptos de revezamento, salvo negociação coletiva.",
     "8h por dia E 44h por semana (as duas condições). Turno ininterrupto de revezamento tem jornada reduzida de 6h.",
     "Inverter para ‘44 diárias e 8 semanais’ ou dizer ‘48 horas semanais’. Atenção também ao ‘salvo negociação coletiva’.",
     "8 por dia, 44 por semana. Revezamento = 6."),

    ("Art. 7º — Férias, 13º e RSR",
     "<b>Férias anuais</b> remuneradas com, <b>pelo menos, um terço (1/3) a mais</b> que o salário normal; <b>13º salário</b> com base na remuneração integral; <b>repouso semanal remunerado</b>, preferencialmente aos domingos.",
     "Férias = salário + 1/3. 13º = remuneração integral (não meio salário). RSR preferencialmente (não obrigatoriamente) aos domingos.",
     "Dizer que o adicional de férias é ‘1/2’ ou que o RSR é ‘obrigatoriamente aos domingos’.",
     "Férias: +1/3. RSR: ‘preferencialmente’ domingo."),

    ("Art. 7º — Licença-maternidade e paternidade",
     "<b>Licença à gestante</b>, sem prejuízo do emprego e do salário, com duração de <b>120 dias</b>; <b>licença-paternidade</b>, nos termos fixados em lei (atualmente 5 dias, no ADCT).",
     "120 dias para a gestante, garantido emprego E salário. A paternidade é ‘nos termos da lei’ — a CF não fixa o número (são 5 dias pelo ADCT).",
     "Trocar 120 por 90 ou 180 dias; ou afirmar que a CF fixa a licença-paternidade em 30 dias.",
     "Maternidade = 120 dias (na CF). Paternidade = ‘lei’."),

    ("Art. 7º — Hora extra, adicional noturno e aviso prévio",
     "Remuneração do serviço extraordinário <b>superior, no mínimo, em 50%</b> à do normal; <b>adicional noturno</b> superior ao diurno; <b>aviso prévio proporcional</b> ao tempo de serviço, <b>no mínimo de 30 dias</b>.",
     "Hora extra: acréscimo mínimo de 50%. Aviso prévio: proporcional, mas nunca menor que 30 dias.",
     "Dizer que a hora extra é ‘no mínimo 20%’ ou que o aviso prévio é ‘fixo de 30 dias’ (é proporcional, com piso de 30).",
     "Extra: +50%. Aviso: ≥ 30 dias (proporcional)."),

    ("Art. 7º — Idade mínima para o trabalho",
     "Proibição de trabalho <b>noturno, perigoso ou insalubre a menores de 18 anos</b> e de <b>qualquer trabalho a menores de 16</b>, salvo na condição de <b>aprendiz, a partir dos 14 anos</b>.",
     "Três números: 18 (nada de noturno/perigoso/insalubre), 16 (regra geral), 14 (aprendiz).",
     "Trocar as idades (ex.: ‘aprendiz a partir dos 12’ ou ‘proibido qualquer trabalho a menores de 18’).",
     "18 perigoso · 16 geral · 14 aprendiz."),

    ("Art. 7º — Outras garantias cobradas",
     "<b>FGTS</b>; <b>seguro-desemprego</b>; <b>irredutibilidade salarial</b> (salvo convenção/acordo); <b>proteção contra despedida arbitrária</b> (nos termos de lei complementar); <b>participação nos lucros</b>, desvinculada da remuneração; <b>creche e pré-escola até os 5 anos</b> de idade.",
     "A proteção contra despedida arbitrária depende de <b>lei complementar</b>. A participação nos lucros é <b>desvinculada</b> do salário.",
     "Afirmar que a estabilidade contra despedida é automática (depende de LC) ou que a participação nos lucros integra a remuneração.",
     "Despedida arbitrária → depende de LC."),

    ("Art. 8º — Liberdade sindical",
     "É <b>livre</b> a associação profissional ou sindical, <b>vedada a interferência do Poder Público</b>; é <b>vedada a criação de mais de um sindicato</b> na mesma base territorial (mínimo de um município) — <b>unicidade sindical</b>. Ninguém é obrigado a filiar-se ou a manter-se filiado.",
     "Liberdade sindical, MAS com unicidade (um sindicato por base territorial, no mínimo o município). O aposentado filiado pode votar e ser votado.",
     "Dizer que vigora a ‘pluralidade sindical’ (errado: é unicidade) ou que a filiação é obrigatória.",
     "Sindicato: livre, mas ÚNICO por base (unicidade)."),

    ("Arts. 9º a 11 — Greve e participação",
     "<b>Greve (art. 9º):</b> direito assegurado, competindo aos <b>trabalhadores</b> decidir sobre a oportunidade e os interesses a defender; lei definirá os <b>serviços essenciais</b>. <b>Art. 11:</b> nas empresas de <b>mais de 200 empregados</b>, é assegurada a eleição de um representante dos trabalhadores.",
     "Quem decide a greve são os próprios trabalhadores. O representante do art. 11 só é garantido acima de 200 empregados.",
     "Dizer que o sindicato (e não os trabalhadores) decide a greve; ou trocar ‘200’ por ‘100’ empregados.",
     "Greve: trabalhadores decidem · Representante: +200."),
]

# (tema, enunciado, [A..E], idx_correto, comentario) — gabarito A-E equilibrado
Q = [
    ("Art. 6º", "Assinale a opção que apresenta um direito social expressamente previsto no art. 6º da Constituição Federal.",
     ["o transporte", "o pleno emprego", "o saneamento básico", "o acesso à internet", "o crédito popular"],
     0, "‘Transporte’ foi incluído pela EC 90/2015 e consta do rol. Os demais não estão no art. 6º. Gabarito A."),
    ("Art. 7º — gestante", "A licença à gestante, sem prejuízo do emprego e do salário, tem a duração de",
     ["sessenta dias.", "cento e vinte dias.", "noventa dias.", "cento e oitenta dias.", "trinta dias."],
     1, "A CF fixa 120 dias para a licença-maternidade. Gabarito B. PEGADINHA: 90/180 dias."),
    ("Art. 7º — hora extra", "A remuneração do serviço extraordinário deve ser superior à do serviço normal, no mínimo, em",
     ["vinte por cento.", "trinta por cento.", "cinquenta por cento.", "cem por cento.", "setenta por cento."],
     2, "Hora extra: acréscimo mínimo de 50%. Gabarito C. PEGADINHA: 20%/30%."),
    ("Art. 7º — jornada", "A duração do trabalho normal, salvo negociação, não deve ser superior a",
     ["seis horas diárias e quarenta e quatro semanais.", "oito horas diárias e quarenta e oito semanais.", "dez horas diárias e quarenta e quatro semanais.", "oito horas diárias e quarenta e quatro semanais.", "doze horas diárias e trinta e seis semanais."],
     3, "Jornada: 8h diárias e 44h semanais. Gabarito D. PEGADINHA: ‘48 semanais’ ou inverter os números."),
    ("Art. 7º — idade", "Sobre a idade mínima para o trabalho, é correto afirmar que é proibido o trabalho a menores de",
     ["quatorze anos, sem qualquer exceção prevista.", "dezoito anos em qualquer atividade laboral.", "doze anos, salvo na condição de aprendiz.", "dezesseis anos, salvo aprendiz a partir dos doze.", "dezesseis anos, salvo na condição de aprendiz, a partir dos quatorze."],
     4, "Proibido a menores de 16, salvo aprendiz a partir dos 14. Gabarito E. PEGADINHA: trocar as idades."),
    ("Art. 8º — sindical", "Acerca da organização sindical (art. 8º), assinale a opção correta.",
     ["Vigora a pluralidade sindical, admitida a criação de vários sindicatos na mesma base territorial.", "É permitida a interferência do Poder Público na organização sindical, para garantir a ordem.", "É vedada a criação de mais de um sindicato na mesma base territorial, que não será inferior a um município.", "A filiação ao sindicato da categoria é obrigatória para todos os trabalhadores.", "O aposentado filiado não pode votar nem ser votado nas eleições sindicais."],
     2, "Unicidade sindical: um sindicato por base territorial (mínimo o município). Gabarito C. PEGADINHA: ‘pluralidade’."),
    ("Art. 9º — greve", "A respeito do direito de greve (art. 9º), assinale a opção correta.",
     ["Compete aos trabalhadores decidir sobre a oportunidade de exercê-lo e os interesses a defender.", "Compete exclusivamente ao sindicato decidir sobre a deflagração do movimento grevista.", "O direito de greve é vedado a todos os trabalhadores da iniciativa privada.", "A greve em atividades essenciais é proibida em qualquer hipótese pela Constituição.", "O direito de greve depende de autorização prévia do Ministério do Trabalho."],
     0, "São os trabalhadores que decidem oportunidade e interesses. Gabarito A. PEGADINHA: atribuir a decisão só ao sindicato."),
    ("Art. 7º — férias", "Quanto às férias anuais remuneradas, a Constituição assegura o pagamento",
     ["com, pelo menos, um terço a mais do que o salário normal.", "com, pelo menos, a metade a mais do que o salário normal.", "em valor igual ao do salário normal, sem acréscimo.", "com, pelo menos, o dobro do salário normal.", "com, pelo menos, dois terços a mais do que o salário normal."],
     0, "Férias = salário + no mínimo 1/3. Gabarito A. PEGADINHA: ‘metade’/‘dobro’."),
    ("Art. 7º — aviso prévio", "O aviso prévio, proporcional ao tempo de serviço, é assegurado com duração",
     ["fixa de quinze dias, independentemente do tempo de serviço.", "mínima de trinta dias, nos termos da lei.", "máxima de trinta dias, em qualquer caso.", "fixa de sessenta dias para todos os trabalhadores.", "definida exclusivamente em convenção coletiva, sem piso legal."],
     1, "Aviso prévio: proporcional ao tempo de serviço, mínimo de 30 dias. Gabarito B."),
    ("Art. 7º — 13º", "O décimo terceiro salário, segundo o art. 7º, tem como base de cálculo",
     ["metade da remuneração do mês de dezembro.", "o valor de um salário mínimo, em qualquer caso.", "a remuneração integral ou o valor da aposentadoria.", "apenas o salário-base, excluídos os adicionais.", "a média dos seis últimos salários recebidos."],
     2, "13º com base na remuneração integral (ou no valor da aposentadoria). Gabarito C."),
    ("Art. 6º", "Assinale a opção em que ambos os itens constituem direitos sociais previstos no art. 6º.",
     ["lazer e segurança", "emprego e renda", "internet e cultura", "turismo e desporto", "habitação e saneamento"],
     0, "Lazer e segurança constam do art. 6º. Os demais pares trazem itens fora do rol. Gabarito A."),
    ("Art. 7º — irredutibilidade", "A irredutibilidade do salário, prevista no art. 7º, comporta exceção quando houver",
     ["determinação unilateral do empregador, por dificuldade financeira.", "convenção ou acordo coletivo de trabalho.", "autorização individual e verbal do empregado.", "ordem direta do Ministério do Trabalho.", "previsão em regulamento interno da empresa."],
     1, "A redução salarial só é admitida por convenção ou acordo coletivo. Gabarito B."),
    ("Art. 11", "Nas empresas, é assegurada a eleição de um representante dos trabalhadores, com a finalidade de promover o entendimento direto com os empregadores, quando a empresa tiver",
     ["mais de cinquenta empregados.", "mais de cem empregados.", "mais de duzentos empregados.", "mais de quinhentos empregados.", "qualquer número de empregados."],
     2, "Art. 11: empresas com mais de 200 empregados. Gabarito C. PEGADINHA: 100/500."),
    ("Art. 7º — despedida", "A proteção da relação de emprego contra despedida arbitrária ou sem justa causa, nos termos do art. 7º, I,",
     ["é automática e independe de qualquer regulamentação posterior.", "foi inteiramente disciplinada por medida provisória.", "depende de edição de lei complementar que preveja indenização compensatória, entre outros direitos.", "aplica-se somente aos servidores públicos estatutários.", "vigora apenas para contratos por prazo determinado."],
     2, "A proteção depende de lei complementar. Gabarito C. PEGADINHA: ‘automática’."),
    ("Art. 7º — menor", "É vedado o trabalho noturno, perigoso ou insalubre aos",
     ["maiores de dezesseis e menores de dezoito anos apenas.", "menores de quatorze anos, em qualquer atividade.", "menores de dezesseis anos, salvo como aprendiz.", "menores de dezoito anos.", "menores de vinte e um anos, sem exceção."],
     3, "A vedação ao trabalho noturno, perigoso ou insalubre alcança todos os menores de 18 anos. Gabarito D."),
    ("Art. 8º — filiação", "Sobre a liberdade de filiação sindical, a Constituição estabelece que",
     ["todo trabalhador é obrigado a filiar-se ao sindicato de sua categoria.", "ninguém será obrigado a filiar-se ou a manter-se filiado a sindicato.", "a filiação depende de prévia autorização do empregador.", "somente os trabalhadores na ativa podem filiar-se a sindicato.", "a desfiliação depende de autorização judicial."],
     1, "A filiação sindical é livre: ninguém é obrigado a filiar-se ou manter-se filiado. Gabarito B."),
    ("Art. 7º — creche", "A assistência gratuita em creches e pré-escolas é assegurada aos filhos e dependentes dos trabalhadores desde o nascimento até os",
     ["três anos de idade.", "quatro anos de idade.", "cinco anos de idade.", "seis anos de idade.", "sete anos de idade."],
     2, "Creche e pré-escola: do nascimento aos 5 anos de idade. Gabarito C."),
    ("Art. 6º — emendas", "Assinale a opção que apresenta direito social incluído no art. 6º por emenda constitucional posterior a 1988.",
     ["a saúde", "a previdência social", "o transporte", "o trabalho", "a educação"],
     2, "‘Transporte’ foi incluído pela EC 90/2015 (moradia e alimentação também são posteriores). Gabarito C."),
    ("Art. 7º — lucros", "A participação nos lucros ou resultados da empresa, prevista no art. 7º, é",
     ["integrante da remuneração para todos os efeitos legais.", "desvinculada da remuneração, conforme definido em lei.", "obrigatória apenas para empresas estatais.", "calculada sempre em um salário mínimo.", "vedada nas empresas privadas."],
     1, "A participação nos lucros é desvinculada da remuneração. Gabarito B."),
    ("Art. 7º — salário mínimo", "Quanto ao salário mínimo, o art. 7º estabelece que ele é",
     ["fixado por decreto e regionalmente diferenciado entre os estados.", "nacionalmente unificado e passível de vinculação como índice.", "fixado em lei, nacionalmente unificado, vedada sua vinculação para qualquer fim.", "reajustado a critério exclusivo do empregador.", "destinado a atender apenas às necessidades do trabalhador, excluída a família."],
     2, "Salário mínimo: fixado em lei, nacionalmente unificado, vedada a vinculação para qualquer fim, atendendo o trabalhador e sua família. Gabarito C."),
]


def card(c):
    t, lei, expl, peg, mac = c
    return f"""<div class="card"><div class="head"><span class="tit">{t}</span></div>
      <div class="lei">{lei}</div>
      <div class="block"><span class="tag t-trad">O que significa</span><br>{expl}</div>
      <div class="block peg"><span class="tag t-peg">Pegadinha Quadrix</span><br>{peg}</div>
      <div class="block mac"><span class="tag t-mac">Macete</span> &nbsp;{mac}</div></div>"""


def q(i, item):
    tema, enun, opts, ok, com = item
    lis = "".join(f'<li class="{"ok" if j==ok else ""}">{o}</li>' for j, o in enumerate(opts))
    return f"""<div class="q"><div class="tema">{tema}</div>
      <div class="qh"><span class="qn">Questão {i}.</span> {enun}</div>
      <ol>{lis}</ol>
      <div class="com"><b class="g">Gabarito: {"ABCDE"[ok]}.</b> {com}</div></div>"""


def gabarito():
    cells = "".join(f'<div class="cell">{i}<b> {"ABCDE"[it[3]]}</b></div>' for i, it in enumerate(Q, 1))
    from collections import Counter
    cnt = Counter("ABCDE"[it[3]] for it in Q)
    dist = " · ".join(f"{k}: {cnt.get(k,0)}" for k in "ABCDE")
    return f'<div class="gabarito"><h3>Gabarito — 20 questões</h3><div class="grid">{cells}</div><div class="note">Distribuição — {dist}.</div></div>'


CSS = """
@page { size:A4; margin:14mm 13mm 16mm 13mm; }
* { box-sizing:border-box; }
body { font-family:'Segoe UI','Helvetica Neue',Arial,sans-serif; color:#1f2733; font-size:10.2px; line-height:1.5; margin:0; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
h1,h2,h3,h4 { margin:0; font-weight:700; }
.cover { height:252mm; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; background:linear-gradient(135deg,#7a0c1c 0%,#b3122a 55%,#8e1020 100%); color:#fff; border-radius:6px; page-break-after:always; padding:0 24mm; }
.cover .kicker { letter-spacing:4px; font-size:12px; opacity:.85; font-weight:600; }
.cover h1 { font-size:44px; line-height:1.05; margin:10px 0 6px; }
.cover .sub { font-size:16px; font-weight:400; opacity:.95; max-width:135mm; }
.cover .rule { width:70px; height:4px; background:#ffd27a; margin:22px 0; border-radius:2px; }
.cover .meta { font-size:12.5px; opacity:.9; line-height:1.7; }
.cover .badge { margin-top:26px; background:rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.4); padding:9px 18px; border-radius:40px; font-size:13px; font-weight:600; }
.section-title { font-size:19px; color:#b3122a; border-bottom:3px solid #b3122a; padding-bottom:5px; margin:4px 0 12px; page-break-after:avoid; }
.lead { font-size:11px; color:#3a4658; margin-bottom:10px; }
.grid2 { display:grid; grid-template-columns:1fr 1fr; gap:9px; }
.callout { border-radius:7px; padding:9px 11px; margin:7px 0; page-break-inside:avoid; }
.c-key { background:#eefaf1; border-left:4px solid #1f9d57; }
.c-tip { background:#eef4ff; border-left:4px solid #2b6cb0; }
.callout h4 { font-size:11px; margin-bottom:4px; text-transform:uppercase; letter-spacing:.5px; color:#1f9d57; }
.c-tip h4 { color:#2b6cb0; }
.callout ul { margin:3px 0 0; padding-left:16px; } .callout li { margin:2px 0; }
.card { border:1px solid #e2e6ee; border-radius:9px; padding:11px 13px; margin:0 0 11px; page-break-inside:avoid; background:#fff; box-shadow:0 1px 2px rgba(20,30,50,.04); }
.card .head { margin-bottom:5px; }
.card .tit { font-size:12px; color:#7a0c1c; font-weight:700; border-left:4px solid #b3122a; padding-left:8px; }
.card .lei { background:#f4f6fa; border-left:3px solid #9aa6b8; border-radius:4px; padding:6px 9px; font-style:italic; color:#2a3340; font-size:9.6px; margin:5px 0; }
.tag { font-weight:700; font-size:9px; text-transform:uppercase; letter-spacing:.4px; }
.t-trad { color:#2b6cb0; } .t-peg { color:#c0392b; } .t-mac { color:#1f9d57; }
.block { margin-top:4px; }
.block.peg { background:#fff5f5; border-radius:5px; padding:6px 8px; }
.block.mac { background:#eefaf1; border-radius:5px; padding:6px 8px; }
.q { border:1px solid #e2e6ee; border-radius:8px; padding:9px 11px; margin:0 0 9px; page-break-inside:avoid; }
.q .qh { font-size:10.5px; font-weight:700; color:#1f2733; margin-bottom:5px; }
.q .qh .qn { color:#b3122a; }
.q .tema { display:inline-block; background:#eef0f5; color:#56627a; font-size:8.3px; font-weight:700; text-transform:uppercase; letter-spacing:.4px; padding:2px 7px; border-radius:20px; margin-bottom:5px; }
.q ol { margin:4px 0 0; padding-left:0; list-style:none; counter-reset:opt; }
.q ol li { counter-increment:opt; margin:2.5px 0; padding-left:20px; position:relative; font-size:9.6px; }
.q ol li::before { content:counter(opt,upper-alpha); position:absolute; left:0; top:0; font-weight:700; color:#56627a; }
.q ol li.ok::before { color:#1f9d57; } .q ol li.ok { background:#eefaf1; border-radius:4px; }
.q .com { margin-top:6px; font-size:9.1px; color:#46536a; background:#fafbfd; border-left:3px solid #1f9d57; border-radius:4px; padding:5px 8px; }
.q .com b.g { color:#1f9d57; }
.gabarito { background:#1f2733; color:#fff; border-radius:9px; padding:14px 16px; page-break-inside:avoid; }
.gabarito h3 { color:#ffd27a; font-size:14px; margin-bottom:8px; }
.gabarito .grid { display:grid; grid-template-columns:repeat(10,1fr); gap:5px; }
.gabarito .cell { background:rgba(255,255,255,.08); border-radius:5px; text-align:center; padding:5px 0; font-size:9.5px; }
.gabarito .cell b { color:#ffd27a; }
.note { font-size:8.6px; color:#9aa6b8; margin-top:8px; }
.h-chapter { page-break-before:always; }
"""

cards_html = "".join(card(c) for c in CARDS)
questoes_html = "".join(q(i, it) for i, it in enumerate(Q, 1))

HTML = f"""<!DOCTYPE html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="cover">
  <div class="kicker">DIREITO CONSTITUCIONAL</div>
  <h1>Direitos<br>Sociais</h1>
  <div class="rule"></div>
  <div class="sub">Arts. 6º a 11 da CF/88 — os números que a banca adora e 20 questões comentadas</div>
  <div class="meta" style="margin-top:26px;">Concurso <b>Sedes/DF</b> · Banca <b>Quadrix</b> · 2026<br>Técnico Administrativo (Cargo 202)</div>
  <div class="badge">Dia 5 · Direitos sociais</div>
</div>

<h2 class="section-title">1. Por que os direitos sociais caem (e derrubam)</h2>
<p class="lead">Os arts. 6º a 11 são a parte mais ‘decoreba’ de Constitucional: a banca cobra <b>números</b> (120 dias, 1/3, 50%, 16/14/18 anos, 200 empregados) e <b>listas</b> (o rol do art. 6º). A pegadinha quase sempre é trocar um número ou inventar um direito fora do rol. Quem fixa os números acerta.</p>
<div class="grid2">
  <div class="callout c-tip"><h4>O mapa dos artigos</h4><ul>
    <li><b>Art. 6º</b> — rol dos 11 direitos sociais.</li>
    <li><b>Art. 7º</b> — direitos dos trabalhadores (a maioria das questões).</li>
    <li><b>Art. 8º</b> — organização sindical (unicidade).</li>
    <li><b>Art. 9º</b> — direito de greve.</li>
    <li><b>Arts. 10–11</b> — participação e representante dos trabalhadores.</li>
  </ul></div>
  <div class="callout c-key"><h4>Os números de ouro</h4><ul>
    <li><b>120</b> dias — licença-maternidade.</li>
    <li><b>+1/3</b> — adicional de férias · <b>+50%</b> — hora extra.</li>
    <li><b>8h/44h</b> — jornada · <b>6h</b> — turno de revezamento.</li>
    <li><b>16/14/18</b> — idade (geral/aprendiz/noturno-insalubre).</li>
    <li><b>200</b> — empregados para ter representante (art. 11).</li>
  </ul></div>
</div>

<h2 class="section-title h-chapter">2. Teoria em cards</h2>
{cards_html}

<h2 class="section-title h-chapter">3. 20 Questões Comentadas</h2>
<p class="lead">Distratores equilibrados e gabarito distribuído A–E. Tente identificar o número/elemento trocado antes de conferir.</p>
{questoes_html}

<h2 class="section-title h-chapter">4. Gabarito</h2>
{gabarito()}
</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("HTML gerado:", OUT, "| cards:", len(CARDS), "| questoes:", len(Q))
