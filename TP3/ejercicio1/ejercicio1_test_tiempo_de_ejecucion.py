import ejercicio1 as ej1
import utilidades as utilidades
from time import time


NUMEROS_DISPONIBLES: list = [
    20000000, 22000000, 24000000, 26000000, 28000000,
    30000000, 32000000, 34000000, 36000000, 38000000,
    40000000, 42000000, 44000000, 46000000, 48000000,
    50000000, 52000000, 54000000, 56000000, 58000000,
    60000000, 62000000, 64000000, 66000000, 68000000,
    70000000, 72000000, 74000000, 76000000, 78000000,
    80000000, 82000000, 84000000, 86000000, 88000000,
    90000000, 92000000, 94000000, 96000000, 98000000,
    100000000
]


def generar_datos(cantidad_numeros: int) -> str:

    numeros: list = []

    for i in range(cantidad_numeros):
        numeros.append(i + 1)

    return numeros


def test_tiempo_de_ejecucion() -> None:

    utilidades.limpiar_pantalla()

    with open("test_tiempos_de_ejecucion.txt", "w") as archivo:
        for cantidad_numeros in NUMEROS_DISPONIBLES:
            numeros_disponibles: list = generar_datos(cantidad_numeros)
            tiempo_inicial: float = time()
            _: tuple = ej1.mejor_subconjunto_aproximado(numeros_disponibles, cantidad_numeros)
            tiempo_final: float = time()

            tiempo_de_ejecucion: float = tiempo_final - tiempo_inicial

            print(f"Para una cantidad de números = {cantidad_numeros}:")
            print(f"Tiempo de ejecución: {tiempo_de_ejecucion} segundos.")
            print("\n\n")

            archivo.write(f"{tiempo_de_ejecucion}\n")


test_tiempo_de_ejecucion()