# -*- coding: utf-8 -*-
"""Material DENSO (apostila) — Dia 4: Direito Constitucional, Art. 5º da CF/88.
Teoria em prosa + leitura da lei seca comentada + 35 questões (15 C/E + 20 A-E)
com gabarito comentado completo. Segue docs/prompt-mestre.md. Render via Chrome.
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(_HERE)
OUTDIR = os.path.join(_REPO, "materiais", "dia04-art5-cf88")
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "Dia4_Art5_Completo.html")

# ---- Lei seca comentada (texto | comentário/armadilha) ----
LEISECA = [
    ("II — Ninguém será obrigado a fazer ou deixar de fazer alguma coisa senão em virtude de lei.",
     "Só LEI formal cria obrigação ao particular. Banca troca “lei” por “decreto”, “portaria” ou “ato administrativo”."),
    ("IV — É livre a manifestação do pensamento, sendo vedado o anonimato.",
     "Pode falar, não pode se esconder. Troca-armadilha: “sendo permitido o anonimato” ou “liberdade absoluta”."),
    ("X — São invioláveis a intimidade, a vida privada, a honra e a imagem das pessoas…",
     "Quatro bens (I-V-H-I). Banca exclui um (ex.: tira “imagem”) ou acrescenta “patrimônio”."),
    ("XI — A casa é asilo inviolável… salvo flagrante delito ou desastre, ou para prestar socorro, ou, durante o dia, por determinação judicial.",
     "Mandado judicial só DE DIA; flagrante/desastre/socorro a qualquer hora. Troca: “a qualquer hora, por ordem judicial”."),
    ("XII — É inviolável o sigilo… das comunicações telefônicas, salvo, no último caso, por ordem judicial…",
     "Interceptação telefônica só por JUIZ e para fins penais. Troca: “autoridade policial” ou “processo civil”."),
    ("XL — A lei penal não retroagirá, salvo para beneficiar o réu.",
     "Retroage só para o bem do réu. Troca: “não retroagirá em hipótese alguma” (omite a exceção)."),
    ("XLII — A prática do racismo constitui crime inafiançável e imprescritível, sujeito à pena de reclusão…",
     "Inafiançável E imprescritível. Troca: “prescreve em 20 anos” ou “afiançável” / “contravenção”."),
    ("XLIII — …inafiançáveis e insuscetíveis de graça ou anistia a tortura, o tráfico, o terrorismo e os hediondos.",
     "São inafiançáveis e sem graça/anistia, mas PRESCREVEM. Troca: dizer que são “imprescritíveis” como o racismo."),
    ("LVII — Ninguém será considerado culpado até o trânsito em julgado de sentença penal condenatória.",
     "Inocente até o fim dos recursos. Troca: “até a condenação em segunda instância”."),
    ("LXIX — Conceder-se-á mandado de segurança para proteger direito líquido e certo… não amparado por habeas corpus ou habeas data.",
     "MS = direito líquido e certo (prova pronta). Troca: confundir com mandado de injunção (falta de norma)."),
]

# ---- 15 Certo/Errado ----
QCE = [
    ("Os direitos e garantias do art. 5º são assegurados aos brasileiros e aos estrangeiros residentes no País.",
     "C", "Correto. É a literalidade do caput. A palavra-chave “residentes” é o ponto que a banca costuma explorar."),
    ("Por não ser residente, o turista estrangeiro não pode invocar nenhum direito fundamental enquanto estiver no Brasil.",
     "E", "Errado. Embora o caput cite “residentes”, o STF estende o núcleo essencial (vida, integridade, acesso à Justiça) a qualquer pessoa em território nacional. “Nenhum direito” é generalização indevida."),
    ("É livre a manifestação do pensamento, sendo permitido o anonimato quando necessário à proteção da fonte.",
     "E", "Errado. O inciso IV veda o anonimato. A troca de “vedado” por “permitido” é a armadilha clássica."),
    ("Durante o dia, é possível ingressar na casa, sem consentimento do morador, por determinação judicial.",
     "C", "Correto. O inciso XI autoriza o ingresso por ordem judicial apenas durante o dia."),
    ("Havendo determinação judicial, admite-se o ingresso no domicílio a qualquer hora do dia ou da noite.",
     "E", "Errado. O mandado judicial vale só durante o dia. À noite, só com flagrante, desastre ou para prestar socorro."),
    ("A interceptação das comunicações telefônicas pode ser determinada pela autoridade policial no curso da investigação.",
     "E", "Errado. A interceptação depende de ordem JUDICIAL e se destina a fins penais (inciso XII). Delegado ou promotor, sozinho, não pode."),
    ("A prática do racismo constitui crime inafiançável e imprescritível, sujeito à pena de reclusão.",
     "C", "Correto. É a literalidade do inciso XLII. Racismo não prescreve e não admite fiança."),
    ("Os crimes hediondos, a exemplo do racismo, são imprescritíveis.",
     "E", "Errado. Hediondos e equiparados são inafiançáveis e insuscetíveis de graça/anistia, mas PRESCREVEM. Imprescritíveis são apenas o racismo e a ação de grupos armados."),
    ("A lei penal não retroagirá, salvo para beneficiar o réu.",
     "C", "Correto. Literalidade do inciso XL: a lei penal mais benéfica retroage, inclusive para quem já foi condenado."),
    ("Nenhum brasileiro será extraditado, não havendo qualquer exceção a essa regra.",
     "E", "Errado. O nato nunca é extraditado, mas o naturalizado pode ser, por crime comum anterior à naturalização ou por tráfico (inciso LI). A generalização “qualquer exceção” torna o item falso."),
    ("Ninguém será considerado culpado até o trânsito em julgado de sentença penal condenatória.",
     "C", "Correto. Literalidade do inciso LVII (presunção de inocência). A culpa só se firma após esgotados os recursos."),
    ("São inadmissíveis as provas obtidas por meios ilícitos, salvo quando forem a única forma de comprovar a verdade.",
     "E", "Errado. O inciso LVI não traz essa ressalva: a prova ilícita é inadmissível e contamina as provas dela derivadas. A oração com “salvo” insere uma exceção inexistente."),
    ("O contraditório e a ampla defesa são assegurados apenas no processo judicial.",
     "E", "Errado. O inciso LV garante o contraditório e a ampla defesa também no processo administrativo. A palavra “apenas” restringe indevidamente."),
    ("A pena não passará da pessoa do condenado, mas a obrigação de reparar o dano pode estender-se aos sucessores, até o limite do patrimônio transferido.",
     "C", "Correto. É a redação do inciso XLV: a pena é pessoal; a reparação e o perdimento de bens alcançam os herdeiros, limitados à herança."),
    ("As normas definidoras dos direitos e garantias fundamentais têm aplicação imediata.",
     "C", "Correto. É o § 1º do art. 5º. A regra é a aplicabilidade imediata, ainda que algumas normas dependam de lei."),
]

# ---- 20 múltipla escolha A-E (enunciado, [A..E], idx, comentário) ----
QME = [
    ("Sigilo (XII)", "Acerca do sigilo das comunicações, assinale a opção correta.",
     ["É absoluto o sigilo das comunicações telefônicas, não se admitindo exceção.",
      "A interceptação telefônica pode ser determinada diretamente pela autoridade policial.",
      "O sigilo telefônico pode ser afastado por ordem de comissão parlamentar de inquérito municipal.",
      "A interceptação das comunicações telefônicas é admitida para instruir processo de natureza civil.",
      "A interceptação telefônica é admitida por ordem judicial, na forma da lei, para fins penais."],
     4, "Gabarito E: a exceção ao sigilo exige ordem judicial e fim penal. ✗A: o sigilo não é absoluto. ✗B: delegado não pode sozinho. ✗C: CPI municipal não tem esse poder. ✗D: a exceção é para a investigação criminal, não o processo civil."),
    ("Escusa de consciência (VIII)", "A respeito da escusa de consciência, assinale a opção correta.",
     ["A crença religiosa autoriza, em qualquer hipótese, o descumprimento de obrigação legal.",
      "A privação de direitos por convicção política é vedada de forma absoluta.",
      "A escusa aplica-se somente às obrigações ligadas ao serviço militar.",
      "Haverá privação de direitos se a pessoa recusar a obrigação legal e também a prestação alternativa fixada em lei.",
      "Não se admite, em nenhum caso, a fixação de prestação alternativa."],
     3, "Gabarito D: a perda de direitos só ocorre na dupla recusa (obrigação + alternativa). ✗A: não é “em qualquer hipótese”. ✗B: não é “absoluta”, há a exceção. ✗C: não se limita ao serviço militar. ✗E: a prestação alternativa existe e é fixada em lei."),
    ("Reunião (XVI)", "Acerca do direito de reunião, assinale a opção correta.",
     ["A reunião em local aberto ao público depende de prévia autorização da autoridade.",
      "É permitida a reunião armada, desde que pacífica.",
      "A reunião pacífica, sem armas, em local aberto, independe de autorização, exigido apenas aviso prévio.",
      "É vedada toda reunião em local aberto ao público sem fiscalização estatal.",
      "Exige-se autorização judicial para qualquer reunião."],
     2, "Gabarito C: reunião pacífica e sem armas só exige aviso prévio. ✗A e ✗E: não se exige autorização (administrativa ou judicial). ✗B: reunião não pode ser armada. ✗D: a regra é a liberdade, não a vedação."),
    ("Pessoalidade da pena (XLV)", "Sobre a pessoalidade da pena, assinale a opção correta.",
     ["A pena privativa de liberdade pode passar aos sucessores do condenado.",
      "A obrigação de reparar o dano pode ser estendida aos sucessores, até o limite do patrimônio transferido.",
      "A decretação do perdimento de bens não pode, em nenhuma hipótese, atingir os sucessores.",
      "A obrigação de reparar o dano jamais atinge os sucessores.",
      "A pena privativa de liberdade pode ser cumprida pelos sucessores."],
     1, "Gabarito B: a reparação e o perdimento alcançam os herdeiros até o limite da herança. ✗A e ✗E: a pena é pessoal, não se transmite. ✗C e ✗D: reparação e perdimento podem, sim, estender-se aos sucessores."),
    ("Domicílio (XI)", "Quanto à inviolabilidade do domicílio, assinale a opção correta.",
     ["Durante o dia, a casa pode ser invadida por determinação judicial, na forma da lei.",
      "Em flagrante delito, a casa só pode ser invadida durante o dia.",
      "O ingresso para prestar socorro depende sempre de prévia ordem judicial.",
      "A determinação judicial autoriza o ingresso a qualquer hora do dia ou da noite.",
      "Em caso de desastre, o ingresso exige o consentimento do morador ausente."],
     0, "Gabarito A: ordem judicial autoriza o ingresso durante o dia. ✗B: o flagrante autoriza a qualquer hora. ✗C: socorro independe de ordem judicial. ✗D: mandado só de dia. ✗E: desastre dispensa consentimento."),
    ("Titulares (caput)", "Acerca dos destinatários dos direitos do art. 5º, assinale a opção correta.",
     ["São assegurados exclusivamente aos brasileiros natos.",
      "Os estrangeiros de passagem equiparam-se em tudo aos residentes.",
      "São assegurados aos brasileiros e aos estrangeiros residentes, sem distinção de qualquer natureza.",
      "A igualdade do caput refere-se à igualdade de resultados sociais.",
      "Os brasileiros naturalizados não têm a garantia da inviolabilidade da vida."],
     2, "Gabarito C: é a literalidade do caput. ✗A: alcança também naturalizados e estrangeiros residentes. ✗B: turista não se equipara “em tudo” ao residente. ✗D: é igualdade formal (perante a lei). ✗E: o naturalizado é plenamente titular."),
    ("Legalidade (II)", "Considerando o princípio da legalidade, assinale a opção correta.",
     ["O particular pode ser obrigado a algo em virtude de decreto do Executivo.",
      "A obrigação pode decorrer de portaria de autoridade administrativa.",
      "Atos normativos criam obrigações novas independentemente de lei.",
      "A Administração, por sua supremacia, pode impor deveres sem lei formal.",
      "Ninguém será obrigado a fazer ou deixar de fazer algo senão em virtude de lei."],
     4, "Gabarito E: literalidade do inciso II. ✗A, ✗B, ✗C: decreto, portaria e atos normativos não criam obrigação ao particular sem lei. ✗D: a supremacia não dispensa a lei formal."),
    ("Anonimato (IV)", "Sobre a liberdade de manifestação do pensamento, assinale a opção correta.",
     ["A liberdade de expressão é absoluta e afasta responsabilização.",
      "É livre a manifestação do pensamento, sendo vedado o anonimato.",
      "O anonimato é assegurado para proteger a fonte jornalística.",
      "A manifestação depende de prévio licenciamento do poder público.",
      "A vedação ao anonimato só vale para meios impressos."],
     1, "Gabarito B: literalidade do inciso IV. ✗A: a liberdade não é absoluta (há o direito de resposta e a indenização). ✗C: o anonimato é vedado. ✗D: não há licenciamento prévio. ✗E: a vedação é geral, não só para impressos."),
    ("Resposta (V)", "Quanto ao direito de resposta, assinale a opção correta.",
     ["O ofendido deve optar entre resposta e indenização.",
      "A indenização restringe-se ao dano material.",
      "O direito de resposta independe de proporcionalidade ao agravo.",
      "É assegurado o direito de resposta, proporcional ao agravo, além da indenização por dano material, moral ou à imagem.",
      "A indenização só cabe quando inexistir direito de resposta."],
     3, "Gabarito D: literalidade do inciso V (“além da” = cumulação). ✗A: são cumuláveis, não excludentes. ✗B: cabe dano moral e à imagem. ✗C: a resposta é proporcional ao agravo. ✗E: a indenização não depende da inexistência de resposta."),
    ("Inafastabilidade (XXXV)", "A respeito do acesso à Justiça, assinale a opção correta.",
     ["A lei pode excluir da apreciação do Judiciário a ameaça a direito.",
      "O acesso ao Judiciário pressupõe o esgotamento da via administrativa.",
      "Somente a lesão, e não a ameaça, pode ser submetida ao Judiciário.",
      "A apreciação judicial depende de autorização do órgão de origem.",
      "A lei não excluirá da apreciação do Poder Judiciário lesão ou ameaça a direito."],
     4, "Gabarito E: literalidade do inciso XXXV — alcança lesão E ameaça. ✗A e ✗C: a ameaça também é apreciável. ✗B: em regra não se exige exaurir a via administrativa. ✗D: não depende de autorização."),
    ("Racismo (XLII)", "Sobre o crime de racismo, assinale a opção correta.",
     ["Prescreve em vinte anos.",
      "Admite fiança ao réu primário.",
      "Constitui contravenção penal.",
      "É inafiançável e imprescritível, sujeito a reclusão.",
      "É afiançável, mas imprescritível."],
     3, "Gabarito D: literalidade do inciso XLII. ✗A: é imprescritível. ✗B e ✗E: é inafiançável. ✗C: é crime, não contravenção."),
    ("Devido processo (LIV)", "A privação da liberdade ou de bens, segundo o art. 5º, exige",
     ["mera decisão administrativa.",
      "apenas ordem do chefe imediato.",
      "concordância da vítima.",
      "decreto do Poder Executivo.",
      "o devido processo legal."],
     4, "Gabarito E: literalidade do inciso LIV. ✗A, ✗B, ✗D: nenhuma decisão isolada substitui o devido processo. ✗C: a vontade da vítima não é requisito."),
    ("Ampla defesa (LV)", "Sobre o contraditório e a ampla defesa, assinale a opção correta.",
     ["Existem apenas no processo judicial.",
      "São assegurados também no processo administrativo.",
      "Dependem de previsão em estatuto.",
      "Valem só no processo penal.",
      "São dispensáveis quando a prova é robusta."],
     1, "Gabarito B: o inciso LV alcança o processo judicial E o administrativo. ✗A e ✗D: não se restringem ao judicial/penal. ✗C: a garantia é constitucional. ✗E: nunca são dispensáveis."),
    ("Extradição (LI)", "Brasileiro naturalizado, acusado de tráfico cometido após a naturalização, quanto à extradição,",
     ["não pode ser extraditado, por ser brasileiro.",
      "só poderia se o crime fosse anterior à naturalização.",
      "depende de plebiscito.",
      "pode ser extraditado, pois o envolvimento com o tráfico autoriza a medida.",
      "só cabe para brasileiro nato."],
     3, "Gabarito D: o naturalizado é extraditável por tráfico (antes ou depois) ou por crime comum anterior à naturalização. ✗A: a naturalização não blinda nesse caso. ✗B: o tráfico não exige anterioridade. ✗C: não há plebiscito. ✗E: o nato é justamente o inextraditável."),
    ("Penas (XLVII)", "Assinale a única pena admitida, excepcionalmente, pela Constituição.",
     ["pena de morte em caso de guerra declarada.",
      "prisão perpétua para hediondos.",
      "trabalhos forçados.",
      "banimento de reincidentes.",
      "penas cruéis para terroristas."],
     0, "Gabarito A: a única exceção é a pena de morte em guerra declarada. ✗B, ✗C, ✗D, ✗E: perpétua, trabalhos forçados, banimento e penas cruéis são sempre vedados."),
    ("Presunção de inocência (LVII)", "Réu condenado em primeira instância, ainda cabível recurso, é",
     ["culpado, pois já houve condenação.",
      "presumido inocente até o trânsito em julgado da sentença penal condenatória.",
      "culpado a partir da segunda instância.",
      "semi-culpado.",
      "culpado, mas com direito a recurso."],
     1, "Gabarito B: só é culpado após o trânsito em julgado. ✗A, ✗C, ✗E: condenação recorrível não firma a culpa. ✗D: não existe tal categoria."),
    ("Provas ilícitas (LVI)", "A única prova da autoria foi obtida mediante tortura. Essa prova",
     ["é admissível por ser decisiva.",
      "é admissível se confirmada por outra.",
      "é inadmissível, por ter origem ilícita.",
      "vale apenas na fase de investigação.",
      "é válida se o réu confessar depois."],
     2, "Gabarito C: prova ilícita é inadmissível e contamina as derivadas. ✗A e ✗B: a relevância não convalida a ilicitude. ✗D: não vale em fase alguma do processo. ✗E: a confissão posterior não a legitima."),
    ("Petição (XXXIV)", "Sobre o direito de petição e a obtenção de certidões, assinale a opção correta.",
     ["Dependem do pagamento de taxa de expediente.",
      "Exigem demonstração de interesse econômico.",
      "São assegurados a todos, independentemente do pagamento de taxas.",
      "São exclusivos de brasileiros natos.",
      "Podem ser cobrados em caráter de urgência."],
     2, "Gabarito C: petição e certidões são gratuitas e para todos. ✗A, ✗E: independem de taxa. ✗B: não se exige interesse econômico. ✗D: não são exclusivos de natos."),
    ("Segurança jurídica (XXXVI)", "Assinale o que a lei NÃO pode prejudicar, segundo o art. 5º.",
     ["a expectativa de direito.",
      "o direito adquirido, o ato jurídico perfeito e a coisa julgada.",
      "os interesses da Administração.",
      "os contratos futuros.",
      "as meras liberalidades."],
     1, "Gabarito B: o trio protegido é direito adquirido, ato jurídico perfeito e coisa julgada. ✗A: a expectativa de direito NÃO é protegida. ✗C, ✗D, ✗E: não integram a garantia do inciso XXXVI."),
    ("Remédios (LXXI)", "O instrumento cabível diante da falta de norma regulamentadora que inviabiliza um direito é o",
     ["habeas corpus.",
      "mandado de injunção.",
      "habeas data.",
      "mandado de segurança.",
      "ação popular."],
     1, "Gabarito B: o mandado de injunção combate a omissão legislativa. ✗A: HC protege a locomoção. ✗C: HD trata de dados pessoais. ✗D: MS protege direito líquido e certo já existente. ✗E: ação popular anula ato lesivo ao patrimônio público."),
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
table { width:100%; border-collapse:collapse; margin:7px 0; font-size:9.7px; page-break-inside:avoid; }
th { background:#7a0c1c; color:#fff; text-align:left; padding:6px 8px; }
td { border:1px solid #e2e6ee; padding:6px 8px; vertical-align:top; }
tr:nth-child(even) td { background:#fbf6f7; }
td .rn { font-weight:700; color:#b3122a; }
.ls td:first-child { font-style:italic; color:#2a3340; }
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

leiseca_rows = "".join(f"<tr><td>{t}</td><td>{c}</td></tr>" for (t, c) in LEISECA)
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
  <h1>Artigo 5º<br>da CF/88</h1>
  <div class="rule"></div>
  <div class="sub">Direitos e deveres individuais e coletivos — apostila, lei seca comentada e 35 questões com gabarito comentado</div>
  <div class="meta" style="margin-top:26px;">Concurso <b>Sedes/DF</b> · Banca <b>Quadrix</b> · 2026<br>Técnico Administrativo (Cargo 202)</div>
  <div class="badge">Dia 4 · 35 questões para fazer agora</div>
</div>

<h2 class="section-title">1. Por que o art. 5º derruba tanta gente</h2>
<p>O art. 5º é o coração da Constituição: nele estão os direitos e garantias fundamentais, e por isso é cobrado em praticamente toda prova da Quadrix — em geral, de três a cinco questões. A dificuldade não está no volume, e sim no fato de a banca ser de <b>literalidade</b>: ela transcreve o dispositivo trocando <b>um único elemento</b> para criar o erro — uma palavra (“vedado” por “permitido”), um número, uma condição (“durante o dia” por “a qualquer hora”) ou um nome de remédio constitucional. Quem decorou o inciso solto se confunde; quem entendeu a lógica reconhece a troca. Este material explica cada instituto e, em seguida, mostra a leitura da lei seca lado a lado com o ponto exato que a banca costuma alterar.</p>

<h2 class="section-title">2. O caput: quem tem direito e a quê</h2>
<p>O caput abre afirmando que “todos são iguais perante a lei, sem distinção de qualquer natureza”. Trata-se da <b>igualdade formal</b> — o mesmo tratamento pelas regras, sem privilégios — que não se confunde com a <b>igualdade material</b>, aquela que trata os desiguais na medida de suas diferenças (e que fundamenta, por exemplo, as ações afirmativas). Em seguida, o texto enuncia os cinco bens que serão protegidos: <b>vida, liberdade, igualdade, segurança e propriedade</b>. Esse rol, contudo, é <b>exemplificativo</b>: o § 2º deixa claro que existem outros direitos decorrentes do regime e dos princípios constitucionais e dos tratados.</p>
<p>O ponto mais explorado do caput são os <b>titulares</b>. O texto assegura os direitos “aos brasileiros e aos estrangeiros <b>residentes</b> no País”. A palavra “residentes” é a armadilha: a banca afirma que o turista estrangeiro “não tem direito algum” (falso, porque o STF estende o núcleo essencial — vida, integridade, acesso à Justiça — a qualquer pessoa em território nacional) ou, ao contrário, que o caput protege “qualquer pessoa do mundo, sem exceção” (falso pela letra do dispositivo). Saber distinguir o <b>texto literal</b> da <b>interpretação do STF</b> resolve a questão.</p>
<p>Por fim, três parágrafos completam o quadro. O <b>§ 1º</b> estabelece que as normas definidoras de direitos e garantias fundamentais têm <b>aplicação imediata</b> — regra que admite exceções, pois algumas normas dependem de lei. O <b>§ 3º</b> dispõe que os tratados internacionais de direitos humanos aprovados em <b>dois turnos, por três quintos</b> dos votos de cada Casa do Congresso equivalem a <b>emendas constitucionais</b> (sem esse rito, têm status supralegal). O <b>§ 4º</b> reconhece a submissão do Brasil ao Tribunal Penal Internacional.</p>
<div class="callout c-mnem"><h4>Mnemônico — os 5 pilares (V.L.I.S.P.)</h4><b>V</b>ida · <b>L</b>iberdade · <b>I</b>gualdade · <b>S</b>egurança · <b>P</b>ropriedade. Rol exemplificativo (há outros direitos, § 2º).</div>

<h2 class="section-title">3. As liberdades individuais</h2>
<p>O inciso <b>II</b> consagra a <b>legalidade</b>: ninguém é obrigado a fazer ou deixar de fazer algo senão em virtude de <b>lei</b> formal — decreto, portaria ou ato administrativo não bastam para impor obrigação ao particular. O inciso <b>IV</b> garante a livre manifestação do pensamento, mas <b>veda o anonimato</b>: pode-se falar, não se pode esconder a autoria, o que justifica o direito de resposta e a indenização do inciso <b>V</b> (que são <b>cumuláveis</b> — resposta “além da” indenização). O inciso <b>VI</b> torna inviolável a liberdade de consciência e de crença, assegurando o livre exercício dos cultos; e o <b>VIII</b> trata da escusa de consciência: ninguém é privado de direitos por convicção, <b>salvo</b> se invocá-la para se eximir de obrigação a todos imposta <b>e</b> recusar a prestação alternativa fixada em lei. O inciso <b>X</b>, por sua vez, declara invioláveis a <b>intimidade, a vida privada, a honra e a imagem</b>, assegurando indenização pelo dano — é a base do dano moral.</p>

<h2 class="section-title">4. As inviolabilidades: domicílio e comunicações</h2>
<p>O inciso <b>XI</b> protege a casa como “asilo inviolável”. Há quatro hipóteses de ingresso sem consentimento do morador: <b>flagrante delito</b>, <b>desastre</b>, para <b>prestar socorro</b> — essas três a qualquer hora, dia ou noite — e, somente <b>durante o dia</b>, por <b>determinação judicial</b>. A pegadinha mais comum afirma que o mandado judicial autoriza a entrada “a qualquer hora”, o que é falso. O inciso <b>XII</b> garante o sigilo da correspondência e das comunicações; a única exceção — a interceptação das <b>comunicações telefônicas</b> — exige <b>ordem judicial</b> e destina-se a fins penais (investigação criminal ou instrução processual penal). Nem o delegado nem o promotor, isoladamente, podem determiná-la.</p>
<div class="callout c-peg"><h4>Pegadinhas de domicílio e sigilo</h4>
  <ul>
    <li>“Por ordem judicial, ingressa-se a qualquer hora.” — Falso: <b>mandado só de dia</b>.</li>
    <li>“A autoridade policial pode interceptar o telefone.” — Falso: só por <b>juiz</b>, e para fins penais.</li>
  </ul></div>

<h2 class="section-title">5. Reunião, associação e propriedade</h2>
<p>O inciso <b>XVI</b> assegura a reunião pacífica, sem armas, em locais abertos ao público, <b>independentemente de autorização</b> e exigido apenas o <b>aviso prévio</b> à autoridade. Os incisos <b>XVII a XXI</b> tratam da liberdade de associação: ela é plena para fins lícitos, <b>vedada a de caráter paramilitar</b>, e a dissolução compulsória de uma associação só ocorre por <b>decisão judicial transitada em julgado</b>. Quanto à <b>propriedade</b> (XXII a XXVI), ela é garantida, mas deve atender à sua <b>função social</b>; a desapropriação por necessidade ou utilidade pública depende de <b>justa e prévia indenização</b>, em regra em dinheiro.</p>

<h2 class="section-title">6. Garantias penais e processuais</h2>
<p>Esse é o bloco mais cobrado. O inciso <b>XXXIX</b> fixa a <b>legalidade penal</b> (não há crime sem lei anterior que o defina); o <b>XL</b> determina que a lei penal <b>não retroage, salvo para beneficiar o réu</b>. O <b>XLII</b> trata do <b>racismo</b> — crime <b>inafiançável e imprescritível</b>; já o <b>XLIII</b> torna a tortura, o tráfico, o terrorismo e os hediondos <b>inafiançáveis e insuscetíveis de graça ou anistia</b>, mas, atenção, <b>prescritíveis</b> (a confusão entre os dois incisos é a pegadinha preferida: imprescritíveis são apenas o racismo e a ação de grupos armados). O <b>XLV</b> estabelece a <b>pessoalidade da pena</b> (a pena não passa do condenado, mas a reparação e o perdimento de bens alcançam os herdeiros até o limite da herança); o <b>XLVII</b> veda as penas de morte (salvo guerra declarada), perpétua, de trabalhos forçados, de banimento e cruéis. Em matéria de extradição, o <b>LI</b> dispõe que o brasileiro <b>nato</b> nunca é extraditado, e o <b>naturalizado</b> só em dois casos (crime comum anterior à naturalização ou tráfico). No campo processual, o <b>LIV</b> exige o <b>devido processo legal</b>; o <b>LV</b> assegura o <b>contraditório e a ampla defesa</b> no processo judicial <b>e</b> administrativo; o <b>LVI</b> torna <b>inadmissíveis as provas ilícitas</b>; e o <b>LVII</b> consagra a <b>presunção de inocência</b> até o trânsito em julgado.</p>

<h2 class="section-title">7. Os remédios constitucionais</h2>
<p>É quase certo cair uma questão pedindo “qual o instrumento cabível?”. O segredo é o <b>objeto</b> de cada remédio.</p>
<table>
  <thead><tr><th style="width:14%">Inciso</th><th style="width:26%">Remédio</th><th>Cabe quando…</th></tr></thead>
  <tbody>
    <tr><td><span class="rn">LXVIII</span></td><td>Habeas corpus</td><td>a liberdade de locomoção (ir e vir) é ameaçada ou violada. Gratuito.</td></tr>
    <tr><td><span class="rn">LXIX</span></td><td>Mandado de segurança</td><td>há direito líquido e certo (prova pronta) não amparado por HC ou HD.</td></tr>
    <tr><td><span class="rn">LXXI</span></td><td>Mandado de injunção</td><td>a falta de norma regulamentadora inviabiliza um direito.</td></tr>
    <tr><td><span class="rn">LXXII</span></td><td>Habeas data</td><td>se quer conhecer ou retificar dados pessoais em bancos públicos.</td></tr>
    <tr><td><span class="rn">LXXIII</span></td><td>Ação popular</td><td>o cidadão anula ato lesivo ao patrimônio público, à moralidade ou ao meio ambiente.</td></tr>
  </tbody>
</table>
<div class="callout c-banca"><h4>Como a Quadrix cobra os remédios</h4>Ela descreve a situação e troca o remédio: oferece “mandado de segurança” quando o caso é de <b>falta de norma</b> (mandado de injunção), ou “ação popular” como se fosse privativa do Ministério Público (é do <b>cidadão</b>; a do MP é a ação civil pública). Decore o objeto de cada um.</div>

<h2 class="section-title pagebreak">8. Leitura da lei seca comentada</h2>
<p>Como a Quadrix cobra a literalidade, ler o texto e saber onde ela costuma mexer vale mais do que qualquer resumo. À esquerda, o dispositivo; à direita, o significado e a <b>troca-armadilha</b> provável.</p>
<table class="ls">
  <thead><tr><th style="width:52%">Texto do art. 5º (lei seca)</th><th>O que significa / o que a banca troca</th></tr></thead>
  <tbody>{leiseca_rows}</tbody>
</table>

<h2 class="section-title pagebreak">9. 35 questões para fazer agora</h2>
<p class="lead">Resolva sem olhar o gabarito. <b>Itens 1 a 15:</b> julgue como CERTO ou ERRADO. <b>Itens 16 a 35:</b> múltipla escolha (A–E). O gabarito comentado está na seção 10.</p>
<p class="subhead">Parte I — Julgue os itens (Certo / Errado)</p>
{ce_html}
<p class="subhead">Parte II — Múltipla escolha (A–E)</p>
{me_html}

<h2 class="section-title pagebreak">10. Gabarito comentado</h2>
<p class="lead">Cada item traz a resposta e a explicação: por que a correta está certa e, nas de múltipla escolha, qual elemento torna cada alternativa errada.</p>
{gab_html}

</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("HTML gerado:", OUT, "| C/E:", len(QCE), "| A-E:", len(QME), "| total:", len(QCE)+len(QME))
