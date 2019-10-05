# Author: Drayton Corrêa Filho
# Email: <drayton80@hotmail.com>
# GitHub: Drayton80
#
# LAViD - Laboratório de Aplicações de Vídeo Digital


import os
import sys
import spacy
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('..')))

from src.GramaticaVerbal import GramaticaVerbal
from src.GramaticaPronome import GramaticaPronome


class Sentence:
    def __init__(self):
        _todos_verbos_negacao = pd.read_csv(r'../data/parametros_libras_verbos_negacao.csv', low_memory=False)

        self._conjugacao_de_verbos = GramaticaVerbal().get_conjucacao_de_verbos()
        self._todos_os_verbos = self._retira_o_nao_dos_verbos(_todos_verbos_negacao)['VERBOS'].tolist()

        self.nlp = spacy.load('pt_core_news_sm')

    # Retira de todos os verbos do data frame a parte com 'nao_' para poder
    # obter apenas os verbos da lista:
    def _retira_o_nao_dos_verbos(self, data_frame: pd.DataFrame):
        modified_data_frame = pd.DataFrame(data_frame)
        
        i = 0

        for verbo_com_nao in modified_data_frame['VERBOS'].tolist():
            verbo_sem_nao = verbo_com_nao.split('_')[1]
            modified_data_frame.at[i, 'VERBOS'] = verbo_sem_nao.lower()

            i += 1

        return modified_data_frame

    def _sentence_list_to_text(self, sentence_list: list, grammar_class_list: list, is_glosa_sentence=False):
        sentence_text = ''
        first_sentence_word = True
        
        for word_index in range(len(sentence_list)):
            if first_sentence_word:
                first_sentence_word = False
            elif grammar_class_list[word_index] == 'PUNCT':
                pass                            
            else:
                sentence_text += ' '

            sentence_text += sentence_list[word_index]
        
        if is_glosa_sentence:
            # Retorna a frase com todas as letras em maisculo:
            sentence_text = sentence_text.upper()
        else:
            # Retorna a frase com a primeira letra em maiusculo:
            sentence_text = sentence_text.capitalize()
        
        return sentence_text
    
    def search_word_index_in_glosa(self, doc_glosa, word, word_grammar_class=None, approximate_position=None):        
        if not word:
            return None
        
        if not word_grammar_class:
            word_grammar_class = self.nlp(word).pos_
        
        if   word_grammar_class.upper() in ['PROPN', 'PRON']:
            search_word = word.lower()
        elif word_grammar_class.upper() in ['VERB']:
            search_word = GramaticaVerbal().get_verbo_infinitivo(word).lower()
        else:
            search_word = None

        if search_word:
            sentence = [token.orth_ for token in doc_glosa]
            # Se houver uma posição aproximada para iniciar, busca nessas proximidades 
            if approximate_position and isinstance(approximate_position, int):
                start_index = approximate_position-3 if approximate_position-3 > 0 else 0
                end_index   = approximate_position+3 if approximate_position+3 < len(doc_glosa) else len(doc_glosa)-1

                for word_index in range(start_index, end_index):
                    if search_word == sentence[word_index]:
                        return word_index
            # Caso não haja uma posição aproximada ou caso não ache a palavra na posição aproximada, 
            # é feita uma busca em toda a frase:
            for word_index in range(len(sentence)):
                if search_word == sentence[word_index]:
                    return word_index 

        # Caso nada seja encontrado, é retornado None
        return None


    def search_first_subject_in_previous_words(self, doc, final_limit_index, ignore_obliquos_pronouns=False):
        pronoun_grammar = GramaticaPronome()
        subject = None
        index = None
        person = None
        grammar_class = None

        
        for previous_word_index in reversed(range(final_limit_index)):
            previous_word = doc[previous_word_index].orth_
            previous_word_grammar_class = doc[previous_word_index].pos_
            
            if previous_word_grammar_class == 'PRON':
                pronoun_person_and_case = pronoun_grammar.get_pessoa_e_caso_do_pronome(previous_word)
                
                # Pronomes obliquos não influenciam na flexão do verbo, então é necessário ignorá-los:
                #  Ex.: na frase 'Ele me viu fazendo', o verbo 'ver' está na 3ª Pessoa do Singular
                #       pois o pronome de caso reto 'Ele' é o sujeito, mesmo havendo o pronome 
                #       obliquo 'me' antecendendo o verbo
                if ignore_obliquos_pronouns and 'oblíquo' in pronoun_person_and_case['caso']:
                    continue
                else:
                    subject = previous_word
                    index = previous_word_index
                    person = pronoun_person_and_case['pessoa']
                    grammar_class = doc[previous_word_index].pos_
                    break

            if previous_word_grammar_class in ['PROPN', 'NOUN']:
                subject = previous_word
                index = previous_word_index
                grammar_class = doc[previous_word_index].pos_
                # Para dar um chute mais certeiro acerca da pessoa verbal que um sujeito qualquer
                # possuí, faz-se uma checagem simples para ver se o nome proprio é da 3ª Pessoa 
                # do Plural caso termine com 's' ou 3ª Pessoa do Singular caso contrário
                if previous_word.endswith('s'):
                    person = '3PP'
                else:
                    person = '3PS'
                break
        
        return {'subject': subject, 'index': index, 'person': person, 'grammar class': grammar_class}


    # OBS.: para usar essa função é preciso baixar o pacote 
    #       em português utilizando o comando:
    #       python -m spacy download pt
    def sentences_with_verbs_replaced_for_other_conjugations(self, sentence_portuguese: str, sentence_glosa: str):
        sentence_portuguese = sentence_portuguese.lower()
        sentence_glosa = sentence_glosa.lower()
        
        verbal_grammar = GramaticaVerbal()
        pronoun_grammar = GramaticaPronome()
        replaced_sentences = []

        try:
            doc_portuguese = self.nlp(sentence_portuguese)
            #print([token.pos_ for token in doc_portuguese])
            doc_glosa = self.nlp(sentence_glosa)
            
            verb_information = {}
            verb_information['index portuguese'] = None
            verb_information['original verb'] = None
            verb_information['conjugations'] = None

            verbal_subject_information = {}
            verbal_subject_information['subject'] = None
            verbal_subject_information['index portuguese'] = None
            verbal_subject_information['index glosa'] = None
            verbal_subject_information['person'] = None
            verbal_subject_information['grammar class'] = None
            
            word_index = 0
            # Encontra os verbos na frase e os armazena em conjunto com 
            # todas as suas conjugações possíveis (com exceção da 
            # conjugação dele na frase original)
            for token in doc_portuguese:
                word_text = token.orth_
                word_grammar_class = token.pos_

                # Apenas gera novas sentenças se for um verbo:
                if word_grammar_class == 'VERB':
                    # Se encontra um verbo, checa pela classe grmaatical de cada palavra
                    # anterior a ele para encontrar pronome ou sujeito mais próximo:
                    verbal_subject_information_portuguese = self.search_first_subject_in_previous_words(doc_portuguese, word_index, ignore_obliquos_pronouns=True)
                    verbal_subject_information['subject']          = verbal_subject_information_portuguese['subject']
                    verbal_subject_information['person']           = verbal_subject_information_portuguese['person']
                    verbal_subject_information['grammar class']    = verbal_subject_information_portuguese['grammar class']
                    verbal_subject_information['index portuguese'] = verbal_subject_information_portuguese['index']
                    verbal_subject_information['index glosa']      = self.search_word_index_in_glosa(doc_glosa, verbal_subject_information['subject'], 
                                                                                                     word_grammar_class=verbal_subject_information['grammar class'],
                                                                                                     approximate_position=verbal_subject_information['index portuguese'])
                    if verbal_grammar.verbo_eh_irregular(word_text):
                        ignore_value = word_text
                    else:
                        verb_radical = verbal_grammar.extrai_radical_verbo(word_text)

                        if verb_radical:
                            verb_termination = word_text[len(verb_radical):]
                        else:
                            verb_termination = None

                        ignore_value = verb_termination

                    verb_information['original verb'] = word_text
                    verb_information['index portuguese'] = word_index
                    verb_information['index glosa'] = self.search_word_index_in_glosa(doc_glosa, verbal_grammar.get_verbo_infinitivo(word_text),
                                                                                      word_grammar_class='VERB', approximate_position=word_index)

                    if verbal_subject_information['grammar class'] == 'PRON':
                        verb_information['conjugations'] = verbal_grammar.todas_conjugacoes_do_verbo(word_text, ignorar_valores=ignore_value)
                    else:
                        verb_information['conjugations'] = verbal_grammar.todas_conjugacoes_do_verbo(word_text, ignorar_valores=ignore_value, apenas_estas_pessoas_verbais=verbal_subject_information['person'])

                word_index += 1
            

            if verb_information['conjugations']:
                for modo_verbal in verb_information['conjugations'].values():
                    for tempo_verbal in modo_verbal.values():
                        for verbal_person, verb_conjugation in tempo_verbal.items():
                            # Manipulação da Frase em Português:
                            replaced_sentence_portuguese = [token.orth_ for token in doc_portuguese]
                            replaced_sentence_portuguese[verb_information['index portuguese']] = verb_conjugation['portugues']

                            # Manipulação da Frase em Glosa:
                            replaced_sentence_glosa = [token.orth_ for token in doc_glosa]
                            if verb_information['index glosa']:
                                replaced_sentence_glosa[verb_information['index glosa']] = verb_conjugation['glosa']
                                # Se a próxima palavra for PASSADO ou FUTURO ela é excluída
                                if  replaced_sentence_glosa[verb_information['index glosa']+1].upper() in ['PASSADO', 'FUTURO']:
                                    replaced_sentence_glosa.pop(verb_information['index glosa']+1)

                            # Substituição do Sujeito:
                            if verbal_subject_information['grammar class'] == 'PRON':
                                for person_by_gender in pronoun_grammar._pronomes['reto'][verbal_person]:
                                    replaced_sentence_portuguese[verbal_subject_information['index portuguese']] = person_by_gender
                                    replaced_sentence_glosa[verbal_subject_information['index glosa']] = person_by_gender

                                    replaced_sentences.append([replaced_sentence_portuguese.copy(), replaced_sentence_glosa.copy()])
                            else:
                                replaced_sentences.append([replaced_sentence_portuguese, replaced_sentence_glosa])

            for index in range(len(replaced_sentences)):
                replaced_sentences[index][0] = self._sentence_list_to_text(replaced_sentences[index][0], [token.pos_ for token in doc_portuguese])
                replaced_sentences[index][1] = self._sentence_list_to_text(replaced_sentences[index][1], [token.pos_ for token in doc_glosa], is_glosa_sentence=True)

            return replaced_sentences

        except UnicodeDecodeError:
            raise UnicodeDecodeError
            

nlp = spacy.load('pt_core_news_sm')
frase_original = 'O diagrama seguinte representa as localidades num raio de 16 km ao redor de Martin'
frase_glosa = 'DIAGRAMA SEGUINTE REPRESENTAR LOCALIDADE NUM RAIO 16 KM REDOR MARTIN'
#doc = nlp(frase_original)
print('Frase original:')
print(frase_original)
#print([(token.orth_, token.pos_) for token in doc])
print('Frases geradas:')

for nova_frase in Sentence().sentences_with_verbs_replaced_for_other_conjugations(frase_original, frase_glosa):
    print(nova_frase)
'''
nlp = spacy.load('pt_core_news_sm')
frase_original = 'Eu criei aquilo'
frase_glosa = 'EU CRIAR PASSADO AQUILO'
#doc = nlp(frase_original)
print('\nFrase original:')
print(frase_original)
#print([(token.orth_, token.pos_) for token in doc])
print('Frases geradas:')

for nova_frase in Sentence().sentences_with_verbs_replaced_for_other_conjugations(frase_original, frase_glosa):
    print(nova_frase)
    '''