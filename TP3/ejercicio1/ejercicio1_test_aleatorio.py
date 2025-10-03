import ejercicio1 as ej1
import utilidades as utilidades
from random import seed, randint


CANTIDAD_SETS: int = 20
CANTIDAD_NUMEROS: int = 10


def generar_datos_aleatorios(semilla: int, cantidad_elementos: int) -> str:

    seed(semilla)

    lista_de_numeros: list = []
    numero_limite: int = randint(1, 100)

    for _ in range(cantidad_elementos):
        numero = randint(1, numero_limite)
        lista_de_numeros.append(numero)

    return lista_de_numeros, numero_limite


def test_aleatorio() -> None:

    utilidades.limpiar_pantalla()

    with open("test_aleatorio.txt", "w") as archivo:
        for i in range(CANTIDAD_SETS):
            lista_de_numeros, numero_objetivo = generar_datos_aleatorios(i, CANTIDAD_NUMEROS)
            subconjunto_aproximado, _ = ej1.mejor_subconjunto_aproximado(lista_de_numeros, numero_objetivo)

            utilidades.imprimir_subconjuntos(lista_de_numeros, numero_objetivo, subconjunto_aproximado)
            print("\n\n")

            archivo.write(f"Lista de números disponibles: {lista_de_numeros}.\n")
            archivo.write(f"El valor más próximo al número {numero_objetivo} es {sum(subconjunto_aproximado)}.\n")
            archivo.write(f"Se obtiene sumando los números de la siguiente lista: {subconjunto_aproximado}.\n")
            archivo.write("\n\n\n")


test_aleatorio()