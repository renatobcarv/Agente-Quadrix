# -*- coding: utf-8 -*-
"""Material de estudo: Português — Ortografia, Morfossintaxe e Coesão Textual.
Gera HTML profissional (render via Chrome) com teoria + 35 questões comentadas.

Uso:
    python engine/gerar_portugues_morfossintaxe.py
    chrome --headless=new --no-pdf-header-footer --print-to-pdf=saida.pdf arquivo.html
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(_HERE)
OUTDIR = os.path.join(_REPO, "materiais", "dia02-portugues-morfossintaxe")
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "Dia2_Portugues_Morfossintaxe.html")

# ============================================================
# ORTOGRAFIA — pares e regras que mais caem
# ============================================================
ORTO = [
    ("Por que · Porque · Por quê · Porquê",
     "<b>Por que</b> (separado, sem acento) = pergunta ou “pelo qual”. <b>Porque</b> (junto) = resposta/causa. "
     "<b>Por quê</b> (separado, com acento) = fim de frase. <b>Porquê</b> (junto, com acento) = substantivo (“o motivo”).",
     "“<b>Por que</b> você faltou? <b>Porque</b> fiquei doente. Faltei, mas não sei <b>por quê</b>. Ninguém entendeu o <b>porquê</b>.”",
     "A banca troca os quatro. Se vier <b>artigo antes</b> (o, um), é o substantivo <b>porquê</b>. Se for fim de frase, leva acento.",
     "Pergunta = separado · Resposta = junto · Fim de frase = acento."),

    ("Mau × Mal",
     "<b>Mau</b> é adjetivo (oposto de <b>bom</b>). <b>Mal</b> é advérbio (oposto de <b>bem</b>) ou substantivo (“o mal”).",
     "“Ele é um <b>mau</b> aluno (bom).” / “Ele dormiu <b>mal</b> (bem).” / “O <b>mal</b> venceu.”",
     "Troque por <b>bom/bem</b>: se couber “bom” → <b>mau</b>; se couber “bem” → <b>mal</b>.",
     "mAU ↔ bOM · maL ↔ beM (as vogais combinam)."),

    ("Mas × Mais",
     "<b>Mas</b> = conjunção adversativa (= porém). <b>Mais</b> = advérbio de intensidade (oposto de <b>menos</b>).",
     "“Estudei muito, <b>mas</b> não passei.” / “Quero <b>mais</b> tempo.”",
     "Se equivale a <b>porém</b>, é <b>mas</b>. Se for quantidade/intensidade, é <b>mais</b>.",
     "maS = porém · maIs = quantIdade."),

    ("A × Há (tempo)",
     "<b>Há</b> (verbo haver) = tempo <b>passado/decorrido</b> (= faz). <b>A</b> (preposição) = tempo <b>futuro</b> ou distância.",
     "“Cheguei <b>há</b> dois dias (passado).” / “Volto daqui <b>a</b> dois dias (futuro).”",
     "Passado → <b>há</b>. Futuro/distância → <b>a</b>. Nunca use “<b>há</b> atrás” (redundância).",
     "Há = já passou (faz). A = ainda vai."),

    ("Senão × Se não",
     "<b>Senão</b> (junto) = “caso contrário”, “a não ser”, “mas sim”. <b>Se não</b> (separado) = “caso não” (condição).",
     "“Corra, <b>senão</b> perderá o ônibus (caso contrário).” / “<b>Se não</b> chover, sairemos (caso não).”",
     "Se puder trocar por <b>caso não</b>, escreve separado. Se for “caso contrário/a não ser”, junto.",
     "“Caso não” = separado."),

    ("Onde × Aonde",
     "<b>Onde</b> = lugar fixo (verbos sem movimento: estar, ficar). <b>Aonde</b> = lugar com <b>movimento</b> (= a + onde; verbos ir, chegar).",
     "“<b>Onde</b> você mora?” / “<b>Aonde</b> você vai?”",
     "Verbo de movimento (ir, chegar, dirigir-se) pede <b>aonde</b>. A banca usa “aonde você está” (errado).",
     "Movimento → aOnde (tem o ‘a’ de ‘ação’)."),

    ("Acerca de · Há cerca de · A cerca de",
     "<b>Acerca de</b> = sobre, a respeito de. <b>Há cerca de</b> = faz aproximadamente (tempo). <b>A cerca de</b> = a uma distância aproximada.",
     "“Falamos <b>acerca de</b> política.” / “Saiu <b>há cerca de</b> uma hora.” / “Fica <b>a cerca de</b> 3 km.”",
     "“a respeito de” = <b>acerca de</b>. Tempo decorrido = <b>há cerca de</b> (verbo haver).",
     "Acerca = Assunto."),

    ("Afim × A fim de",
     "<b>Afim</b> (adjetivo) = semelhante, que tem afinidade. <b>A fim de</b> (locução) = com a finalidade de / com vontade de.",
     "“São áreas <b>afins</b> (semelhantes).” / “Estudo <b>a fim de</b> passar (para).”",
     "Se equivale a <b>para</b>/finalidade, é <b>a fim de</b> (separado).",
     "Finalidade = a Fim de (Para)."),

    ("Sessão · Seção/Secção · Cessão",
     "<b>Sessão</b> = período de tempo (reunião, cinema). <b>Seção/Secção</b> = divisão, repartição. <b>Cessão</b> = ato de ceder.",
     "“<b>Sessão</b> de cinema.” / “<b>Seção</b> de esportes do jornal.” / “<b>Cessão</b> de direitos.”",
     "Reunião/tempo = <b>Sessão</b>. Parte/divisão = <b>Seção</b>. Ceder = <b>Cessão</b>.",
     "Sessão = teSSão de tempo · Cessão = Ceder."),

    ("Acentuação (Acordo Ortográfico)",
     "Paroxítonas com ditongos abertos <b>éi/ói</b> perderam o acento (<b>ideia, heroico, jiboia</b>). Hiatos <b>oo/ee</b> sem acento (<b>voo, creem, leem</b>). "
     "O <b>trema</b> foi abolido. Mantêm-se os acentos diferenciais <b>pôde</b> (passado) × pode, <b>pôr</b> (verbo) × por.",
     "“A <b>ideia</b> do <b>voo</b> foi <b>heroica</b>.” / “Ele <b>pôde</b> ontem o que não <b>pode</b> hoje.”",
     "A banca cobra “idéia/heróico/vôo” (grafia antiga = erradas hoje) e o diferencial <b>pôde × pode</b>.",
     "Ditongo aberto em paroxítona: sem acento (ideia)."),
]

# ============================================================
# MORFOSSINTAXE — conceitos-chave
# ============================================================
MORFO = [
    ("Frase · Oração · Período",
     "<b>Frase</b>: enunciado com sentido (pode não ter verbo: “Fogo!”). <b>Oração</b>: tem <b>verbo</b>. "
     "<b>Período</b>: frase com uma (simples) ou mais orações (composto). Conta-se uma oração por verbo/locução.",
     "“Que susto!” (frase sem verbo) · “Estudo.” (período simples) · “Estudo porque quero passar.” (período composto: 2 verbos).",
     "Conte os <b>verbos</b> para achar quantas orações há. Locução verbal (“vou estudar”) conta como <b>uma</b> oração.",
     "1 verbo (ou locução) = 1 oração."),

    ("Sujeito — tipos",
     "<b>Simples</b> (1 núcleo), <b>Composto</b> (2+ núcleos), <b>Oculto/elíptico</b> (desinência), "
     "<b>Indeterminado</b> (verbo na 3ª pl. sem referente, ou VTI + <b>se</b>), <b>Oração sem sujeito</b> (haver=existir, fazer/ser de tempo, fenômenos da natureza).",
     "“<b>Os alunos</b> chegaram.” (simples) · “Chegamos.” (oculto: nós) · “Roubaram o banco.” (indeterminado) · “<b>Havia</b> erros.” (sem sujeito).",
     "“<b>Há</b> pessoas” NÃO tem sujeito — “pessoas” é <b>objeto direto</b>. Trocar por “existir” mostra o erro de concordância (<b>haver</b> fica no singular).",
     "Haver = existir → impessoal, fica no singular."),

    ("Predicado — tipos",
     "<b>Verbal</b> (núcleo é verbo de ação). <b>Nominal</b> (verbo de ligação + <b>predicativo do sujeito</b>). "
     "<b>Verbo-nominal</b> (ação + predicativo).",
     "“Ela <b>correu</b>.” (verbal) · “Ela <b>está cansada</b>.” (nominal: ‘cansada’ = predicativo) · “Ela <b>chegou cansada</b>.” (verbo-nominal).",
     "Verbo de ligação (ser, estar, parecer, permanecer, ficar, continuar, andar) pede <b>predicativo</b>, não objeto.",
     "VL + estado = predicado nominal."),

    ("Transitividade verbal",
     "<b>VI</b> (intransitivo): sentido completo. <b>VTD</b>: pede objeto <b>direto</b> (sem preposição). "
     "<b>VTI</b>: pede objeto <b>indireto</b> (com preposição). <b>VTDI</b>: os dois. <b>VL</b> (de ligação): liga sujeito a predicativo.",
     "“Ele <b>chegou</b>.” (VI) · “Comprei <b>o livro</b>.” (VTD) · “Gosto <b>de música</b>.” (VTI) · “Dei <b>um presente a ela</b>.” (VTDI).",
     "“Assistir” (=ver) é <b>VTI</b>: “assisti <b>ao</b> filme”. “Obedecer/visar/aspirar(=desejar)” também regem preposição.",
     "Tem preposição obrigatória = objeto indireto (VTI)."),

    ("Adjunto adnominal × Complemento nominal",
     "Ambos vêm com preposição após um nome. <b>Complemento nominal</b> = <b>paciente</b> (alvo da ação/sentido). "
     "<b>Adjunto adnominal</b> = <b>agente</b> ou posse/qualidade. Só nomes <b>abstratos</b> têm complemento nominal.",
     "“A destruição <b>da cidade</b>” → se a cidade <b>foi</b> destruída = complemento nominal (paciente); se a cidade <b>destruiu</b> = adjunto adnominal (agente).",
     "Pergunta clássica da banca. Teste: o termo <b>sofre</b> a ação (CN) ou <b>pratica</b>/possui (adj. adnominal)?",
     "Paciente = Complemento Nominal. Agente/posse = Adjunto Adnominal."),

    ("Termos da oração — mapa",
     "<b>Essenciais</b>: sujeito e predicado. <b>Integrantes</b> (completam): objeto direto, objeto indireto, complemento nominal, agente da passiva. "
     "<b>Acessórios</b>: adjunto adnominal, adjunto adverbial, aposto. À parte: <b>vocativo</b> (chamamento).",
     "“<b>Pedro</b> (sujeito) <b>deu</b> (predicado) <b>um livro</b> (OD) <b>ao amigo</b> (OI) <b>ontem</b> (adj. adverbial).”",
     "<b>Vocativo</b> não pertence à oração (é um chamamento, isolado por vírgula): “<b>João</b>, venha!”. Não confundir com sujeito.",
     "Vocativo = chamar alguém (vírgula isola)."),

    ("Período composto — coordenação × subordinação",
     "<b>Coordenadas</b>: orações independentes (aditiva: e; adversativa: mas; alternativa: ou; conclusiva: logo, portanto; explicativa: pois). "
     "<b>Subordinadas</b>: dependem da principal — <b>substantivas</b> (função de nome), <b>adjetivas</b> (função de adjetivo, iniciadas por relativo), <b>adverbiais</b> (circunstância).",
     "“Estudei, <b>mas</b> não passei.” (coord. adversativa) · “Espero <b>que você venha</b>.” (sub. substantiva) · “O livro <b>que comprei</b>…” (sub. adjetiva).",
     "Conjunção <b>integrante</b> (que/se) inicia <b>substantiva</b>; pronome <b>relativo</b> (que/o qual/cujo) inicia <b>adjetiva</b>.",
     "Relativo (retoma nome) = adjetiva · Integrante (completa verbo) = substantiva."),

    ("Os valores do “QUE”",
     "<b>Pronome relativo</b> (retoma um nome, = ‘o qual’): “o livro <b>que</b> li”. <b>Conjunção integrante</b> (introduz substantiva): “Disse <b>que</b> viria”. "
     "<b>Conj. subordinativa</b> (causal/consecutiva): “tão alto <b>que</b> caiu”. <b>Substantivo</b>: “um <b>quê</b> de mistério”. <b>Partícula expletiva</b> (realce): “Quase <b>que</b> não vim”.",
     "Teste do relativo: substitua por <b>o qual / a qual</b>. Se couber, é pronome relativo.",
     "Banca adora pedir o valor do “que”. Se vier após substantivo e puder virar “o qual”, é <b>relativo</b> (inicia adjetiva).",
     "Cabe ‘o qual’? → pronome relativo."),

    ("Os valores do “SE”",
     "<b>Conj. integrante</b>: “Não sei <b>se</b> virá”. <b>Conj. condicional</b>: “<b>Se</b> chover, fico”. "
     "<b>Pronome apassivador</b> (com VTD, há sujeito): “Vendem-<b>se</b> casas” (=casas são vendidas). "
     "<b>Índice de indeterminação do sujeito</b> (com VTI/VI, verbo no singular): “Precisa-<b>se</b> de pedreiros”. <b>Pronome reflexivo</b>: “Ele se feriu”.",
     "“Aluga-<b>se</b> salas” → VTD, ‘salas’ é <b>sujeito</b> (apassivador) → verbo concorda: “Alugam-se salas”.",
     "VTD + se = apassivador (verbo concorda com o sujeito). VTI/VI + se = IIS (verbo fica no singular).",
     "VTD→apassivador (plural) · VTI→indeterminação (singular)."),

    ("Classes de palavras (10)",
     "<b>Variáveis</b>: substantivo, artigo, adjetivo, numeral, pronome, verbo. <b>Invariáveis</b>: advérbio, preposição, conjunção, interjeição. "
     "A função muda conforme o contexto: a mesma palavra pode ser de classes diferentes.",
     "“O <b>jantar</b> (substantivo) está pronto.” × “Vamos <b>jantar</b> (verbo).” · “Ele fala <b>bem</b> (advérbio).”",
     "A banca destaca uma palavra e pede a classe <b>naquele contexto</b>. ‘Que’, ‘a’, ‘como’ e ‘se’ mudam de classe.",
     "Classe depende do contexto, não da palavra isolada."),
]

# ============================================================
# COESÃO TEXTUAL — teoria
# ============================================================
CONECTIVOS = [
    ("Adição", "e, também, não só… mas também, além disso, ademais"),
    ("Oposição / Adversidade", "mas, porém, contudo, todavia, entretanto, no entanto"),
    ("Concessão", "embora, ainda que, mesmo que, conquanto, apesar de"),
    ("Conclusão", "portanto, logo, por isso, assim, então, pois (após o verbo)"),
    ("Causa", "porque, pois (antes do verbo), já que, visto que, uma vez que"),
    ("Consequência", "tão/tanto… que, de modo que, de sorte que"),
    ("Condição", "se, caso, contanto que, desde que, a menos que, salvo se"),
    ("Finalidade", "para que, a fim de que, com o intuito de"),
    ("Conformidade", "conforme, segundo, consoante, como"),
    ("Proporção", "à medida que, à proporção que, quanto mais… mais"),
    ("Tempo", "quando, enquanto, assim que, logo que, antes que, depois que"),
    ("Explicação", "que, porque, pois, porquanto"),
]

# ============================================================
# 35 QUESTÕES DE MORFOSSINTAXE — gabarito variado A–E
# (tema, enunciado, [A..E], índice_correto, comentário)
# ============================================================
Q = [
    ("Tipo de sujeito", "Em “Faltaram dois funcionários à reunião”, o termo destacado “dois funcionários” exerce a função de:",
     ["Objeto direto", "Sujeito simples", "Adjunto adverbial", "Complemento nominal", "Predicativo do sujeito"],
     1, "‘Faltar’ é VI; quem falta, falta — ‘dois funcionários’ é quem pratica = sujeito. O verbo concorda com ele (Faltaram). PEGADINHA: achar que é objeto."),

    ("Oração sem sujeito", "Na frase “Havia muitos problemas na empresa”, é correto afirmar que:",
     ["‘muitos problemas’ é o sujeito do verbo haver", "o verbo deveria ir para o plural: ‘Haviam’", "a oração não tem sujeito; ‘muitos problemas’ é objeto direto", "‘na empresa’ é o sujeito", "o sujeito é indeterminado"],
     2, "‘Haver’ = existir é impessoal: oração SEM sujeito, fica no singular, e ‘muitos problemas’ é objeto direto. PEGADINHA clássica: ‘Haviam’ (errado)."),

    ("Valor do SE", "Em “Precisa-se de bons profissionais”, a palavra “se” é:",
     ["Pronome apassivador", "Conjunção condicional", "Índice de indeterminação do sujeito", "Conjunção integrante", "Pronome reflexivo"],
     2, "‘Precisar de’ é VTI → o ‘se’ é índice de indeterminação do sujeito; o verbo fica no singular. Se fosse VTD (‘Vendem-se casas’), seria apassivador."),

    ("Valor do SE", "Em “Alugam-se salas comerciais”, o “se” é pronome apassivador porque:",
     ["o verbo é intransitivo", "‘salas comerciais’ é o sujeito paciente, com o qual o verbo concorda", "indica condição", "introduz oração substantiva", "indica reflexão do sujeito"],
     1, "VTD ‘alugar’ + se = voz passiva sintética: ‘salas’ é sujeito paciente; por isso o verbo vai ao plural (Alugam-se). Equivale a ‘salas são alugadas’."),

    ("Valor do QUE", "Em “O documento que assinei está válido”, a palavra “que”:",
     ["é conjunção integrante", "é pronome relativo, retomando ‘o documento’", "é advérbio de intensidade", "é partícula expletiva", "é conjunção causal"],
     1, "Cabe trocar por ‘o qual’ (‘o documento o qual assinei’) → pronome relativo; inicia oração subordinada adjetiva. PEGADINHA: confundir com integrante."),

    ("Valor do QUE", "Em “Afirmo que cumprirei o prazo”, o “que” é:",
     ["pronome relativo", "conjunção integrante, introduzindo oração subordinada substantiva", "preposição", "conjunção adversativa", "pronome interrogativo"],
     1, "‘Afirmo [algo]’ — a oração ‘que cumprirei o prazo’ completa o verbo (objeto direto) → conjunção integrante (substantiva). Não cabe ‘o qual’."),

    ("Transitividade verbal", "Em “Os espectadores assistiram ao filme”, o verbo ‘assistir’ é:",
     ["transitivo direto", "intransitivo", "transitivo indireto", "de ligação", "transitivo direto e indireto"],
     2, "‘Assistir’ no sentido de ‘ver’ rege a preposição ‘a’ → VTI (‘assistiram AO filme’). ‘ao filme’ é objeto indireto. PEGADINHA: tratar como VTD."),

    ("Predicado", "Em “O candidato permaneceu tranquilo durante a prova”, o predicado é:",
     ["verbal", "nominal, e ‘tranquilo’ é predicativo do sujeito", "verbo-nominal", "nominal, e ‘tranquilo’ é objeto direto", "verbal, e ‘tranquilo’ é adjunto adverbial"],
     1, "‘Permanecer’ é verbo de ligação (estado); ‘tranquilo’ é predicativo do sujeito → predicado nominal. VL não tem objeto."),

    ("Função sintática", "Em “Entreguei o relatório ao diretor”, os termos ‘o relatório’ e ‘ao diretor’ são, respectivamente:",
     ["sujeito e objeto direto", "objeto direto e objeto indireto", "objeto indireto e objeto direto", "objeto direto e adjunto adverbial", "complemento nominal e objeto direto"],
     1, "‘Entregar’ é VTDI: ‘o relatório’ (sem prep.) = OD; ‘ao diretor’ (com prep.) = OI. Ordem importa."),

    ("Adj. adnominal × Compl. nominal", "Em “A nomeação do servidor ocorreu ontem”, o termo ‘do servidor’ é:",
     ["complemento nominal, pois o servidor sofre a nomeação", "adjunto adnominal de posse", "objeto indireto", "agente da passiva", "adjunto adverbial"],
     0, "O servidor é PACIENTE (foi nomeado) e ‘nomeação’ é nome abstrato → complemento nominal. Se fosse agente (‘a chegada do servidor’), seria adjunto adnominal."),

    ("Vocativo", "Em “Senhores, a sessão está encerrada”, o termo ‘Senhores’ é:",
     ["sujeito", "aposto", "vocativo", "objeto direto", "predicativo"],
     2, "‘Senhores’ é um chamamento, isolado por vírgula, fora da estrutura da oração → vocativo. Não é sujeito (o sujeito é ‘a sessão’)."),

    ("Aposto", "Em “Brasília, capital do país, completou anos”, o termo ‘capital do país’ é:",
     ["vocativo", "aposto explicativo", "sujeito", "adjunto adverbial", "objeto direto"],
     1, "Explica/identifica ‘Brasília’, entre vírgulas → aposto explicativo. Difere do vocativo (que chama o interlocutor)."),

    ("Oração subordinada", "Em “Embora estivesse cansado, terminou o trabalho”, a oração destacada é subordinada adverbial:",
     ["causal", "condicional", "concessiva", "temporal", "final"],
     2, "‘Embora’ introduz concessão (um obstáculo que não impede o fato) → adverbial concessiva. PEGADINHA: confundir com causal (‘porque’)."),

    ("Oração coordenada", "Em “Estudou muito, portanto merece passar”, a segunda oração é coordenada sindética:",
     ["aditiva", "adversativa", "alternativa", "conclusiva", "explicativa"],
     3, "‘Portanto’ indica conclusão → coordenada sindética conclusiva. Sentido de consequência lógica do que se afirmou antes."),

    ("Coesão — conectivo", "“O prazo terminou; ____, ninguém foi penalizado.” A lacuna, para indicar OPOSIÇÃO, é preenchida por:",
     ["portanto", "porque", "no entanto", "à medida que", "assim que"],
     2, "Há contraste (terminou, mas não houve punição) → conectivo adversativo ‘no entanto’. ‘Portanto’ daria conclusão (errado)."),

    ("Coesão — conectivo", "Assinale a opção em que o conectivo destacado exprime CONCLUSÃO:",
     ["Saiu cedo PORQUE estava cansado.", "EMBORA chovesse, saiu.", "Estudou; LOGO, foi aprovado.", "Fez tudo CONFORME pediram.", "Chegou ASSIM QUE pôde."],
     2, "‘Logo’ = conclusão. ‘Porque’=causa, ‘embora’=concessão, ‘conforme’=conformidade, ‘assim que’=tempo."),

    ("Coesão referencial", "Em “Maria comprou um livro e o leu num dia”, o pronome ‘o’ retoma:",
     ["Maria", "um livro", "um dia", "comprou", "leu"],
     1, "‘o’ é pronome anafórico que retoma ‘um livro’ (coesão referencial por substituição pronominal). Garante economia e ligação entre as orações."),

    ("Classe de palavra", "Em “Ele chegou bem cedo”, a palavra ‘bem’ pertence à classe:",
     ["adjetivo", "substantivo", "advérbio", "preposição", "conjunção"],
     2, "‘bem’ intensifica o advérbio ‘cedo’ → advérbio (de intensidade). Invariável. PEGADINHA: tratar como adjetivo."),

    ("Classe de palavra", "Em “O jantar foi servido às oito”, a palavra ‘jantar’ é:",
     ["verbo", "substantivo", "adjetivo", "advérbio", "preposição"],
     1, "Precedida do artigo ‘O’, ‘jantar’ está substantivada → substantivo. A mesma palavra seria verbo em ‘Vamos jantar’. A classe depende do contexto."),

    ("Concordância verbal", "Assinale a frase com concordância CORRETA:",
     ["Houveram muitas reclamações.", "Fazem dois anos que parti.", "Existem soluções viáveis.", "Tratam-se de casos graves.", "Aluga-se casas."],
     2, "‘Existir’ é verbo pessoal e concorda com o sujeito ‘soluções’ → ‘Existem’. As demais erram: haver/fazer impessoais ficam no singular; ‘tratar-se de’ é invariável; ‘alugar-se’ (VTD) vai ao plural."),

    ("Concordância nominal", "Assinale a opção correta quanto à concordância nominal:",
     ["É proibido entrada.", "Seguem anexo os documentos.", "Ela mesma resolveu.", "Bastante pessoas vieram.", "Água é bom para a saúde."],
     2, "‘mesma’ concorda com ‘Ela’ (= ela própria). Erros: ‘proibida a entrada’ (com artigo concorda), ‘anexos’, ‘Bastantes pessoas’ (adjetivo), ‘boa para a saúde’."),

    ("Regência verbal", "Em “Aspiro a um cargo melhor”, o verbo ‘aspirar’:",
     ["é VTD e ‘a um cargo’ é objeto direto", "é VTI (aspirar = almejar) e ‘a um cargo’ é objeto indireto", "é intransitivo", "é de ligação", "exige objeto direto preposicionado"],
     1, "‘Aspirar’ no sentido de ‘desejar/almejar’ é VTI e rege ‘a’ → ‘a um cargo’ é objeto indireto. (Aspirar=cheirar seria VTD.)"),

    ("Voz verbal", "A frase “A proposta foi aprovada pela comissão” está na voz:",
     ["ativa", "passiva analítica, sendo ‘pela comissão’ o agente da passiva", "passiva sintética", "reflexiva", "ativa com sujeito indeterminado"],
     1, "‘ser + particípio’ = voz passiva analítica; ‘pela comissão’ pratica a ação = agente da passiva. Na ativa: ‘A comissão aprovou a proposta’."),

    ("Função do termo", "Em “A casa de Pedro é grande”, o termo ‘de Pedro’ é:",
     ["complemento nominal", "adjunto adnominal (posse)", "objeto indireto", "agente da passiva", "aposto"],
     1, "Indica posse e liga-se a nome concreto (‘casa’) → adjunto adnominal. Nome concreto não admite complemento nominal."),

    ("Pronome relativo CUJO", "Assinale o emprego correto de ‘cujo’:",
     ["O autor cujo li o livro.", "O autor cujo o livro li.", "O autor cujo livro li.", "O autor que o livro li.", "O autor de cujo livro."],
     2, "‘cujo’ indica posse e NÃO admite artigo depois: ‘O autor cujo livro li’ (= o livro do autor). Concorda com o termo possuído (livro)."),

    ("Sujeito indeterminado", "Em “Telefonaram para você hoje”, o sujeito é:",
     ["simples: ‘você’", "oculto: eles", "indeterminado", "inexistente (oração sem sujeito)", "‘para você’"],
     2, "Verbo na 3ª pessoa do plural sem referente identificável → sujeito indeterminado. Não se sabe quem telefonou."),

    ("Predicativo do objeto", "Em “O júri considerou o réu inocente”, o termo ‘inocente’ é:",
     ["adjunto adnominal", "predicativo do objeto", "objeto direto", "aposto", "complemento nominal"],
     1, "‘inocente’ atribui qualidade ao objeto ‘o réu’ → predicativo do objeto (predicado verbo-nominal). Quem considera, considera alguém [como] algo."),

    ("Locução adjetiva", "A locução ‘de manhã’ em “reunião de manhã” equivale ao adjetivo:",
     ["matinal", "noturno", "diário", "mensal", "anual"],
     0, "‘de manhã’ = matinal → locução adjetiva (preposição + substantivo com valor de adjetivo). Funciona como adjunto adnominal de ‘reunião’."),

    ("Classe — porquê", "Em “Ninguém entendeu o porquê da decisão”, a palavra ‘porquê’ é:",
     ["conjunção", "advérbio", "substantivo", "preposição", "pronome"],
     2, "Precedido do artigo ‘o’, ‘porquê’ é substantivo (= o motivo) e por isso vem junto e acentuado. A presença do artigo é a pista."),

    ("Oração subordinada substantiva", "Em “É necessário que todos colaborem”, a oração destacada é subordinada substantiva:",
     ["subjetiva (funciona como sujeito)", "objetiva direta", "completiva nominal", "predicativa", "apositiva"],
     0, "‘que todos colaborem’ é o sujeito de ‘É necessário’ → subordinada substantiva subjetiva. Teste: ‘Isso é necessário’ — ‘isso’ = a oração."),

    ("Crase", "Assinale a frase em que o uso do acento grave (crase) está CORRETO:",
     ["Refiro-me à você.", "Cheguei à Brasília.", "Entreguei o livro à secretária.", "Ando à pé.", "Falei à respeito disso."],
     2, "‘Entregar a’ + ‘a secretária’ (palavra feminina) = à. Erros: ‘a você’ (pronome não admite), ‘a Brasília’ (cidade sem artigo), ‘a pé’ (palavra masculina), ‘a respeito’ (masculina)."),

    ("Colocação pronominal", "Assinale a colocação pronominal correta:",
     ["Me diga a verdade.", "Não diga-me mentiras.", "Nunca se esqueça disso.", "Tudo resolveu-se.", "Quem disse-te isso?"],
     2, "Palavra atrativa (‘Nunca’) exige próclise: ‘se esqueça’. Erros: início de frase com átono, negação/‘quem’/‘tudo’ atraem o pronome (próclise obrigatória)."),

    ("Função sintática do termo", "Em “Gosto muito de poesia”, o termo ‘de poesia’ é:",
     ["objeto direto", "objeto indireto", "complemento nominal", "adjunto adverbial", "predicativo"],
     1, "‘Gostar’ é VTI (gostar DE algo) → ‘de poesia’ é objeto indireto (completa um VERBO). Se completasse um nome, seria complemento nominal."),

    ("Conjunção — valor", "Em “Não foi à aula, pois estava doente”, a conjunção ‘pois’ tem valor:",
     ["conclusivo", "explicativo/causal", "adversativo", "temporal", "condicional"],
     1, "‘pois’ ANTES (aqui equivale a ‘porque’) exprime causa/explicação. Se viesse depois do verbo (‘Estava doente; não foi, pois, à aula’), seria conclusivo."),

    ("Período — nº de orações", "Quantas orações há em “Quando cheguei, todos já tinham saído”?",
     ["Uma", "Duas", "Três", "Quatro", "Nenhuma"],
     1, "Conta-se uma oração por verbo OU locução verbal: ‘cheguei’ (1) e ‘tinham saído’ (locução = 1) → duas orações. PEGADINHA: contar a locução ‘tinham saído’ como dois verbos."),
]


def render_card(it, accent_tags=True):
    tit, expl, ex, peg, mac = it
    return f"""
    <div class="card">
      <div class="head"><span class="tit">{tit}</span></div>
      <div class="block"><span class="tag t-trad">Como funciona</span><br>{expl}</div>
      <div class="row">
        <div class="block"><span class="tag t-ex">Exemplo</span><br>{ex}</div>
        <div class="block peg"><span class="tag t-peg">Pegadinha Quadrix</span><br>{peg}</div>
      </div>
      <div class="block mac"><span class="tag t-mac">Macete</span> &nbsp;{mac}</div>
    </div>"""


def render_q(i, q):
    tema, enun, opts, ok, com = q
    lis = "".join(f'<li class="{"ok" if j==ok else ""}">{o}</li>' for j, o in enumerate(opts))
    letra = "ABCDE"[ok]
    return f"""
    <div class="q">
      <div class="tema">{tema}</div>
      <div class="qh"><span class="qn">Questão {i}.</span> {enun}</div>
      <ol>{lis}</ol>
      <div class="com"><b class="g">Gabarito: {letra}.</b> {com}</div>
    </div>"""


def render_gabarito():
    cells = "".join(f'<div class="cell">{i}<b> {"ABCDE"[q[3]]}</b></div>' for i, q in enumerate(Q, 1))
    from collections import Counter
    cnt = Counter("ABCDE"[q[3]] for q in Q)
    dist = " · ".join(f"{k}: {cnt.get(k,0)}" for k in "ABCDE")
    return f"""
    <div class="gabarito">
      <h3>Gabarito — 35 questões</h3>
      <div class="grid">{cells}</div>
      <div class="note">Distribuição das respostas — {dist}.</div>
    </div>"""


CSS = """
@page { size: A4; margin: 14mm 13mm 16mm 13mm; }
* { box-sizing: border-box; }
body { font-family: 'Segoe UI','Helvetica Neue',Arial,sans-serif; color:#1f2733; font-size:10.2px; line-height:1.5; margin:0;
  -webkit-print-color-adjust: exact; print-color-adjust: exact; }
