import sys

clp_sol = float(sys.argv[1])
clp_arg = float(sys.argv[2])
clp_usd = float(sys.argv[3])
monto = float(sys.argv[4])

total_soles = clp_sol * monto
total_peso_argentino = clp_arg * monto
total_usd = clp_usd * monto

print(f'Los {monto} pesos equivalen a: \n {total_soles} Soles \n {total_peso_argentino} Pesos Argentinos \n {total_usd} Dólares')

