# -*- coding: utf-8 -*-
"""Treino de Português — 75 questões: 15 sobre os PORQUÊS (julgue C/E),
30 de classe gramatical (morfossintaxe) e 30 de ortografia. Gabarito comentado.
Render via Chrome. Segue docs/prompt-mestre.md (gabarito comentado completo).
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(_HERE)
OUTDIR = os.path.join(_REPO, "materiais", "dia02-portugues-morfossintaxe")
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "Treino_Portugues_Porques_Morfo_Ortografia.html")

# ===== BLOCO 1 — PORQUÊS (julgue Certo/Errado) =====
PORQUE = [
    ("Não sei por que ele faltou à reunião.", "C", "Pergunta indireta → “por que” (separado, sem acento). Cabe “por qual motivo”."),
    ("Ela saiu porque estava cansada.", "C", "Relação de causa/resposta → “porque” (junto, sem acento)."),
    ("Você está triste por quê?", "C", "Fim de frase → “por quê” (separado e acentuado)."),
    ("Ninguém entende o porque da briga.", "E", "Com artigo “o”, é substantivo → “o porquê” (junto e acentuado)."),
    ("Por quê você não veio ontem?", "E", "Pergunta no início da frase → “Por que” (separado, sem acento)."),
    ("Estudo muito, por que quero passar.", "E", "Relação de causa → “porque” (junto)."),
    ("Eis o porquê de toda a confusão.", "C", "Substantivo (= o motivo), precedido de artigo → “porquê”."),
    ("Por que motivo você mentiu para mim?", "C", "“Por que” separado e sem acento (cabe “por qual motivo”)."),
    ("Ele não explicou porquê sumiu da festa.", "E", "Pergunta indireta → “por que” (separado, sem acento)."),
    ("Afinal, lutamos por quê?", "C", "Fim de frase → “por quê” (acentuado)."),
    ("A razão por que luto é justa.", "C", "Equivale a “pela qual” → “por que” (separado, sem acento)."),
    ("Não irei à festa, porque não fui convidado.", "C", "Causa → “porque” (junto)."),
    ("Você sabe o por quê disso tudo?", "E", "Com artigo “o”, é substantivo → “o porquê” (junto e acentuado)."),
    ("Por que você está rindo tanto?", "C", "Pergunta direta no início → “Por que” (separado, sem acento)."),
    ("Cheguei atrasado porquê o ônibus quebrou.", "E", "Causa → “porque” (junto, sem acento)."),
]

# ===== BLOCO 2 — CLASSE GRAMATICAL (frase + pedido) =====
# (frase com a palavra-alvo em MAIÚSCULAS, resposta)
MORFO = [
    ("O ALUNO entregou a prova.", "Substantivo (núcleo do sujeito)."),
    ("Ela é MUITO esforçada.", "Advérbio (de intensidade — modifica o adjetivo)."),
    ("Comprei TRÊS cadernos.", "Numeral (cardinal)."),
    ("ELE chegou cedo à reunião.", "Pronome pessoal (do caso reto)."),
    ("O céu ESTÁ limpo.", "Verbo (de ligação)."),
    ("Que dia BONITO!", "Adjetivo."),
    ("Viajei COM meus colegas.", "Preposição."),
    ("Tentei, MAS não consegui.", "Conjunção coordenativa adversativa."),
    ("NOSSA, que susto!", "Interjeição."),
    ("A casa é espaçosa.", "Artigo definido (“A”)."),
    ("Ele dirige RAPIDAMENTE.", "Advérbio (de modo)."),
    ("Cheguei em PRIMEIRO lugar.", "Numeral (ordinal)."),
    ("ALGUÉM deixou a porta aberta.", "Pronome indefinido."),
    ("O JANTAR está servido.", "Substantivo."),
    ("Vamos JANTAR mais tarde.", "Verbo (infinitivo)."),
    ("Ele se expressa BEM.", "Advérbio (de modo)."),
    ("Desejo o seu BEM.", "Substantivo."),
    ("Entreguei o relatório A ela.", "Preposição."),
    ("Este é o livro QUE comprei.", "Pronome relativo."),
    ("Espero QUE você compareça.", "Conjunção integrante."),
    ("MUITOS candidatos desistiram.", "Pronome indefinido (adjetivo)."),
    ("Ai! Cortei o dedo.", "Interjeição."),
    ("SE estudar, você passará.", "Conjunção subordinativa condicional."),
    ("Não sei SE ele virá.", "Conjunção integrante."),
    ("Ele FERIU-SE no acidente.", "Pronome reflexivo (“se”)."),
    ("Trabalhamos DURANTE a madrugada.", "Preposição."),
    ("Ela canta MARAVILHOSAMENTE.", "Advérbio (de modo)."),
    ("O Brasil é um país TROPICAL.", "Adjetivo."),
    ("Vendem-SE apartamentos.", "Pronome apassivador (partícula apassivadora)."),
    ("Comprei DOIS quilos de arroz.", "Numeral (cardinal)."),
]

# ===== BLOCO 3 — ORTOGRAFIA (escolha a forma correta) =====
# (frase com (opcao1/opcao2), forma_correta, regra)
ORTO = [
    ("Ele se comportou (mau / mal) na entrevista.", "mal", "Advérbio (oposto de “bem”)."),
    ("O tempo está (mau / mal) hoje; vai chover.", "mau", "Adjetivo (oposto de “bom”), qualifica “tempo”."),
    ("Estudei muito, (mas / mais) não passei.", "mas", "Conjunção adversativa (= porém)."),
    ("Preciso de (mas / mais) tempo.", "mais", "Advérbio de intensidade/quantidade."),
    ("Cheguei (a / há) dois dias na cidade.", "há", "Tempo decorrido (= faz)."),
    ("Daqui (a / há) uma semana viajarei.", "a", "Tempo futuro/distância."),
    ("(Onde / Aonde) você vai com tanta pressa?", "Aonde", "Verbo de movimento (ir)."),
    ("(Onde / Aonde) você mora atualmente?", "Onde", "Lugar fixo (sem movimento)."),
    ("Corra, (senão / se não) você cairá.", "senão", "Equivale a “caso contrário”."),
    ("(Senão / Se não) chover, faremos o passeio.", "Se não", "Equivale a “caso não” (condição)."),
    ("Conversamos (acerca de / há cerca de) política.", "acerca de", "Significa “a respeito de”."),
    ("Ele saiu (acerca de / há cerca de) uma hora.", "há cerca de", "Tempo decorrido aproximado (verbo haver)."),
    ("Estudo (afim / a fim) de passar no concurso.", "a fim", "“A fim de” = com a finalidade de."),
    ("São duas áreas (afins / a fins).", "afins", "“Afins” = semelhantes (adjetivo)."),
    ("Comprei o aparelho na (sessão / seção) de eletrônicos.", "seção", "“Seção” = divisão/parte."),
    ("A (sessão / seção) de cinema começou atrasada.", "sessão", "“Sessão” = período de tempo/reunião."),
    ("Houve a (sessão / cessão) dos direitos ao autor.", "cessão", "“Cessão” = ato de ceder."),
    ("A forma correta é (idéia / ideia).", "ideia", "Paroxítona com ditongo aberto perdeu o acento."),
    ("Escreve-se (vôo / voo).", "voo", "Hiato “oo” não é mais acentuado."),
    ("A grafia correta é (heróico / heroico).", "heroico", "Paroxítona com ditongo aberto sem acento."),
    ("Ontem ele (pôde / pode) comparecer.", "pôde", "Pretérito leva acento diferencial."),
    ("Hoje ele não (pôde / pode) sair, pois está doente.", "pode", "Presente, sem acento."),
    ("Levei o carro para (consertar / concertar).", "consertar", "“Consertar” = reparar."),
    ("Assistimos a um lindo (conserto / concerto).", "concerto", "“Concerto” = espetáculo musical."),
    ("Ele tem (mau / mal) hálito.", "mau", "Adjetivo (qualifica “hálito”)."),
    ("Tudo correu (mau / mal) na viagem.", "mal", "Advérbio (oposto de “bem”)."),
    ("Vim (a fim / afim) de resolver o problema.", "a fim", "“A fim de” = finalidade."),
    ("Não sei (porque / por que) ele faltou.", "por que", "Pergunta indireta (separado, sem acento)."),
    ("Faltei ao trabalho (porque / por que) adoeci.", "porque", "Causa/resposta (junto)."),
    ("A palavra é grafada com (x / ch) em “enxergar”.", "x", "“Enxergar” escreve-se com x."),
]

CSS = """
@page { size:A4; margin:13mm 13mm 15mm 13mm; }
* { box-sizing:border-box; }
body { font-family:'Segoe UI','Helvetica Neue',Arial,sans-serif; color:#1d2733; font-size:10.6px; line-height:1.5; margin:0; orphans:3; widows:3; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
h1,h2,h3,h4 { margin:0; font-weight:700; }
p { margin:0 0 6px; }
.cover { height:250mm; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; background:linear-gradient(135deg,#13235e 0%,#1d4ed8 55%,#16307a 100%); color:#fff; border-radius:6px; page-break-after:always; padding:0 24mm; }
.cover .kicker { letter-spacing:4px; font-size:12px; opacity:.85; font-weight:600; }
.cover h1 { font-size:40px; line-height:1.07; margin:10px 0 6px; }
.cover .sub { font-size:15px; font-weight:400; opacity:.95; max-width:140mm; }
.cover .rule { width:70px; height:4px; background:#ffd27a; margin:22px 0; border-radius:2px; }
.cover .meta { font-size:12.5px; opacity:.9; line-height:1.7; }
.cover .badge { margin-top:26px; background:rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.4); padding:9px 18px; border-radius:40px; font-size:13px; font-weight:600; }
.section-title { font-size:16px; color:#1d4ed8; border-bottom:3px solid #1d4ed8; padding-bottom:4px; margin:14px 0 4px; page-break-after:avoid; }
.section-title:first-of-type { margin-top:4px; }
.hint { font-size:9.6px; color:#56627a; margin:0 0 7px; }
.qcols { column-count:2; column-gap:16px; }
.qi { break-inside:avoid; margin:0 0 6px; font-size:10.2px; line-height:1.45; }
.qi .n { font-weight:700; color:#1d4ed8; }
.qi .ce { color:#56627a; font-weight:600; white-space:nowrap; }
.qi .alt { font-weight:700; color:#13235e; }
.gabwrap { column-count:2; column-gap:16px; }
.gi { break-inside:avoid; margin:0 0 5px; font-size:9.4px; line-height:1.4; color:#46536a; }
.gi .n { font-weight:700; color:#13235e; }
.gi .resp { font-weight:700; }
.gab-c { color:#1f9d57; } .gab-e { color:#c0392b; }
.gi .ok { font-weight:700; color:#1f9d57; }
.pagebreak { page-break-before:always; }
"""

# ---- montagem das questões ----
b1 = ""
for i, (fr, _g, _c) in enumerate(PORQUE, 1):
    b1 += f'<div class="qi"><span class="n">{i}.</span> {fr} <span class="ce">( ) C&nbsp; ( ) E</span></div>'

b2 = ""
for i, (fr, _r) in enumerate(MORFO, 1):
    b2 += f'<div class="qi"><span class="n">{i}.</span> {fr} <i>Classe gramatical da palavra destacada?</i></div>'

b3 = ""
for i, (fr, _r, _reg) in enumerate(ORTO, 1):
    b3 += f'<div class="qi"><span class="n">{i}.</span> {fr}</div>'

# ---- gabaritos ----
g1 = ""
for i, (fr, g, c) in enumerate(PORQUE, 1):
    cls = "gab-c" if g == "C" else "gab-e"
    rot = "CERTO" if g == "C" else "ERRADO"
    g1 += f'<div class="gi"><span class="n">{i}.</span> <span class="resp {cls}">{rot}</span> — {c}</div>'
g2 = ""
for i, (fr, r) in enumerate(MORFO, 1):
    g2 += f'<div class="gi"><span class="n">{i}.</span> <span class="ok">{r}</span></div>'
g3 = ""
for i, (fr, r, reg) in enumerate(ORTO, 1):
    g3 += f'<div class="gi"><span class="n">{i}.</span> <span class="ok">{r}</span> — {reg}</div>'

HTML = f"""<!DOCTYPE html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body>

<div class="cover">
  <div class="kicker">LÍNGUA PORTUGUESA · TREINO</div>
  <h1>Porquês,<br>Classes &amp;<br>Ortografia</h1>
  <div class="rule"></div>
  <div class="sub">75 questões para resolver: 15 sobre os porquês · 30 de classe gramatical · 30 de ortografia — com gabarito comentado</div>
  <div class="meta" style="margin-top:26px;">Concurso <b>Sedes/DF</b> · Banca <b>Quadrix</b> · 2026<br>Técnico Administrativo (Cargo 202)</div>
  <div class="badge">Treino · 75 questões</div>
</div>

<h2 class="section-title">Bloco 1 — Os porquês (julgue Certo ou Errado)</h2>
<p class="hint">Julgue o emprego do porquê em cada frase: marque C (certo) ou E (errado). Estilo Quadrix.</p>
<div class="qcols">{b1}</div>

<h2 class="section-title">Bloco 2 — Classe gramatical (morfossintaxe)</h2>
<p class="hint">Indique a classe gramatical da palavra destacada (em MAIÚSCULAS) em cada frase.</p>
<div class="qcols">{b2}</div>

<h2 class="section-title pagebreak">Bloco 3 — Ortografia (escolha a forma correta)</h2>
<p class="hint">Escolha, entre as duas formas em parênteses, a que está correta.</p>
<div class="qcols">{b3}</div>

<h2 class="section-title pagebreak">Gabarito comentado</h2>
<p class="hint"><b>Bloco 1 — Os porquês</b></p>
<div class="gabwrap">{g1}</div>
<p class="hint" style="margin-top:8px;"><b>Bloco 2 — Classe gramatical</b></p>
<div class="gabwrap">{g2}</div>
<p class="hint" style="margin-top:8px;"><b>Bloco 3 — Ortografia</b></p>
<div class="gabwrap">{g3}</div>

</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("HTML gerado:", OUT, "| porques:", len(PORQUE), "| morfo:", len(MORFO), "| orto:", len(ORTO), "| total:", len(PORQUE)+len(MORFO)+len(ORTO))
