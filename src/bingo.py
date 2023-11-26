import random

# Número de filas y columnas del cartón
FILAS = 3
COLUMNAS = 5
# Números que hay por cartón
NUMEROS_POR_CARTON = FILAS * COLUMNAS
# Rango de números
RANGO_NUMEROS = list(range(1, 91))

def menu() -> str:
    print("---- BINGO ----\n\n"+
          "1. Jugar\n"+
          "2. Salir\n")
    return input("Escoja una opción: ")

def generar_carton(cantidad):
    cartones = []
    numeros_disponibles = list(RANGO_NUMEROS)

    for _ in range(cantidad):
        numeros_carton = random.sample(numeros_disponibles, NUMEROS_POR_CARTON)
        numeros_disponibles = list(set(numeros_disponibles) - set(numeros_carton))
        carton = [numeros_carton[i:i+COLUMNAS] for i in range(0, NUMEROS_POR_CARTON, COLUMNAS)]
        cartones.append(carton)
    return cartones

def mostrar_cartones(cartones, numeros_generados):
    for i, carton in enumerate(cartones, start=1):
        print(f"Cartón {i}:\n")
        for fila in carton:
            for numero in fila:
                if numero in numeros_generados:
                    print("X", end=" ")
                else:
                    print(numero, end=" ")
            print()

def generar_numero(numeros_generados):
    numero = random.choice(list(set(RANGO_NUMEROS) - numeros_generados))
    numeros_generados.add(numero)
    print("Número generado:", numero)
    print("Números generados:", numeros_generados)
    return numero

def verificar_linea(carton, numeros_generados):
    return any(all(numero in numeros_generados for numero in fila) for fila in carton)

def verificar_bingo(carton, numeros_generados):
    return all(all(numero in numeros_generados for numero in fila) for fila in carton)

if __name__ == "__main__":
    cartones = []
    numeros_generados = set()
    opcion = menu()
    
    while opcion != "2":
        if opcion == "1":

            cantidad_cartones = input("Ingrese la cantidad de cartones a imprimir (no más de 3): ")
            while not (cantidad_cartones.isdigit() and 1 <= int(cantidad_cartones) <= 3):
                print("Error: Ingrese una cantidad válida (1-3).")
                cantidad_cartones = input("Ingrese la cantidad de cartones a imprimir (no más de 3): ")

            cartones = generar_carton(int(cantidad_cartones))
            mostrar_cartones(cartones, numeros_generados)
            
            bingo_completo = False
            lineas_cantadas = 0

            while not bingo_completo:

                input("Presione Enter para generar un número: ")
                numero_generado = generar_numero(numeros_generados)
                mostrar_cartones(cartones, numeros_generados)

                # Es una lista de booleanos que indica si se ha cantado una línea en cada cartón.
                lineas_cantadas_carton = [verificar_linea(c, numeros_generados) for c in cartones]

                if any(lineas_cantadas_carton) and lineas_cantadas < 2:
                    # Se utiliza para encontrar el índice de la primera ocurrencia de True en la 
                    # lista lineas_cantadas_carton
                    print(f"¡LINEA en el Cartón {lineas_cantadas_carton.index(True) + 1}!")
                    lineas_cantadas += 1

                if verificar_bingo(cartones[lineas_cantadas_carton.index(True)], numeros_generados):
                    print(f"¡BINGO en el Cartón {lineas_cantadas_carton.index(True) + 1}!")
                    print("Números completos:")
                    for fila in cartones[lineas_cantadas_carton.index(True)]:
                        print(fila)
                    bingo_completo = True

                if bingo_completo:
                    respuesta = input("¿Quieres volver a jugar? (s/n): ")
                    if respuesta.lower() == 'si':
                        numeros_generados.clear()
                    else:
                        exit()

        opcion = menu()
    print("--- ¡¡¡GRACIAS POR JUGAR!!! ----")