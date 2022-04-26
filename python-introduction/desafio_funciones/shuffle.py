import preguntas as p
import random

def shuffle_alt(pregunta):
    """Toma una pregunta desde preguntas.py (con un nivel y una pregunta definida) y mezcla
    las alternativas. 

    Args:
        pregunta (diccionario): diccionario con enunciado y alternativas.

    Returns:
        Lista de alternativas mezcladas.
    """
    
    random.shuffle(pregunta['alternativas'])
    
    return pregunta['alternativas']

if __name__ == '__main__':
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1']))
    