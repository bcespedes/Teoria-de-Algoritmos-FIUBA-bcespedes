import ejercicio2 as ej2
import utilidades as utilidades
from random import seed, randint

CANTIDAD_DE_SETS: int = 10
CANTIDAD_DE_DISTANCIAS: int = 10

def generar_datos_aleatorios(semilla: int, cantidad_de_distancias: int) -> list:

    seed(semilla)
    distancia_max_actual: int = 0
    distancias: list = []

    for _ in range(cantidad_de_distancias):
        distancia = randint(0, ej2.DISTANCIA_MAXIMA + 1)
        distancia_max_actual += distancia
        distancias.append(distancia_max_actual)

    return distancias


def test_aleatorio() -> None:

    utilidades.limpiar_pantalla()
    with open("test_aleatorio.txt", "w") as archivo:
        for i in range(CANTIDAD_DE_SETS):

            distancias: list = generar_datos_aleatorios(i, CANTIDAD_DE_DISTANCIAS)
            paradas: list = ej2.planificar_paradas(distancias)

            print(f"Set aleatorio número {i + 1}:\n")
            print(f"Lista de distancias generada aleatoriamente: {distancias}.")
            utilidades.imprimir_paradas(paradas)

            archivo.write(f"Set aleatorio número {i + 1}:\n\n")
            archivo.write(f"Lista de distancias generada aleatoriamente: {distancias}.\n")
            archivo.write(f"Lista de paradas en base a las distancias: {paradas}.\n\n\n")


test_aleatorio()
