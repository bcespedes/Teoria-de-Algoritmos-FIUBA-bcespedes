DISTANCIA_MAXIMA: int = 7


def planificar_paradas(distancias: list) -> list:

    distancias: list = list(set(distancias)) # Elimina duplicados
    distancias.sort()

    paradas: list = []

    if distancias[-1] <= DISTANCIA_MAXIMA:
        paradas.append(distancias[-1])
        return paradas

    if distancias[0] > DISTANCIA_MAXIMA:
        return paradas

    numero_de_elementos: int = len(distancias)
    ultima_parada: int = 0

    for i in range(numero_de_elementos):
        if distancias[i] - ultima_parada > DISTANCIA_MAXIMA:
            if distancias[i] - distancias[i - 1] > DISTANCIA_MAXIMA:

                return []

            paradas.append(distancias[i - 1])
            ultima_parada = distancias[i - 1]

    return paradas