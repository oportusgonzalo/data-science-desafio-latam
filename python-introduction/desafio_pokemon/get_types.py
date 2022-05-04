from get_module import get_info
from translate import translate

'''Función recibe como input un type (fuego, bicho, etc) --> id o nombre del tipo'''

def get_types_info(type):
    url = f'https://pokeapi.co/api/v2/type/{type}'
    data = get_info(url)
    
    # obtenemos fortalezas y debilidades desde damage_relations en la seccion 'type' en ingles
    data_types_en = {
        'double_damage_from': [data['damage_relations']['double_damage_from'][element]['name'] for element in range(0, len(data['damage_relations']['double_damage_from']))],
        'double_damage_to': [data['damage_relations']['double_damage_to'][element]['name'] for element in range(0, len(data['damage_relations']['double_damage_to']))],
        'half_damage_from': [data['damage_relations']['half_damage_from'][element]['name'] for element in range(0, len(data['damage_relations']['half_damage_from']))],
        'half_damage_to': [data['damage_relations']['half_damage_to'][element]['name'] for element in range(0, len(data['damage_relations']['half_damage_to']))],
        'no_damage_from': [data['damage_relations']['no_damage_from'][element]['name'] for element in range(0, len(data['damage_relations']['no_damage_from']))],
        'no_damage_to': [data['damage_relations']['no_damage_to'][element]['name'] for element in range(0, len(data['damage_relations']['no_damage_to']))]}
    
    # transformamos a español cada fortaleza y debilidad haciendo uso de la funcion translate
    base_url = 'https://pokeapi.co/api/v2/type/'
    data_types = {
        'double_damage_from': [translate(name=value, url=base_url + value) for value in data_types_en['double_damage_from']],
        'double_damage_to': [translate(name=value, url=base_url + value) for value in data_types_en['double_damage_to']],
        'half_damage_from': [translate(name=value, url=base_url + value) for value in data_types_en['half_damage_from']],
        'half_damage_to': [translate(name=value, url=base_url + value) for value in data_types_en['half_damage_to']],
        'no_damage_from': [translate(name=value, url=base_url + value) for value in data_types_en['no_damage_from']],
        'no_damage_to': [translate(name=value, url=base_url + value) for value in data_types_en['no_damage_to']],
        'type_es': translate(name=type, url=base_url + type)
    }    

    return data_types

if __name__ == "__main__":
    name = 'fire'
    print(get_types_info(name))