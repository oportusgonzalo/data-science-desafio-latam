from poke_validation import validate
import data as d

# solicitamos al usuario ingresar el nombre de un Pokémon
# nos hacemos cargo de la limpieza del nombre
pokemon = input("Ingrese el nombre de un Pokémon. Nota: Si el pokémon tiene espacios reemplace por '-'. No coloque ningún tipo de signo de puntuación adicional: ").lower()

if pokemon == "type-null":
    pokemon = "codigo-cero"

# verificamos la existencia de puntuación o espacios en el nombre ingresado
while '.' in pokemon or ' ' in pokemon:
    pokemon = input("El nombre ingresado no es válido. Ingrese nuevamente el nombre de un Pokémon: ")

# validar nombre(existencia)
pokemon = validate(pokemon)

for key, url in d.key_url_dict.items():
    pass
    #get_info(url)

