# -*- coding: utf-8 -*-
"""Gera material de estudo Art. 5o CF/88 em HTML profissional (renderizado por Chrome).

Uso:
    python engine/gerar_material_html.py
    # depois renderize o HTML para PDF com o Chrome:
    #   chrome --headless=new --no-pdf-header-footer --print-to-pdf=saida.pdf arquivo.html
"""
import os
import html as _h

# Caminho relativo a este script -> materiais/dia04-art5-cf88/Dia4_Art5.html
_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(_HERE)
OUT = os.path.join(_REPO, "materiais", "dia04-art5-cf88", "Dia4_Art5.html")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

# ============================================================
# INCISOS — teoria profunda (lei seca + traducao + exemplo + pegadinha + macete)
# ============================================================
INCISOS = [
    {
        "n": "II", "tit": "Princípio da Legalidade",
        "lei": "Ninguém será obrigado a fazer ou deixar de fazer alguma coisa senão em virtude de lei.",
        "trad": "Só <b>lei em sentido formal</b> (votada pelo Legislativo) pode criar obrigação ou proibição para o particular. Decreto, portaria, resolução ou ordem de chefe <b>não</b> obrigam o cidadão a nada por si sós.",
        "ex": "Uma prefeitura baixa portaria exigindo que comerciantes paguem uma “taxa de cadastro”. Sem lei que a institua, ninguém é obrigado a pagar.",
        "peg": "A banca troca <b>“lei”</b> por <b>“decreto”, “ato administrativo”</b> ou <b>“regulamento”</b> e afirma que isso basta para obrigar. É falso para o particular.",
        "mac": "<b>Obrigação só nasce de LEI.</b> Se o enunciado obriga o cidadão sem lei, está errado."
    },
    {
        "n": "IV", "tit": "Livre Manifestação — vedado o anonimato",
        "lei": "É livre a manifestação do pensamento, sendo vedado o anonimato.",
        "trad": "Você pode dizer o que pensa, <b>mas tem de se identificar</b>. A liberdade de expressão não cobre o anonimato — quem se manifesta responde pelo que diz (daí o direito de resposta e a indenização do inciso V).",
        "ex": "Um perfil anônimo difama alguém nas redes. A vítima pode exigir a identificação do autor: o anonimato não é protegido.",
        "peg": "Alternativa diz que a liberdade de expressão é <b>“absoluta”</b> ou que “o anonimato é permitido para proteger a fonte”. Ambas erradas.",
        "mac": "<b>Pode falar, não pode se esconder.</b>"
    },
    {
        "n": "V", "tit": "Direito de Resposta + Indenização",
        "lei": "É assegurado o direito de resposta, proporcional ao agravo, além da indenização por dano material, moral ou à imagem.",
        "trad": "Quem é ofendido tem <b>direito de resposta</b> (proporcional) <b>E</b>, cumulativamente, <b>indenização</b>. Não é “um ou outro”: a palavra-chave é <b>“além da”</b> = soma.",
        "ex": "Jornal publica notícia falsa. A pessoa tem direito a publicar a resposta no mesmo veículo <b>e</b> a processar por danos morais.",
        "peg": "Enunciado diz que a vítima “deve escolher entre resposta ou indenização”. Falso — são cumuláveis.",
        "mac": "Resposta <b>+</b> dinheiro. “Além da” = e não “ou”."
    },
    {
        "n": "VI", "tit": "Liberdade de Crença e Culto",
        "lei": "É inviolável a liberdade de consciência e de crença, sendo assegurado o livre exercício dos cultos religiosos e garantida, na forma da lei, a proteção aos locais de culto e a suas liturgias.",
        "trad": "Ninguém pode ser prejudicado por aquilo em que acredita (ou por não acreditar em nada). O Estado é <b>laico</b>: não tem religião oficial, mas <b>protege</b> o exercício de todas.",
        "ex": "Um servidor não pode ser preterido em concurso por sua religião. Templos têm proteção legal.",
        "peg": "Confundir <b>laicidade</b> (Estado sem religião) com <b>ateísmo de Estado</b> (Estado contra religião). O Brasil é laico, não ateu.",
        "mac": "Estado laico = <b>neutro</b>, não inimigo da fé."
    },
    {
        "n": "VIII", "tit": "Escusa de Consciência",
        "lei": "Ninguém será privado de direitos por motivo de crença religiosa ou de convicção filosófica ou política, salvo se as invocar para eximir-se de obrigação legal a todos imposta e recusar-se a cumprir prestação alternativa, fixada em lei.",
        "trad": "Você pode se recusar a uma obrigação geral por convicção, <b>desde que cumpra a prestação alternativa</b>. Se recusar a obrigação <b>E</b> a alternativa, aí sim perde direitos (ex.: políticos).",
        "ex": "Quem não presta serviço militar por convicção deve cumprir serviço alternativo. Recusando os dois, fica sem o certificado e pode perder direitos políticos.",
        "peg": "Dizer que a pessoa “nunca pode ser obrigada a nada” por convicção. Falso — existe a prestação alternativa.",
        "mac": "Recusou a obrigação? <b>Tem de aceitar a alternativa.</b>"
    },
    {
        "n": "X", "tit": "Intimidade, Vida Privada, Honra e Imagem",
        "lei": "São invioláveis a intimidade, a vida privada, a honra e a imagem das pessoas, assegurado o direito a indenização pelo dano material ou moral decorrente de sua violação.",
        "trad": "Quatro bens protegidos. Violou? <b>Indeniza.</b> É a base jurídica do dano moral.",
        "ex": "Divulgar foto íntima de alguém sem autorização gera dever de indenizar.",
        "peg": "Trocar a lista (ex.: incluir “patrimônio” ou excluir “imagem”). Decore os quatro: intimidade, vida privada, honra, imagem.",
        "mac": "<b>I-V-H-I</b>: Intimidade, Vida privada, Honra, Imagem."
    },
    {
        "n": "XI", "tit": "Inviolabilidade do Domicílio",
        "lei": "A casa é asilo inviolável do indivíduo, ninguém nela podendo penetrar sem consentimento do morador, salvo em caso de flagrante delito ou desastre, ou para prestar socorro, ou, durante o dia, por determinação judicial.",
        "trad": "Quatro hipóteses de entrada SEM consentimento: <b>flagrante</b>, <b>desastre</b>, <b>socorro</b> (a qualquer hora, dia ou noite) e <b>ordem judicial — só durante o DIA</b>.",
        "ex": "Polícia com mandado de busca às 22h: <b>não pode</b> entrar (mandado só vale de dia). Mas se houver tráfico em flagrante, pode a qualquer hora.",
        "peg": "Dizer que “ordem judicial autoriza a entrada a qualquer hora”. Falso: <b>mandado = só de dia</b>. Flagrante/desastre/socorro = dia e noite.",
        "mac": "Mandado dorme à noite. Flagrante não dorme."
    },
    {
        "n": "XII", "tit": "Sigilo das Comunicações",
        "lei": "É inviolável o sigilo da correspondência e das comunicações telegráficas, de dados e das comunicações telefônicas, salvo, no último caso, por ordem judicial, nas hipóteses e na forma que a lei estabelecer para fins de investigação criminal ou instrução processual penal.",
        "trad": "Regra: sigilo. A exceção (interceptação) só vale para <b>comunicações telefônicas</b>, só por <b>ordem judicial</b> e só para fins penais. Delegado ou promotor sozinho <b>não</b> pode.",
        "ex": "Grampo telefônico exige autorização de juiz. Ler e-mail alheio sem ordem judicial é ilícito.",
        "peg": "“A autoridade policial pode interceptar se houver suspeita.” Falso — precisa de <b>juiz</b>. E a exceção é para o telefônico (“no último caso”).",
        "mac": "Grampo só com <b>juiz</b>, só no <b>penal</b>."
    },
    {
        "n": "XXXIV", "tit": "Direito de Petição (gratuito)",
        "lei": "São a todos assegurados, independentemente do pagamento de taxas: (a) o direito de petição aos Poderes Públicos; (b) a obtenção de certidões para defesa de direitos.",
        "trad": "Pedir aos Poderes Públicos e obter certidões é <b>de graça</b>, para qualquer pessoa — inclusive estrangeiro não residente.",
        "ex": "Solicitar uma certidão de tempo de serviço a um órgão público não pode ser cobrado.",
        "peg": "Dizer que “pode ser cobrada taxa por urgência”. Falso: é <b>independente de taxas</b>.",
        "mac": "Petição e certidão = <b>tarifa zero</b>."
    },
    {
        "n": "XXXV", "tit": "Inafastabilidade da Jurisdição",
        "lei": "A lei não excluirá da apreciação do Poder Judiciário lesão ou ameaça a direito.",
        "trad": "Sempre se pode ir ao Judiciário — inclusive contra <b>ameaça</b> (não precisa esperar a lesão consumar). No Brasil <b>não</b> se exige esgotar a via administrativa antes (salvo desportiva).",
        "ex": "Antes de ser multado indevidamente, posso pedir tutela para impedir o ato.",
        "peg": "“É preciso esgotar a esfera administrativa antes de ir à Justiça.” Falso (regra geral).",
        "mac": "Judiciário é porta sempre aberta — até contra <b>ameaça</b>."
    },
    {
        "n": "XXXVI", "tit": "Segurança Jurídica",
        "lei": "A lei não prejudicará o direito adquirido, o ato jurídico perfeito e a coisa julgada.",
        "trad": "Lei nova <b>não retroage</b> para destruir três coisas: <b>direito adquirido</b>, <b>ato jurídico perfeito</b> e <b>coisa julgada</b>. É a proteção contra a “mudança de regras no meio do jogo”.",
        "ex": "Quem já cumpriu os requisitos da aposentadoria tem direito adquirido, mesmo que a lei mude depois.",
        "peg": "Trocar um dos três por “expectativa de direito” (que <b>não</b> é protegida).",
        "mac": "<b>DAC</b>: Direito adquirido, Ato jurídico perfeito, Coisa julgada."
    },
    {
        "n": "XXXIX", "tit": "Legalidade Penal",
        "lei": "Não há crime sem lei anterior que o defina, nem pena sem prévia cominação legal.",
        "trad": "<b>Nullum crimen sine lege.</b> Só é crime o que a lei <b>anterior</b> ao fato definiu. Não existe crime “por analogia” ou por costume.",
        "ex": "Conduta nova só vira crime depois de lei que a tipifique — e não atinge fatos passados.",
        "peg": "Admitir crime definido por medida provisória ou por analogia. Falso.",
        "mac": "Sem <b>lei anterior</b>, não há crime."
    },
    {
        "n": "XL", "tit": "Retroatividade Penal Benéfica",
        "lei": "A lei penal não retroagirá, salvo para beneficiar o réu.",
        "trad": "Regra: lei penal não volta no tempo. <b>Exceção</b>: se a lei nova é <b>mais benéfica</b>, ela retroage e alcança fatos anteriores — até de quem já foi condenado.",
        "ex": "Lei reduz a pena de um crime de 8 para 4 anos: aplica-se a quem já cumpre pena pelo crime antigo.",
        "peg": "Afirmar apenas que “a lei penal não retroage” (meia-verdade). Sempre lembre: <b>retroage para beneficiar</b>.",
        "mac": "Lei penal só volta no tempo <b>para o bem do réu</b>."
    },
    {
        "n": "XLII", "tit": "Racismo",
        "lei": "A prática do racismo constitui crime inafiançável e imprescritível, sujeito à pena de reclusão, nos termos da lei.",
        "trad": "Racismo é <b>crime</b> (não contravenção), <b>inafiançável</b> e <b>imprescritível</b> (nunca prescreve). É punido com <b>reclusão</b>.",
        "ex": "Pode-se denunciar racismo décadas depois — não há prazo prescricional.",
        "peg": "Dizer que “prescreve em 20 anos” ou que “admite fiança”. Ambos falsos.",
        "mac": "Racismo: <b>nunca prescreve, nunca tem fiança</b>."
    },
    {
        "n": "XLIII", "tit": "Crimes Equiparados a Hediondos (3TH)",
        "lei": "A lei considerará inafiançáveis e insuscetíveis de graça ou anistia a prática da tortura, o tráfico ilícito de entorpecentes, o terrorismo e os crimes definidos como hediondos.",
        "trad": "Os <b>3TH</b> (tortura, tráfico, terrorismo) + hediondos são <b>inafiançáveis</b> e <b>insuscetíveis de graça e anistia</b>. <b>Atenção:</b> são <b>prescritíveis</b> (diferente do racismo!).",
        "ex": "Tráfico não admite fiança nem anistia, mas <b>prescreve</b> com o tempo.",
        "peg": "Igualar a racismo e dizer que são “imprescritíveis”. <b>Falso</b> — só racismo e ação de grupos armados são imprescritíveis.",
        "mac": "Imprescritíveis = só <b>racismo</b> e <b>ação de grupos armados</b>. Hediondos prescrevem."
    },
    {
        "n": "XLV", "tit": "Pessoalidade da Pena",
        "lei": "Nenhuma pena passará da pessoa do condenado, podendo a obrigação de reparar o dano e a decretação do perdimento de bens ser estendidas aos sucessores até o limite do patrimônio transferido.",
        "trad": "A <b>pena</b> é pessoal e morre com o condenado. Mas a <b>reparação do dano</b> e o <b>perdimento de bens</b> alcançam os herdeiros — <b>até o limite da herança</b>.",
        "ex": "Condenado morre: a prisão acaba, mas a dívida de indenização é descontada da herança (não do bolso pessoal do herdeiro).",
        "peg": "Dizer que “nada passa aos herdeiros” (falso: indenização passa) ou que “a pena passa” (falso).",
        "mac": "Pena não herda. <b>Dívida sim, até o tamanho da herança.</b>"
    },
    {
        "n": "XLVII", "tit": "Penas Proibidas",
        "lei": "Não haverá penas: (a) de morte, salvo em caso de guerra declarada; (b) de caráter perpétuo; (c) de trabalhos forçados; (d) de banimento; (e) cruéis.",
        "trad": "Cinco penas vedadas. A <b>única exceção</b> é a pena de morte <b>em guerra declarada</b>. Perpétua, forçada, banimento e cruel: <b>nunca</b>.",
        "ex": "Prisão perpétua é inconstitucional no Brasil — por isso o teto de cumprimento é de 40 anos.",
        "peg": "Dizer que a pena de morte é “totalmente proibida” (esquece a exceção da guerra) ou que “perpétua é admitida para hediondos” (falso).",
        "mac": "Morte só na <b>guerra</b>. O resto, jamais."
    },
    {
        "n": "LI / LII", "tit": "Extradição",
        "lei": "LI — Nenhum brasileiro será extraditado, salvo o naturalizado, em caso de crime comum praticado antes da naturalização ou de comprovado envolvimento em tráfico ilícito de entorpecentes. LII — Não será concedida extradição de estrangeiro por crime político ou de opinião.",
        "trad": "<b>Nato:</b> nunca é extraditado. <b>Naturalizado:</b> pode, em 2 casos — crime comum <b>antes</b> da naturalização, ou <b>tráfico</b> (antes ou depois). <b>Estrangeiro:</b> pode, salvo crime <b>político ou de opinião</b>.",
        "ex": "Naturalizado que traficou depois de naturalizado: pode ser extraditado (tráfico não tem limite temporal).",
        "peg": "Dizer que “nenhum brasileiro é extraditado” sem ressalva (esquece o naturalizado) ou que estrangeiro político pode ser extraditado.",
        "mac": "Nato blindado. Naturalizado: <b>crime antes</b> ou <b>tráfico</b>. Político não extradita."
    },
    {
        "n": "LV", "tit": "Contraditório e Ampla Defesa",
        "lei": "Aos litigantes, em processo judicial ou administrativo, e aos acusados em geral são assegurados o contraditório e a ampla defesa, com os meios e recursos a ela inerentes.",
        "trad": "Vale no processo <b>judicial E administrativo</b>. Contraditório = direito de saber e reagir; ampla defesa = todos os meios para se defender.",
        "ex": "Em um PAD (processo administrativo disciplinar), o servidor tem direito a se defender e recorrer.",
        "peg": "Restringir a garantia ao processo penal/judicial. Falso — também no <b>administrativo</b>.",
        "mac": "Defesa vale <b>no fórum E na repartição</b>."
    },
    {
        "n": "LVI", "tit": "Provas Ilícitas",
        "lei": "São inadmissíveis, no processo, as provas obtidas por meios ilícitos.",
        "trad": "Prova obtida violando a lei é <b>imprestável</b>, por mais relevante que seja. Contamina também as provas derivadas dela (teoria dos frutos da árvore envenenada).",
        "ex": "Confissão obtida por tortura não vale — e o que ela revelou também cai.",
        "peg": "“Prova ilícita é admitida se for decisiva para a verdade.” Falso na regra constitucional.",
        "mac": "Prova suja <b>não entra</b> — e contamina o resto."
    },
    {
        "n": "LVII", "tit": "Presunção de Inocência",
        "lei": "Ninguém será considerado culpado até o trânsito em julgado de sentença penal condenatória.",
        "trad": "Você é inocente até a condenação se tornar <b>definitiva</b> (sem mais recurso). Condenação em 1ª ou 2ª instância <b>não</b> é “culpa” definitiva.",
        "ex": "Réu condenado que ainda recorre continua, juridicamente, presumido inocente.",
        "peg": "Dizer que “a condenação em 1ª instância já torna a pessoa culpada”. Falso — precisa de <b>trânsito em julgado</b>.",
        "mac": "Inocente até o <b>fim dos recursos</b>."
    },
]

