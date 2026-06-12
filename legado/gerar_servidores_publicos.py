# -*- coding: utf-8 -*-
"""Material DENSO — Dia 9: Servidores Publicos (arts. 37-41) + Revisao Constitucional.
35 questoes (15 C/E + 20 A-E) com gabarito comentado.
"""
import os
_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(_HERE)
OUTDIR = os.path.join(_REPO, "materiais", "dia09-servidores-publicos")
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "Dia9_Servidores_Publicos.html")

QCE = [
    ("A Administracao Publica direta ou indireta de qualquer dos Poderes deve obdecer ao princípio da legalidade.",
     "C", "Correto. Art. 37: legalidade é fundamento (nao pode fazer nada sem lei)."),
    ("Servidor publico em estagio probatorio pode ser exonerado sem justa causa.",
     "C", "Correto. O estagio probatorio permite exoneracao imotivada; após 3 anos, adquire estabilidade."),
    ("A estabilidade do servidor publico é absoluta; nao pode ser perfeita em hipotese alguma.",
     "E", "Errado. Estabilidade pode ser perdida por sentenca judicial, processo administrativo ou avaliacao periodica de desempenho."),
    ("Lei municipal pode criar cargos de provimento vitalicio.",
     "E", "Errado. Cargo vitalicio é proibido desde 1988 (art. 41). Todos os cargos devem ter estagio probatorio de 3 anos."),
    ("O servidor estavel so pode ser demitido por sentenca judicial.",
     "E", "Errado. Pode ser demitido também por processo administrativo (com direito a defesa) ou por insuficiencia em avaliacao de desempenho."),
    ("Acumulacao de cargos publicos é proibida em qualquer hipotese.",
     "E", "Errado. É permitida em casos específicos: dois cargos de professor; um cargo de professor + tecnico/cientif; dois magistério; médico + professor (art. 37, inciso XVI)."),
    ("A remuneracao dos servidores publicos deve respeitar o limite constitucional de subsídio do Presidente da Republica.",
     "C", "Correto. Art. 37, parágrafo 11: remuneracao nao pode ultrapassar o subsídio presidencial (regra do teto)."),
    ("Servidores publicos estaduais podem receber remuneracao superior ao subsídio do Governador.",
     "E", "Errado. O teto constitucional é o subsídio do Governador para Estado e do Prefeito para Municipio (art. 37, parágrafo 11)."),
    ("Servidor publico nao tem direito a greve.",
     "E", "Errado. O direito de greve é assegurado a servidores publicos, mas a lei pode regulamentar (art. 37, parágrafo 7º)."),
    ("Despedida sem justa causa de servidor estavel é permitida em tempos de crise economica.",
     "E", "Errado. Estabilidade protege contra demissao sem justa causa, ponto. Crise economica nao autoriza arbitrio."),
    ("O Presidente da Republica pode perder a estabilidade por avaliacao periodica de desempenho.",
     "E", "Errado. Presidente é  cargo eletivo, nao se submete ao regime dos servidores publicos."),
    ("Todos os cargos publicos devem ser criados por lei.",
     "C", "Correto. Art. 37, parágrafo 5º: criacao de cargos, funcoes, empregos só por lei (em cada ente)."),
    ("Servidor publico em estagio probatorio adquire estabilidade automaticamente apos 3 anos.",
     "C", "Correto. Art. 41, parágrafo 1º: apos 3 anos de estagio probatorio, servidor adquire estabilidade."),
    ("Pode haver criacao de novos direitos sociais sem lei complementar.",
     "C", "Correto. Lei ordinaria é suficiente para criar direitos sociais; lei complementar é exceção."),
    ("Leis ordinarias podem revogar lei complementar.",
     "E", "Errado. Lei ordinaria nao pode revogar lei complementar; apenas outra lei complementar pode."),
]

