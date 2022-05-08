from get_module import get_info
from clean_names import clean_name

# funcion que extrae atributos base
def get_base_pokemon(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    data = get_info(url)
    data_dict = {
        'id': data['id'],
        'name': clean_name(data['name']),
        'weight': data['weight'],
        'stats_name': [elemento['stat']['name'] for elemento in data['stats']],
        'stats': [elemento['base_stat'] for elemento in data['stats']],
        'types': [elemento['type']['name'] for elemento in data['types']],
        'image': data['sprites']['other']['official-artwork']['front_default']}
    return data_dict

if __name__ == "__main__":
    name = 'charizard'
    print(get_base_pokemon(name))
