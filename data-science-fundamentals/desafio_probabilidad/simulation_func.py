import numpy as np
from pet_simulation import generate_pet

# definimos semilla pseudoaleatoria igual a 1
np.random.seed(1)

def simulate_pets_prob(n):
    # definiciones de contadores de casos
    at_least_one_dog = 0
    old_pet_equal_dog = 0
    both_dogs = 0
    # simulamos n veces
    for i in range(n):
        young_pet = generate_pet()
        old_pet = generate_pet()
        # situacion donde young_pet o old_pet son iguales a un perro
        if young_pet == 'perro' or old_pet == 'perro':
            at_least_one_dog += 1
        # situacion donde old_pet es igual a un perro
        if old_pet == 'perro':
            old_pet_equal_dog += 1
        # situacion donde young y old son iguales a un perro
        if young_pet == 'perro' and old_pet == 'perro':
            both_dogs += 1
    
    # redondeamos probabilidades a dos decimales
    print(f'Probabilidad de obtener al menos una mascota igual a perro: {round(at_least_one_dog/n, 2)}')
    print(f'Probabilidad de que old_pet sea igual a un perro: {round(old_pet_equal_dog/n, 2)}')
    print(f'Probabilidad de ambas mascotas ser iguales a un perro: {round(both_dogs/n, 2)}')


if __name__ == "__main__":
    n = 10000
    simulate_pets_prob(n)

    print()
    print('El escenario menos probable es que ambos perros sean iguales a un perro.')
    print('El escenario mas probable es que yound_pet o old_pet sean iguales a un perro.')

    '''Esto ocurre porque recibir dos resultados iguales toma la intersección de dos eventos. En cambio la posibilidad
    de un evento A o un evento B toma la unión de ambos espacios.'''
    
    