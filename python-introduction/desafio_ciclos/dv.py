
rut = list(input("Ingresa tu RUT sin puntos ni dígito verificador: "))
serie = list(range(2, 7 + 1))

# invertimos el rut
rut_ = rut[::-1]
rut_ = [int(x) for x in rut_]

suma = 0
for tupla in enumerate(rut_):
    if tupla[0] > 5:
        posicion = tupla[0] - 6
        suma += tupla[1] * serie[posicion]
    else:
        suma += tupla[1] * serie[tupla[0]]

mod_11 = suma % 11
resto = 11 - mod_11

if resto == 10:
    dv = 'k'
elif resto == 11:
    dv = 0
else:
    dv = resto

print(f"Su dígito verificador es {dv}")