QME = [
    ("Legalidade", "O princípio da legalidade na Administracao Publica significa que",
     ["a Administracao pode fazer tudo aquilo nao proibido em lei.",
      "a Administracao so pode fazer aquilo expressamente autorizado em lei.",
      "nao ha necessidade de lei para atos da Administracao.",
      "a Administracao é livre de vinculacoes legais.",
      "leis podem nao ser cumpridas conforme a conveniencia."],
     1, "Gabarito B: Administracao so faz o que lei permite (art. 37). A: incorreto (deve ser autorizado). C, D, E: violam legalidade."),
    ("Estagio probatorio", "Servidor em estagio probatorio de 3 anos pode ser",
     ["exonerado sem justa causa, se nao aprovado ao final.",
      "automaticamente promovido apos 2 anos.",
      "demitido apenas por justa causa comprovada.",
      "afastado para sempre sem qualquer avaliacao.",
      "transformado em vitalicio."],
     0, "Gabarito A: estagio permite exoneracao imotivada se nao aprovado (art. 41, parágrafo 1º). B: nao há promocao automatica. C: nao é necessaria justa causa. D, E: incorretos."),
    ("Estabilidade", "Servidor estavel pode perder a estabilidade por",
     ["decisao arbitraria do Presidente.",
      "falta de comparecimento em um dia de trabalho.",
      "sentenca judicial transitada em julgado, processo administrativo ou insuficiencia em avaliacao periodica.",
      "recusa em realizar atividades extras nao pagas.",
      "opinioes politicas discordantes."],
     2, "Gabarito C: as tres hipoteses que permitem perda de estabilidade (art. 41, parágrafo 1º, incisos). A: arbitrio proibido. B: exagerado. D, E: proibidos."),
    ("Acumulacao", "E permitido ao servidor publico acumular",
     ["dois cargos quaisquer.",
      "tres ou mais funcoes.",
      "dois cargos de professor ou um professor + um de tecnico/cientifico.",
      "cargos sem limite.",
      "funcoes eletivas com cargos tecnicos simultaneamente."],
     2, "Gabarito C: excecoes permitidas listadas no art. 37, inciso XVI. A, B: limite dois. D: ha limite. E: incompatibilidades."),
    ("Teto remuneratorio", "A remuneracao de servidores estaduais nao pode ultrapassar",
     ["o dobro do salario minimo.",
      "valor arbitrado pelo Governador.",
      "o subsídio do Governador.",
      "o salario minimo.",
      "o subsídio do Presidente."],
     2, "Gabarito C: teto estadual é subsídio do Governador; Federal é subsídio do Presidente (art. 37, parágrafo 11). E: apenas para federal."),
    ("Criacao de cargos", "Cargos e funcoes publicos devem ser criados por",
     ["decreto do Executivo.",
      "portaria da administracao.",
      "lei em cada ente.",
      "decisao do tribunal.",
      "costume administrativo."],
     2, "Gabarito C: lei em cada ente federado (art. 37, parágrafo 5º). A, B, D, E: nao têm competencia."),
    ("Regime estatutario", "Servidores publicos civis nao podem ser regidos por",
     ["consolidacao das leis trabalhistas (CLT).",
      "lei local (estatuto).",
      "regime juridico unico.",
      "direito administrativo.",
      "Constituicao Federal."],
     0, "Gabarito A: CLT é para setor privado; publico segue estatuto ou regime juridico (art. 39). B, C, D, E: sao aplicaveis."),
    ("Greve", "O direito de greve de servidores publicos",
     ["é inexistente; servidores nao podem greve.",
      "é assegurado, conforme lei que o regulamenta.",
      "depende de autorizacao do Presidente.",
      "é limitado a sindicatos.",
      "nao pode ser regulado por lei."],
     1, "Gabarito B: direito assegurado, regulado por lei (art. 37, parágrafo 7º). A: existe. C: nao depende de autorizacao. D: é direito do servidor. E: lei regula."),
    ("Avaliacao de desempenho", "Servidor estavel pode ser demitido por insuficiencia em",
     ["uma unica avaliacao.",
      "avaliacao periodica de desempenho conforme lei.",
      "avaliacao escolhida arbitrariamente.",
      "avaliacao sem direito a defesa.",
      "avaliacao sem regulamentacao."],
     1, "Gabarito B: avaliacao periodica conforme lei, com devido processo (art. 41, parágrafo 1º, inciso II). A: exige repetidao. C, D, E: violam direitos."),
    ("Limite de mandato", "Presidente da Republica tem mandato de",
     ["2 anos.",
      "3 anos.",
      "4 anos, com reeleicao permitida uma vez.",
      "4 anos, sem possibilidade de reeleicao.",
      "5 anos."],
     2, "Gabarito C: 4 anos, reelegivél uma vez (maximo 8 anos) (art. 82). A, B: incorretos. D: reeleicao é permitida. E: incorreto."),
    ("Conselho Nacional de Justica", "O CNJ é responsavel por",
     ["julgar causas civeis e criminais.",
      "controlar administrativa e financeiramente o Poder Judiciario.",
      "editar codigos de processo.",
      "criar novos tribunais.",
      "substituir o STF."],
     1, "Gabarito B: CNJ controla Judiciario (art. 103-B). A: nao julga. C, D: outras competencias. E: nao substitui STF."),
    ("Emendas constitucionais", "Proposta de emenda a Constituicao pode ser rejeitada por",
     ["maioria simples do Congresso.",
      "maioria dos dois terços do Senado apenas.",
      "maioria de tres quintos em duas votacoes em cada Casa.",
      "decisao do STF.",
      "veto do Presidente."],
     2, "Gabarito C: exige tres quintos em ambas as Casas, em dois turnos (art. 60, parágrafo 2º). A: nao é maioria simples. B: exige ambas as Casas. D, E: nao têm essas competencias."),
    ("Mandado de injuncao", "Mandado de injuncao é cabível quando",
     ["existe lesao a direito.",
      "falta norma regulamentadora que inviabiliza direito constitucional.",
      "ha ameaca a liberdade de locomocao.",
      "se quer conhecer dados pessoais.",
      "ha abuso de autoridade."],
     1, "Gabarito B: injuncao combate omissao legislativa (art. 5º, inciso LXXI). A: é mandado seg. C: é habeas corpus. D: é habeas data. E: é mandado seg."),
    ("Subsidio", "Subsidio nada mais é do que",
     ["bonificacao voluntaria.",
      "salario fixado conforme o nivel salarial de cada um.",
      "valor unico de remuneracao estabelecido em lei, por cargo ou funcao.",
      "valor variavel conforme desempenho.",
      "complemento de renda."],
     2, "Gabarito C: subsidio é valor fixo, unico, por cargo/funcao, sem adicionais (art. 39, parágrafo 1º). A: nao é voluntario. B, D: podem variar indevidamente. E: é parte principal da remuneracao."),
    ("Princípio da moralidade", "O princípio da moralidade administrativa exige",
     ["honestidade publica e conformidade com regras de conduta social.",
      "apenas cumprimento formal da lei.",
      "que todos os atos sejam apreciados pelo povo.",
      "inexistencia de qualquer controle.",
      "liberdade absoluta de conducao."],
     0, "Gabarito A: moralidade é dever de honestidade e respeito a etica publica (art. 37, caput). B: vai alem do formal. C: nao é necessario. D, E: ha controle."),
]

