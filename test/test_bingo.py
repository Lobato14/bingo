from src.bingo import generar_carton, generar_numero, verificar_linea, verificar_bingo

def test_generar_carton():
    cartones = generar_carton(2)
    assert len(cartones) == 2
    for carton in cartones:
        assert len(carton) == 3
        for fila in carton:
            assert len(fila) == 5

def test_generar_numero():
    numeros_generados = set()
    numero = generar_numero(numeros_generados)
    assert 1 <= numero <= 90
    assert numero in numeros_generados

def test_verificar_linea():
    carton = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]
    numeros_generados = {1, 2, 3, 4, 5}
    assert verificar_linea(carton, numeros_generados)

def test_verificar_bingo():
    carton = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]
    numeros_generados = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
    assert verificar_bingo(carton, numeros_generados)