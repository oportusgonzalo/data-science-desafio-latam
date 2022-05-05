
'''Esta función limpia el nombre del pokemon. Para ello, reemplaza - por un espacio y también,
cambia el formato del nombre a "title" para un mejor diseño y comprensión.'''

def clean_name(name):
    if name == 'type-null':
        clean_name = 'Código Cero'
    else:
        clean_name = name.replace('-', ' ').title()
    return clean_name