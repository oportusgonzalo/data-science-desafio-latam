import preguntas as p

def print_pregunta(enunciado, alternativas):
    
    print('{}\n'.format(enunciado[0]))
    
    letras = ['A', 'B', 'C', 'D']
    i = 0
    for alternativa in alternativas:
        print('{}. {}'.format(letras[i], alternativa[0]))
        i += 1
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4