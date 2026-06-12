# -*- coding: utf-8 -*-
"""Folha de redação imprimível (A4): cabeçalho + área do tema + 30 linhas
numeradas (texto definitivo) + página de rascunho. Render via Chrome.
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(_HERE)
OUTDIR = os.path.join(_REPO, "materiais", "dia12-redacao-dissertativa")
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "Folha_Redacao.html")

N_LINHAS = 30

linhas_def = "".join(
    f'<div class="linha"><span class="num">{i:02d}</span><span class="ln"></span></div>'
    for i in range(1, N_LINHAS + 1)
)
linhas_rasc = "".join('<div class="linha r"><span class="ln"></span></div>' for _ in range(N_LINHAS + 4))

CSS = """
@page { size:A4; margin:12mm 12mm 10mm 12mm; }
* { box-sizing:border-box; }
body { font-family:'Segoe UI','Helvetica Neue',Arial,sans-serif; color:#1b2330; font-size:11px; margin:0; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
h1,h2 { margin:0; }
.head { border:1.5px solid #0f3d2e; border-radius:6px; overflow:hidden; }
.head .top { background:#0f3d2e; color:#fff; padding:6px 12px; display:flex; justify-content:space-between; align-items:center; }
.head .top h1 { font-size:15px; letter-spacing:1px; }
.head .top .sub { font-size:9.5px; opacity:.9; text-align:right; line-height:1.3; }
.head .fields { display:flex; gap:14px; padding:8px 12px; font-size:10px; }
.head .fields .f { flex:1; }
.head .fields .lbl { font-size:8px; text-transform:uppercase; letter-spacing:.5px; color:#5a6573; }
.head .fields .blank { border-bottom:1px solid #9aa3ad; height:15px; }
.tema { border:1px solid #c2cbd2; border-radius:6px; margin-top:8px; padding:7px 10px; }
.tema .lbl { font-size:8.5px; text-transform:uppercase; letter-spacing:.6px; color:#0f3d2e; font-weight:700; margin-bottom:5px; }
.tema .tline { border-bottom:1px solid #c9ced6; height:13px; margin-bottom:7px; }
.instr { font-size:8.6px; color:#5a6573; margin:6px 2px 4px; display:flex; justify-content:space-between; }
.titulo-bloco { font-size:9px; text-transform:uppercase; letter-spacing:1px; color:#0f3d2e; font-weight:700; margin:8px 2px 5px; border-left:3px solid #0f3d2e; padding-left:7px; }
.linhas { margin-top:2px; }
.linha { display:flex; align-items:flex-end; height:8mm; }
.linha .num { width:7mm; font-size:7.5px; color:#9aa3ad; padding-bottom:1mm; }
.linha .ln { flex:1; border-bottom:1px solid #c2c8d0; height:100%; }
.linha.r { height:8mm; }
.linha.r .ln { border-bottom:1px solid #d7dce2; }
.pagebreak { page-break-before:always; }
.rasc-head { font-size:13px; font-weight:700; color:#0f3d2e; letter-spacing:1px; margin-bottom:4px; }
.foot { font-size:8px; color:#9aa3ad; text-align:center; margin-top:6px; }
"""

HTML = f"""<!DOCTYPE html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body>

<div class="head">
  <div class="top">
    <h1>FOLHA DE REDAÇÃO</h1>
    <div class="sub">Concurso Sedes/DF · Banca Quadrix · 2026<br>Técnico Administrativo (Cargo 202)</div>
  </div>
  <div class="fields">
    <div class="f" style="flex:2"><div class="lbl">Nome</div><div class="blank"></div></div>
    <div class="f"><div class="lbl">Cargo / Inscrição</div><div class="blank"></div></div>
    <div class="f" style="flex:.6"><div class="lbl">Data</div><div class="blank"></div></div>
  </div>
</div>

<div class="tema">
  <div class="lbl">Tema</div>
  <div class="tline"></div>
  <div class="tline"></div>
</div>

<div class="instr">
  <span>Texto dissertativo-argumentativo · mínimo de 20 e máximo de 30 linhas · caneta azul ou preta.</span>
  <span>Linhas usadas: ______ / 30</span>
</div>

<div class="titulo-bloco">Texto definitivo</div>
<div class="linhas">{linhas_def}</div>

<div class="pagebreak"></div>
<div class="rasc-head">RASCUNHO</div>
<div class="instr"><span>Este espaço não será corrigido. Passe o texto a limpo na folha definitiva.</span><span></span></div>
<div class="linhas">{linhas_rasc}</div>
<div class="foot">Agente Quadrix · folha de redação para treino</div>

</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("HTML gerado:", OUT, "| linhas definitivas:", N_LINHAS)
