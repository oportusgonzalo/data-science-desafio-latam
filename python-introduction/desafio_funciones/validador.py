
def validate(opciones, eleccion):
    """Permite determinar si un valor se encuentra incluido en un conjunto de opciones.

    Args:
        opciones (lista): conjunto de opciones
        eleccion (string): valor a verificar
    """
    while eleccion not in opciones:
        eleccion = input('Opción no válida, ingrese una de las opciones válidas: ')

    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    letras = ['a','b','c','d']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(letras, eleccion)
    
    
