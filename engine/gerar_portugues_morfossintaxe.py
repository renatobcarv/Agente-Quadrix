# -*- coding: utf-8 -*-
"""Material DENSO (apostila) — Dia 2: Português: ortografia, classes de palavras,
morfossintaxe e coesão textual + 35 questões (15 Certo/Errado + 20 A-E) com
gabarito comentado completo. Segue docs/prompt-mestre.md. Render via Chrome.
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(_HERE)
OUTDIR = os.path.join(_REPO, "materiais", "dia02-portugues-morfossintaxe")
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "Dia2_Portugues_Completo.html")

# ============ QUESTÕES CERTO/ERRADO (15) ============
# (afirmacao, 'C'|'E', comentario)
QCE = [
    ("Na frase “Fazem dois anos que ele partiu”, o verbo “fazer” está corretamente flexionado.",
     "E", "O verbo “fazer” indicando tempo decorrido é IMPESSOAL e fica sempre no singular: “Faz dois anos”. A flexão no plural é justamente a armadilha mais cobrada pela banca."),
    ("Em “Houve muitos problemas na reunião”, o verbo “haver”, no sentido de existir, é impessoal e permanece no singular.",
     "C", "Correto. “Haver” = existir não tem sujeito (oração sem sujeito) e não vai ao plural; “muitos problemas” é objeto direto. Dizer “Houveram” seria o erro."),
    ("Conforme o Acordo Ortográfico vigente, as palavras “ideia”, “heroico” e “voo” são grafadas sem acento.",
     "C", "Correto. Paroxítonas com ditongos abertos “ei/oi” perderam o acento (ideia, heroico) e os hiatos “oo” também (voo). As grafias “idéia/heróico/vôo” estão erradas hoje."),
    ("Na frase “Ele se comportou mau na reunião”, a palavra “mau” está empregada corretamente.",
     "E", "Errado. Aqui se exige o ADVÉRBIO “mal” (oposto de “bem”): “comportou-se mal”. “Mau” é adjetivo (oposto de “bom”). Teste: cabe “bem” → usa-se “mal”."),
    ("Em “Aonde você nasceu?”, o emprego de “aonde” está de acordo com a norma culta.",
     "E", "Errado. “Nascer” não exprime movimento; o correto é “Onde você nasceu?”. “Aonde” (a + onde) só com verbos de movimento (ir, chegar): “Aonde você vai?”."),
    ("Em “Alugam-se salas comerciais”, o “se” é partícula apassivadora e “salas comerciais” funciona como sujeito.",
     "C", "Correto. Verbo transitivo direto (“alugar”) + “se” = voz passiva sintética; “salas” é sujeito paciente, por isso o verbo concorda no plural (“Alugam-se”)."),
    ("Em “Precisa-se de vendedores”, o verbo deve ir para o plural — “Precisam-se de vendedores”.",
     "E", "Errado. “Precisar de” é transitivo indireto; o “se” é índice de indeterminação do sujeito e o verbo fica no SINGULAR: “Precisa-se de vendedores”."),
    ("Em “Este é o relatório que assinei ontem”, a palavra “que” é conjunção integrante.",
     "E", "Errado. O “que” retoma “o relatório” e equivale a “o qual” → é PRONOME RELATIVO, que inicia oração subordinada adjetiva. Conjunção integrante completaria um verbo (“Disse que…”)."),
    ("Em “Não sei se ela virá à reunião”, a palavra “se” é conjunção integrante.",
     "C", "Correto. “Se” introduz oração que completa o verbo “saber” (objeto direto): “Não sei [isto]” → conjunção integrante (oração subordinada substantiva)."),
    ("Na frase “Assisti o jogo ontem à noite”, a regência do verbo “assistir” está de acordo com a norma culta.",
     "E", "Errado. “Assistir” no sentido de “ver/presenciar” é transitivo indireto e exige a preposição “a”: “Assisti AO jogo”. Sem a preposição, viola a norma culta."),
    ("Em “Faz cinco anos que moro nesta cidade”, o verbo “fazer” está corretamente empregado no singular.",
     "C", "Correto. “Fazer” indicando tempo decorrido é impessoal e fica no singular. “Fazem cinco anos” seria o erro."),
    ("O conectivo “portanto” estabelece, entre as orações, uma relação de causa.",
     "E", "Errado. “Portanto” exprime CONCLUSÃO (“Estudou; portanto, passou”). Causa seria “porque/pois (antes do verbo)”. Trocar conclusão por causa é pegadinha clássica de coesão."),
    ("Em “O candidato que se preparou foi aprovado”, a oração “que se preparou” é subordinada adjetiva restritiva.",
     "C", "Correto. Sem vírgulas, a oração restringe o sentido (só o candidato que se preparou) → adjetiva restritiva. Com vírgulas, seria explicativa."),
    ("Em “Meu irmão, que mora em Brasília, virá amanhã”, as vírgulas isolam uma oração subordinada adjetiva explicativa.",
     "C", "Correto. A informação entre vírgulas apenas acrescenta um dado (ele tem um irmão); por isso é explicativa. Retirá-la não muda o referente."),
    ("Em “Ninguém sabe o porquê da decisão”, a grafia “porquê” (junta e acentuada) está correta.",
     "C", "Correto. Precedido do artigo “o”, “porquê” é substantivo (= o motivo) e, por isso, vem junto e acentuado. O artigo é a pista que confirma a grafia."),
]

# ============ QUESTÕES MÚLTIPLA ESCOLHA A-E (20) ============
# (tema, enunciado, [A..E], idx_correto, comentario_completo)
QME = [
    ("Ortografia", "Assinale a opção em que o emprego de por que / porque / por quê / porquê está correto.",
     ["Não sei porque ele se atrasou para a reunião.", "Ela faltou por quê estava doente.", "Você ainda está aqui? Por quê?", "Ninguém explicou o por que da decisão.", "Estudo muito, porquê quero passar."],
     2, "Gabarito C: em fim de frase usa-se “por quê” (separado e acentuado). ✗A: pergunta indireta pede “por que” separado. ✗B: relação de causa pede “porque” junto. ✗D: com artigo “o” seria o substantivo “porquê”. ✗E: causa = “porque” junto, sem acento."),
    ("Ortografia", "Assinale a opção em que a palavra destacada (mau/mal) está empregada corretamente.",
     ["Ele se comportou mau na entrevista.", "O tempo está mau hoje; vai chover.", "Ela dormiu muito mau ontem.", "Tudo acabou mau para eles.", "Ele é um mal aluno."],
     1, "Gabarito B: “mau” é adjetivo (oposto de “bom”) e qualifica “tempo” → “tempo está mau (ruim)”. ✗A, ✗C, ✗D: exigem o advérbio “mal” (comportou-se mal, dormiu mal, acabou mal). ✗E: antes de substantivo é adjetivo → “mau aluno”."),
    ("Ortografia", "Assinale a opção em que o emprego de a / há (tempo) está correto.",
     ["Cheguei a dois dias na cidade.", "Daqui há uma semana viajarei.", "Estou aqui a três horas esperando.", "Não o vejo há muitos anos.", "Espero por ele a muito tempo."],
     3, "Gabarito D: tempo passado/decorrido pede “há” (verbo haver). ✗A e ✗C: passado também pediria “há” (há dois dias; há três horas). ✗B: tempo futuro pede “a” (daqui a uma semana). ✗E: passado → “há muito tempo”."),
    ("Ortografia", "Assinale a opção em que todas as palavras estão grafadas conforme o Acordo Ortográfico.",
     ["idéia, vôo, heróico", "ideia, vôo, heroico", "idéia, voo, heróico", "ideía, voo, heroíco", "ideia, voo, heroico"],
     4, "Gabarito E: paroxítonas com ditongo aberto (ideia, heroico) e hiato “oo” (voo) não levam acento. ✗A, ✗B, ✗C: mantêm acentos abolidos (idéia, vôo, heróico). ✗D: acentuação inexistente (ideía, heroíco)."),
    ("Ortografia/Crase", "Assinale a opção em que o emprego do acento grave (crase) está correto.",
     ["Refiro-me à essa questão.", "Cheguei à Brasília ontem.", "Entreguei o documento à diretora.", "Estou disposto à ajudar.", "Falei à respeito do caso."],
     2, "Gabarito C: “entregar a” + “a diretora” (feminino) = à. ✗A: pronome demonstrativo “essa” não admite crase. ✗B: “Brasília” não exige artigo (cidade sem artigo) → “a Brasília”. ✗D: antes de verbo não há crase. ✗E: “a respeito” (masculino) não tem crase."),
    ("Ortografia", "Assinale a opção em que o emprego de senão / se não está correto.",
     ["Estude, se não você será reprovado.", "Ele não quer outra coisa se não vencer.", "Apresse-se, se não chegará atrasado.", "Não havia ninguém, se não o porteiro.", "Se não chover, faremos o passeio."],
     4, "Gabarito E: “se não” (separado) = “caso não” (condição). ✗A e ✗C: equivalem a “caso contrário” → “senão” junto. ✗B e ✗D: equivalem a “a não ser” → “senão” junto."),
    ("Classes de palavras", "Em “Ele fala bem demais”, as palavras “bem” e “demais” classificam-se, respectivamente, como",
     ["adjetivo e substantivo.", "substantivo e advérbio.", "advérbio e advérbio.", "advérbio e adjetivo.", "preposição e advérbio."],
     2, "Gabarito C: “bem” modifica o verbo “fala” e “demais” intensifica “bem” → ambos advérbios (invariáveis). ✗ demais opções classificam errado: “bem”/“demais” aqui não são adjetivo, substantivo nem preposição."),
    ("Classes de palavras", "Em “O jantar foi servido às oito”, a palavra “jantar” classifica-se como",
     ["verbo.", "substantivo.", "adjetivo.", "advérbio.", "preposição."],
     1, "Gabarito B: precedida do artigo “O”, a palavra está substantivada → substantivo. ✗A: seria verbo em “Vamos jantar”. A classe depende do contexto, e o artigo é a pista decisiva."),
    ("Classes de palavras", "Em “Ela é a aluna que mais estuda”, a palavra “que” classifica-se como",
     ["pronome relativo.", "conjunção integrante.", "preposição.", "interjeição.", "advérbio."],
     0, "Gabarito A: “que” retoma “a aluna” (= a qual) → pronome relativo, iniciando oração adjetiva. ✗B: integrante completaria verbo (Disse que…). ✗C/D/E: não exerce esses papéis aqui."),
    ("Morfossintaxe", "Em “Faltaram três candidatos à prova”, o termo “três candidatos” exerce a função de",
     ["sujeito.", "objeto direto.", "adjunto adverbial.", "complemento nominal.", "predicativo do sujeito."],
     0, "Gabarito A: “faltar” é intransitivo; quem falta pratica a ação → sujeito (o verbo concorda: “Faltaram”). ✗B: não há objeto, pois o verbo não é transitivo. ✗C/D/E: não cabem à estrutura."),
    ("Morfossintaxe", "Em “Vendem-se imóveis usados”, a palavra “se” classifica-se como",
     ["índice de indeterminação do sujeito.", "conjunção integrante.", "pronome apassivador.", "pronome reflexivo.", "conjunção condicional."],
     2, "Gabarito C: VTD “vender” + “se” = voz passiva sintética; “imóveis” é sujeito paciente (verbo no plural). ✗A: o IIS ocorre com VTI/VI (verbo no singular). ✗B/D/E: funções diversas, não cabíveis."),
    ("Morfossintaxe", "Em “Os alunos assistiram ao documentário”, o verbo “assistir” classifica-se como",
     ["transitivo indireto.", "transitivo direto.", "intransitivo.", "de ligação.", "transitivo direto e indireto."],
     0, "Gabarito A: “assistir” = ver exige preposição “a” → transitivo indireto (“ao documentário” = objeto indireto). ✗B: seria VTD se não exigisse preposição. ✗C/D/E: não correspondem à regência."),
    ("Morfossintaxe", "Em “A construção da ponte durou meses”, o termo “da ponte” exerce a função de",
     ["adjunto adverbial.", "objeto indireto.", "complemento nominal.", "adjunto adnominal.", "agente da passiva."],
     2, "Gabarito C: a ponte SOFRE a ação (foi construída) e “construção” é nome abstrato → complemento nominal. ✗D: seria adjunto adnominal se a ponte praticasse/possuísse (ex.: “a torre da igreja”). ✗A/B/E: não cabem."),
    ("Morfossintaxe", "Em “Embora estivesse cansado, terminou o serviço”, a oração destacada é subordinada adverbial",
     ["causal.", "condicional.", "temporal.", "concessiva.", "consecutiva."],
     3, "Gabarito D: “embora” introduz concessão (um obstáculo que não impede o fato). ✗A: causa seria “porque”. ✗B: condição seria “se”. ✗C: tempo seria “quando”. ✗E: consequência seria “tão… que”."),
    ("Morfossintaxe", "A frase “O projeto foi aprovado pela comissão” está na voz",
     ["passiva analítica.", "ativa.", "passiva sintética.", "reflexiva.", "reflexiva recíproca."],
     0, "Gabarito A: “ser + particípio” = voz passiva analítica; “pela comissão” é agente da passiva. ✗C: a sintética usa “se” (Aprovou-se o projeto). ✗B/D/E: não correspondem à estrutura."),
    ("Morfossintaxe", "Assinale a opção em que a colocação pronominal está correta.",
     ["Me empreste o seu livro.", "Não diga-me isso.", "Quem contou-te a verdade?", "Nunca se deve mentir.", "Tudo resolveu-se rápido."],
     3, "Gabarito D: “Nunca” é palavra atrativa → próclise obrigatória (“se deve”). ✗A: não se inicia frase com pronome átono. ✗B: a negação atrai (“Não me diga”). ✗C: “Quem” atrai (“Quem te contou”). ✗E: “Tudo” atrai (“Tudo se resolveu”)."),
    ("Morfossintaxe", "Quantas orações há no período “Quando cheguei, todos já tinham saído”?",
     ["uma.", "duas.", "três.", "quatro.", "nenhuma."],
     1, "Gabarito B: conta-se uma oração por verbo ou locução verbal — “cheguei” (1) e “tinham saído” (locução = 1) → duas. ✗ As demais erram a contagem; a pegadinha é contar a locução como dois verbos."),
    ("Coesão", "No período “Esforçou-se muito; ____, não obteve o resultado esperado”, a lacuna, para exprimir oposição, deve ser preenchida com",
     ["contudo", "portanto", "porque", "assim que", "à medida que"],
     0, "Gabarito A: há contraste → conectivo adversativo “contudo”. ✗B: “portanto” daria conclusão. ✗C: “porque” daria causa. ✗D: “assim que” é tempo. ✗E: “à medida que” é proporção."),
    ("Coesão", "Assinale a opção em que o conectivo destacado exprime CONCLUSÃO.",
     ["Faltou ao trabalho PORQUE adoeceu.", "Estudou muito; PORTANTO, foi aprovado.", "EMBORA chovesse, ele saiu.", "Tudo correu CONFORME o combinado.", "Saiu LOGO QUE o sinal tocou."],
     1, "Gabarito B: “portanto” = conclusão. ✗A: “porque” = causa. ✗C: “embora” = concessão. ✗D: “conforme” = conformidade. ✗E: “logo que” = tempo."),
    ("Coesão", "Em “O cão latia sem parar; o animal parecia assustado”, o termo “o animal” retoma “o cão” por meio de",
     ["elipse do sujeito.", "catáfora.", "repetição do mesmo termo.", "emprego de pronome relativo.", "substituição por hiperônimo."],
     4, "Gabarito E: “animal” é palavra de sentido mais amplo que “cão” → substituição por hiperônimo (coesão referencial). ✗A: não há omissão. ✗B: catáfora antecipa, não retoma. ✗C: não houve repetição. ✗D: não há pronome relativo."),
]

# ---------- CSS ----------
CSS = """
@page { size:A4; margin:13mm 13mm 15mm 13mm; }
* { box-sizing:border-box; }
body { font-family:'Segoe UI','Helvetica Neue',Arial,sans-serif; color:#1d2733; font-size:11px; line-height:1.6; margin:0; orphans:3; widows:3; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
h1,h2,h3,h4 { margin:0; font-weight:700; }
p { margin:0 0 7px; text-align:justify; orphans:3; widows:3; }
.cover { height:250mm; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; background:linear-gradient(135deg,#13235e 0%,#1d4ed8 55%,#16307a 100%); color:#fff; border-radius:6px; page-break-after:always; padding:0 24mm; }
.cover .kicker { letter-spacing:4px; font-size:12px; opacity:.85; font-weight:600; }
.cover h1 { font-size:42px; line-height:1.06; margin:10px 0 6px; }
.cover .sub { font-size:15px; font-weight:400; opacity:.95; max-width:140mm; }
.cover .rule { width:70px; height:4px; background:#ffd27a; margin:22px 0; border-radius:2px; }
.cover .meta { font-size:12.5px; opacity:.9; line-height:1.7; }
.cover .badge { margin-top:26px; background:rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.4); padding:9px 18px; border-radius:40px; font-size:13px; font-weight:600; }
.section-title { font-size:17px; color:#1d4ed8; border-bottom:3px solid #1d4ed8; padding-bottom:4px; margin:16px 0 9px; page-break-after:avoid; }
.section-title:first-of-type { margin-top:4px; }
.subhead { font-size:12.5px; color:#13235e; font-weight:700; margin:11px 0 4px; border-left:4px solid #1d4ed8; padding-left:8px; page-break-after:avoid; }
.box2 { display:grid; grid-template-columns:1fr 1fr; gap:9px; margin:7px 0; }
.callout { border-radius:7px; padding:9px 12px; page-break-inside:avoid; margin:6px 0; }
.c-banca { background:#eef4ff; border-left:4px solid #1d4ed8; }
.c-peg { background:#fff5f5; border-left:4px solid #c0392b; }
.c-mnem { background:#fff8e6; border-left:4px solid #d4a017; }
.c-key { background:#eefaf1; border-left:4px solid #1f9d57; }
.callout h4 { font-size:10.5px; margin-bottom:4px; text-transform:uppercase; letter-spacing:.4px; }
.c-banca h4 { color:#1d4ed8; } .c-peg h4 { color:#c0392b; } .c-mnem h4 { color:#a07400; } .c-key h4 { color:#1f9d57; }
.callout ul { margin:3px 0 0; padding-left:15px; } .callout li { margin:2.5px 0; }
table { width:100%; border-collapse:collapse; margin:7px 0; font-size:9.9px; page-break-inside:avoid; }
th { background:#13235e; color:#fff; text-align:left; padding:6px 8px; }
td { border:1px solid #e2e6ee; padding:6px 8px; vertical-align:top; }
tr:nth-child(even) td { background:#f6f8fc; }
td .rn { font-weight:700; color:#1d4ed8; }
.qbox { border:1px solid #e2e6ee; border-radius:8px; padding:9px 12px; margin:0 0 8px; page-break-inside:avoid; }
.qbox .qn { color:#1d4ed8; font-weight:700; }
.qbox .tema { display:inline-block; background:#eef0f5; color:#56627a; font-size:8.2px; font-weight:700; text-transform:uppercase; letter-spacing:.4px; padding:2px 7px; border-radius:20px; margin-left:6px; }
.qbox ol { margin:5px 0 0; padding-left:0; list-style:none; counter-reset:opt; }
.qbox ol li { counter-increment:opt; margin:2.5px 0; padding-left:20px; position:relative; }
.qbox ol li::before { content:counter(opt,upper-alpha)")"; position:absolute; left:0; top:0; font-weight:700; color:#56627a; }
.ce { margin-top:5px; font-size:10px; color:#56627a; font-weight:700; }
.gab-item { border-bottom:1px solid #eef0f4; padding:6px 0; page-break-inside:avoid; }
.gab-item .n { font-weight:700; color:#13235e; }
.gab-item .resp { font-weight:700; }
.gab-c { color:#1f9d57; } .gab-e { color:#c0392b; }
.pagebreak { page-break-before:always; }
.lead { font-size:11px; color:#33414f; }
"""

# ---------- montagem das questões ----------
ce_html = ""
for i, (af, _g, _c) in enumerate(QCE, 1):
    ce_html += (f'<div class="qbox"><span class="qn">{i}.</span> {af}'
                f'<div class="ce">(&nbsp;&nbsp;) Certo&nbsp;&nbsp;&nbsp;(&nbsp;&nbsp;) Errado</div></div>')

me_html = ""
for k, (tema, enun, opts, ok, com) in enumerate(QME, 16):
    lis = "".join(f"<li>{o}</li>" for o in opts)
    me_html += (f'<div class="qbox"><span class="qn">{k}.</span> {enun}'
                f'<span class="tema">{tema}</span><ol>{lis}</ol></div>')

# gabarito comentado
gab_html = ""
for i, (af, g, c) in enumerate(QCE, 1):
    cls = "gab-c" if g == "C" else "gab-e"
    rotulo = "CERTO" if g == "C" else "ERRADO"
    gab_html += f'<div class="gab-item"><span class="n">{i}.</span> <span class="resp {cls}">{rotulo}</span> — {c}</div>'
for k, (tema, enun, opts, ok, com) in enumerate(QME, 16):
    gab_html += f'<div class="gab-item"><span class="n">{k}.</span> {com}</div>'

HTML = f"""<!DOCTYPE html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body>

<div class="cover">
  <div class="kicker">LÍNGUA PORTUGUESA</div>
  <h1>Ortografia,<br>Morfossintaxe<br>&amp; Coesão</h1>
  <div class="rule"></div>
  <div class="sub">Apostila completa: ortografia, classes de palavras, análise sintática e coesão textual — com 35 questões e gabarito comentado</div>
  <div class="meta" style="margin-top:26px;">Concurso <b>Sedes/DF</b> · Banca <b>Quadrix</b> · 2026<br>Técnico Administrativo (Cargo 202)</div>
  <div class="badge">Dia 2 · 35 questões para fazer agora</div>
</div>

<h2 class="section-title">1. Por que Português decide a prova</h2>
<p>Português é a matéria com o maior número de questões na maioria dos concursos e, não por acaso, a que mais elimina candidatos por descuido. A Quadrix é uma banca de <b>literalidade</b>: ela cobra a regra de forma fria e, para criar o erro, troca <b>um único elemento</b> — uma palavra, um acento, uma preposição, um conectivo. Quem entende a lógica por trás da regra reconhece essa troca; quem apenas decorou nomenclatura cai na armadilha. Por isso, este material não lista regras soltas: explica o porquê de cada uma e aponta exatamente onde a banca costuma mexer.</p>
<p>O dia de hoje cobre quatro frentes que se sustentam mutuamente. A <b>ortografia</b> trata da grafia correta das palavras e dos pares que confundem (mau/mal, por que/porque, a/há). As <b>classes de palavras</b> identificam a que categoria gramatical cada vocábulo pertence — e mostram que a mesma palavra muda de classe conforme o contexto. A <b>morfossintaxe</b> une morfologia (classe) e sintaxe (função): é o coração da prova, porque dela dependem concordância, regência, crase e pontuação. Por fim, a <b>coesão textual</b> cuida da amarração entre as partes do texto. Domine essas quatro frentes e você terá a base de quase todas as questões de língua.</p>

<h2 class="section-title">2. Ortografia: os pares que mais confundem</h2>
<p>A ortografia de concurso quase nunca cobra palavras difíceis isoladas; cobra <b>parônimos</b> — palavras parecidas com sentidos diferentes — e o emprego correto de pequenas expressões. O segredo não é decorar, e sim ter um <b>teste rápido</b> para cada par. A tabela a seguir reúne os casos mais cobrados, com o critério de decisão de cada um.</p>
<table>
  <thead><tr><th style="width:22%">Par / expressão</th><th style="width:40%">Regra (o teste)</th><th>Exemplo correto</th></tr></thead>
  <tbody>
    <tr><td><span class="rn">por que / porque</span></td><td>Separado em perguntas (cabe “por qual motivo”); junto nas respostas (causa). Acento no fim de frase (por quê) e no substantivo (o porquê).</td><td>“Por que faltou? Porque adoeceu. Não sei por quê. Eis o porquê.”</td></tr>
    <tr><td><span class="rn">mau / mal</span></td><td>“Mau” = adjetivo (oposto de bom); “mal” = advérbio (oposto de bem) ou substantivo.</td><td>“Um mau exemplo.” / “Agiu mal.”</td></tr>
    <tr><td><span class="rn">mas / mais</span></td><td>“Mas” = porém (oposição); “mais” = quantidade/intensidade (oposto de menos).</td><td>“Tentou, mas falhou.” / “Quero mais tempo.”</td></tr>
    <tr><td><span class="rn">a / há (tempo)</span></td><td>“Há” = tempo passado (= faz); “a” = tempo futuro ou distância. Nunca “há… atrás”.</td><td>“Saiu há uma hora.” / “Volto daqui a uma hora.”</td></tr>
    <tr><td><span class="rn">senão / se não</span></td><td>“Senão” = caso contrário / a não ser; “se não” = caso não (condição + verbo).</td><td>“Corra, senão cairá.” / “Se não chover, sairemos.”</td></tr>
    <tr><td><span class="rn">onde / aonde</span></td><td>“Onde” = lugar fixo (estar); “aonde” = movimento (ir, chegar).</td><td>“Onde mora?” / “Aonde vai?”</td></tr>
    <tr><td><span class="rn">afim / a fim de</span></td><td>“Afim” = semelhante; “a fim de” = com a finalidade de.</td><td>“Áreas afins.” / “Estudo a fim de passar.”</td></tr>
    <tr><td><span class="rn">sessão / seção / cessão</span></td><td>Sessão = tempo/reunião; seção = divisão; cessão = ato de ceder.</td><td>“Sessão de cinema.” / “Seção de esportes.” / “Cessão de direitos.”</td></tr>
  </tbody>
</table>
<p class="subhead">Acentuação pelo Acordo Ortográfico</p>
<p>O Acordo Ortográfico mudou alguns acentos que a banca adora cobrar na grafia antiga. As <b>paroxítonas</b> com os ditongos abertos “ei” e “oi” <b>perderam o acento</b>: escreve-se <i>ideia, heroico, jiboia, assembleia</i>. Os <b>hiatos</b> “oo” e “ee” também ficaram sem acento: <i>voo, enjoo, creem, leem</i>. O <b>trema</b> foi abolido (<i>linguiça, sequência</i>). Permaneceram, porém, os <b>acentos diferenciais</b> que evitam ambiguidade: <i>pôde</i> (pretérito) × <i>pode</i> (presente) e <i>pôr</i> (verbo) × <i>por</i> (preposição). Já <i>pára</i> (do verbo parar) perdeu o acento e virou <i>para</i>, igual à preposição.</p>
<div class="callout c-banca"><h4>Como a Quadrix cobra ortografia</h4>A banca apresenta uma frase com a grafia antiga (“idéia”, “vôo”, “heróico”) e pede que você a julgue como correta — é a troca de um único elemento. Também explora o par certo no contexto errado (“assisti o filme”, “aonde você está”). Leia cada palavra destacada e aplique o teste rápido.</div>

<h2 class="section-title">3. As dez classes de palavras</h2>
<p>Classe de palavra (ou classe gramatical) é a categoria a que um vocábulo pertence. São <b>dez</b>, divididas em <b>variáveis</b> — que flexionam em gênero, número ou grau — e <b>invariáveis</b>. As variáveis são <b>substantivo</b> (nomeia seres e conceitos), <b>artigo</b> (define ou indetermina o substantivo), <b>adjetivo</b> (qualifica o substantivo), <b>numeral</b> (indica quantidade ou ordem), <b>pronome</b> (substitui ou acompanha o substantivo) e <b>verbo</b> (exprime ação, estado ou fenômeno). As invariáveis são <b>advérbio</b> (modifica verbo, adjetivo ou outro advérbio), <b>preposição</b> (liga termos), <b>conjunção</b> (liga orações) e <b>interjeição</b> (exprime emoção).</p>
<p>O ponto que a banca explora é simples e poderoso: <b>a classe de uma palavra depende do contexto</b>, não da palavra isolada. A mesma forma pode pertencer a classes diferentes conforme a função que exerce na frase. Por isso, ao classificar, observe o <b>papel</b> da palavra naquela oração específica.</p>
<div class="box2">
  <div class="callout c-key"><h4>A mesma palavra, classes diferentes</h4>
    <ul>
      <li>“O <b>jantar</b> está pronto” (substantivo) × “Vou <b>jantar</b> cedo” (verbo).</li>
      <li>“Ele fala <b>bem</b>” (advérbio) × “Quero o seu <b>bem</b>” (substantivo).</li>
      <li>“<b>A</b> aluna chegou” (artigo) × “Dei o livro <b>a</b> ela” (preposição).</li>
    </ul></div>
  <div class="callout c-peg"><h4>Pegadinha: palavras camaleão</h4>
    <ul>
      <li><b>que</b>: pronome relativo, conjunção integrante, advérbio, substantivo…</li>
      <li><b>se</b>: conjunção (integrante/condicional), pronome (apassivador/reflexivo), IIS.</li>
      <li><b>como</b>: advérbio, conjunção, preposição. Sempre veja o contexto.</li>
    </ul></div>
</div>

<h2 class="section-title">4. Morfossintaxe: a estrutura da oração</h2>
<p>Morfossintaxe é o estudo conjunto da <b>classe</b> (morfologia) e da <b>função</b> (sintaxe) das palavras. O caminho seguro para analisar qualquer frase é sempre o mesmo: localize o <b>verbo</b>, descubra sua <b>transitividade</b>, identifique o <b>sujeito</b> e, então, classifique os demais termos. Dominar esse roteiro resolve não só as questões de análise sintática, mas também as de concordância, regência e crase.</p>
<p class="subhead">Termos da oração</p>
<p>Os termos dividem-se em três grupos. Os <b>essenciais</b> são o <b>sujeito</b> (de quem se fala) e o <b>predicado</b> (o que se diz). Os <b>integrantes</b> completam o sentido: <b>objeto direto</b> (sem preposição), <b>objeto indireto</b> (com preposição), <b>complemento nominal</b> (completa um nome) e <b>agente da passiva</b>. Os <b>acessórios</b> acrescentam informação: <b>adjunto adnominal</b> (liga-se a um nome, indicando posse ou qualidade), <b>adjunto adverbial</b> (circunstância: tempo, lugar, modo) e <b>aposto</b> (explica um termo). À parte fica o <b>vocativo</b>, que é um chamamento e não pertence à estrutura da oração.</p>
<p class="subhead">Transitividade verbal</p>
<p>É a relação do verbo com seus complementos. O <b>intransitivo</b> (VI) tem sentido completo (“Ele chegou”). O <b>transitivo direto</b> (VTD) pede objeto sem preposição (“Comprei o livro”). O <b>transitivo indireto</b> (VTI) pede objeto com preposição (“Gosto de música”). O <b>transitivo direto e indireto</b> (VTDI) pede os dois (“Dei um presente a ela”). O <b>verbo de ligação</b> (VL) liga o sujeito a um predicativo (“Ela está cansada”). A transitividade é decisiva: dela depende a regência — e é nela que mora a pegadinha de verbos como “assistir”, “obedecer”, “aspirar” e “visar”, que exigem preposição.</p>
<p class="subhead">Sujeito e predicado</p>
<p>O sujeito pode ser <b>simples</b> (um núcleo), <b>composto</b> (dois ou mais), <b>oculto</b> (identificável pela desinência), <b>indeterminado</b> (verbo na 3ª pessoa do plural sem referente, ou VTI + “se”) ou inexistente — caso das <b>orações sem sujeito</b>, com verbos como “haver” (= existir), “fazer”/“ser” indicando tempo e os que exprimem fenômenos da natureza. O predicado é <b>verbal</b> (núcleo de ação), <b>nominal</b> (verbo de ligação + predicativo) ou <b>verbo-nominal</b> (ação + predicativo).</p>
<div class="callout c-peg"><h4>Pegadinha: adjunto adnominal × complemento nominal</h4>Ambos vêm com preposição depois de um nome. O <b>complemento nominal</b> é PACIENTE (sofre a ação): “a construção <b>da casa</b>” (a casa é construída). O <b>adjunto adnominal</b> é AGENTE ou posse: “a chegada <b>do trem</b>” (o trem chega) / “o carro <b>do João</b>” (posse). Teste: o termo sofre a ação (complemento nominal) ou pratica/possui (adjunto adnominal)?</div>
<p class="subhead">Os valores do “que” e do “se”</p>
<p>Duas palavras concentram boa parte das questões. O <b>“que”</b> é mais comumente <b>pronome relativo</b> (retoma um nome e equivale a “o qual”: “o livro <b>que</b> li”) ou <b>conjunção integrante</b> (introduz oração que completa um verbo: “Disse <b>que</b> viria”). O teste decisivo: se couber “o qual”, é pronome relativo. O <b>“se”</b>, por sua vez, pode ser <b>conjunção integrante</b> (“Não sei <b>se</b> virá”), <b>conjunção condicional</b> (“<b>Se</b> chover, fico”), <b>pronome apassivador</b> (com VTD, havendo sujeito: “Vendem-<b>se</b> casas”) ou <b>índice de indeterminação do sujeito</b> (com VTI/VI, verbo no singular: “Precisa-<b>se</b> de pedreiros”).</p>
<table>
  <thead><tr><th style="width:20%">Palavra/uso</th><th style="width:40%">Como identificar</th><th>Exemplo</th></tr></thead>
  <tbody>
    <tr><td><span class="rn">que (relativo)</span></td><td>Retoma um nome; cabe “o qual”. Inicia oração adjetiva.</td><td>“A prova que fiz foi difícil.”</td></tr>
    <tr><td><span class="rn">que (integrante)</span></td><td>Completa um verbo; inicia oração substantiva.</td><td>“Espero que você venha.”</td></tr>
    <tr><td><span class="rn">se (apassivador)</span></td><td>VTD + se; há sujeito paciente; verbo concorda (plural).</td><td>“Alugam-se salas.”</td></tr>
    <tr><td><span class="rn">se (indet. do sujeito)</span></td><td>VTI/VI + se; verbo no singular; sujeito indeterminado.</td><td>“Precisa-se de ajudantes.”</td></tr>
  </tbody>
</table>
<p class="subhead">Período composto: coordenação × subordinação</p>
<p>Quando o período tem mais de uma oração, elas se relacionam por <b>coordenação</b> (orações independentes) ou <b>subordinação</b> (uma depende da outra). As <b>coordenadas sindéticas</b> classificam-se pelo conectivo: aditiva (e), adversativa (mas), alternativa (ou), conclusiva (logo, portanto) e explicativa (pois). As <b>subordinadas</b> exercem função de termo da oração principal: <b>substantivas</b> (valor de nome, iniciadas por conjunção integrante), <b>adjetivas</b> (valor de adjetivo, iniciadas por pronome relativo) e <b>adverbiais</b> (valor de advérbio, exprimindo circunstância: causal, condicional, concessiva, temporal etc.).</p>

<h2 class="section-title">5. Coesão textual</h2>
<p><b>Coesão</b> é a amarração gramatical entre as partes de um texto — a “costura” que liga frases e parágrafos. Não se confunde com <b>coerência</b>, que é a lógica de sentido: um texto pode estar coeso (bem ligado) e, ainda assim, incoerente (sem lógica). A coesão se realiza de dois modos principais: a <b>coesão referencial</b>, que retoma termos já ditos, e a <b>coesão sequencial</b>, que conecta ideias por meio de conectivos.</p>
<p>A <b>coesão referencial</b> evita a repetição e mantém o texto amarrado. Faz-se por <b>anáfora</b> (retomada de um termo anterior: “Comprei um livro e <b>o</b> li”), <b>catáfora</b> (antecipação do que virá: “Só quero <b>isto</b>: justiça”), <b>elipse</b> (omissão de termo recuperável: “João entrou e [ele] sentou-se”) e <b>substituição lexical</b> por sinônimos ou hiperônimos (“o cão… o <b>animal</b>”). A <b>coesão sequencial</b>, por sua vez, depende dos conectivos, que estabelecem a relação de sentido entre as orações — e trocá-los muda o texto.</p>
<table>
  <thead><tr><th style="width:26%">Relação de sentido</th><th>Principais conectivos</th></tr></thead>
  <tbody>
    <tr><td><span class="rn">Adição</span></td><td>e; também; além disso; não só… mas também</td></tr>
    <tr><td><span class="rn">Oposição</span></td><td>mas; porém; contudo; todavia; no entanto; entretanto</td></tr>
    <tr><td><span class="rn">Conclusão</span></td><td>portanto; logo; por isso; assim; pois (após o verbo)</td></tr>
    <tr><td><span class="rn">Causa</span></td><td>porque; pois (antes do verbo); já que; visto que; uma vez que</td></tr>
    <tr><td><span class="rn">Condição</span></td><td>se; caso; contanto que; desde que; a menos que</td></tr>
    <tr><td><span class="rn">Concessão</span></td><td>embora; ainda que; mesmo que; conquanto; apesar de</td></tr>
  </tbody>
</table>
<div class="callout c-peg"><h4>Pegadinhas de coesão preferidas da banca</h4>
  <ul>
    <li><b>“pois”</b> antes do verbo = causa; depois do verbo = conclusão. (“Faltou, pois adoeceu” × “Adoeceu; faltou, pois, à aula.”)</li>
    <li><b>“portanto”</b> (conclusão) ≠ <b>“porque”</b> (causa). A banca inverte os dois.</li>
    <li>Pronome retomando o <b>referente errado</b>: confira sempre a quem o “ele/o/que” se refere.</li>
  </ul></div>

<h2 class="section-title pagebreak">6. 35 questões para fazer agora</h2>
<p class="lead">Resolva sem olhar o gabarito. <b>Itens 1 a 15:</b> julgue como CERTO ou ERRADO (estilo Quadrix). <b>Itens 16 a 35:</b> múltipla escolha (A–E). O gabarito comentado, com a justificativa da correta e o motivo de cada alternativa errada, está na seção 7.</p>
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
