def choose_level(n_pregunta, p_level):
    """Permite escoger el nivel de dificultar de la pregunta a realizar.

    Args:
        n_pregunta (int): numero de la pregunta
        p_level (int): numero de preguntas por nivel (rango=1,..,3)
    """
    global level

    if p_level == 1:
        if n_pregunta == 1:
            level = 'basicas'
        elif n_pregunta == 2:
            level = 'intermedias'
        elif n_pregunta == 3:
            level = 'avanzadas'
    elif p_level == 2:
        if n_pregunta == 1 or n_pregunta == 2:
            level = 'basicas'
        elif n_pregunta == 3 or n_pregunta == 4:
            level = 'intermedias'
        elif n_pregunta == 5 or n_pregunta == 6:
            level = 'avanzadas'
    elif p_level == 3:
        if n_pregunta == 1 or n_pregunta == 2 or n_pregunta == 3:
            level = 'basicas'
        elif n_pregunta == 4 or n_pregunta == 5 or n_pregunta == 6:
            level = 'intermedias'
        elif n_pregunta == 7 or n_pregunta == 8 or n_pregunta == 9:
            level = 'avanzadas'
    else:
        print('Número de preguntas por nivel fuera de rango.')
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(6, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias