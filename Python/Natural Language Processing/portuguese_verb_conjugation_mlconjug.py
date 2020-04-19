import mlconjug

# Set the conjugator defining the language:
conjugator = mlconjug.Conjugator(language="pt")
# Get all the possible conjugations organized in a dictionary 
# formated in the way of modo verbal>tempo verbal>pessoa verbal
verbo_ver_information = conjugator.conjugate("ver").conjug_info

# Printing every single verb
for modo_verbal, tempos_verbais in verbo_ver_information.items():
    print(str(modo_verbal), ':', sep='')

    for tempo_verbal, pessoas_verbais in tempos_verbais.items():
        print(tempo_verbal, ':', sep='')

        for pessoa_verbal in pessoas_verbais.items():
            print(pessoa_verbal)
