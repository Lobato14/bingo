import random

# Número de filas y columnas del cartón
FILAS = 3
COLUMNAS = 9
# Números que hay por cartón
NUMEROS_POR_CARTON = FILAS * COLUMNAS
# Rango de numeros
RANGO_NUMEROS = range(1, 91)

def menu() -> str:
    print("---- BINGO ----\n\n"+
          "1. Jugar\n"+
          "2. Salir\n")
    return input("Escoja una opción: ")
    

def generar_carton(cantidad):
    """
    Genera un cartón de bingo con FILAS filas y COLUMNAS columnas.
    Cada columna contendrá 5 números aleatorios del 1 al 90.

    Returns
    -------
    list of lists: Un cartón de bingo representado como una lista de listas.
    """
    cartones = []
    numeros_disponibles = list(RANGO_NUMEROS)

    for _ in range(cantidad):

        # Selecciona 15 números aleatorios sin repetir
        numeros_carton = random.sample(numeros_disponibles, NUMEROS_POR_CARTON)
        numeros_disponibles = list(set(numeros_disponibles) - set(numeros_carton))
        
        # Organiza los números en filas y columnas
        carton = [numeros_carton[i:i+COLUMNAS] for i in range(0, NUMEROS_POR_CARTON, COLUMNAS)]
        cartones.append(carton)
    return cartones

def mostrar_cartones(cartones):
    for i, carton in enumerate(cartones, start=1):
        print(f"Cartón {i}:")
        for fila in carton:
            print(fila)

if __name__ == "__main__":

    opcion = menu()

    while opcion != "2":

        if opcion == "1":
            pass
        opcion = menu()

    print("---¡¡¡GRACIAS POR JUGAR!!!----")