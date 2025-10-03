import ejercicio2 as ej2
import utilidades as utilidades
from time import time

DISTANCIAS_MAXIMAS: list = [
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

def generar_datos(distancia_maxima: int) -> list:

    distancias: list = []

    for i in range(ej2.DISTANCIA_MAXIMA, distancia_maxima + 1, ej2.DISTANCIA_MAXIMA):
        distancias.append(i)

    return distancias


def test_tiempo_de_ejecucion() -> None:

    utilidades.limpiar_pantalla()
    for distancia in DISTANCIAS_MAXIMAS:
        distancias: list = generar_datos(distancia)
        tiempo_inicial: float = time()
        _: list = ej2.planificar_paradas(distancias)
        tiempo_final: float = time()

        tiempo_de_ejecucion: float = tiempo_final - tiempo_inicial

        print(f"Para n = {distancia // 7}:")
        print(f"Tiempo de ejecución: {tiempo_de_ejecucion} segundos.")
        print("\n\n")


test_tiempo_de_ejecucion()
