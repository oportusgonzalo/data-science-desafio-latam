import numpy as np
import pandas as pd

'''Al fijar np.random.seed(2) se le entrega un punto de partida constante al generador. Dado ello,
todas las simulaciones posterior a su declaración serán idénticas en cuanto las probabilidades de escoger
perro o gato.'''
np.random.seed(2)

def generate_pet():
    return np.random.choice(['perro', 'gato'])


if __name__ == "__main__":

    n = 20
    df = pd.DataFrame()
    df['pet'] = 0
    for i in range(0, n):
        df.at[i, 'pet'] = generate_pet()
    
    print("La probabilidad de elegir un perro o un gato es:")
    print(df['pet'].value_counts(normalize=True))