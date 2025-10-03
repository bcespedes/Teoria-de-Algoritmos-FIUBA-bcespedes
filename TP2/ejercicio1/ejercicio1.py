from math import inf


def calcular_palindromos(cadena: str) -> list:

    longitud_cadena: int = len(cadena)
    es_palindromo = [[False] * longitud_cadena for _ in range(longitud_cadena)]

    for longitud_subcadena in range(1, longitud_cadena + 1):
        for i in range(longitud_cadena - longitud_subcadena + 1):
            j = i + longitud_subcadena - 1
            if cadena[i] == cadena[j]:
                if longitud_subcadena <= 2 or es_palindromo[i + 1][j - 1]:
                    es_palindromo[i][j] = True

    return es_palindromo


def reconstruir_palindromos(opt: list, cadena: str) -> list:

    diccionario_reconstruccion: dict = {}
    longitud_cadena: int = len(opt)

    for i in range(longitud_cadena):
        if opt[i] not in diccionario_reconstruccion:
            diccionario_reconstruccion[opt[i]] = [i, i + 1]
        else:
            diccionario_reconstruccion[opt[i]][1] = i + 1
            if opt[i] + 1 in diccionario_reconstruccion:
                del diccionario_reconstruccion[opt[i] + 1]

    resultado: list = []
    for par_de_indices in diccionario_reconstruccion.values():
        resultado.append(cadena[par_de_indices[0]:par_de_indices[1]])

    return resultado


def encontrar_minimos_palindromos(cadena: str) -> tuple:

    cadena = cadena.replace(" ", "")
    cadena = cadena.upper()
    longitud_cadena: int = len(cadena)
    es_palindromo: list = calcular_palindromos(cadena)
    opt: list = [inf] * longitud_cadena

    for i in range(longitud_cadena):
        if es_palindromo[0][i]:
            opt[i] = 1
        else:
            for j in range(1, i + 1):
                if es_palindromo[j][i]:
                    opt[i] = min(opt[i], opt[j - 1] + 1)

    minima_cantidad_palindromos: int = opt[-1]
    resultado: list = reconstruir_palindromos(opt, cadena)

    return minima_cantidad_palindromos, resultado