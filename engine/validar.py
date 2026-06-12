# -*- coding: utf-8 -*-
"""Validador (o "conselho mecânico") do Agente Quadrix.

Uso:
    python engine/validar.py                 # valida todo o banco
    python engine/validar.py <slug> [...]    # valida bancos específicos

Checagens por arquivo de banco:
  1. ids únicos e campos obrigatórios presentes;
  2. todo item tem comentário não vazio (gabarito comentado é obrigatório);
  3. CE: gabarito C/E e equilíbrio (nenhum lado > 70%);
  4. ME: 5 alternativas, gabarito 0-4, letras distribuídas (nenhuma > 40%),
     correta não pode ser sistematicamente a mais longa;
  5. acentuação: texto em português SEM acentos = defeito grave (pega material
     digitado sem acento);
Arquivos marcados com "revisar": true geram AVISO em vez de FALHA (defeito já
conhecido e registrado). Sai com código 1 se houver qualquer FALHA.
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
ACENTOS = "áàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ"


def texto_da_questao(q):
    partes = [q.get("enunciado", ""), q.get("comentario", "")]
    partes += q.get("alternativas", [])
    return " ".join(partes)


def validar_arquivo(caminho):
    nome = os.path.basename(caminho)
    with open(caminho, encoding="utf-8") as f:
        dados = json.load(f)
    relax = dados.get("revisar", False)
    falhas, avisos = [], []

    def problema(msg):
        (avisos if relax else falhas).append(msg)

    qs = dados.get("questoes", [])
    if not qs:
        problema("banco vazio")

    ids = [q.get("id") for q in qs]
    if len(ids) != len(set(ids)):
        problema("ids duplicados")

    ce = [q for q in qs if q.get("tipo") == "CE"]
    me = [q for q in qs if q.get("tipo") == "ME"]

    for q in qs:
        if not q.get("comentario", "").strip():
            problema(f"{q.get('id')}: sem comentário (gabarito comentado é obrigatório)")
        if not q.get("enunciado", "").strip():
            problema(f"{q.get('id')}: sem enunciado")

    for q in ce:
        if q.get("gabarito") not in ("C", "E"):
            problema(f"{q.get('id')}: gabarito CE inválido ({q.get('gabarito')})")
    if len(ce) >= 6:
        c = sum(1 for q in ce if q.get("gabarito") == "C")
        frac = c / len(ce)
        if frac > 0.70 or frac < 0.30:
            avisos.append(f"CE desequilibrado: {c}/{len(ce)} certos")

    letras = {l: 0 for l in "ABCDE"}
    razoes = []
    for q in me:
        alts = q.get("alternativas", [])
        g = q.get("gabarito")
        if len(alts) != 5:
            problema(f"{q.get('id')}: {len(alts)} alternativas (esperado 5)")
            continue
        if not isinstance(g, int) or not 0 <= g <= 4:
            problema(f"{q.get('id')}: gabarito ME inválido ({g})")
            continue
        letras["ABCDE"[g]] += 1
        outras = [len(a) for i, a in enumerate(alts) if i != g]
        if outras and sum(outras):
            razoes.append(len(alts[g]) / (sum(outras) / len(outras)))
    if len(me) >= 6:
        for l, qtd in letras.items():
            if qtd / len(me) > 0.40:
                avisos.append(f"letra {l} concentra {qtd}/{len(me)} gabaritos")
        if razoes and sum(razoes) / len(razoes) > 1.30:
            problema("a alternativa correta é sistematicamente a mais longa (vicia o chute)")

    texto = " ".join(texto_da_questao(q) for q in qs)
    letras_texto = len(re.sub(r"[^A-Za-zÀ-ÿ]", "", texto))
    n_acentos = sum(texto.count(a) for a in ACENTOS)
    if letras_texto > 500 and n_acentos / letras_texto < 0.01:
        problema(f"texto praticamente SEM ACENTOS ({n_acentos} acentos em {letras_texto} letras) — defeito grave")
    # palavras comuns digitadas sem acento (pega desacentuação parcial)
    sem_acento = re.findall(r"\b(nao|sao|voce|publico|publica|questoes|secao|tres|porem|atraves|juridico|orgao)\b", texto, re.IGNORECASE)
    if sem_acento:
        exemplos = ", ".join(sorted(set(w.lower() for w in sem_acento))[:6])
        problema(f"{len(sem_acento)} palavras sem acento no texto (ex.: {exemplos}) — defeito grave")

    return nome, dados.get("tema", "?"), len(qs), falhas, avisos, relax


def main():
    pasta = os.path.join(REPO, "banco", "questoes")
    if len(sys.argv) > 1:
        arquivos = [os.path.join(pasta, s + ".json") for s in sys.argv[1:]]
    else:
        arquivos = sorted(glob.glob(os.path.join(pasta, "*.json")))
    if not arquivos:
        print("Nenhum banco encontrado em banco/questoes/.")
        sys.exit(1)

    houve_falha = False
    for arq in arquivos:
        nome, tema, n, falhas, avisos, relax = validar_arquivo(arq)
        marca = " [revisar]" if relax else ""
        status = "FALHOU" if falhas else ("AVISOS" if avisos else "ok")
        print(f"{status:7} {nome}{marca} — {tema} ({n} questões)")
        for f in falhas:
            print(f"   FALHA: {f}")
        for a in avisos:
            print(f"   aviso: {a}")
        houve_falha = houve_falha or bool(falhas)

    print()
    if houve_falha:
        print(">>> REPROVADO pelo conselho. Corrija as falhas antes de commitar.")
        sys.exit(1)
    print(">>> Aprovado pelo conselho.")


if __name__ == "__main__":
    main()
