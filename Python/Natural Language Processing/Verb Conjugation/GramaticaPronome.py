# Author: Drayton Corrêa Filho
# Email: <drayton80@hotmail.com>
# GitHub: Drayton80
#
# LAViD - Laboratório de Aplicações de Vídeo Digital


class GramaticaPronome:
    def __init__(self):
        self._pronomes = {}

        self._pronomes['reto'] = {'1PS': ['eu'], '2PS': ['tu'], '3PS': ['ele', 'ela'], '1PP': ['nós'], '2PP': ['vós'], '3PP': ['eles', 'elas']}

        self._pronomes['oblíquo'] = {}
        self._pronomes['oblíquo']['átono']  = {'1PS': ['me'] , '2PS': ['te'], '3PS': ['se', 'o', 'a', 'lhe'], '1PP': ['nos'], '2PP': ['vos'], '3PP': ['se', 'os', 'as', 'lhes']}
        self._pronomes['oblíquo']['tônico'] = {'1PS': ['mim'], '2PS': ['ti'], '3PS': ['si', 'ele', 'ela']   , '1PP': ['nós'], '2PP': ['vós'], '3PP': ['si', 'eles', 'elas']}

    def get_pessoa_e_caso_do_pronome(self, pronome: str):
        pronome = pronome.lower()
        
        for (pessoa, pronome_reto) in self._pronomes['reto'].items():
            if pronome in pronome_reto:
                return {'pessoa': pessoa, 'caso': 'reto'}

        for (pessoa, pronome_atono) in self._pronomes['oblíquo']['átono'].items():
            if pronome in pronome_atono:
                return {'pessoa': pessoa, 'caso': 'oblíquo átono'}

        for (pessoa, pronome_tonico) in self._pronomes['oblíquo']['tônico'].items():
            if pronome in pronome_tonico:
                return {'pessoa': pessoa, 'caso': 'oblíquo tônico'}

        return {'pessoa': '', 'caso': ''}
