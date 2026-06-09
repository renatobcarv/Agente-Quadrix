<div align="center">

# 🎯 Agente Quadrix

### Sistema de geração de materiais de estudo para concursos da banca **Instituto Quadrix**

Transforma a análise empírica de **64 provas reais** em **simulados comentados** e **materiais de teoria** com design profissional — feitos para gerar **acerto sob pressão**, não apenas leitura.

![Banca](https://img.shields.io/badge/Banca-Quadrix-b3122a)
![Provas analisadas](https://img.shields.io/badge/Provas%20analisadas-64-1f9d57)
![Engine](https://img.shields.io/badge/Engine-Python%20%2B%20HTML%2FCSS-2b6cb0)
![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-7a0c1c)

</div>

---

## 📌 O que é isto

O **Agente Quadrix** é o motor por trás da preparação para o concurso **Sedes/DF — Técnico Administrativo (Quadrix, 2026)**.
Ele junta três coisas que normalmente vivem separadas:

1. **Base empírica** — 64 cadernos de prova + 10 gabaritos definitivos da Quadrix 2025, de 10 conselhos diferentes.
2. **Engenharia de padrões** — o estudo de _como a banca escreve_: mecânicas de distrator, frases de comando, ciclagem de gabarito, pegadinhas recorrentes.
3. **Motor de geração** — scripts que produzem PDFs e materiais HTML com **design de cursinho** (capa, cards, caixas de pegadinha/macete, tabelas comparativas) a partir de dados estruturados.

> **Princípio central:** concurso não premia quem leu mais — premia quem **reconhece padrões mais rápido, interpreta melhor e erra menos sob pressão**. Todo material aqui é construído com esse objetivo.

---

## 🗂️ Estrutura do repositório

```
Agente-Quadrix/
├── README.md                  ← você está aqui
├── LICENSE                    ← MIT (código) + aviso sobre material de terceiros
│
├── docs/                      📚 conhecimento do sistema
│   ├── metodologia.md         ← como um bom material de concurso deve ensinar
│   ├── padroes-da-banca.md    ← referência técnica: 8 mecânicas de pegadinha + padrões
│   └── cronograma-estudos.md  ← plano diário de 100 dias (prova em 06/09/2026)
│
├── engine/                    ⚙️ motor de geração
│   ├── gerar_prova_quadrix.py ← PDF no layout FIEL da Quadrix (reportlab)
│   ├── gerar_material_html.py ← material de estudo em HTML/CSS (render via Chrome)
│   ├── exemplo_prova.json     ← modelo de entrada do gerador de prova
│   └── requirements.txt
│
├── skill/                     🧩 kit reutilizável (instruções para o agente)
│   ├── SKILLQUADRIX.md        ← a skill operacional
│   └── README.md              ← como fazer pedidos num chat
│
├── materiais/                 🎓 saídas geradas (produto final)
│   └── dia04-art5-cf88/       ← Dia 4: Art. 5º — teoria + 35 questões comentadas
│       ├── Dia4_Art5_PRO.pdf  ← material profissional (HTML→PDF)
│       ├── Dia4_Art5.html
│       └── ...
│
├── provas-originais/          🗃️ 64 cadernos de prova Quadrix 2025 (base empírica)
└── gabaritos/                 ✅ 10 gabaritos definitivos
```

---

## 🚀 Como usar

### Pré-requisitos
- **Python 3.10+**
- **Google Chrome** (para converter HTML → PDF)
- `pip install -r engine/requirements.txt`

### 1) Gerar um material de estudo (teoria + questões comentadas)

```bash
python engine/gerar_material_html.py
```

Isso escreve um `.html` em `materiais/`. Para virar PDF, renderize com o Chrome:

```bash
chrome --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="materiais/dia04-art5-cf88/Dia4_Art5_PRO.pdf" \
  "materiais/dia04-art5-cf88/Dia4_Art5.html"
```

> No Windows, o executável costuma ficar em
> `C:\Program Files\Google\Chrome\Application\chrome.exe`.

### 2) Gerar uma prova no layout fiel da Quadrix

```bash
python engine/gerar_prova_quadrix.py engine/exemplo_prova.json saida.pdf
```

---

## 🎨 Dois motores, dois propósitos

| Motor | Saída | Quando usar |
|---|---|---|
| **`gerar_prova_quadrix.py`** | PDF que **imita o caderno oficial** da Quadrix (cabeçalho, bandas, duas colunas, caixa de questão) | Treino de **simulado cronometrado** com a cara da prova real |
| **`gerar_material_html.py`** | Material de **estudo** com design moderno (capa, cards de inciso, caixas de pegadinha/macete, gabarito equilibrado) | **Aprender a teoria** e revisar com reconhecimento de padrões |

---

## 🧠 A metodologia (resumo)

O material **não** ensina como uma faculdade (discussão, interpretação aberta). Ensina como a **prova** cobra:

- **Lógica antes de memória** — cada regra vem com o _porquê_ ela existe.
- **A pegadinha é integrada** — mostramos _como a Quadrix arma a armadilha_, para você reconhecê-la.
- **Macete de memória** — um gancho curto para a hora da prova.
- **Questões comentadas** — não só o gabarito, mas a _estratégia de resolução_.
- **Design para reconhecimento** — cores e cards que viram memória visual (🔴 pegadinha · 🟢 macete · 🔵 explicação).

Detalhes em [`docs/metodologia.md`](docs/metodologia.md).

---

## 📊 Base empírica

64 cadernos + 10 gabaritos definitivos da Quadrix 2025, de **10 conselhos**:
CORE-BA, CORE-SP, CORE-RS, CORE-SE, COREN-AC, CONRERP-2ª/SP, CAU-MA, CRA-SP, CRB-1ª/DF e CFP (XV Concurso).

A análise desses cadernos está sistematizada em [`docs/padroes-da-banca.md`](docs/padroes-da-banca.md).

---

## 🗓️ Contexto de estudo

Repositório de apoio à preparação para o concurso **Sedes/DF — Técnico Administrativo (Cargo 202)**, prova em **06/09/2026**.
O plano diário completo (100 dias, 3 fases) está em [`docs/cronograma-estudos.md`](docs/cronograma-estudos.md).

| Fase | Dias | Foco |
|---|---|---|
| 1 — Conteúdo | 1–40 | Todo o edital + questões após cada bloco |
| 2 — Prática | 41–70 | 80% questões, simulados parciais, foco em fraquezas |
| 3 — Simulados | 71–100 | Simulados completos (60q + discursiva) + revisão |

---

## ⚠️ Sobre direitos autorais

As provas e gabaritos em `provas-originais/` e `gabaritos/` pertencem ao **Instituto Quadrix** e aos respectivos órgãos aplicadores. Estão aqui **somente para estudo pessoal e análise de padrões**, sem fins lucrativos. O código e os materiais próprios deste repositório seguem a licença **MIT** (ver [`LICENSE`](LICENSE)).

---

<div align="center">
<sub>Construído para estudar com inteligência — reconhecer padrões, não decorar listas.</sub>
</div>