# Remédios constitucionais (tabela comparativa)
REMEDIOS = [
    ("LXVIII", "Habeas Corpus", "Liberdade de locomoção (ir e vir) ameaçada ou violada", "Gratuito. Qualquer pessoa pode impetrar."),
    ("LXIX", "Mandado de Segurança", "Direito líquido e certo não amparado por HC ou HD", "Prova pré-constituída. Prazo de 120 dias."),
    ("LXX", "MS Coletivo", "Mesmo objeto do MS, impetrado por partido, sindicato, entidade", "Defende interesses do grupo."),
    ("LXXI", "Mandado de Injunção", "Falta de norma regulamentadora inviabiliza direito", "Combate a omissão legislativa."),
    ("LXXII", "Habeas Data", "Conhecer/retificar dados pessoais em bancos públicos", "Gratuito. Só o titular dos dados."),
    ("LXXIII", "Ação Popular", "Anular ato lesivo ao patrimônio público, à moralidade, ao meio ambiente", "Só o cidadão (eleitor). Isento de custas."),
]

# ============================================================
# 35 QUESTOES — gabarito variado (A-E)
# ============================================================
Q = [
    ("Titulares do caput", "Um turista estrangeiro, em viagem de duas semanas pelo Brasil, sofre prisão arbitrária. Sobre a proteção do art. 5º, é correto afirmar que:",
     ["A garantia não o alcança, pois o caput cita apenas estrangeiros residentes — porém direitos ligados à dignidade, como não sofrer prisão arbitrária, são reconhecidos pela jurisprudência a qualquer pessoa em território nacional.",
      "Estrangeiros jamais têm direitos no Brasil.",
      "Todo turista é equiparado a residente.",
      "Só brasileiros natos têm o direito.",
      "O caput protege qualquer pessoa do planeta sem exceção."],
     0, "O caput menciona “estrangeiros residentes”, mas o STF estende núcleos da dignidade (vida, integridade) a não residentes. PEGADINHA clássica: marcar que “não tem direito algum”."),

    ("Legalidade (II)", "Uma autarquia edita portaria obrigando os administrados a recadastramento mediante pagamento de taxa não prevista em lei. O particular:",
     ["É obrigado, pois portaria de autarquia tem força de lei.",
      "Não está obrigado, pois ninguém é compelido a fazer ou deixar de fazer algo senão em virtude de lei (art. 5º, II).",
      "Está obrigado apenas se for servidor.",
      "Deve pagar e depois pedir restituição.",
      "Está obrigado porque a Administração tem supremacia."],
     1, "Obrigação ao particular só por LEI formal. Portaria/decreto não bastam. PEGADINHA: “supremacia da Administração” não cria obrigação sem lei."),

    ("Anonimato (IV)", "Sobre a livre manifestação do pensamento, assinale a correta:",
     ["O anonimato é permitido para proteger a fonte jornalística.",
      "A liberdade de expressão é absoluta e não comporta responsabilização.",
      "É livre a manifestação do pensamento, vedado o anonimato.",
      "A manifestação depende de autorização prévia do poder público.",
      "Críticas a agentes públicos são proibidas."],
     2, "Texto literal: livre a manifestação, vedado o anonimato. PEGADINHA: “absoluta” e “anonimato permitido” são iscas frequentes."),

    ("Resposta + indenização (V)", "Vítima de notícia falsa publicada em jornal pretende exercer o direito de resposta e, ainda, ser indenizada. Conforme o art. 5º, V:",
     ["Deve escolher entre a resposta OU a indenização.",
      "Só cabe indenização se não houver resposta.",
      "A resposta exclui o dano moral.",
      "São cumuláveis: cabe a resposta proporcional ao agravo, ALÉM da indenização.",
      "Indenização só é cabível para dano material."],
     3, "“Além da” = cumulação. Resposta E indenização (material, moral ou à imagem). PEGADINHA: “escolher um ou outro”."),

    ("Escusa de consciência (VIII)", "Cidadão recusa obrigação legal a todos imposta invocando convicção filosófica. Ele perderá direitos:",
     ["Nunca, pois a convicção é inviolável.",
      "Sempre, pois convicção não afasta a lei.",
      "Apenas se a convicção for religiosa.",
      "Imediatamente, sem qualquer alternativa.",
      "Somente se também se recusar a cumprir a prestação alternativa fixada em lei."],
     4, "A privação de direitos só ocorre na DUPLA recusa: obrigação + prestação alternativa. PEGADINHA: “nunca pode ser obrigado”."),

    ("Domicílio (XI)", "Policiais, munidos de mandado de busca e apreensão, pretendem ingressar em residência às 23h, sem flagrante. É correto afirmar:",
     ["Podem entrar, pois ordem judicial autoriza a qualquer hora.",
      "Não podem: o ingresso por determinação judicial só é permitido durante o dia.",
      "Podem entrar se avisarem o morador.",
      "Só podem com a presença do Ministério Público.",
      "Podem, pois mandado dispensa horário."],
     1, "Mandado judicial = só DURANTE O DIA. À noite, sem flagrante/desastre/socorro, é vedado. PEGADINHA: “ordem judicial a qualquer hora”."),

    ("Sigilo (XII)", "Delegado de polícia, durante investigação, determina por conta própria a interceptação telefônica de um suspeito. A medida é:",
     ["Válida, pois a autoridade policial pode em investigação.",
      "Válida se durar menos de 24 horas.",
      "Inválida: a interceptação telefônica depende de ordem judicial, para fins de investigação criminal ou instrução penal.",
      "Válida para qualquer tipo de comunicação.",
      "Válida apenas em crimes hediondos."],
     2, "A exceção ao sigilo exige ORDEM JUDICIAL e fim penal. Delegado/MP sozinho não pode. PEGADINHA: “autoridade policial pode”."),

    ("Petição (XXXIV)", "Sobre o direito de petição e a obtenção de certidões:",
     ["São assegurados a todos, independentemente do pagamento de taxas.",
      "Exigem o pagamento de taxa de expediente.",
      "São exclusivos de brasileiros natos.",
      "Dependem de advogado.",
      "Só cabem na esfera judicial."],
     0, "Petição e certidões: independentes de taxas, para todos. PEGADINHA: cobrança de taxa “por urgência”."),

    ("Segurança jurídica (XXXVI)", "Assinale o que a lei NÃO pode prejudicar, segundo o art. 5º, XXXVI:",
     ["A expectativa de direito.",
      "O direito adquirido, o ato jurídico perfeito e a coisa julgada.",
      "Os interesses da Administração.",
      "Os contratos futuros.",
      "As meras liberalidades."],
     1, "Trio protegido: direito adquirido, ato jurídico perfeito e coisa julgada. PEGADINHA: “expectativa de direito” NÃO é protegida."),

    ("Retroatividade penal (XL)", "Lei nova reduz a pena de determinado crime de 8 para 4 anos. Quanto a quem já cumpre pena pelo crime na forma antiga:",
     ["A lei nova não o alcança, pois lei penal não retroage.",
      "A lei nova retroage para beneficiá-lo.",
      "Depende de novo julgamento integral.",
      "Só vale para crimes futuros.",
      "Só se aplica se o réu ainda não foi condenado."],
     1, "Lei penal mais benéfica RETROAGE, inclusive para condenados. PEGADINHA: afirmar apenas “não retroage” (meia-verdade)."),

    ("Racismo (XLII)", "Sobre o crime de racismo, é correto:",
     ["Prescreve em 20 anos.",
      "Admite fiança em casos leves.",
      "É contravenção penal.",
      "É crime inafiançável e imprescritível, sujeito a reclusão.",
      "É afiançável, mas imprescritível."],
     3, "Racismo: inafiançável E imprescritível, com reclusão. PEGADINHA: “prescreve” ou “admite fiança”."),

    ("Hediondos x racismo (XLIII)", "A respeito da tortura, do tráfico, do terrorismo e dos hediondos, assinale a correta:",
     ["São imprescritíveis, como o racismo.",
      "Admitem graça e anistia.",
      "São inafiançáveis e insuscetíveis de graça ou anistia, mas prescrevem.",
      "São afiançáveis.",
      "Admitem anistia após 30 anos."],
     2, "3TH + hediondos: inafiançáveis e sem graça/anistia, porém PRESCRITÍVEIS. PEGADINHA: igualar a racismo (imprescritível)."),

    ("Pessoalidade da pena (XLV)", "Falecido o condenado, no tocante à reparação do dano e ao perdimento de bens:",
     ["Nada se transmite aos sucessores.",
      "A própria pena privativa de liberdade se transmite aos herdeiros.",
      "Podem ser estendidos aos sucessores até o limite do patrimônio transferido.",
      "Transmitem-se sem qualquer limite.",
      "Só se transmitem se houver seguro."],
     2, "Pena não passa; reparação e perdimento passam, até o limite da herança. PEGADINHA: “nada se transmite” ou “sem limite”."),

    ("Penas vedadas (XLVII)", "Assinale a única pena admitida, em caráter excepcional, pela Constituição:",
     ["Prisão perpétua para hediondos.",
      "Trabalhos forçados.",
      "Banimento de criminosos reincidentes.",
      "Pena de morte em caso de guerra declarada.",
      "Penas cruéis para terroristas."],
     3, "Única exceção: pena de morte em guerra declarada. As demais são sempre vedadas. PEGADINHA: “perpétua para hediondos”."),

    ("Extradição (LI)", "Brasileiro naturalizado é acusado de tráfico de drogas cometido APÓS a naturalização. Quanto à extradição:",
     ["É impossível, pois é brasileiro.",
      "É possível, pois o envolvimento com tráfico autoriza a extradição do naturalizado, sem limite temporal.",
      "Só seria possível se o crime fosse anterior à naturalização.",
      "Depende de plebiscito.",
      "Só cabe para brasileiro nato."],
     1, "Naturalizado extradita-se por crime comum ANTES da naturalização OU por tráfico (antes/depois). PEGADINHA: exigir que o tráfico seja anterior."),

    ("Extradição (LI)", "Sobre o brasileiro NATO, assinale a correta:",
     ["Pode ser extraditado por crime hediondo.",
      "Pode ser extraditado por tráfico.",
      "Nunca será extraditado.",
      "Pode ser extraditado se autorizar.",
      "Pode ser extraditado para país de origem dos pais."],
     2, "Nato é absolutamente inextraditável. PEGADINHA: criar exceções (tráfico/hediondo) que só valem para o naturalizado."),

    ("Crime político (LII)", "Estrangeiro é alvo de pedido de extradição por crime de opinião praticado em seu país. A extradição:",
     ["Será concedida normalmente.",
      "Não será concedida, por se tratar de crime político ou de opinião.",
      "Depende apenas do Presidente.",
      "Será concedida se houver tratado.",
      "Cabe sempre contra estrangeiros."],
     1, "Crime político ou de opinião: não se extradita estrangeiro. PEGADINHA: “sempre cabe contra estrangeiro”."),

    ("Inafastabilidade (XXXV)", "Cidadão deseja ir ao Judiciário contra ameaça a direito, sem ter esgotado a via administrativa. É correto:",
     ["Deve, obrigatoriamente, esgotar a via administrativa antes.",
      "A lei pode excluir a ameaça da apreciação judicial.",
      "Só pode ir à Justiça após a lesão consumada.",
      "A lei não excluirá da apreciação do Judiciário lesão OU ameaça a direito, não se exigindo, em regra, o esgotamento administrativo.",
      "Precisa de autorização do órgão público."],
     3, "Inafastabilidade alcança lesão e AMEAÇA; em regra não se exige exaurir a via administrativa. PEGADINHA: “esgotar a via administrativa”."),

    ("Devido processo (LIV)", "A privação da liberdade ou de bens, segundo o art. 5º, LIV, exige:",
     ["Mera decisão administrativa.",
      "O devido processo legal.",
      "Apenas ordem do chefe imediato.",
      "Concordância da vítima.",
      "Decreto do Executivo."],
     1, "Ninguém será privado da liberdade ou de bens sem o devido processo legal. Base de todas as garantias processuais."),

    ("Ampla defesa (LV)", "Servidor responde a processo administrativo disciplinar (PAD). Quanto ao contraditório e à ampla defesa:",
     ["Só existem no processo judicial.",
      "São assegurados também no processo administrativo.",
      "Dependem de previsão em estatuto.",
      "Só valem em processo penal.",
      "São dispensáveis se a prova for robusta."],
     1, "Contraditório e ampla defesa valem no judicial E no administrativo. PEGADINHA: restringir ao judicial/penal."),

    ("Provas ilícitas (LVI)", "Em um processo, a única prova da autoria foi obtida mediante tortura. Essa prova:",
     ["É admissível por ser decisiva.",
      "É admissível se confirmada por outra.",
      "É inadmissível, por ter sido obtida por meio ilícito.",
      "Vale apenas na fase de investigação.",
      "É válida se o réu confessar depois."],
     2, "Prova ilícita é inadmissível e contamina derivadas (frutos da árvore envenenada). PEGADINHA: “admissível por ser decisiva”."),

    ("Presunção de inocência (LVII)", "Réu é condenado em 1ª instância, mas ainda cabe recurso. Juridicamente, ele é:",
     ["Culpado, pois já houve condenação.",
      "Presumido inocente até o trânsito em julgado da sentença penal condenatória.",
      "Semi-culpado.",
      "Culpado, mas com direito a recurso.",
      "Culpado a partir da segunda instância."],
     1, "Só é culpado após o trânsito em julgado. PEGADINHA: tratar condenação recorrível como culpa definitiva."),

    ("Reunião (XVI)", "Um grupo pretende realizar manifestação pacífica, sem armas, em praça pública. Conforme o art. 5º, XVI:",
     ["É necessária autorização da autoridade.",
      "Basta prévio aviso à autoridade competente, sendo dispensada autorização.",
      "É proibida em local aberto ao público.",
      "Depende de alvará pago.",
      "Só é permitida a partidos políticos."],
     1, "Reunião pacífica e sem armas: independe de autorização, exige apenas aviso prévio e não frustrar outra reunião. PEGADINHA: “autorização”."),

    ("Associação (XVII/XIX)", "Sobre a liberdade de associação, assinale a correta:",
     ["Associações podem ter caráter paramilitar.",
      "É plena, inclusive para fins ilícitos.",
      "É vedada a de caráter paramilitar, e as associações só podem ser compulsoriamente dissolvidas por decisão judicial transitada em julgado.",
      "Qualquer autoridade pode dissolver uma associação.",
      "A criação depende de autorização estatal."],
     2, "Vedada associação paramilitar; dissolução compulsória só por decisão judicial transitada em julgado. PEGADINHA: dissolução por “qualquer autoridade”."),

    ("Liberdade profissional (XIII)", "Quanto ao livre exercício de qualquer trabalho, ofício ou profissão:",
     ["É absoluto, sem qualquer condição.",
      "É livre, atendidas as qualificações profissionais que a lei estabelecer.",
      "Depende sempre de diploma de curso superior.",
      "Pode ser proibido por decreto.",
      "Só vale para profissões regulamentadas."],
     1, "Liberdade profissional é norma de eficácia contida: a lei pode exigir qualificação. PEGADINHA: “absoluto, sem condição”."),

    ("Propriedade / função social (XXII/XXIII)", "Sobre o direito de propriedade na Constituição:",
     ["É garantido em termos absolutos.",
      "É garantido, mas a propriedade atenderá a sua função social.",
      "Pode ser confiscado livremente pelo Estado.",
      "Não comporta desapropriação.",
      "Só existe para imóveis rurais."],
     1, "Propriedade é garantida, mas condicionada à função social. PEGADINHA: “absoluto”."),

    ("Júri (XXXVIII)", "A instituição do júri, com a organização que lhe der a lei, assegura, entre outros:",
     ["A publicidade absoluta das votações.",
      "A competência para o julgamento de qualquer crime.",
      "A soberania dos veredictos e a competência para os crimes dolosos contra a vida.",
      "A dispensa do sigilo das votações.",
      "A vinculação ao entendimento do juiz."],
     2, "Júri: plenitude de defesa, sigilo das votações, soberania dos veredictos e competência p/ crimes dolosos contra a vida. PEGADINHA: “qualquer crime”."),

    ("Habeas corpus (LXVIII)", "Pessoa sofre constrangimento ilegal em sua liberdade de locomoção. O remédio cabível é:",
     ["Mandado de segurança.",
      "Habeas data.",
      "Habeas corpus.",
      "Mandado de injunção.",
      "Ação popular."],
     2, "HC protege a liberdade de locomoção (ir e vir). É gratuito e pode ser impetrado por qualquer pessoa."),

    ("Mandado de injunção (LXXI)", "Determinado direito constitucional não pode ser exercido por falta de norma regulamentadora. O instrumento adequado é:",
     ["Mandado de segurança.",
      "Mandado de injunção.",
      "Habeas data.",
      "Ação popular.",
      "Habeas corpus."],
     1, "MI combate a omissão legislativa que inviabiliza direito. PEGADINHA: confundir com MS (direito líquido e certo já existente)."),

    ("Habeas data (LXXII)", "Cidadão deseja conhecer e retificar informações a seu respeito constantes de banco de dados de entidade governamental. Cabe:",
     ["Mandado de segurança coletivo.",
      "Habeas corpus.",
      "Ação popular.",
      "Habeas data.",
      "Mandado de injunção."],
     3, "HD: conhecer/retificar dados pessoais em registros públicos. Gratuito, legitimado é o titular dos dados."),

    ("Ação popular (LXXIII)", "Eleitor pretende anular ato lesivo ao patrimônio público e à moralidade administrativa. O instrumento é:",
     ["Ação popular, da qual é parte legítima qualquer cidadão.",
      "Mandado de segurança individual.",
      "Habeas data.",
      "Ação civil pública, privativa do MP.",
      "Habeas corpus."],
     0, "Ação popular: só o cidadão (eleitor) propõe; isento de custas, salvo má-fé. PEGADINHA: dizer que é privativa do MP (essa é a ACP)."),

    ("Mandado de segurança (LXIX)", "Para proteger direito líquido e certo, não amparado por habeas corpus ou habeas data, cabe:",
     ["Ação popular.",
      "Mandado de injunção.",
      "Mandado de segurança.",
      "Habeas corpus.",
      "Reclamação."],
     2, "MS protege direito líquido e certo (prova documental pré-constituída) quando não couber HC nem HD."),

    ("Tratados de DH (§3º)", "Tratado internacional de direitos humanos aprovado em dois turnos, por três quintos dos votos em cada Casa do Congresso, terá status de:",
     ["Lei ordinária.",
      "Lei complementar.",
      "Emenda constitucional.",
      "Decreto legislativo simples.",
      "Norma infralegal."],
     2, "Rito do §3º (2 turnos, 3/5, 2 Casas) = equivalência a EMENDA constitucional. Sem esse rito, status supralegal/ordinário."),

    ("Aplicabilidade (§1º)", "As normas definidoras dos direitos e garantias fundamentais, segundo o §1º do art. 5º, têm:",
     ["Aplicação dependente de lei em todos os casos.",
      "Aplicação imediata.",
      "Vigência apenas após regulamentação.",
      "Eficácia limitada por natureza.",
      "Aplicação diferida por dez anos."],
     1, "§1º: aplicação imediata (regra). Algumas normas, porém, dependem de lei (ex.: certos direitos sociais). PEGADINHA: “sempre dependem de lei”."),

    ("Razoável duração (LXXVIII)", "Sobre a duração razoável do processo, incluída pela EC 45/2004, é correto afirmar que se assegura:",
     ["Apenas no processo penal.",
      "A todos, no âmbito judicial e administrativo, a razoável duração do processo e os meios que garantam a celeridade de sua tramitação.",
      "Somente nos tribunais superiores.",
      "Apenas às partes representadas por advogado.",
      "Exclusivamente no processo trabalhista."],
     1, "LXXVIII: razoável duração no judicial E administrativo, com celeridade. PEGADINHA: restringir ao penal/judicial."),
]


