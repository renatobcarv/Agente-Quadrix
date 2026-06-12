# -*- coding: utf-8 -*-
"""Renderizador ÚNICO do Agente Quadrix: spec JSON -> HTML -> PDF.

Uso:
    python engine/render.py conteudo/<id>.json [--sem-pdf]

O spec define capa, seções de teoria (HTML denso) e quais bancos de questões
incluir. O render numera as questões (CE primeiro, depois ME), monta o bloco
de questões e o gabarito comentado automaticamente, e imprime o nº de páginas
do PDF gerado.
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
CHROME = os.environ.get("CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")


def carregar(caminho):
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


def carregar_bancos(slugs):
    """Carrega questões dos bancos referenciados, na ordem: CE primeiro, ME depois."""
    ce, me, outras = [], [], []
    for slug in slugs:
        arq = os.path.join(REPO, "banco", "questoes", slug + ".json")
        dados = carregar(arq)
        for q in dados["questoes"]:
            t = q.get("tipo")
            (ce if t == "CE" else me if t == "ME" else outras).append(q)
    return ce, me, outras


def html_questoes(ce, me):
    blocos = []
    n = 0
    if ce:
        blocos.append('<p class="subhead">Parte I — Julgue os itens (Certo / Errado)</p>')
        for q in ce:
            n += 1
            blocos.append(
                f'<div class="qbox"><span class="qn">{n}.</span> {q["enunciado"]}'
                f'<div class="ce">(&nbsp;&nbsp;) Certo&nbsp;&nbsp;&nbsp;(&nbsp;&nbsp;) Errado</div></div>'
            )
    if me:
        blocos.append('<p class="subhead">Parte II — Múltipla escolha (A–E)</p>')
        for q in me:
            n += 1
            tag = f'<span class="tema">{q["tag"]}</span>' if q.get("tag") else ""
            lis = "".join(f"<li>{a}</li>" for a in q["alternativas"])
            blocos.append(
                f'<div class="qbox"><span class="qn">{n}.</span> {q["enunciado"]}{tag}<ol>{lis}</ol></div>'
            )
    return "".join(blocos), n


def html_gabarito(ce, me):
    itens = []
    n = 0
    for q in ce:
        n += 1
        certo = q["gabarito"] == "C"
        cls, rot = ("gab-c", "CERTO") if certo else ("gab-e", "ERRADO")
        itens.append(
            f'<div class="gab-item"><span class="n">{n}.</span> '
            f'<span class="resp {cls}">{rot}</span> — {q["comentario"]}</div>'
        )
    for q in me:
        n += 1
        letra = "ABCDE"[q["gabarito"]]
        com = q["comentario"]
        prefixo = "" if com.lower().startswith("gabarito") else f"Gabarito {letra}: "
        itens.append(f'<div class="gab-item"><span class="n">{n}.</span> {prefixo}{com}</div>')
    return "".join(itens)


def render(spec_path, gerar_pdf=True):
    spec = carregar(spec_path)
    css = open(os.path.join(REPO, "templates", "base.css"), encoding="utf-8").read()
    css = css.replace("__COR1__", spec.get("cor", "#b3122a"))
    css = css.replace("__COR2__", spec.get("cor_escura", "#7a0c1c"))

    secoes = []
    for s in spec.get("secoes", []):
        quebra = " pagebreak" if s.get("quebra") else ""
        secoes.append(f'<h2 class="section-title{quebra}">{s["titulo"]}</h2>{s["html"]}')

    ce, me, _ = carregar_bancos(spec.get("bancos", []))
    q_html, total = html_questoes(ce, me)
    partes_q = ""
    if total:
        partes_q = (
            f'<h2 class="section-title pagebreak">{total} questões para fazer agora</h2>'
            f'<p class="lead">Resolva sem olhar o gabarito. O gabarito comentado está na seção seguinte.</p>'
            f"{q_html}"
            f'<h2 class="section-title pagebreak">Gabarito comentado</h2>'
            f'<p class="lead">Cada item traz a resposta e a explicação: por que a correta está certa '
            f'e, nas de múltipla escolha, qual elemento torna cada alternativa errada.</p>'
            f"{html_gabarito(ce, me)}"
        )

    html = f"""<!DOCTYPE html><html lang="pt-br"><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="cover">
  <div class="kicker">{spec["kicker"]}</div>
  <h1>{spec["titulo"]}</h1>
  <div class="rule"></div>
  <div class="sub">{spec["subtitulo"]}</div>
  <div class="meta" style="margin-top:26px;">Concurso <b>Sedes/DF</b> · Banca <b>Quadrix</b> · 2026<br>Técnico Administrativo (Cargo 202)</div>
  <div class="badge">{spec["badge"]}</div>
</div>
{"".join(secoes)}
{partes_q}
</body></html>"""

    outdir = os.path.join(REPO, "materiais", spec["id"])
    os.makedirs(outdir, exist_ok=True)
    base = spec.get("arquivo_saida") or spec["id"]
    html_path = os.path.join(outdir, base + ".html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"HTML: {html_path}  ({total} questões)")

    if gerar_pdf:
        pdf_path = os.path.join(outdir, base + "_PRO.pdf")
        uri = "file:///" + html_path.replace("\\", "/")
        subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
             f"--print-to-pdf={pdf_path}", uri],
            capture_output=True, timeout=120,
        )
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as f:
                paginas = len(re.findall(rb"/Type\s*/Page[^s]", f.read()))
            kb = round(os.path.getsize(pdf_path) / 1024, 1)
            print(f"PDF:  {pdf_path}  ({paginas} páginas, {kb} KB)")
        else:
            print("ERRO: PDF não foi gerado.", file=sys.stderr)
            sys.exit(1)
    return html_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    render(sys.argv[1], gerar_pdf="--sem-pdf" not in sys.argv)
