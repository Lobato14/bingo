import random

# Número de filas y columnas del cartón
FILAS = 3
COLUMNAS = 5
# Números que hay por cartón
NUMEROS_POR_CARTON = FILAS * COLUMNAS
# Rango de números
RANGO_NUMEROS = list(range(1, 91))

def menu() -> str:
    """
    Muestra el menú de opciones del juego de Bingo y solicita al usuario que elija una opción.

    Returns
    -------
    - str: La opción seleccionada por el usuario.
    """
    print("---- BINGO ----\n\n"+
          "1. Jugar\n"+
          "2. Salir\n")
    return input("Escoja una opción: ")

def generar_carton(cantidad:int) -> list:
    """
    Genera uno o más cartones de bingo.

    Parameters
    ----------
    - cantidad : int
        La cantidad de cartones a generar.

    Returns
    -------

    - list: 
        Una lista de cartones generados. Cada cartón es una lista de listas,
        donde cada lista representa una fila del cartón y contiene los números 
        correspondientes.
    """
    cartones = []
    numeros_disponibles = list(RANGO_NUMEROS)

    for _ in range(cantidad):
        numeros_carton = random.sample(numeros_disponibles, NUMEROS_POR_CARTON)
        numeros_disponibles = list(set(numeros_disponibles) - set(numeros_carton))
        carton = [numeros_carton[i:i+COLUMNAS] for i in range(0, NUMEROS_POR_CARTON, COLUMNAS)]
        cartones.append(carton)
    return cartones

def mostrar_cartones(cartones:list, numeros_generados:set) -> None:
    """
    Muestra en consola los cartones de bingo con los números generados.

    Parameters
    ----------

    - cartones : list
        Una lista de cartones. Cada cartón es una lista de listas,
        donde cada lista representa una fila del cartón y contiene 
        los números correspondientes.

    - numeros_generados : set
        Un conjunto de números que ya han sido generados y deben ser marcados con "X".

    Returns
    -------
    - None
    """
    for i, carton in enumerate(cartones, start=1):
        print(f"Cartón {i}:\n")
        for fila in carton:
            for numero in fila:
                if numero in numeros_generados:
                    print("X", end=" ")
                else:
                    print(numero, end=" ")
            print()

def generar_numero(numeros_generados: set) -> int:
    """
    Genera un número aleatorio que no ha sido generado previamente.

    Parameters
    ----------
    - numeros_generados : set
        Un conjunto de números que ya han sido generados.

    Returns
    -------
    - int: El número generado.
    """
    input("Presione Enter para generar un número: ")
    numero = random.choice(list(set(RANGO_NUMEROS) - numeros_generados))
    numeros_generados.add(numero)
    print("Número generado:", numero)
    print("Números generados:", numeros_generados)
    return numero

def verificar_linea(carton:list[list[int]], numeros_generados:set) -> bool:
    """
    Verifica si hay al menos una línea completa en un cartón de bingo.

    Parameters
    ----------

    - carton : list[list[int]]
        Una lista de listas que representa un cartón de bingo.
    - numeros_generados : set
        Un conjunto de números que ya han sido generados.

    Returns
    -------
    - bool: 
        True si hay al menos una línea completa en el cartón, False de lo contrario.
    """
    return any(all(numero in numeros_generados for numero in fila) for fila in carton)

def verificar_bingo(carton:list[list[int]], numeros_generados:set) -> bool:
    """
    Verifica si hay un bingo completo en un cartón de bingo.

    Parameters
    ----------
    - carton : list[list[int]]
        Una lista de listas que representa un cartón de bingo.
    - numeros_generados : set
        Un conjunto de números que ya han sido generados.

    Returns
    -------
    - bool: 
        True si hay un bingo completo en el cartón, False de lo contrario.
    """
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
                generar_numero(numeros_generados)
                mostrar_cartones(cartones, numeros_generados)
                
                lineas_cantadas_carton = [verificar_linea(c, numeros_generados) for c in cartones]

                if any(lineas_cantadas_carton) and lineas_cantadas < 2:
                    try:
                        index_true = lineas_cantadas_carton.index(True)
                        print(f"¡LINEA en el Cartón {index_true + 1}!")
                        lineas_cantadas += 1
                    except ValueError:
                        print("No se han encontrado ninguna línea en ningún cartón")

                if any(lineas_cantadas_carton) and verificar_bingo(cartones[lineas_cantadas_carton.index(True)], numeros_generados):
                    print(f"¡BINGO en el Cartón {lineas_cantadas_carton.index(True) + 1}!")
                    print("Números completos:")
                    for fila in cartones[lineas_cantadas_carton.index(True)]:
                        print(fila)
                    bingo_completo = True

                if bingo_completo:
                    respuesta = input("¿Quieres volver a jugar? (si/no): ").lower()
                    while respuesta not in ['si', 'no']:
                        print("Error: Ingresa 'si' o 'no'.")
                        respuesta = input("¿Quieres volver a jugar? (si/no): ").lower()
                    if respuesta == 'si':
                        numeros_generados.clear()
                    else:
                        break

        opcion = menu()
    print("--- ¡¡¡GRACIAS POR JUGAR!!! ----")