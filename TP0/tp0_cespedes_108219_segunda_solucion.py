from time import time
from math import isqrt
import tp0_cespedes_108219_utilidades as utilidades


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


def encontrar_cuartetos_de_numeros_primos(limite: int) -> float:

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
    utilidades.imprimir_resultados(resultados, cantidad_de_cuartetos)

    return tiempo_de_ejecucion