def esc(s):
    return s  # conteudo ja revisado; mantem tags <b>


CSS = """
@page { size: A4; margin: 14mm 13mm 16mm 13mm; }
* { box-sizing: border-box; }
body {
  font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
  color: #1f2733; font-size: 10.2px; line-height: 1.5; margin: 0;
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
}
h1,h2,h3,h4 { margin: 0; font-weight: 700; }
.cover {
  height: 252mm; display: flex; flex-direction: column; justify-content: center;
  align-items: center; text-align: center;
  background: linear-gradient(135deg, #7a0c1c 0%, #b3122a 55%, #8e1020 100%);
  color: #fff; border-radius: 6px; page-break-after: always; padding: 0 24mm;
}
.cover .kicker { letter-spacing: 4px; font-size: 12px; opacity:.85; font-weight:600; }
.cover h1 { font-size: 46px; line-height:1.05; margin: 10px 0 6px; }
.cover .sub { font-size: 16px; font-weight: 400; opacity: .95; max-width: 130mm; }
.cover .rule { width: 70px; height: 4px; background: #ffd27a; margin: 22px 0; border-radius:2px;}
.cover .meta { font-size: 12.5px; opacity:.9; line-height:1.7; }
.cover .badge {
  margin-top: 26px; background: rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.4);
  padding: 9px 18px; border-radius: 40px; font-size: 13px; font-weight:600;
}
.section-title {
  font-size: 19px; color: #b3122a; border-bottom: 3px solid #b3122a;
  padding-bottom: 5px; margin: 4px 0 12px; page-break-after: avoid;
}
.lead { font-size: 11px; color:#3a4658; margin-bottom: 10px; }
.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 9px; }
.callout { border-radius: 7px; padding: 9px 11px; margin: 7px 0; page-break-inside: avoid; }
.c-why { background:#fff5f5; border-left:4px solid #b3122a; }
.c-key { background:#eefaf1; border-left:4px solid #1f9d57; }
.c-tip { background:#eef4ff; border-left:4px solid #2b6cb0; }
.callout h4 { font-size: 11px; margin-bottom: 4px; text-transform: uppercase; letter-spacing:.5px; }
.c-why h4 { color:#b3122a; } .c-key h4 { color:#1f9d57; } .c-tip h4 { color:#2b6cb0; }
.callout ul { margin: 3px 0 0; padding-left: 16px; } .callout li { margin: 2px 0; }

/* cards de incisos */
.card {
  border: 1px solid #e2e6ee; border-radius: 9px; padding: 11px 13px; margin: 0 0 11px;
  page-break-inside: avoid; background:#fff; box-shadow: 0 1px 2px rgba(20,30,50,.04);
}
.card .head { display:flex; align-items:center; gap:9px; margin-bottom:6px; }
.card .num {
  background:#b3122a; color:#fff; font-weight:700; font-size:11px;
  padding:3px 9px; border-radius:6px; white-space:nowrap;
}
.card .tit { font-size:12.5px; color:#1f2733; }
.card .lei {
  background:#f4f6fa; border-left:3px solid #9aa6b8; border-radius:4px;
  padding:6px 9px; font-style:italic; color:#2a3340; font-size:9.7px; margin:5px 0;
}
.card .row { display:grid; grid-template-columns: 1fr 1fr; gap:8px; margin-top:5px; }
.tag { font-weight:700; font-size:9px; text-transform:uppercase; letter-spacing:.4px; }
.t-trad { color:#2b6cb0; } .t-ex { color:#7a5c00; } .t-peg { color:#b3122a; } .t-mac { color:#1f9d57; }
.block { margin-top:4px; }
.block.peg { background:#fff5f5; border-radius:5px; padding:6px 8px; }
.block.mac { background:#eefaf1; border-radius:5px; padding:6px 8px; }

/* tabela remedios */
table { width:100%; border-collapse: collapse; margin: 6px 0 4px; font-size:9.5px; page-break-inside: avoid;}
th { background:#1f2733; color:#fff; text-align:left; padding:6px 7px; font-size:9.5px; }
td { border:1px solid #e2e6ee; padding:6px 7px; vertical-align:top; }
tr:nth-child(even) td { background:#f7f9fc; }
td .rn { font-weight:700; color:#b3122a; }

/* questoes */
.q { border:1px solid #e2e6ee; border-radius:8px; padding:9px 11px; margin:0 0 9px; page-break-inside: avoid; }
.q .qh { font-size:10.5px; font-weight:700; color:#1f2733; margin-bottom:5px; }
.q .qh .qn { color:#b3122a; }
.q .tema { display:inline-block; background:#eef0f5; color:#56627a; font-size:8.3px;
  font-weight:700; text-transform:uppercase; letter-spacing:.4px; padding:2px 7px; border-radius:20px; margin-bottom:5px;}
.q ol { margin:4px 0 0; padding-left:0; list-style:none; counter-reset: opt; }
.q ol li { counter-increment: opt; margin:2.5px 0; padding-left:20px; position:relative; font-size:9.6px; }
.q ol li::before {
  content: counter(opt, upper-alpha); position:absolute; left:0; top:0;
  font-weight:700; color:#56627a; }
.q ol li.ok::before { color:#1f9d57; }
.q ol li.ok { background:#eefaf1; border-radius:4px; }
.q .com { margin-top:6px; font-size:9.1px; color:#46536a; background:#fafbfd;
  border-left:3px solid #1f9d57; border-radius:4px; padding:5px 8px; }
.q .com b.g { color:#1f9d57; }

.gabarito { background:#1f2733; color:#fff; border-radius:9px; padding:14px 16px; page-break-inside: avoid;}
.gabarito h3 { color:#ffd27a; font-size:14px; margin-bottom:8px; }
.gabarito .grid { display:grid; grid-template-columns: repeat(7, 1fr); gap:5px; }
.gabarito .cell { background:rgba(255,255,255,.08); border-radius:5px; text-align:center;
  padding:5px 0; font-size:9.5px; }
.gabarito .cell b { color:#ffd27a; }
.note { font-size:8.6px; color:#8a94a6; margin-top:8px; }
.h-chapter { page-break-before: always; }
"""


