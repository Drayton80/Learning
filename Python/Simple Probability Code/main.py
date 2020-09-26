dice_maximum = 4

def num_successes(dices_values_list):
    num_successes = 0
    
    for value in dices_values_list:
        if value in [dice_maximum]:
            num_successes += 1
        
    return num_successes


def show_probabilities(dices_values, total_failures, total_normals, total_successes, total_precises, total_superiors):
    total_probabilities = dice_maximum**len(dices_values)

    print("Probabilidade de Sucesso Normal   = " + str(total_normals) + "/" + str(total_probabilities) + " = " + str((total_normals/total_probabilities)*100) + " %")
    print("Probabilidade de Sucesso Preciso  = " + str(total_precises) + "/" + str(total_probabilities) + " = " + str((total_precises/total_probabilities)*100) + " %")
    print("Probabilidade de Sucesso Superior = " + str(total_superiors) + "/" + str(total_probabilities) + " = " + str((total_superiors/total_probabilities)*100) + " %")
    print("Probabilidade de Falhas Normals   = " + str(total_failures) + "/" + str(total_probabilities) + " = " + str((total_failures/total_probabilities)*100) + " %" + "\n")


def sum_totals(total_successes, total_failures, total_normals, total_precises, total_superiors):
    if total_successes == 0:
        total_failures += 1
    elif total_successes == 1:
        total_normals += 1
    elif total_successes in [2,3]:
        total_precises += 1
    else:
        total_superiors += 1

    return (total_failures, total_normals, total_precises, total_superiors)

def prob_1dices(dice_range):
    dices_values = [0]
    total_failures = 0
    total_normals = 0
    total_precises = 0
    total_superiors = 0

    print("PROBABILIDADES PARA " + str(len(dices_values)) + "d" + str(dice_maximum) + " de ACERTO")
    
    for dices_values[0]  in dice_range:      
        total_successes = num_successes(dices_values)

        (total_failures, total_normals, total_precises, total_superiors) = sum_totals(total_successes, total_failures, total_normals, total_precises, total_superiors)
    
    show_probabilities(dices_values, total_failures, total_normals, total_successes, total_precises, total_superiors)

def prob_2dices(dice_range):
    dices_values = [0,0]
    total_failures = 0
    total_normals = 0
    total_precises = 0
    total_superiors = 0

    print("PROBABILIDADES PARA " + str(len(dices_values)) + "d" + str(dice_maximum) + " de ACERTO")
    
    for dices_values[0]  in dice_range:      
        total_successes = 0
        
        for dices_values[1] in dice_range:
            total_successes = num_successes(dices_values)

            (total_failures, total_normals, total_precises, total_superiors) = sum_totals(total_successes, total_failures, total_normals, total_precises, total_superiors)
    
    show_probabilities(dices_values, total_failures, total_normals, total_successes, total_precises, total_superiors)


def prob_3dices(dice_range):
    dices_values = [0,0,0]
    total_failures = 0
    total_normals = 0
    total_precises = 0
    total_superiors = 0

    print("PROBABILIDADES PARA " + str(len(dices_values)) + "d" + str(dice_maximum) + " de ACERTO")
    
    for dices_values[0] in dice_range:       
        total_successes = 0

        for dices_values[1] in dice_range:
            for dices_values[2] in dice_range:
                total_successes = num_successes(dices_values)

                (total_failures, total_normals, total_precises, total_superiors) = sum_totals(total_successes, total_failures, total_normals, total_precises, total_superiors)
    
    show_probabilities(dices_values, total_failures, total_normals, total_successes, total_precises, total_superiors)


def prob_4dices(dice_range):
    dices_values = [0,0,0,0]
    total_failures = 0
    total_normals = 0
    total_precises = 0
    total_superiors = 0

    print("PROBABILIDADES PARA " + str(len(dices_values)) + "d" + str(dice_maximum) + " de ACERTO")
    
    for dices_values[0] in dice_range:       
        total_successes = 0

        for dices_values[1] in dice_range:
            for dices_values[2] in dice_range:
                for dices_values[3] in dice_range:
                    total_successes = num_successes(dices_values)

                    (total_failures, total_normals, total_precises, total_superiors) = sum_totals(total_successes, total_failures, total_normals, total_precises, total_superiors)
    
    show_probabilities(dices_values, total_failures, total_normals, total_successes, total_precises, total_superiors)


