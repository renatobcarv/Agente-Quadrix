# -*- coding: utf-8 -*-
"""
gerar_prova_quadrix.py — Gera uma prova objetiva em PDF visualmente fiel ao
layout do Instituto Quadrix (padrao 2025), com gabarito em pagina separada.

USO:
    python gerar_prova_quadrix.py entrada.json saida.pdf

ESQUEMA DO JSON DE ENTRADA:
{
  "orgao": "CONSELHO REGIONAL ... NO ESTADO DE SAO PAULO",
  "cargo": "Assistente Administrativo",
  "ano": 2025,
  "instrucao": "Nas questoes a seguir, marque, ...",   # opcional (tem padrao)
  "blocos": [
    {
      "titulo": "CONHECIMENTOS BASICOS",
      "questoes": [
        {
          "texto_base": "Texto para a questao 1.\\n\\nTitulo\\n\\nCorpo...",  # opcional
          "enunciado": "Predomina no texto a funcao",
          "alternativas": ["metalinguistica...", "fatica...", "informativa...",
                           "poetica...", "conativa..."],
          "gabarito": "C"
        }
      ]
    }
  ]
}

Regras de fidelidade embutidas: 5 alternativas A-E, duas colunas justificadas,
cabecalho com orgao + "Quadrix | ANO", caixa de instrucao, faixa PROVA OBJETIVA,
faixas de secao, rotulo "QUESTAO N" em caixa arredondada com icone, fonte
Calibri (sans-serif), e GABARITO em pagina separada (com ciclagem de letras
preservada conforme o JSON).
"""
import sys, os, json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ---------- fontes (Calibri do Windows; fallback Helvetica) ----------
FONT, FONT_B, FONT_I = "Helvetica", "Helvetica-Bold", "Helvetica-Oblique"
try:
    fdir = r"C:\Windows\Fonts"
    pdfmetrics.registerFont(TTFont("Calibri", os.path.join(fdir, "calibri.ttf")))
    pdfmetrics.registerFont(TTFont("Calibri-Bold", os.path.join(fdir, "calibrib.ttf")))
    pdfmetrics.registerFont(TTFont("Calibri-Italic", os.path.join(fdir, "calibrii.ttf")))
    FONT, FONT_B, FONT_I = "Calibri", "Calibri-Bold", "Calibri-Italic"
except Exception:
    pass

# ---------- geometria ----------
PW, PH = A4
ML, MR, MT, MB = 38, 38, 40, 34
GUTTER = 18
CONTENT_W = PW - ML - MR
COL_W = (CONTENT_W - GUTTER) / 2.0
COL_X = [ML, ML + COL_W + GUTTER]
COL_BOTTOM = MB + 10

# ---------- estilos ----------
GREY_HDR = HexColor("#7f7f7f")
DARK_BAND = HexColor("#595959")
SEC_BAND = HexColor("#8c8c8c")
INSTR_BG = HexColor("#ededed")
QBOX_STROKE = HexColor("#1a1a1a")

BODY_SZ, BODY_LEAD = 9.6, 12.4
ALT_INDENT = 20  # recuo da alternativa apos "(A) "

DEFAULT_INSTR = ("Nas questoes a seguir, marque, para cada uma, a unica opcao correta, "
                 "de acordo com o respectivo comando. Para as devidas marcacoes, use a "
                 "folha de respostas, unico documento valido para a correcao da sua prova.")


def wrap(c, text, font, size, maxw):
    """Quebra texto em linhas que cabem em maxw."""
    out = []
    for para in text.split("\n"):
        if para.strip() == "":
            out.append("")
            continue
        words, line = para.split(" "), ""
        for w in words:
            t = w if not line else line + " " + w
            if c.stringWidth(t, font, size) <= maxw:
                line = t
            else:
                if line:
                    out.append(line)
                line = w
        out.append(line)
    return out


def draw_justified(c, lines, x, y, font, size, lead, maxw, justify=True, color=black):
    """Desenha linhas; justifica todas menos a ultima de cada paragrafo."""
    c.setFillColor(color)
    c.setFont(font, size)
    for i, ln in enumerate(lines):
        last = (i == len(lines) - 1) or (i + 1 < len(lines) and lines[i + 1] == "")
        if ln == "":
            y -= lead
            continue
        words = ln.split(" ")
        if justify and not last and len(words) > 1:
            tw = sum(c.stringWidth(w, font, size) for w in words)
            gap = (maxw - tw) / (len(words) - 1)
            cx = x
            for w in words:
                c.drawString(cx, y, w)
                cx += c.stringWidth(w, font, size) + gap
        else:
            c.drawString(x, y, ln)
        y -= lead
    return y


def measure(c, text, font, size, lead, maxw):
    lines = wrap(c, text, font, size, maxw)
    return lines, len(lines) * lead


