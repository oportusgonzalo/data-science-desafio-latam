from string import ascii_lowercase
import getpass

password = getpass.getpass("Ingrese la clave secreta: ")
password = password.lower()

contador = 0
for letra in password:
    for key in ascii_lowercase:
        contador += 1
        if letra == key:
            break

print(f"La contraseña fue forzada en {contador} intentos")
