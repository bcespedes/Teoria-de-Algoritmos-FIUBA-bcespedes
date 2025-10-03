from itertools import combinations


def mejor_subconjunto_aproximado(numeros_disponibles: list, numero_objetivo: int) -> tuple:

    numeros_disponibles.sort(reverse=True)

    mejor_conjunto: list = list()
    mejor_suma: int = 0

    for numero in numeros_disponibles:
        if mejor_suma + numero <= numero_objetivo:
            mejor_conjunto.append(numero)
            mejor_suma += numero

    return mejor_conjunto, mejor_suma


# Únicamente usado por motivos de comparación.
def mejor_subconjunto_exacto(numeros, objetivo):

    mejor_suma = 0
    mejor_conjunto = []

    for i in range(1, len(numeros) + 1):
        for subconjunto in combinations(numeros, i):

            suma = sum(subconjunto)

            if suma <= objetivo and suma > mejor_suma:
                mejor_suma = suma
                mejor_conjunto = list(subconjunto)

    return mejor_conjunto, mejor_suma