from get_module import get_info
import random

# funcion que permite extraer atributos relacionados a la especie
def get_species(name):
    url = f'https://pokeapi.co/api/v2/pokemon-species/{name}'
    data = get_info(url)
    data_species = {
        'etapa_previa': [data['evolves_from_species']['name'] if data['evolves_from_species'] else False],
        'is_baby': data['is_baby'], 
        'is_legendary': data['is_legendary'], 
        'is_mythical': data['is_mythical'],
        # seleccionamos aleatoriamente una descripcion desde una lista de descripciones que cumplen el criterio
        # de estar en idioma español
        'flavor_text_entries': random.choice([data['flavor_text_entries'][element]['flavor_text'].strip('\n').replace('\n', ' ') for element in range(0, len(data['flavor_text_entries'])) if data['flavor_text_entries'][element]['language']['name'] == 'es'])
    }
    return data_species

if __name__ == "__main__":
    name = 'charizard'
    print(get_species(name))