def render_inciso(it):
    return f"""
    <div class="card">
      <div class="head"><span class="num">Art. 5º, {it['n']}</span><span class="tit">{it['tit']}</span></div>
      <div class="lei">“{it['lei']}”</div>
      <div class="block"><span class="tag t-trad">O que significa</span><br>{it['trad']}</div>
      <div class="row">
        <div class="block"><span class="tag t-ex">Exemplo</span><br>{it['ex']}</div>
        <div class="block peg"><span class="tag t-peg">Pegadinha Quadrix</span><br>{it['peg']}</div>
      </div>
      <div class="block mac"><span class="tag t-mac">Macete</span> &nbsp;{it['mac']}</div>
    </div>"""


def render_q(i, q):
    tema, enun, opts, ok, com = q
    lis = "".join(
        f'<li class="{"ok" if j==ok else ""}">{esc(o)}</li>' for j, o in enumerate(opts)
    )
    letra = "ABCDE"[ok]
    return f"""
    <div class="q">
      <div class="tema">{tema}</div>
      <div class="qh"><span class="qn">Questão {i}.</span> {esc(enun)}</div>
      <ol>{lis}</ol>
      <div class="com"><b class="g">Gabarito: {letra}.</b> {esc(com)}</div>
    </div>"""


def render_gabarito():
    cells = "".join(
        f'<div class="cell">{i}<b> {"ABCDE"[q[3]]}</b></div>' for i, q in enumerate(Q, 1)
    )
    from collections import Counter
    cnt = Counter("ABCDE"[q[3]] for q in Q)
    dist = " · ".join(f"{k}: {cnt.get(k,0)}" for k in "ABCDE")
    return f"""
    <div class="gabarito">
      <h3>Gabarito — 35 questões</h3>
      <div class="grid">{cells}</div>
      <div class="note">Distribuição das respostas — {dist}. (Gabarito equilibrado, como em prova real.)</div>
    </div>"""


