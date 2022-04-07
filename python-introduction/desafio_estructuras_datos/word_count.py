import sys

# Especificando desde la línea de comandos el archivo a leer
file_name = sys.argv[1]

# Leyendo archivo .txt
with open(f'{file_name}', 'r') as file:
    texto=file.read()

# Caracteres unicos
chars_ = set(texto)

# Todas las palabras unicas en el archivo se agregan a una lista y se dejan en minúscula
words_list = [word.lower() for word in set(texto.split())]

# Eliminando caracteres especiales ya que generan duplicación de palabras
words = [word.replace('.', '') for word in words_list]
words = [word.replace(',', '') for word in words]

# Selección final de palabras unicas
words = list(set(words))

# print statements
print(f'El número de caracteres distintos es: {len(chars_)}')
print(f'El número de palabras distintas es: {len(words)}')