h1,h2,h3,h4 { margin:0; font-weight:700; }
.cover { height:252mm; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;
  background: linear-gradient(135deg,#13235e 0%,#1d4ed8 55%,#16307a 100%); color:#fff; border-radius:6px;
  page-break-after: always; padding:0 24mm; }
.cover .kicker { letter-spacing:4px; font-size:12px; opacity:.85; font-weight:600; }
.cover h1 { font-size:44px; line-height:1.05; margin:10px 0 6px; }
.cover .sub { font-size:16px; font-weight:400; opacity:.95; max-width:135mm; }
.cover .rule { width:70px; height:4px; background:#ffd27a; margin:22px 0; border-radius:2px; }
.cover .meta { font-size:12.5px; opacity:.9; line-height:1.7; }
.cover .badge { margin-top:26px; background:rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.4);
  padding:9px 18px; border-radius:40px; font-size:13px; font-weight:600; }
.section-title { font-size:19px; color:#1d4ed8; border-bottom:3px solid #1d4ed8; padding-bottom:5px; margin:4px 0 12px; page-break-after: avoid; }
.lead { font-size:11px; color:#3a4658; margin-bottom:10px; }
.grid2 { display:grid; grid-template-columns:1fr 1fr; gap:9px; }
.callout { border-radius:7px; padding:9px 11px; margin:7px 0; page-break-inside: avoid; }
.c-why { background:#fff5f5; border-left:4px solid #c0392b; }
.c-key { background:#eefaf1; border-left:4px solid #1f9d57; }
.c-tip { background:#eef4ff; border-left:4px solid #1d4ed8; }
.callout h4 { font-size:11px; margin-bottom:4px; text-transform:uppercase; letter-spacing:.5px; }
.c-why h4 { color:#c0392b; } .c-key h4 { color:#1f9d57; } .c-tip h4 { color:#1d4ed8; }
.callout ul { margin:3px 0 0; padding-left:16px; } .callout li { margin:2px 0; }
.card { border:1px solid #e2e6ee; border-radius:9px; padding:11px 13px; margin:0 0 11px; page-break-inside: avoid;
  background:#fff; box-shadow:0 1px 2px rgba(20,30,50,.04); }
.card .head { display:flex; align-items:center; gap:9px; margin-bottom:6px; }
.card .tit { font-size:12.5px; color:#13235e; font-weight:700; border-left:4px solid #1d4ed8; padding-left:8px; }
.card .row { display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-top:5px; }
.tag { font-weight:700; font-size:9px; text-transform:uppercase; letter-spacing:.4px; }
.t-trad { color:#1d4ed8; } .t-ex { color:#7a5c00; } .t-peg { color:#c0392b; } .t-mac { color:#1f9d57; }
.block { margin-top:4px; }
.block.peg { background:#fff5f5; border-radius:5px; padding:6px 8px; }
.block.mac { background:#eefaf1; border-radius:5px; padding:6px 8px; }
table { width:100%; border-collapse:collapse; margin:6px 0 4px; font-size:9.5px; page-break-inside: avoid; }
th { background:#13235e; color:#fff; text-align:left; padding:6px 7px; font-size:9.5px; }
td { border:1px solid #e2e6ee; padding:6px 7px; vertical-align:top; }
tr:nth-child(even) td { background:#f7f9fc; }
td .rn { font-weight:700; color:#1d4ed8; }
.q { border:1px solid #e2e6ee; border-radius:8px; padding:9px 11px; margin:0 0 9px; page-break-inside: avoid; }
.q .qh { font-size:10.5px; font-weight:700; color:#1f2733; margin-bottom:5px; }
.q .qh .qn { color:#1d4ed8; }
.q .tema { display:inline-block; background:#eef0f5; color:#56627a; font-size:8.3px; font-weight:700; text-transform:uppercase;
  letter-spacing:.4px; padding:2px 7px; border-radius:20px; margin-bottom:5px; }
.q ol { margin:4px 0 0; padding-left:0; list-style:none; counter-reset:opt; }
.q ol li { counter-increment:opt; margin:2.5px 0; padding-left:20px; position:relative; font-size:9.6px; }
.q ol li::before { content: counter(opt, upper-alpha); position:absolute; left:0; top:0; font-weight:700; color:#56627a; }
.q ol li.ok::before { color:#1f9d57; }
.q ol li.ok { background:#eefaf1; border-radius:4px; }
.q .com { margin-top:6px; font-size:9.1px; color:#46536a; background:#fafbfd; border-left:3px solid #1f9d57; border-radius:4px; padding:5px 8px; }
.q .com b.g { color:#1f9d57; }
.gabarito { background:#13235e; color:#fff; border-radius:9px; padding:14px 16px; page-break-inside: avoid; }
.gabarito h3 { color:#ffd27a; font-size:14px; margin-bottom:8px; }
.gabarito .grid { display:grid; grid-template-columns:repeat(7,1fr); gap:5px; }
.gabarito .cell { background:rgba(255,255,255,.08); border-radius:5px; text-align:center; padding:5px 0; font-size:9.5px; }
.gabarito .cell b { color:#ffd27a; }
.note { font-size:8.6px; color:#9fb0d0; margin-top:8px; }
.h-chapter { page-break-before: always; }
"""

orto_html = "".join(render_card(c) for c in ORTO)
morfo_html = "".join(render_card(c) for c in MORFO)
conectivos_rows = "".join(
    f"<tr><td><span class='rn'>{sentido}</span></td><td>{lista}</td></tr>" for (sentido, lista) in CONECTIVOS
)
questoes_html = "".join(render_q(i, q) for i, q in enumerate(Q, 1))

HTML = f"""<!DOCTYPE html>
<html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head>
<body>

<div class="cover">
  <div class="kicker">LÍNGUA PORTUGUESA</div>
  <h1>Ortografia,<br>Morfossintaxe<br>&amp; Coesão</h1>
  <div class="rule"></div>
  <div class="sub">Regras que mais caem, análise sintática sem decoreba e 35 questões de morfossintaxe comentadas</div>
  <div class="meta" style="margin-top:26px;">Concurso <b>Sedes/DF</b> · Banca <b>Quadrix</b> · 2026<br>Técnico Administrativo (Cargo 202)</div>
  <div class="badge">Português · Meta: 35 questões</div>
</div>

<!-- 1. ABERTURA -->
<h2 class="section-title">1. Por que Português decide a prova</h2>
<p class="lead">Português é a matéria com mais questões e a que mais elimina por descuido. A Quadrix cobra <b>regra aplicada</b>, não teoria: identificar a função de um termo, o valor de uma palavra (‘que’, ‘se’), o sentido de um conectivo. Quem domina morfossintaxe acerta também concordância, regência, crase e pontuação — tudo depende de enxergar a <b>estrutura da frase</b>.</p>
<div class="grid2">
  <div class="callout c-why">
    <h4>Onde o candidato perde ponto</h4>
    <ul>
      <li><b>Decora nomenclatura</b> sem saber identificar na frase real.</li>
      <li><b>Erra o valor da palavra</b> — o mesmo ‘se’/‘que’ muda de função conforme o contexto.</li>
      <li><b>Confunde conectivos</b> — troca causa por conclusão, oposição por adição.</li>
      <li><b>Ignora a regência</b> — ‘assistir’, ‘aspirar’, ‘visar’ mudam de sentido com a preposição.</li>
    </ul>
  </div>
  <div class="callout c-key">
    <h4>A estratégia deste material</h4>
    <ul>
      <li><b>Testes práticos</b>: troque por ‘o qual’, por ‘bom/bem’, por ‘porém’ — e a resposta aparece.</li>
      <li><b>Morfossintaxe como mapa</b>: achar o verbo → achar o sujeito → classificar o resto.</li>
      <li><b>Coesão</b> ensinada pelo sentido do conectivo, não pela lista decorada.</li>
      <li>35 questões no estilo da banca, comentadas com a <b>estratégia de resolução</b>.</li>
    </ul>
  </div>
</div>

<!-- 2. ORTOGRAFIA -->
<h2 class="section-title h-chapter">2. Ortografia — os pares que mais caem</h2>
<p class="lead">A banca adora as palavras parônimas (parecidas) e a acentuação do Novo Acordo. Cada card traz o teste rápido para não errar.</p>
{orto_html}

<!-- 3. MORFOSSINTAXE -->
<h2 class="section-title h-chapter">3. Morfossintaxe — a estrutura da frase</h2>
<p class="lead">Morfologia = a <b>classe</b> da palavra. Sintaxe = a <b>função</b> dela na oração. Morfossintaxe junta as duas: a mesma palavra muda de classe e de função conforme o contexto. O caminho seguro: ache o <b>verbo</b>, descubra sua <b>transitividade</b>, ache o <b>sujeito</b>, classifique o resto.</p>
{morfo_html}

<!-- 4. COESAO -->
<h2 class="section-title h-chapter">4. Coesão Textual</h2>
<p class="lead"><b>Coesão</b> é a amarração entre as partes do texto (a “costura” gramatical). Não confunda com <b>coerência</b> (a lógica de sentido). Um texto pode estar coeso e incoerente. A coesão tem dois grandes tipos: <b>referencial</b> (retomar termos) e <b>sequencial</b> (ligar ideias com conectivos).</p>

<div class="grid2">
  <div class="callout c-tip">
    <h4>Coesão referencial (retomada)</h4>
    <ul>
      <li><b>Anáfora</b>: retoma termo já dito (“Comprei um livro e <b>o</b> li”).</li>
      <li><b>Catáfora</b>: antecipa o que vem (“Só quero <b>isto</b>: paz”).</li>
      <li><b>Elipse</b>: omite termo recuperável (“João entrou e [ele] sentou”).</li>
      <li><b>Substituição lexical</b>: sinônimo/hiperônimo (“o cão… o <b>animal</b>”).</li>
    </ul>
  </div>
  <div class="callout c-tip">
    <h4>Coesão sequencial (conexão)</h4>
    <ul>
      <li>Feita por <b>conjunções, advérbios e preposições</b> que ligam orações e parágrafos.</li>
      <li>O conectivo <b>determina a relação de sentido</b> — trocá-lo muda o texto.</li>
      <li><b>Pegadinha:</b> a banca substitui o conectivo por outro de sentido diferente e pede se o sentido se mantém.</li>
    </ul>
  </div>
</div>

<div class="card">
  <div class="head"><span class="tit">Conectivos por sentido (decore a relação, não a lista)</span></div>
  <table>
    <thead><tr><th style="width:26%">Relação</th><th>Principais conectivos</th></tr></thead>
    <tbody>{conectivos_rows}</tbody>
  </table>
</div>
<div class="callout c-why">
  <h4>Pegadinhas de coesão preferidas da Quadrix</h4>
  <ul>
    <li><b>‘pois’</b> antes do verbo = causa/explicação; depois do verbo = conclusão. (“Estava doente, <b>pois</b> faltou” × “Faltou; estava, <b>pois</b>, doente”.)</li>
    <li><b>‘mas’/‘porém’</b> = oposição; trocar por ‘e’ (adição) altera o sentido.</li>
    <li><b>‘portanto’</b> (conclusão) ≠ <b>‘porque’</b> (causa). A banca inverte os dois.</li>
    <li>Pronome retomando o <b>referente errado</b>: confira sempre a quem o ‘ele/o/que’ se refere.</li>
  </ul>
</div>

<!-- 5. QUESTOES -->
<h2 class="section-title h-chapter">5. 35 Questões de Morfossintaxe</h2>
<p class="lead">Antes de marcar, faça os testes: ache o verbo, classifique a transitividade, teste ‘o qual’ no ‘que’. A correta vem destacada e comentada.</p>
{questoes_html}

<!-- 6. GABARITO -->
<h2 class="section-title h-chapter">6. Gabarito</h2>
{render_gabarito()}

</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("HTML gerado:", OUT)
print("Cards orto:", len(ORTO), "| Cards morfo:", len(MORFO), "| Questoes:", len(Q))
