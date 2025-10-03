from Herramientas import utilidades

def flujo(grafo, fuente, sumidero):
    flujo = {}
    for vertice in grafo:
        for adyacente in grafo.adyacentes(vertice):
            flujo[(vertice, adyacente)] = 0

    grafo_residual = utilidades.inicializar_Grafo_Residual(grafo)

    while (camino := utilidades.obtener_camino(grafo_residual, fuente, sumidero)) is not None:
        capacidad_residual_camino = utilidades.minimo_peso_del_camino(grafo_residual, camino)
        for i in range(1, len(camino)):
            if grafo.estan_unidos(camino[i-1], camino[i]):
                flujo[(camino[i-1], camino[i])] += capacidad_residual_camino
            else:
                flujo[(camino[i], camino[i-1])] -= capacidad_residual_camino
            utilidades.actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], capacidad_residual_camino)
    
    return flujo