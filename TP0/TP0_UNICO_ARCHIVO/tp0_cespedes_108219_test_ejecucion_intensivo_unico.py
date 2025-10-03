from time import time
from math import isqrt
from os import system, name


def limpiar_pantalla() -> None:

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def imprimir_resultados(resultados: list, cantidad_de_cuartetos: int) -> None:

    print(f"Cuartetos de números primos encontrados:\n")
    print(*resultados, sep = "\n")
    print(f"\nSe encontraron {cantidad_de_cuartetos} cuartetos de números primos.\n\n")


def elegir_opcion(texto: str, opcion_minima: int, opcion_maxima: int) -> int:

    while True:
        opcion: str = input(texto)
        if not opcion.isdigit() or int(opcion) < opcion_minima or int(opcion) > opcion_maxima:
            limpiar_pantalla()
            print("Ingresó algo que no es válido. Intente nuevamente.\n")
        elif int(opcion) >= opcion_minima and int(opcion) <= opcion_maxima:
            return int(opcion)


def es_primo(numero_a_analizar: int) -> bool:

    if numero_a_analizar < 2:
        return False
    if numero_a_analizar in (2, 3):
        return True
    if numero_a_analizar % 2 == 0 or numero_a_analizar % 3 == 0:
        return False

    limite_divisor: int = isqrt(numero_a_analizar) + 1

    for i in range(5, limite_divisor, 6):
        if numero_a_analizar % i == 0 or numero_a_analizar % (i + 2) == 0:
            return False

    return True


def encontrar_cuartetos_de_numeros_primos_1(limite: int) -> float:

    tiempo_inicial: float = time()
    cantidad_de_cuartetos: int = 0
    resultados: list = []

    for i in range(11, limite, 30):

        primer_candidato: int = i
        segundo_candidato: int = i + 2
        tercer_candidato: int = i + 6
        cuarto_candidato: int = i + 8

        if es_primo(primer_candidato) and es_primo(segundo_candidato) and es_primo(tercer_candidato) and es_primo(cuarto_candidato):
            resultados.append(f"{primer_candidato} - {segundo_candidato} - {tercer_candidato} - {cuarto_candidato}")
            cantidad_de_cuartetos += 1

    tiempo_final: float = time()
    tiempo_de_ejecucion: float = tiempo_final - tiempo_inicial
    imprimir_resultados(resultados, cantidad_de_cuartetos)

    return tiempo_de_ejecucion


def criba_de_eratostenes(limite: int) -> bytearray:

    limite_divisor: int = isqrt(limite) + 1
    limite += 1
    primos: bytearray = bytearray([True]) * limite
    primos[0] = False
    primos[1] = False

    for i in range(2, limite_divisor):
        if primos[i]:
            cuadrado = i ** 2
            primos[cuadrado:limite:i] = [False] * len(range(cuadrado, limite, i))

    return primos


def encontrar_cuartetos_de_numeros_primos_2(limite: int) -> float:

    tiempo_inicial: float = time()
    primos: bytearray = criba_de_eratostenes(limite)
    cantidad_de_cuartetos: int = 0
    resultados: list = []
    limite -= 8

    for i in range(11, limite, 30):
    
        primer_candidato: int = i
        segundo_candidato: int = i + 2
        tercer_candidato: int = i + 6
        cuarto_candidato: int = i + 8
    
        if primos[primer_candidato] and primos[segundo_candidato] and primos[tercer_candidato] and primos[cuarto_candidato]:
            resultados.append(f"{primer_candidato} - {segundo_candidato} - {tercer_candidato} - {cuarto_candidato}")
            cantidad_de_cuartetos += 1

    tiempo_final: float = time()
    tiempo_de_ejecucion: float = tiempo_final - tiempo_inicial
    imprimir_resultados(resultados, cantidad_de_cuartetos)

    return tiempo_de_ejecucion


def ejecutar_pruebas_intensivas(solucion_ingresada: int, numero_de_iteraciones: int, limite: int, funcion_a_probar) -> None:

    tiempos_de_ejecucion: list = []
    limpiar_pantalla()

    for i in range(numero_de_iteraciones):
        limpiar_pantalla()

        tiempo_de_ejecucion: float = funcion_a_probar(limite)

        tiempos_de_ejecucion.append(tiempo_de_ejecucion)

    print(f"Resultados obtenidos para n = {limite} (SOLUCIÓN {solucion_ingresada}):\n")

    if numero_de_iteraciones > 1:
        print(f"\tMenor tiempo de ejecución registrado tras {numero_de_iteraciones} iteraciones: {min(tiempos_de_ejecucion)} segundos.\n")
        print(f"\tPromedio: {sum(tiempos_de_ejecucion) / len(tiempos_de_ejecucion)} segundos.\n\n")
    elif numero_de_iteraciones == 1:
        print(f"\tTiempo de ejecución: {tiempos_de_ejecucion[0]} segundos.\n\n")


def test_tiempos_de_ejecucion_intensivo() -> None:

    while True:

        print("Este programa realiza pruebas intensivas sobre las dos soluciones propuestas.\n\n")
        solucion_ingresada: int = elegir_opcion("Ingrese la solución que desea probar intensivamente (1 / 2) (0 para finalizar la ejecución): ", 0, 2)
        if solucion_ingresada == 0:
            break

        numero_de_iteraciones: int = elegir_opcion("\nIngrese la cantidad de iteraciones a ejecutar para esta solución (1 a 1000): ", 1, 1000)

        limite: int = elegir_opcion("\nIngrese el valor límite de n (hasta 1000M). Ingrese 0 para usar el valor por defecto (1M): ", 0, 1000000000)
        if limite == 0:
            limite = 1000000

        if solucion_ingresada == 1:
            ejecutar_pruebas_intensivas(solucion_ingresada, numero_de_iteraciones, limite, encontrar_cuartetos_de_numeros_primos_1)
        elif solucion_ingresada == 2:
            ejecutar_pruebas_intensivas(solucion_ingresada, numero_de_iteraciones, limite, encontrar_cuartetos_de_numeros_primos_2)

    print("\n\nSe finalizó la ejecución del programa.")


test_tiempos_de_ejecucion_intensivo()