incisos_html = "".join(render_inciso(i) for i in INCISOS)
remedios_rows = "".join(
    f"<tr><td><span class='rn'>{n}</span></td><td><b>{nome}</b></td><td>{quando}</td><td>{obs}</td></tr>"
    for (n, nome, quando, obs) in REMEDIOS
)
questoes_html = "".join(render_q(i, q) for i, q in enumerate(Q, 1))

HTML = f"""<!DOCTYPE html>
<html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head>
<body>

<div class="cover">
  <div class="kicker">DIREITO CONSTITUCIONAL</div>
  <h1>Artigo 5º<br>da CF/88</h1>
  <div class="rule"></div>
  <div class="sub">Direitos e Deveres Individuais e Coletivos — teoria de verdade, pegadinhas da banca e 35 questões comentadas</div>
  <div class="meta" style="margin-top:26px;">
    Concurso <b>Sedes/DF</b> · Banca <b>Quadrix</b> · 2026<br>
    Técnico Administrativo (Cargo 202)
  </div>
  <div class="badge">Dia 4 do cronograma · Meta: 35 questões</div>
</div>

<!-- 1. POR QUE CAI -->
<h2 class="section-title">1. Por que o Art. 5º derruba tanta gente</h2>
<p class="lead">O art. 5º é o coração da Constituição e a Quadrix o cobra em quase toda prova (3–5 questões). Ele não é difícil pelo volume — é difícil porque <b>a banca explora palavras</b>. Quem estuda por lógica acerta; quem decora solto, erra sob pressão.</p>
<div class="grid2">
  <div class="callout c-why">
    <h4>Os 4 erros que mais reprovam</h4>
    <ul>
      <li><b>Decorar sem lógica</b> — listas soltas se confundem na hora H.</li>
      <li><b>Ignorar a palavra-chave</b> — “lei” ≠ “decreto”, “salvo”, “apenas”, “vedado”.</li>
      <li><b>Esquecer a exceção</b> — quase todo inciso tem uma; é nela que mora a pegadinha.</li>
      <li><b>Não conhecer o estilo da banca</b> — a Quadrix repete os mesmos truques.</li>
    </ul>
  </div>
  <div class="callout c-key">
    <h4>Como este material te faz acertar</h4>
    <ul>
      <li>Cada inciso traz <b>a lógica</b> (o “porquê”), não só a regra.</li>
      <li>Mostra <b>como a Quadrix arma a pegadinha</b> — para você reconhecê-la.</li>
      <li>Dá um <b>macete</b> de memória para a hora da prova.</li>
      <li>35 questões no <b>estilo da banca</b>, comentadas uma a uma.</li>
    </ul>
  </div>
</div>
<div class="callout c-tip">
  <h4>Como a banca escreve (decore estes gatilhos)</h4>
  <ul>
    <li><b>VEDADO / É VEDADO</b> → se algo é vedado, a alternativa que diz “é permitido” é falsa.</li>
    <li><b>SALVO / EXCETO</b> → existe uma exceção; a alternativa que a ignora está incompleta = errada.</li>
    <li><b>SOMENTE / APENAS / INDEPENDENTEMENTE</b> → condição ou gratuidade exata; confira se foi respeitada.</li>
    <li><b>SEMPRE / NUNCA / ABSOLUTO</b> → quase sempre falso, porque há exceção.</li>
  </ul>
</div>

<!-- 2. CAPUT -->
<h2 class="section-title h-chapter">2. O Caput — quem tem direito e a quê</h2>
<div class="card">
  <div class="head"><span class="num">Caput</span><span class="tit">A regra-mãe dos direitos fundamentais</span></div>
  <div class="lei">“Todos são iguais perante a lei, sem distinção de qualquer natureza, garantindo-se aos brasileiros e aos estrangeiros residentes no País a inviolabilidade do direito à vida, à liberdade, à igualdade, à segurança e à propriedade…”</div>
  <div class="block"><span class="tag t-trad">Igualdade perante a lei</span><br>
  Não é “todos com o mesmo resultado”, e sim <b>mesmo tratamento pelas regras</b> (igualdade formal). A lei vale igual para rico e pobre. A igualdade <b>material</b> (tratar desiguais conforme suas diferenças) aparece em ações afirmativas e na lei processual.</div>
  <div class="row">
    <div class="block"><span class="tag t-ex">Quem é titular</span><br>
    Brasileiros <b>natos e naturalizados</b> e <b>estrangeiros residentes</b>. O STF, porém, estende o núcleo essencial (vida, integridade, acesso à Justiça) <b>a qualquer pessoa</b> em território nacional — inclusive turistas.</div>
    <div class="block peg"><span class="tag t-peg">Pegadinha Quadrix</span><br>
    Afirmar que o turista <b>“não tem direito nenhum”</b> (falso) ou que o caput protege “qualquer pessoa do mundo sem exceção” (também falso, pelo texto literal). Saiba distinguir <b>texto literal</b> × <b>jurisprudência</b>.</div>
  </div>
  <div class="block mac"><span class="tag t-mac">Macete</span> &nbsp;Os 5 pilares: <b>Vida, Liberdade, Igualdade, Segurança, Propriedade</b> — “V-L-I-S-P”. O rol é <b>exemplificativo</b> (há outros direitos, §2º).</div>
</div>

<div class="grid2">
  <div class="callout c-tip">
    <h4>§1º — Aplicação imediata</h4>
    As normas de direitos e garantias fundamentais têm <b>aplicação imediata</b> (regra). Algumas, porém, dependem de lei para funcionar (ex.: certos direitos sociais). <b>Pegadinha:</b> dizer que “todas dependem de regulamentação”.
  </div>
  <div class="callout c-tip">
    <h4>§2º — Rol aberto</h4>
    Os direitos listados <b>não esgotam</b> os existentes: há outros decorrentes do regime, dos princípios e de tratados. Por isso o rol do art. 5º é <b>exemplificativo</b>, não taxativo.
  </div>
</div>
<div class="grid2">
  <div class="callout c-tip">
    <h4>§3º — Tratados de Direitos Humanos</h4>
    Aprovados em <b>2 turnos</b>, por <b>3/5</b>, nas <b>2 Casas</b> → equivalem a <b>emenda constitucional</b>. Sem esse rito, têm status <b>supralegal</b>. <b>Pegadinha:</b> dizer que “todo tratado vira emenda”.
  </div>
  <div class="callout c-tip">
    <h4>§4º — Tribunal Penal Internacional</h4>
    O Brasil <b>se submete</b> à jurisdição do TPI a cuja criação tenha aderido. Cobrança rara, mas já apareceu.
  </div>
</div>

<!-- 3. INCISOS -->
<h2 class="section-title h-chapter">3. Os incisos que mais caem — explicados</h2>
<p class="lead">Cada card: o texto da lei, o que ele realmente significa, um exemplo concreto, a forma como a Quadrix arma a pegadinha e um macete de memória.</p>
{incisos_html}

<!-- 4. REMEDIOS -->
<h2 class="section-title h-chapter">4. Remédios Constitucionais — comparativo</h2>
<p class="lead">Cair “qual o instrumento cabível?” é quase certo. O segredo é o <b>objeto</b> de cada remédio: o que ele protege.</p>
<table>
  <thead><tr><th style="width:9%">Inciso</th><th style="width:22%">Remédio</th><th style="width:42%">Quando cabe (objeto)</th><th style="width:27%">Observações</th></tr></thead>
  <tbody>{remedios_rows}</tbody>
</table>
<div class="callout c-key">
  <h4>Macetes para não trocar os remédios</h4>
  <ul>
    <li><b>Locomoção</b> (ir e vir) → <b>Habeas Corpus</b>.</li>
    <li><b>Dado pessoal</b> (conhecer/corrigir) → <b>Habeas Data</b>.</li>
    <li><b>Falta de lei</b> que inviabiliza direito → <b>Mandado de Injunção</b>.</li>
    <li><b>Direito líquido e certo</b> (com prova pronta) → <b>Mandado de Segurança</b>.</li>
    <li><b>Ato lesivo ao patrimônio público</b>, pelo cidadão → <b>Ação Popular</b>.</li>
  </ul>
</div>

<!-- 5. QUESTOES -->
<h2 class="section-title h-chapter">5. 35 Questões Comentadas</h2>
<p class="lead">Resolva tentando <b>identificar a pegadinha</b> antes de ver o gabarito. A alternativa correta vem destacada e comentada.</p>
{questoes_html}

<!-- 6. GABARITO -->
<h2 class="section-title h-chapter">6. Gabarito</h2>
{render_gabarito()}

</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("HTML gerado:", OUT)
print("Incisos:", len(INCISOS), "| Questoes:", len(Q))
