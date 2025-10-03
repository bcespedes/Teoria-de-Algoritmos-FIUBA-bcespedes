from time import time
from math import isqrt
import tp0_cespedes_108219_utilidades as utilidades


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


def encontrar_cuartetos_de_numeros_primos(limite: int) -> float:

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
    utilidades.imprimir_resultados(resultados, cantidad_de_cuartetos)

    return tiempo_de_ejecucion
