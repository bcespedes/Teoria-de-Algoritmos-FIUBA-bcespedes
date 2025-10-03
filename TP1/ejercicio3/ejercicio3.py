import time

def buscar_la_cadena(objetivo, cadena_actual, cadena_minima):
    
    ultimo_numero = cadena_actual[-1]

    if ultimo_numero == objetivo:
        if not cadena_minima or len(cadena_actual) < len(cadena_minima):
            cadena_minima[:] = cadena_actual[:]
        return

    if cadena_minima and len(cadena_actual) >= len(cadena_minima):
        return

    if cadena_minima and max(cadena_actual) * (2 ** (len(cadena_minima) - len(cadena_actual))) < objetivo:
        return

    for i in range(len(cadena_actual) - 1, -1, -1):
        sublista_actual_invertida = reversed(cadena_actual[i:])
        for j in sublista_actual_invertida:
            resultado = cadena_actual[i] + j
            if resultado <= ultimo_numero:
                break
            if resultado > objetivo:
                continue
            cadena_actual.append(resultado)
            buscar_la_cadena(objetivo, cadena_actual, cadena_minima)
            cadena_actual.pop()

def suma_encadenada_minima(n):
    cadena_minima = []
    buscar_la_cadena(n, [1], cadena_minima)
    return cadena_minima