def star(c, cx, cy, r):
    """Icone de estrela de 4 pontas (sparkle) como na caixa de questao."""
    import math
    pts = []
    for k in range(8):
        ang = math.pi / 2 - k * (math.pi / 4)
        rad = r if k % 2 == 0 else r * 0.38
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    p = c.beginPath()
    p.moveTo(*pts[0])
    for pt in pts[1:]:
        p.lineTo(*pt)
    p.close()
    c.setFillColor(HexColor("#1a1a1a"))
    c.drawPath(p, fill=1, stroke=0)


class Prova:
    def __init__(self, c, meta):
        self.c = c
        self.meta = meta
        self.col = 0
        self.page = 0
        self.col_top = 0
        self.y = 0

    # ---- chrome de pagina ----
    def header(self):
        c = self.c
        c.setFont(FONT, 7.6)
        c.setFillColor(GREY_HDR)
        c.drawString(ML, PH - MT + 6, self.meta["orgao"].upper())
        qx = "Quadrix | %s" % self.meta.get("ano", 2025)
        c.drawRightString(PW - MR, PH - MT + 6, qx)
        c.setStrokeColor(HexColor("#bfbfbf"))
        c.setLineWidth(0.6)
        c.line(ML, PH - MT + 1, PW - MR, PH - MT + 1)
        # rodape
        c.setFont(FONT, 8)
        c.setFillColor(GREY_HDR)
        c.drawCentredString(PW / 2, MB - 16, str(self.page))

    def new_page(self, top_matter=False):
        if self.page > 0:
            self.c.showPage()
        self.page += 1
        self.header()
        y = PH - MT - 14
        if top_matter:
            y = self._draw_top_matter(y)
        self.col_top = y
        self.col = 0
        self.y = y

    def _round_box(self, x, y_top, w, h, fill, stroke=None, r=7, lw=1):
        c = self.c
        if fill:
            c.setFillColor(fill)
        if stroke:
            c.setStrokeColor(stroke)
            c.setLineWidth(lw)
        c.roundRect(x, y_top - h, w, h, r, stroke=1 if stroke else 0,
                    fill=1 if fill else 0)

    def _draw_top_matter(self, y):
        c = self.c
        # caixa de instrucao (largura total)
        instr = self.meta.get("instrucao", DEFAULT_INSTR)
        lines, h = measure(c, instr, FONT, 9.2, 12.0, CONTENT_W - 24)
        boxh = h + 14
        self._round_box(ML, y, CONTENT_W, boxh, INSTR_BG, r=7)
        draw_justified(c, lines, ML + 12, y - 13, FONT, 9.2, 12.0,
                       CONTENT_W - 24, justify=True)
        y -= boxh + 10
        # faixa PROVA OBJETIVA
        bh = 22
        self._round_box(ML, y, CONTENT_W, bh, DARK_BAND, r=8)
        c.setFillColor(white)
        c.setFont(FONT_B, 12.5)
        c.drawCentredString(PW / 2, y - bh + 6.5, "PROVA OBJETIVA")
        y -= bh + 8
        return y

    # ---- faixa de secao (forca nova pagina) ----
    def section(self, titulo, first=False):
        self.new_page(top_matter=first)
        c = self.c
        bh = 20
        y = self.col_top
        self._round_box(ML, y, CONTENT_W, bh, SEC_BAND, r=8)
        c.setFillColor(white)
        c.setFont(FONT_B, 11)
        c.drawCentredString(PW / 2, y - bh + 6, titulo.upper())
        y -= bh + 12
        self.col_top = y
        self.col = 0
        self.y = y

    # ---- controle de coluna ----
    def _advance(self):
        if self.col == 0:
            self.col = 1
            self.y = self.col_top
        else:
            # nova pagina (sem faixa de secao)
            self.new_page(top_matter=False)
            self.col_top = self.y
            self.col = 0

    def _fits(self, h):
        return (self.y - h) >= COL_BOTTOM

    def _flow(self, lines, font, size, lead, justify=True, color=black, gap_after=4):
        """Desenha um paragrafo, quebrando entre colunas/paginas se preciso."""
        x = COL_X[self.col]
        i = 0
        while i < len(lines):
            if not self._fits(lead):
                self._advance()
                x = COL_X[self.col]
            self.y = draw_justified(self.c, [lines[i]], x, self.y, font, size,
                                    lead, COL_W, justify=justify, color=color)
            i += 1
        self.y -= gap_after

    # ---- questao ----
    def question(self, n, q):
        c = self.c
        # bloco texto-base (opcional)
        if q.get("texto_base"):
            tb = q["texto_base"]
            lines, _ = measure(c, tb, FONT_B if False else FONT, BODY_SZ, BODY_LEAD, COL_W)
            # primeira linha em negrito se parecer titulo; mantemos simples: italico
            self._flow(wrap(c, tb, FONT, BODY_SZ, COL_W), FONT, BODY_SZ, BODY_LEAD,
                       justify=True, gap_after=6)
        # rotulo QUESTAO N (mantem junto com inicio do enunciado)
        labelh = 17
        enun_lines = wrap(c, q["enunciado"], FONT, BODY_SZ, COL_W)
        need = labelh + 4 + min(2, len(enun_lines)) * BODY_LEAD
        if not self._fits(need):
            self._advance()
        x = COL_X[self.col]
        # caixa do rotulo
        c.setStrokeColor(QBOX_STROKE)
        c.setLineWidth(0.9)
        c.setFillColor(white)
        c.roundRect(x, self.y - labelh, COL_W, labelh, 4, stroke=1, fill=1)
        c.setFillColor(black)
        c.setFont(FONT_B, 9.6)
        c.drawString(x + 7, self.y - labelh + 5, "QUESTAO %d" % n)
        star(c, x + COL_W - 11, self.y - labelh / 2.0, 5.2)
        self.y -= labelh + 6
        # enunciado
        self._flow(enun_lines, FONT, BODY_SZ, BODY_LEAD, justify=True, gap_after=3)
        # alternativas
        letras = "ABCDE"
        for idx, alt in enumerate(q["alternativas"]):
            lab = "(%s)" % letras[idx]
            # primeira linha com rotulo; recuo nas continuacoes
            full = lab + "  " + alt
            lines = wrap(c, full, FONT, BODY_SZ, COL_W)
            # re-wrap continuacoes com recuo
            if len(lines) > 1:
                first = wrap(c, full, FONT, BODY_SZ, COL_W)[0]
                rest_txt = full[len(first):].strip()
                cont = wrap(c, rest_txt, FONT, BODY_SZ, COL_W - ALT_INDENT)
                lines = [first] + [" " + l for l in cont]  # marca recuo
            self._flow_alt(lines, lab)
        self.y -= 5

    def _flow_alt(self, lines, lab):
        c = self.c
        for j, ln in enumerate(lines):
            if not self._fits(BODY_LEAD):
                self._advance()
            x = COL_X[self.col]
            indent = 0
            txt = ln
            if ln.startswith(" "):
                indent = ALT_INDENT
                txt = ln[1:]
            # justifica linhas internas (menos a ultima)
            last = (j == len(lines) - 1)
            words = txt.split(" ")
            c.setFillColor(black)
            c.setFont(FONT, BODY_SZ)
            maxw = COL_W - indent
            if not last and len(words) > 1:
                tw = sum(c.stringWidth(w, FONT, BODY_SZ) for w in words)
                gap = (maxw - tw) / (len(words) - 1)
                cx = x + indent
                for w in words:
                    c.drawString(cx, self.y, w)
                    cx += c.stringWidth(w, FONT, BODY_SZ) + gap
            else:
                c.drawString(x + indent, self.y, txt)
            self.y -= BODY_LEAD

    # ---- gabarito ----
    def gabarito(self, blocos):
        self.new_page(top_matter=False)
        c = self.c
        bh = 22
        y = self.col_top
        self._round_box(ML, y, CONTENT_W, bh, DARK_BAND, r=8)
        c.setFillColor(white)
        c.setFont(FONT_B, 13)
        c.drawCentredString(PW / 2, y - bh + 6.5, "GABARITO")
        y -= bh + 8
        c.setFont(FONT, 9)
        c.setFillColor(GREY_HDR)
        c.drawCentredString(PW / 2, y, "%s — %s" % (self.meta["cargo"], self.meta["orgao"]))
        y -= 22
        # grade: blocos com numeros e letras
        n = 0
        cellw, cellh = 46, 22
        per_row = int(CONTENT_W // cellw)
        for b in blocos:
            c.setFont(FONT_B, 10)
            c.setFillColor(black)
            c.drawString(ML, y, b["titulo"].upper())
            y -= 16
            col = 0
            x = ML
            for q in b["questoes"]:
                n += 1
                gab = q.get("gabarito", "-")
                c.setStrokeColor(HexColor("#999999"))
                c.setLineWidth(0.6)
                c.setFillColor(white)
                c.rect(x, y - cellh, cellw - 6, cellh, stroke=1, fill=1)
                c.setFillColor(black)
                c.setFont(FONT, 8)
                c.drawString(x + 4, y - 8, "%02d" % n)
                c.setFont(FONT_B, 11)
                c.drawRightString(x + cellw - 11, y - cellh + 6, gab)
                col += 1
                x += cellw
                if col >= per_row:
                    col = 0
                    x = ML
                    y -= cellh + 4
            if col != 0:
                y -= cellh + 4
            y -= 10
            if y < MB + 80:
                self.new_page()
                y = self.col_top


def build(data, out_path):
    c = canvas.Canvas(out_path, pagesize=A4)
    c.setTitle("%s - %s" % (data.get("cargo", ""), data.get("orgao", "")))
    p = Prova(c, data)
    blocos = data["blocos"]
    qnum = 0
    for bi, bloco in enumerate(blocos):
        p.section(bloco["titulo"], first=(bi == 0))
        for q in bloco["questoes"]:
            qnum += 1
            p.question(qnum, q)
    p.gabarito(blocos)
    c.showPage()
    c.save()
    print("PDF gerado:", out_path, "| questoes:", qnum)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    with open(sys.argv[1], encoding="utf-8") as f:
        data = json.load(f)
    build(data, sys.argv[2])
