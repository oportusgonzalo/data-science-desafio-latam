import numpy as np
import pandas as pd


# 1.1 Array con numeros entre 1 y 50
array_1_50 = np.linspace(1, 50)

# 1.2 Array con numeros entre 50 y 150 (agregamos num=101 para que los numeros sean enteros con diferencia de 1)
array_50_150 = np.linspace(50, 150, num=101)

# 2. loop que especifica par o impar
for value in array_1_50:
    if value % 2 == 0:
        pass
        print(f'El valor {value} es par.')
    else:
        pass
        print(f'El valor {value} es impar.')

# 3. loop con condiciones en segundo array
div_2_o_3 = []
div_2_y_3 = []
div_3_no_2 = []
no_2_no_3 = []

for value in array_50_150:
    if (value % 2 == 0) or (value % 3 == 0):
        div_2_o_3.append(value)
    if (value % 2 == 0) and (value % 3 == 0):
        div_2_y_3.append(value)
    if  (value % 3 == 0) and (value % 2 != 0):
        div_3_no_2.append(value)
    if (value % 2 != 0) and (value % 3 != 0):
        no_2_no_3.append(value)

print(f'Existen {len(div_2_o_3)} numeros divisibles por 2 o 3.')
print(f'Existen {len(div_2_y_3)} numeros divisibles por 2 y 3.')
print(f'Existen {len(div_3_no_2)} numeros divisibles por 3 y no por 2.')
print(f'Existen {len(no_2_no_3)} numeros no divisibles por 2 y 3.')

# 4. Correcion a:

'''
for i in range(100): --> I no esta definido. debe ser: print(i**2)
    print(I**2)'''

for i in range(100):
    print(i**2)

# 5. Clasificacion de meses con cantidad de pasajeros menor a la media
flights = pd.read_csv('flights.csv')

media = flights['passengers'].mean()
flights['underperforming'] = 0

'''iteramos sobre filas y asignamos 1 a 'underperforming' en caso de ser menor a la media'''
for idx, row in flights.iterrows():
    if row['passengers'] < media:
        flights.at[idx, 'underperforming'] = 1

# 6. Clasificación de meses donde la cantidad de pasajeros escapa de la tendencia
media = flights['passengers'].mean()
desv = flights['passengers'].std()
flights['outlier'] = 0

'''iteramos sobre filas y asignamos 1 a 'outlier' en caso de escaparse de la tendencia'''
count_outliers = 0
for idx, row in flights.iterrows():
    if row['passengers'] < (media-desv):
        flights.at[idx, 'outlier'] = 1
        count_outliers +=1
    elif row['passengers'] > (media+desv):
        flights.at[idx, 'outlier'] = 1
        count_outliers +=1

print(f'Existen {count_outliers} observaciones clasificables como casos extremos.')
