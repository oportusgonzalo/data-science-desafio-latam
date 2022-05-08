
import sys
import webbrowser
import os
import time

# funcion que permite ejecutar el archivo html en un navegador
# reconoce sistema operativo
def show_pics(html, nombre):
    with open(f'{nombre}.html','w') as f:
        f.write(html)
    print('Las fotos se mostrarán en tu Navegador...')
    time.sleep(2)
    if sys.platform == "darwin":
        webbrowser.get('chrome').open(f'file://{sys.path[0]}/{nombre}.html')
    else:
        webbrowser.open(f'{nombre}.html')
    time.sleep(5)
    os.remove(f'{nombre}.html')
    