CSS = """
@page { size:A4; margin:13mm 13mm 15mm 13mm; }
* { box-sizing:border-box; }
body { font-family:'Segoe UI','Helvetica Neue',Arial,sans-serif; color:#1d2733; font-size:11px; line-height:1.6; margin:0; orphans:3; widows:3; -webkit-print-color-adjust:exact; }
h1,h2,h3,h4 { margin:0; font-weight:700; }
p { margin:0 0 7px; text-align:justify; }
.cover { height:250mm; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; background:linear-gradient(135deg,#2d5a3d 0%,#3d7a4d 55%,#1f4730 100%); color:#fff; border-radius:6px; page-break-after:always; padding:0 24mm; }
.cover .kicker { letter-spacing:4px; font-size:12px; opacity:.85; font-weight:600; }
.cover h1 { font-size:43px; line-height:1.06; margin:10px 0 6px; }
.cover .sub { font-size:15px; font-weight:400; opacity:.95; max-width:140mm; }
.cover .rule { width:70px; height:4px; background:#ffd27a; margin:22px 0; }
.cover .meta { font-size:12.5px; opacity:.9; line-height:1.7; }
.cover .badge { margin-top:26px; background:rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.4); padding:9px 18px; border-radius:40px; font-size:13px; font-weight:600; }
.section-title { font-size:17px; color:#3d7a4d; border-bottom:3px solid #3d7a4d; padding-bottom:4px; margin:16px 0 9px; page-break-after:avoid; }
.section-title:first-of-type { margin-top:4px; }
.callout { border-radius:7px; padding:9px 12px; margin:6px 0; page-break-inside:avoid; }
.c-banca { background:#eef4ff; border-left:4px solid #2b6cb0; }
.callout h4 { font-size:10.5px; margin-bottom:4px; text-transform:uppercase; }
.callout ul { margin:3px 0 0; padding-left:15px; }
.callout li { margin:2.5px 0; }
.qbox { border:1px solid #e2e6ee; border-radius:8px; padding:9px 12px; margin:0 0 8px; page-break-inside:avoid; }
.qbox .qn { color:#3d7a4d; font-weight:700; }
.qbox .tema { display:inline-block; background:#eef0f5; color:#56627a; font-size:8.2px; font-weight:700; text-transform:uppercase; padding:2px 7px; border-radius:20px; margin-left:6px; }
.qbox ol { margin:5px 0 0; padding-left:0; list-style:none; counter-reset:opt; }
.qbox ol li { counter-increment:opt; margin:2.5px 0; padding-left:20px; position:relative; }
.qbox ol li::before { content:counter(opt,upper-alpha)")"; position:absolute; left:0; font-weight:700; color:#56627a; }
.ce { margin-top:5px; font-size:10px; color:#56627a; font-weight:700; }
.gab-item { border-bottom:1px solid #eef0f4; padding:6px 0; page-break-inside:avoid; }
.gab-item .n { font-weight:700; color:#2d5a3d; }
.gab-item .resp { font-weight:700; }
.gab-c { color:#1f9d57; }
.gab-e { color:#c0392b; }
.pagebreak { page-break-before:always; }
.lead { font-size:11px; color:#33414f; }
"""

