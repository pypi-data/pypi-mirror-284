# este archivo se trata de definir mi kata, La kata que me toco es la 14 que lo que quiere decir es (For this kata, try implementing a trigram algorithm that generates a couple of hundred words of text using a book-sized file as input. )

import sys
import os

# Añade el directorio raíz del proyecto al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Ahora puedes importar el módulo generar_trigramas desde src.domain
from domain import generar_trigramas

def main():
    parrafo = input("Ingresa un párrafo: ")
    trigramas = generar_trigramas(parrafo)
    for clave, valor in trigramas.items():
        print(f"{clave}: {', '.join(valor)}")

if __name__ == "__main__":
    main()
