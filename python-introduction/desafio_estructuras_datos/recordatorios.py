# Base para crear el código
recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

# Agregando evento para "Empezar el año"
recordatorios.append(['2021-02-02', '06:00', 'Empezar el Año'])

# Modificando 15 julio --> 16 julio
recordatorios[2][0] = '2021-07-16'

# Eliminando evento del día del trabajo
recordatorios.remove(['2021-05-01', "15:00", "No trabajar"])

# Agregando "cena de navidad y año nuevo"
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

# Ordenando recordatorios
recordatorios = sorted(recordatorios)

for date in recordatorios:
    print(date)
