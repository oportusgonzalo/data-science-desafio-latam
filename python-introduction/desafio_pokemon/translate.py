from get_module import get_info

'''Esta función toma un nombre y url, ya sea de pokemon, tipo, o especie; genera una consulta a la API y 
retorna el valor de dicho nombre en español.'''

def translate(url):
    data = get_info(url)
    translated = [data['names'][element]['name'] for element in range(0, len(data['names'])) if data['names'][element]['language']['name'] == 'es']
    return translated[0]

if __name__ == "__main__":
    name = 'fire'
    url = f'https://pokeapi.co/api/v2/type/{name}'
    print(translate(url))
