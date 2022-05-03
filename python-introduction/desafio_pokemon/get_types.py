from get_module import get_info
import random


'''Función recibe como input un type (fuego, bicho, etc) --> id o nombre del tipo'''
def get_types_info(type):
    url = f'https://pokeapi.co/api/v2/type/{type}'
    data = get_info(url)
    data_types = {
        'damage_relations': data['damage_relations']
    }
    return data_types

if __name__ == "__main__":
    name = 'charizard'
    print(get_types_info(name))