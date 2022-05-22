import pandas as pd
import numpy as np

df = pd.read_csv('worldcup2014.csv')

# dataframe con media de las variables solicitadas
df_temp1 = df.groupby('continent').agg({'goles_favor': np.mean, 'goles_contra': np.mean, 'puntos': np.mean}).reset_index()

# dataframe con varianza de las variables solicitadas
df_temp2 = df.groupby('continent').agg({'goles_favor': np.var, 'goles_contra': np.var, 'puntos': np.var}).reset_index()

# dataframe con desviación estándar de las variables solicitadas
df_temp3 = df.groupby('continent').agg({'goles_favor': np.std, 'goles_contra': np.std, 'puntos': np.std}).reset_index()

# insights
df_add = df.groupby('continent').agg({'goles_favor': sum, 'goles_contra': sum}).reset_index()
df_favor = df_add.sort_values(by='goles_favor', ascending=False).reset_index(drop=True)
df_contra = df_add.sort_values(by='goles_contra', ascending=False).reset_index(drop=True)
df_temp1 = df_temp1.sort_values(by='puntos', ascending=False).reset_index(drop=True)

print(f'La mayor cantidad de goles a favor se observa en: {df_favor["continent"][0]}')
print(f'La mayor cantidad de goles en contra se observa en: {df_contra["continent"][0]}')
print(f'La mayor cantidad de puntos en promedio se observa en: {df_temp1["continent"][0]}')