ce_html = "".join(f'<div class="qbox"><span class="qn">{i}.</span> {af}<div class="ce">(&nbsp;&nbsp;) Certo&nbsp;&nbsp;&nbsp;(&nbsp;&nbsp;) Errado</div></div>' for i, (af, _g, _c) in enumerate(QCE, 1))
me_html = "".join(f'<div class="qbox"><span class="qn">{k}.</span> {enun}<span class="tema">{tema}</span><ol>{"".join(f"<li>{o}</li>" for o in opts)}</ol></div>' for k, (tema, enun, opts, ok, com) in enumerate(QME, 16))
gab_html = "".join(f'<div class="gab-item"><span class="n">{i}.</span> <span class="resp {"gab-c" if g == "C" else "gab-e"}">{"CERTO" if g == "C" else "ERRADO"}</span> — {c}</div>' for i, (af, g, c) in enumerate(QCE, 1)) + "".join(f'<div class="gab-item"><span class="n">{k}.</span> {com}</div>' for k, (tema, enun, opts, ok, com) in enumerate(QME, 16))

HTML = f"""<!DOCTYPE html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body>

<div class="cover">
  <div class="kicker">DIREITO CONSTITUCIONAL</div>
  <h1>Servidores<br>Publicos</h1>
  <div class="rule"></div>
  <div class="sub">Arts. 37-41 + Revisao Geral de Constitucional — apostila, estabilidade, remuneracao e direitos, 35 questoes com gabarito comentado</div>
  <div class="meta" style="margin-top:26px;">Concurso <b>Sedes/DF</b> · Banca <b>Quadrix</b> · 2026<br>Tecnico Administrativo (Cargo 202)</div>
  <div class="badge">Dia 9 · 35 questoes para fazer agora</div>
</div>

<h2 class="section-title">1. Princípios da Administracao Publica (art. 37, caput)</h2>
<p>A Administracao Publica deve obdecer a cinco principios: <b>Legalidade</b> (nao pode fazer nada sem lei), <b>Impessoalidade</b> (sem discriminacao ou favorecimento), <b>Moralidade</b> (honestidade e etica), <b>Publicidade</b> (transparencia de atos) e <b>Eficiencia</b> (melhor desempenho). O principio mais cobrado é a <b>legalidade</b>: enquanto o particular pode fazer tudo que nao é proibido, a Administracao so faz o que lei autoriza.</p>

<h2 class="section-title">2. Regime dos servidores publicos (art. 39)</h2>
<p>Os servidores publicos civis são regidos por <b>lei em cada ente federado</b> (Uniao, Estado, DF, Municipio). Podem ter regime <b>estatutario</b> (por lei) ou <b>celetista</b> (contrato por lei, mas regras da CLT). Seu <b>subsidio</b> é valor fixo, unico, por cargo/funcao, sem adicionais (diferencia-se de "salario"). Sao <b>vedados</b> acrescimos pecuniarios nao previstos em lei e vinculacao ou equiparacao de remuneracao.</p>

<h2 class="section-title">3. Acumulacao de cargos (art. 37, inciso XVI)</h2>
<p><b>Regra geral:</b> proibido acumular. <b>Excecoes permitidas:</b> dois cargos de professor; um cargo de professor + um tecnico ou cientif; dois magistério; medico + professor. Limite maximo: dois cargos (nao três ou mais). <b>Indenizacoes e pensoes</b> nao sao consideradas "acumulacao".</p>

<h2 class="section-title">4. Estagio probatorio (art. 41, parágrafo 1º)</h2>
<p>Todo servidor de novo ingresso cumpre <b>3 anos de estagio probatorio</b>. Durante este periodo, pode ser <b>exonerado sem justa causa</b> (se nao aprovado). Apos 3 anos, se aprovado, adquire <b>estabilidade</b> e so pode ser demitido por <b>sentenca judicial</b>, <b>processo administrativo</b> (com contraditorio e ampla defesa) ou <b>insuficiencia em avaliacao periodica de desempenho</b>.</p>

<h2 class="section-title">5. Teto remuneratorio e subsídio (art. 37, parágrafo 11)</h2>
<p>A remuneracao de servidores em cada ente nao pode ultrapassar o subsídio do chefe daquele ente: <b>Uniao</b> → subsídio do Presidente; <b>Estado</b> → subsídio do Governador; <b>Municipio</b> → subsídio do Prefeito; <b>DF</b> → subsídio do Governador. Este é o "teto constitucional" e é inviolavel.</p>

<h2 class="section-title">6. Direito de greve (art. 37, parágrafo 7º)</h2>
<p>Servidores publicos <b>tem direito de greve</b>, conforme <b>lei que o regulamenta</b>. A lei define limites para preservar funcionamento de servicos essenciais. Greve nao autorizada pela lei é abusiva e pode gerar responsabilidade civil.</p>

<h2 class="section-title">7. Revisao geral de Constitucional</h2>
<p><b>Supremo Tribunal Federal (STF):</b> 11 ministros, guardiao da CF, julga acoes constitucionais e define jurisprudencia. <b>Emendas constitucionais:</b> exigem 3/5 em duas votacoes em cada Casa; nao podem emendar clausulas petreas. <b>Direitos fundamentais:</b> arts. 5º-17 (vida, liberdade, igualdade, direitos sociais). <b>Organizacao estatal:</b> Uniao, Estados, DF, Municipios; três Poderes. <b>Lei complementar vs. ordinaria:</b> complementar é superior, exige maioria absoluta. <b>Medida provisoria:</b> 60 dias + prorrogacao de 60 dias. <b>Princípios:</b> legalidade, moralidade, publicidade, impessoalidade, eficiencia.</p>

<h2 class="section-title pagebreak">8. 35 questoes para fazer agora</h2>
<p class="lead">Resolva sem gabarito. <b>1-15:</b> Certo/Errado. <b>16-35:</b> multipla escolha (A-E). Gabarito na secao 9.</p>
<p style="margin:8px 0 4px; font-weight:700; color:#3d7a4d;">Parte I — Julgue os itens (Certo / Errado)</p>
{ce_html}
<p style="margin:8px 0 4px; font-weight:700; color:#3d7a4d;">Parte II — Multipla escolha (A-E)</p>
{me_html}

<h2 class="section-title pagebreak">9. Gabarito comentado</h2>
{gab_html}

</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("Dia9 gerado: %d Q" % (len(QCE) + len(QME)))
