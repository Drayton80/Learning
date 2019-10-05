# Author: Drayton Corrêa Filho
# Email: <drayton80@hotmail.com>
# GitHub: Drayton80
#
# LAViD - Laboratório de Aplicações de Vídeo Digital


import spacy


class GramaticaVerbal:
    def __init__(self):
        self._nlp = spacy.load('pt_core_news_sm')

        # CONJUGAÇÕES DOS VERBOS:
        # Dicionários que contém uma relação da pessoa e do respectivo sufixo que ela gera no verbo, o que pode depender de como
        # o infinitivo do verbo é terminado, (e.g. "falar", por terminar em "ar", na primeira pessoa do singular no tempo presente 
        # fica "falo", na segunda pessoa do singular fica "falas" e assim por diante)
        self._conjucacao_de_verbos = {}
        self._conjucacao_de_verbos['regulares'] = {}
        self._conjucacao_de_verbos['regulares']['ar'] = {}
        self._conjucacao_de_verbos['regulares']['er'] = {}
        self._conjucacao_de_verbos['regulares']['ir'] = {}

        self._conjucacao_de_verbos['regulares']['ar']['indicativo'] = {}
        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['presente'] = {}
        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['preterito imperfeito'] = {}
        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['preterito perfeito'] = {}
        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['preterito mais que perfeito'] ={}
        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['futuro do presente'] = {}
        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['futuro do preterito'] = {}

        self._conjucacao_de_verbos['regulares']['er']['indicativo'] = {}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['presente'] = {}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['preterito imperfeito'] = {}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['preterito perfeito'] = {}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['preterito mais que perfeito'] ={}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['futuro do presente'] = {}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['futuro do preterito'] = {}
        
        self._conjucacao_de_verbos['regulares']['ir']['indicativo'] = {}
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['presente'] = {}
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['preterito imperfeito'] = {}
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['preterito perfeito'] = {}
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['preterito mais que perfeito'] ={}
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['futuro do presente'] = {}
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['futuro do preterito'] = {}
        
        
        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['presente']['glosa']     = {'indicador do tempo': '', 'divisor': ''}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['presente']['glosa']     = {'indicador do tempo': '', 'divisor': ''}
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['presente']['glosa']     = {'indicador do tempo': '', 'divisor': ''}
        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['presente']['portugues'] = {'1PS': 'o', '2PS': 'as', '3PS': 'a', '1PP': 'amos', '2PP': 'ais', '3PP': 'am'}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['presente']['portugues'] = {'1PS': 'o', '2PS': 'es', '3PS': 'e', '1PP': 'emos', '2PP': 'eis', '3PP': 'em'}
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['presente']['portugues'] = {'1PS': 'o', '2PS': 'es', '3PS': 'e', '1PP': 'imos', '2PP': 'is' , '3PP': 'em'}

        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['preterito imperfeito']['glosa']     = {'indicador do tempo': 'PASSADO', 'divisor': ' '}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['preterito imperfeito']['glosa']     = {'indicador do tempo': 'PASSADO', 'divisor': ' '}
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['preterito imperfeito']['glosa']     = {'indicador do tempo': 'PASSADO', 'divisor': ' '}
        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['preterito imperfeito']['portugues'] = {'1PS': 'ava', '2PS': 'avas', '3PS': 'ava', '1PP': 'ávamos', '2PP': 'áveis', '3PP': 'avam'}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['preterito imperfeito']['portugues'] = {'1PS': 'ia' , '2PS': 'ias' , '3PS': 'ia' , '1PP': 'íamos' , '2PP': 'íeis' , '3PP': 'iam' }
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['preterito imperfeito']['portugues'] = {'1PS': 'ia' , '2PS': 'ias' , '3PS': 'ia' , '1PP': 'íamos' , '2PP': 'íeis' , '3PP': 'iam' }

        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['preterito perfeito']['glosa']     = {'indicador do tempo': 'PASSADO', 'divisor': ' '}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['preterito perfeito']['glosa']     = {'indicador do tempo': 'PASSADO', 'divisor': ' '}
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['preterito perfeito']['glosa']     = {'indicador do tempo': 'PASSADO', 'divisor': ' '}
        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['preterito perfeito']['portugues'] = {'1PS': 'ei', '2PS': 'aste', '3PS': 'ou', '1PP': 'amos', '2PP': 'astes', '3PP': 'aram'}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['preterito perfeito']['portugues'] = {'1PS': 'i' , '2PS': 'este', '3PS': 'eu', '1PP': 'emos', '2PP': 'estes', '3PP': 'eram'}
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['preterito perfeito']['portugues'] = {'1PS': 'i' , '2PS': 'iste', '3PS': 'iu', '1PP': 'imos', '2PP': 'istes', '3PP': 'iram'}

        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['preterito mais que perfeito']['glosa']     = {'indicador do tempo': 'PASSADO', 'divisor': ' '}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['preterito mais que perfeito']['glosa']     = {'indicador do tempo': 'PASSADO', 'divisor': ' '}
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['preterito mais que perfeito']['glosa']     = {'indicador do tempo': 'PASSADO', 'divisor': ' '}
        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['preterito mais que perfeito']['portugues'] = {'1PS': 'ara', '2PS': 'aras', '3PS': 'ara', '1PP': 'áramos', '2PP': 'áreis', '3PP': 'aram'}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['preterito mais que perfeito']['portugues'] = {'1PS': 'era', '2PS': 'eras', '3PS': 'era', '1PP': 'êramos', '2PP': 'êreis', '3PP': 'eram'}
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['preterito mais que perfeito']['portugues'] = {'1PS': 'ira', '2PS': 'iras', '3PS': 'ira', '1PP': 'íramos', '2PP': 'íreis', '3PP': 'iram'}
        
        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['futuro do presente']['glosa']     = {'indicador do tempo': 'FUTURO', 'divisor': ' '}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['futuro do presente']['glosa']     = {'indicador do tempo': 'FUTURO', 'divisor': ' '}
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['futuro do presente']['glosa']     = {'indicador do tempo': 'FUTURO', 'divisor': ' '}
        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['futuro do presente']['portugues'] = {'1PS': 'arei', '2PS': 'arás', '3PS': 'ará', '1PP': 'aremos', '2PP': 'areis', '3PP': 'arão'}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['futuro do presente']['portugues'] = {'1PS': 'erei', '2PS': 'erás', '3PS': 'erá', '1PP': 'eremos', '2PP': 'ereis', '3PP': 'erão'}
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['futuro do presente']['portugues'] = {'1PS': 'irei', '2PS': 'irás', '3PS': 'irá', '1PP': 'iremos', '2PP': 'ireis', '3PP': 'irão'}

        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['futuro do preterito']['glosa']     = {'indicador do tempo': 'FUTURO', 'divisor': ' '}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['futuro do preterito']['glosa']     = {'indicador do tempo': 'FUTURO', 'divisor': ' '}
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['futuro do preterito']['glosa']     = {'indicador do tempo': 'FUTURO', 'divisor': ' '}
        self._conjucacao_de_verbos['regulares']['ar']['indicativo']['futuro do preterito']['portugues'] = {'1PS': 'aria', '2PS': 'arias', '3PS': 'aria', '1PP': 'aríamos', '2PP': 'aríeis', '3PP': 'ariam'}
        self._conjucacao_de_verbos['regulares']['er']['indicativo']['futuro do preterito']['portugues'] = {'1PS': 'eria', '2PS': 'erias', '3PS': 'eria', '1PP': 'eríamos', '2PP': 'eríeis', '3PP': 'eriam'}
        self._conjucacao_de_verbos['regulares']['ir']['indicativo']['futuro do preterito']['portugues'] = {'1PS': 'iria', '2PS': 'irias', '3PS': 'iria', '1PP': 'iríamos', '2PP': 'iríeis', '3PP': 'iriam'}
        
        self._conjucacao_de_verbos['irregulares'] = {}
        self._conjucacao_de_verbos['irregulares']['lista de verbos'] = [
            'abster', 'acudir', 'adequar', 'adjazer', 'advertir', 'advir', 'afazer', 'aferir', 'agredir', 'ansiar', 'antedar',
            'antepor', 'antever', 'apor', 'aprazer', 'apropinquar', 'aspergir', 'assentir', 'ateratrair', 'atribuir', 
            'autodestruir', 'avir', 'bem-dizer', 'bem-fazer', 'bem-querer', 'bendizer', 'benfazer', 'benquerer', 'buir',
            'bulir', 'caber', 'cair', 'cerzir', 'circumpor', 'circunver', 'cobrir', 'compor', 'comprazer', 'concernir', 
            'concluir', 'condizer', 'conferir', 'confugir', 'conseguir', 'consentir', 'construir', 'consumir', 
            'conter', 'contradizer', 'contrafazer', 'contrair', 'contrapor', 'contrapropor', 'contravir', 'convergir', 
            'convir', 'crer', 'cuspir', 'dar', 'decompor', 'delinquir', 'denegrir', 'depor', 'desafazer', 'desaguar', 
            'desapor', 'desaprazer', 'desavir', 'descaber', 'descobrir', 'descompor', 'descomprazer', 'desconstruir',
            'desconvir', 'descrer', 'desdar', 'desdizer', 'desimpedir', 'desimpor', 'deslinguar', 'desmedir', 
            'desmentir', 'desmobiliar', 'despedir', 'despolir', 'despor', 'desprazer', 'desprecaver', 'desprover', 
            'desquerer', 'dessaber', 'destruir', 'desvaler', 'desver', 'deter', 'devir', 'digerir', 'disperder', 
            'dispor', 'distrair', 'divertir', 'dizer', 'dormir', 'embair', 'emergir', 'encobrir', 'engolir', 'entredizer', 
            'entrefazer', 'entreouvir', 'entrepor', 'entrequerer', 'entrever', 'entrevir', 'entupir', 'enxaguar', 
            'equivaler', 'escapulir', 'esfazer', 'estar', 'estrear', 'esvair', 'expedir', 'expelir', 'expor', 'extrapor', 
            'fazer', 'fotocompor', 'fraguar', 'frigir', 'fugir', 'gelifazer', 'haver', 'idear', 'imergir', 'impedir', 
            'impelir', 'impor', 'incendiar', 'incluir', 'indispor', 'influir', 'insatisfazer', 'inserir', 'interdizer', 
            'intermediar', 'interpor', 'interver', 'intervir', 'ir', 'jazer', 'justapor', 'ler', 'liquefazer', 'maisquerer',
            'maldispor', 'maldizer', 'malfazer', 'malinguar', 'malparir', 'malquerer', 'manter', 'mediar', 'medir', 
            'mentir', 'minguar', 'obter', 'obvir', 'odiar', 'opor', 'ouvir', 'parir', 'pedir', 'perder', 'perfazer', 
            'perseguir', 'persentir', 'pleitear', 'poder', 'poer', 'polir', 'pospor', 'pôr', 'prazer', 'predispor', 
            'predizer', 'preferir', 'prepor', 'pressentir', 'pressupor', 'preterir', 'prevenir', 'prever', 
            'progredir', 'propor', 'pressupor', 'prover', 'provir', 'pruir', 'puir', 'putrefazer', 'querer', 'roer', 
            'rarefazer', 'readequar', 'reaver', 'reavir', 'recobrir', 'recompor', 'reconvir', 'redar', 'redispor', 
            'redizer', 'reexpedir', 'reexpor', 'refazer', 'regredir', 'reimpor', 'reindispor', 'reler', 'remediar',
            'remedir', 'reobter', 'reouvir', 'repedir', 'repelir', 'repor', 'repropor', 'requerer', 'resfolegar', 
            'ressentir', 'reter', 'retrair', 'retranspor', 'rever', 'revir', 'rir', 'ruir', 'saber', 'sacudir', 
            'sair', 'santiguar', 'satisfazer', 'seguir', 'sentir', 'ser', 'servir', 'sobpor', 'sobre-expor', 
            'sobreexpor', 'sobrepor', 'sobrestar', 'sobrevir', 'sorrir', 'sortear', 'sortir', 'sotopor', 'subir',
            'submergir', 'subpor', 'subsumir', 'subtrair', 'sugerir', 'sumir', 'superexpor', 'superimpor', 
            'superpor', 'supor', 'suster', 'telever', 'ter', 'torrefazer', 'tossir', 'trair', 'transfazer', 'transfugir', 
            'transgredir', 'transpor', 'traspor', 'trazer', 'treler', 'tresler', 'trespor', 'tumefazer', 'valer', 
            'ver', 'vestir', 'vir'
        ]

        self._conjucacao_de_verbos['irregulares']['ser'] = {}
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo'] = {}
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['presente']                    = {}
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['preterito imperfeito']        = {}
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['preterito perfeito']          = {}
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['preterito mais que perfeito'] = {}
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['futuro do presente']          = {}
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['futuro do preterito']         = {}
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['presente']['glosa']                    = {'indicador do tempo': ''       , 'divisor': '' }
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['preterito imperfeito']['glosa']        = {'indicador do tempo': 'PASSADO', 'divisor': ' '}   
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['preterito perfeito']['glosa']          = {'indicador do tempo': 'PASSADO', 'divisor': ' '}
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['preterito mais que perfeito']['glosa'] = {'indicador do tempo': 'PASSADO', 'divisor': ' '}
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['futuro do presente']['glosa']          = {'indicador do tempo': 'FUTURO' , 'divisor': ' '}
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['futuro do preterito']['glosa']         = {'indicador do tempo': 'FUTURO' , 'divisor': ' '}
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['presente']['portugues']                    = {'1PS': 'sou'  , '2PS': 'és'    , '3PS': 'é'    , '1PP': 'somos'   , '2PP': 'sois'   , '3PP': 'são'}
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['preterito imperfeito']['portugues']        = {'1PS': 'era'  , '2PS': 'eras'  , '3PS': 'era'  , '1PP': 'éramos'  , '2PP': 'éreis'  , '3PP': 'eram'}
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['preterito perfeito']['portugues']          = {'1PS': 'fui'  , '2PS': 'foste' , '3PS': 'foi'  , '1PP': 'fomos'   , '2PP': 'fostes' , '3PP': 'foram'}
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['preterito mais que perfeito']['portugues'] = {'1PS': 'fora' , '2PS': 'foras' , '3PS': 'fora' , '1PP': 'fôramos' , '2PP': 'fôreis' , '3PP': 'foram'}
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['futuro do presente']['portugues']          = {'1PS': 'serei', '2PS': 'serás' , '3PS': 'será' , '1PP': 'seremos' , '2PP': 'sereis' , '3PP': 'serão'}
        self._conjucacao_de_verbos['irregulares']['ser']['indicativo']['futuro do preterito']['portugues']         = {'1PS': 'seria', '2PS': 'serias', '3PS': 'seria', '1PP': 'seríamos', '2PP': 'seríeis', '3PP': 'seriam'}
        
    def get_conjucacao_de_verbos(self):
        return self._conjucacao_de_verbos
    
    def get_conjucacao_de_verbos_regulares(self):
        return self._conjucacao_de_verbos['regulares']

    def get_conjugacao_de_verbos_irregulares(self):
        return self._conjucacao_de_verbos['irregulares']
    
    def get_verbo_infinitivo(self, verbo: str):
        verbo_token = self._nlp(verbo)[0]
        return verbo_token.lemma_

    def verbo_eh_irregular(self, verbo: str):
        verbo_no_infinitivo = self.get_verbo_infinitivo(verbo)

        if verbo_no_infinitivo in self._conjucacao_de_verbos['irregulares']['lista de verbos']:
            return True
        else:
            return False

    def verbo_eh_regular(self, verbo: str):
        if not self.verbo_eh_irregular(verbo):
            return True
        else:
            return False

    def extrai_terminacao_infinitivo(self, verbo: str):
        if verbo and not verbo == "":
            verbo_infinitivo = self.get_verbo_infinitivo(verbo)

            # A terminação do infinitivo sempre é ar, er ou ir, possuindo sempre o tamanho 2:
            terminacao_infinitivo = verbo_infinitivo[len(verbo_infinitivo)-2:]
            
            if not terminacao_infinitivo:
                return ""
            else:
                return terminacao_infinitivo
        else:
            return ""

    def extrai_radical_verbo(self, verbo: str):
        if verbo and not verbo == "":
            verbo_infinitivo = self.get_verbo_infinitivo(verbo)
            terminacoes_infinitivo = self._conjucacao_de_verbos['regulares'].keys()

            for terminacao_infinitivo in terminacoes_infinitivo:
                if verbo_infinitivo.endswith(terminacao_infinitivo):
                    # Retirando-se a terminação (ar, er ou ir) do verbo no infinitivo, obtém-se o radical:
                    radical_do_verbo = verbo_infinitivo[:len(verbo_infinitivo)-len(terminacao_infinitivo)]
                    
                    if not radical_do_verbo:
                        return ""
                    else:
                        return radical_do_verbo
        else:
            return verbo


    def todas_conjugacoes_do_verbo(self, verbo: str, ignorar_valores=[], apenas_estas_pessoas_verbais=[]):
        if not isinstance(ignorar_valores, list):
            ignorar_valores = [ignorar_valores]

        radical_do_verbo = self.extrai_radical_verbo(verbo)
        terminacao_infinitivo = self.extrai_terminacao_infinitivo(verbo)
        verbo_no_infinitivo = self.get_verbo_infinitivo(verbo)
        conjugacoes = {}

        if self.verbo_eh_irregular(verbo):
            if verbo_no_infinitivo in self._conjucacao_de_verbos['irregulares'].keys():
                for modo_verbal, modo_verbal_tempos in self._conjucacao_de_verbos['irregulares'][verbo_no_infinitivo].items():
                    conjugacoes[modo_verbal] = {}
                    
                    for tempo_verbal, tempo_verbal_pessoas in modo_verbal_tempos.items():
                        conjugacoes[modo_verbal][tempo_verbal] = {}

                        for pessoa, verbo in tempo_verbal_pessoas['portugues'].items():
                            if verbo in ignorar_valores: 
                                continue
                            elif apenas_estas_pessoas_verbais and pessoa not in apenas_estas_pessoas_verbais:
                                continue
                            else:
                                conjugacoes[modo_verbal][tempo_verbal][pessoa] = {}
                                conjugacoes[modo_verbal][tempo_verbal][pessoa]['portugues'] = verbo
                                conjugacoes[modo_verbal][tempo_verbal][pessoa]['glosa']     = verbo_no_infinitivo + tempo_verbal_pessoas['glosa']['divisor'] + tempo_verbal_pessoas['glosa']['indicador do tempo']

        else:
            if terminacao_infinitivo in self._conjucacao_de_verbos['regulares'].keys():
                for modo_verbal, modo_verbal_tempos in self._conjucacao_de_verbos['regulares'][terminacao_infinitivo].items():
                    conjugacoes[modo_verbal] = {}

                    for tempo_verbal, tempo_verbal_pessoas in modo_verbal_tempos.items():
                        conjugacoes[modo_verbal][tempo_verbal] = {}

                        for pessoa, terminacao in tempo_verbal_pessoas['portugues'].items():
                            if terminacao in ignorar_valores: 
                                continue
                            elif apenas_estas_pessoas_verbais and pessoa not in apenas_estas_pessoas_verbais:
                                continue
                            else:
                                verbo = radical_do_verbo + terminacao
                                conjugacoes[modo_verbal][tempo_verbal][pessoa] = {}
                                conjugacoes[modo_verbal][tempo_verbal][pessoa]['portugues'] = verbo
                                conjugacoes[modo_verbal][tempo_verbal][pessoa]['glosa']     = verbo_no_infinitivo + tempo_verbal_pessoas['glosa']['divisor'] + tempo_verbal_pessoas['glosa']['indicador do tempo']

        return conjugacoes
        

        

                