def prob_5dices(dice_range):
    dices_values = [0,0,0,0,0]
    total_failures = 0
    total_normals = 0
    total_precises = 0
    total_superiors = 0

    print("PROBABILIDADES PARA " + str(len(dices_values)) + "d" + str(dice_maximum) + " de ACERTO")
    
    for dices_values[0] in dice_range:       
        total_successes = 0

        for dices_values[1] in dice_range:
            for dices_values[2] in dice_range:
                for dices_values[3] in dice_range:
                    for dices_values[4] in dice_range:
                        total_successes = num_successes(dices_values)

                        (total_failures, total_normals, total_precises, total_superiors) = sum_totals(total_successes, total_failures, total_normals, total_precises, total_superiors)
    
    show_probabilities(dices_values, total_failures, total_normals, total_successes, total_precises, total_superiors)


def prob_6dices(dice_range):
    dices_values = [0,0,0,0,0,0]
    total_failures = 0
    total_normals = 0
    total_precises = 0
    total_superiors = 0

    print("PROBABILIDADES PARA " + str(len(dices_values)) + "d" + str(dice_maximum) + " de ACERTO")
    
    for dices_values[0] in dice_range:       
        total_successes = 0

        for dices_values[1] in dice_range:
            for dices_values[2] in dice_range:
                for dices_values[3] in dice_range:
                    for dices_values[4] in dice_range:
                        for dices_values[5] in dice_range:
                            total_successes = num_successes(dices_values)

                            (total_failures, total_normals, total_precises, total_superiors) = sum_totals(total_successes, total_failures, total_normals, total_precises, total_superiors)
    
    show_probabilities(dices_values, total_failures, total_normals, total_successes, total_precises, total_superiors)


def prob_7dices(dice_range):
    dices_values = [0,0,0,0,0,0,0]
    total_failures = 0
    total_normals = 0
    total_precises = 0
    total_superiors = 0

    print("PROBABILIDADES PARA " + str(len(dices_values)) + "d" + str(dice_maximum) + " de ACERTO")
    
    for dices_values[0] in dice_range:       
        total_successes = 0

        for dices_values[1] in dice_range:
            for dices_values[2] in dice_range:
                for dices_values[3] in dice_range:
                    for dices_values[4] in dice_range:
                        for dices_values[5] in dice_range:
                            for dices_values[6] in dice_range:
                                total_successes = num_successes(dices_values)

                                (total_failures, total_normals, total_precises, total_superiors) = sum_totals(total_successes, total_failures, total_normals, total_precises, total_superiors)
    
    show_probabilities(dices_values, total_failures, total_normals, total_successes, total_precises, total_superiors)


def prob_8dices(dice_range):
    dices_values = [0,0,0,0,0,0,0,0]
    total_failures = 0
    total_normals = 0
    total_precises = 0
    total_superiors = 0

    print("PROBABILIDADES PARA " + str(len(dices_values)) + "d" + str(dice_maximum) + " de ACERTO")
    
    for dices_values[0] in dice_range:       
        total_successes = 0

        for dices_values[1] in dice_range:
            for dices_values[2] in dice_range:
                for dices_values[3] in dice_range:
                    for dices_values[4] in dice_range:
                        for dices_values[5] in dice_range:
                            for dices_values[6] in dice_range:
                                for dices_values[7] in dice_range:
                                    total_successes = num_successes(dices_values)

                                    (total_failures, total_normals, total_precises, total_superiors) = sum_totals(total_successes, total_failures, total_normals, total_precises, total_superiors)
    
    show_probabilities(dices_values, total_failures, total_normals, total_successes, total_precises, total_superiors)

dice_range = range(1,dice_maximum+1)

prob_1dices(dice_range)
prob_2dices(dice_range)
prob_3dices(dice_range)
prob_4dices(dice_range)
prob_5dices(dice_range)
prob_6dices(dice_range)
prob_7dices(dice_range)
prob_8dices(dice_range)

    

    

