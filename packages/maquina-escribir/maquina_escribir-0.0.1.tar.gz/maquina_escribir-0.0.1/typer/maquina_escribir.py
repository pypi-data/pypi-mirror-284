import time
import os

def maquina(texto):
    os.system('clear')
    for t in texto:
        print(t, end="", flush=True)
        time.sleep(0.1)
    print()
    return texto

if __name__ == '__main__':
    maquina('hola, que tal mundo')