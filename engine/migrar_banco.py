# -*- coding: utf-8 -*-
"""Migração única: extrai as questões presas nos scripts legados (via AST,
sem executá-los) e constrói o banco em banco/questoes/*.json.
Depois de rodar, os scripts viram leitura-apenas em legado/.
"""
import ast
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DEST = os.path.join(REPO, "banco", "questoes")
os.makedirs(DEST, exist_ok=True)

# script: (slug, matéria, tema, revisar?)
FONTES = {
    "gerar_art5_completo.py": ("constitucional-art5", "Direito Constitucional", "Art. 5º — direitos e deveres individuais", False),
    "gerar_direitos_sociais.py": ("constitucional-direitos-sociais", "Direito Constitucional", "Direitos sociais (arts. 6º–11)", False),
    "gerar_portugues_morfossintaxe.py": ("portugues-morfossintaxe", "Língua Portuguesa", "Ortografia, classes, morfossintaxe e coesão", False),
    "gerar_organizacao_estado.py": ("constitucional-organizacao-estado", "Direito Constitucional", "Organização do Estado e Adm. Pública", True),
    "gerar_servidores_publicos.py": ("constitucional-servidores", "Direito Constitucional", "Servidores públicos (arts. 37–41)", True),
    "gerar_treino_portugues.py": ("portugues-treino-drills", "Língua Portuguesa", "Porquês, classes e ortografia (drills)", False),
}


def extrair_listas(caminho):
    """Retorna {nome_da_variavel: valor} para as listas de questões do script."""
    with open(caminho, encoding="utf-8") as f:
        tree = ast.parse(f.read())
    alvo = {"QCE", "QME", "PORQUE", "MORFO", "ORTO"}
    out = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id in alvo:
                    out[t.id] = ast.literal_eval(node.value)
    return out


def migrar(script, slug, materia, tema, revisar):
    caminho = os.path.join(HERE, script)
    if not os.path.exists(caminho):
        caminho = os.path.join(REPO, "legado", script)
    listas = extrair_listas(caminho)
    qs = []

    for i, (enun, gab, com) in enumerate(listas.get("QCE", []), 1):
        qs.append({"id": f"{slug}-ce-{i:02d}", "tipo": "CE", "enunciado": enun,
                   "gabarito": gab, "comentario": com})
    for i, (tag, enun, alts, idx, com) in enumerate(listas.get("QME", []), 1):
        qs.append({"id": f"{slug}-me-{i:02d}", "tipo": "ME", "tag": tag, "enunciado": enun,
                   "alternativas": list(alts), "gabarito": idx, "comentario": com})
    # drills do treino
    for i, (enun, gab, com) in enumerate(listas.get("PORQUE", []), 1):
        qs.append({"id": f"{slug}-porque-{i:02d}", "tipo": "CE", "enunciado": enun,
                   "gabarito": gab, "comentario": com, "tag": "Os porquês"})
    for i, (frase, resp) in enumerate(listas.get("MORFO", []), 1):
        qs.append({"id": f"{slug}-morfo-{i:02d}", "tipo": "ABERTA",
                   "enunciado": frase + " — Classe gramatical da palavra destacada?",
                   "resposta": resp, "comentario": resp, "tag": "Classe gramatical"})
    for i, (frase, resp, regra) in enumerate(listas.get("ORTO", []), 1):
        qs.append({"id": f"{slug}-orto-{i:02d}", "tipo": "ESCOLHA", "enunciado": frase,
                   "resposta": resp, "comentario": f"{resp} — {regra}", "tag": "Ortografia"})

    dados = {"materia": materia, "tema": tema, "revisar": revisar, "questoes": qs}
    destino = os.path.join(DEST, slug + ".json")
    with open(destino, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=1)
    print(f"{slug}: {len(qs)} questões" + ("  [marcado p/ revisar]" if revisar else ""))
    return len(qs)


if __name__ == "__main__":
    total = 0
    for script, (slug, materia, tema, revisar) in FONTES.items():
        total += migrar(script, slug, materia, tema, revisar)
    print(f"\nBanco construído: {total} questões em {DEST}")
