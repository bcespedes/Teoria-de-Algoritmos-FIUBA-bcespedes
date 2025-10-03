import ejercicio1 as ej1
import utilidades as utilidades
from random import seed, randint


CANTIDAD_ITERACIONES = 20
LONGITUD_LISTA = 25
LISTA_CASO_BORDE = [100000, 99999, 99999]
OBJETIVO_CASO_BORDE = 199998


def elegir_numero(texto: str) -> int:

    opcion: int = 0

    while True:
        opcion: str = input(texto)
        if not opcion.isdigit() or int(opcion) < 0:
            utilidades.limpiar_pantalla()
            print("Ingresó algo que no es válido. Intente nuevamente.\n")
        elif int(opcion) == 0:
            utilidades.limpiar_pantalla()
            break
        elif int(opcion) > 0:
            utilidades.limpiar_pantalla()
            break
    
    return int(opcion)


def generar_datos(longitud_lista: int) -> tuple:

    numeros_disponibles: list = list()
    numero_objetivo: int = randint(1, longitud_lista * 10)
    for _ in range(longitud_lista):
        numero: int = randint(1, longitud_lista * 7)
        numeros_disponibles.append(numero)
    
    return numeros_disponibles, numero_objetivo


def mostrar_caso_borde() -> None:

    subconjunto_aproximado, suma_aproximada = ej1.mejor_subconjunto_aproximado(LISTA_CASO_BORDE, OBJETIVO_CASO_BORDE)
    subconjunto_exacto, suma_exacta = ej1.mejor_subconjunto_exacto(LISTA_CASO_BORDE, OBJETIVO_CASO_BORDE)

    print("\n\n===== CASO BORDE =====")
    utilidades.imprimir_subconjuntos(LISTA_CASO_BORDE, OBJETIVO_CASO_BORDE, subconjunto_aproximado)
    print(f"Solución exacta: {subconjunto_exacto}, {suma_exacta}.")
    print(f"La solución aproximada es un {round(suma_aproximada / suma_exacta * 100, 2)}% de la óptima.")
    print("\n\n")


def test_garantia() -> None:

    utilidades.limpiar_pantalla()
    longitud_lista: int = elegir_numero("Ingrese una longitud de lista de números (se recomienda ingresar un valor no mayor a 20, 0 para finalizar la ejecución): ")
    utilidades.limpiar_pantalla()

    if longitud_lista == 0:
        print("Se terminó la ejecución del programa.\n\n")
        return
    cantidad_iteraciones: int = elegir_numero("Ingrese la cantidad de iteraciones (0 para finalizar la ejecución): ")
    if cantidad_iteraciones == 0:
        print("Se terminó la ejecución del programa.\n\n")
        return

    for i in range(cantidad_iteraciones):
        seed(i)
        numeros_disponibles, numero_objetivo = generar_datos(longitud_lista)
        subconjunto_aproximado, suma_aproximada = ej1.mejor_subconjunto_aproximado(numeros_disponibles, numero_objetivo)
        subconjunto_exacto, suma_exacta = ej1.mejor_subconjunto_exacto(numeros_disponibles, numero_objetivo)
        print(f"=== Iteración número {i + 1} ===")
        utilidades.imprimir_subconjuntos(numeros_disponibles, numero_objetivo, subconjunto_aproximado)
        print(f"Solución exacta: {subconjunto_exacto}, {suma_exacta}.")
        if suma_aproximada == suma_exacta:
            print(f"La solución aproximada coincide con la óptima.\n")
        else:
            print(f"La solución aproximada es un {round(suma_aproximada / suma_exacta * 100, 2)}% de la óptima.\n")

    mostrar_caso_borde()


test_garantia()