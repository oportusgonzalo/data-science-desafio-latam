import pandas as pd
import numpy as np

def media(x):
    """Función que calcula la media de un arreglo. Calcula primero la suma, y luego divide por el número de valores
    en el vector.

    Args:
        x (Array): Arreglo de valores.

    Returns:
        float: media de un vector.
    """
    sum_ = np.sum(x)
    mean_val = sum_ / len(x)
    return mean_val

def varianza(x):
    """Función que calcula la varianza de un vector. Calcula la media llamando a la función de arriba, calcula la
    operacion del numerador: (valor-media) al cuadrado, para cada número; y luego de calcular la suma de estos valores,
    divide por N-1.

    Args:
        x (array): Arreglo de valores.

    Returns:
        Float: Varianza del vector.
    """
    mean_val = np.mean(x)
    sqr_vals = [(val-mean_val)**2  for val in x]
    sum_ = np.sum(sqr_vals)
    varianza = sum_ / (len(x)-1)
    return varianza


if __name__ == "__main__":

    df = pd.read_csv('worldcup2014.csv')

    # obtenemos información sobre columnas solicitadas (dataset worldcup)
    cols = ['goles_favor', 'goles_contra', 'puntos']
    for col in cols:
        print(f'Media {col}: {media(df[col])}')
        print(f'Varianza {col}: {varianza(df[col])}')
