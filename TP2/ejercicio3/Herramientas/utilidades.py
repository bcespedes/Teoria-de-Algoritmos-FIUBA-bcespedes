from Grafo import grafo
import copy
from collections import deque

def reconstruir_camino(padre, fuente, sumidero):
    camino = []
    actual = sumidero
    while actual != fuente:
        camino.append(actual)
        actual = padre[actual]
    camino.append(fuente)
    camino.reverse()
    return camino

def obtener_camino(grafo, fuente, sumidero):
    visitados = set()
    padre = {}

    cola = deque()
    cola.append(fuente)
    visitados.add(fuente)

    while cola:
        actual = cola.popleft()
        if actual == sumidero:
            break
        for vecino in grafo.adyacentes(actual):
            if vecino not in visitados and grafo.peso_arista(actual, vecino) > 0:
                visitados.add(vecino)
                padre[vecino] = actual
                cola.append(vecino)

    if sumidero not in padre:
        return None

    return reconstruir_camino(padre, fuente, sumidero)

def inicializar_Grafo_Residual(grafo):
    return copy.deepcopy(grafo)

def minimo_peso_del_camino(grafo_residual, camino):
    minimo = None
    
    for i in range(1, len(camino)):
        peso = grafo_residual.peso_arista(camino[i-1], camino[i])
        if minimo is None or peso < minimo:
            minimo = peso
    
    return minimo

def actualizar_grafo_residual(grafo_residual, u, v, valor):
    peso_anterior = grafo_residual.peso_arista(u,v)
    
    if peso_anterior == valor:
        grafo_residual.borrar_arista(u,v)
    else:
        grafo_residual.cambiar_peso(u,v, peso_anterior - valor)
    
    if not grafo_residual.estan_unidos(v, u):
        grafo_residual.agregar_arista(v, u, valor)
    else:
        grafo_residual.cambiar_peso(v, u, grafo_residual.peso_arista(v,u) + valor)

def imprimir_lista_adyacencia(grafo):
    print("Lista de adyacencias del grafo:")
    for v in grafo:
        adyacentes = grafo.adyacentes(v)
        if not adyacentes:
            print(f"{v} -> []")
            continue
        print(f"{v} -> [{', '.join(f'{w} (peso={grafo.peso_arista(v, w)})' for w in adyacentes)}]")

def imprimir_flujo(flujo):
    for arista, valor in flujo.items():
        if valor > 0:
            print(f"{arista[0]} -> {arista[1]}: flujo = {valor}")

def escribir_solucion(archivo, asignaciones, tiempo, flujo):
    with open(archivo, 'w') as f:
        f.write(f"Flujo total: {flujo}\n")
        f.write(f"tiempo en buscar la solucion: {tiempo}\n")
        f.write("Asignaciones de backups (antena A -> antena B):\n")
        for a, lista_b in asignaciones.items():
            f.write(f"------------\n")
            for b in lista_b:
                f.write(f"Antena{a} -> Antena{b}\n")

def contar_conexiones_validas(matriz_distancias, distancia_maxima):
    n = len(matriz_distancias)
    conexiones = 0
    for i in range(n):
        for j in range(n):
            if i != j and matriz_distancias[i][j] < distancia_maxima:
                conexiones += 1
    return conexiones

def conexiones_por_antena(matriz_distancias, distancia_minima):
    n = len(matriz_distancias)
    conexiones_por_nodo = [0] * n
    for i in range(n):
        for j in range(n):
            if i != j and matriz_distancias[i][j] < distancia_minima:
                conexiones_por_nodo[i] += 1
    return conexiones_por_nodo

def extraer_solucion(flujo):
    solucion = {}

    for (u, v), f in flujo.items():
        if f == 1 and u.startswith("A") and v.startswith("B"):
            i = int(u[1:])  # número de la antena A
            j = int(v[1:])  # número de la antena B
            if i not in solucion:
                solucion[i] = []
            solucion[i].append(j)

    return solucion

def calcular_flujo_total(flujo, fuente):
    return sum(f for (u, _), f in flujo.items() if u == fuente)