import json
from math import floor 
from random import randint, seed
from time import time

# Algoritmo para elegir la mejor oferta
def elegir_mejor_oferta(ofertas):
    n = len(ofertas)
    m = floor(n / 4)
    mejor_oferta = 0

    for i in range(m):
        if ofertas[i] > mejor_oferta:
            mejor_oferta = ofertas[i]
    
    for j in range(m, n):
        if ofertas[j] > mejor_oferta:
            return ofertas[j]
    
    return ofertas[-1]

# Genera una lista de números aleatorios
def generar_lista(tamaño, semilla=0):
    seed(semilla)
    return [randint(0, 500000) for _ in range(tamaño)]

# Función para analizar complejidad 
def prueba_tiempos(promedios=10):
    tamaños = [100000, 250000, 500000]
    resultados = []
    datos_json = []

    for tamaño in tamaños:
        tiempos = []  
        total_tiempo = 0
        datos = generar_lista(tamaño, semilla=tamaño)
        mejor_oferta = max(datos)

        for i in range(promedios):
            inicio = time()
            oferta = elegir_mejor_oferta(datos)
            fin = time()
            tiempo_ejecucion = fin - inicio
            tiempos.append(tiempo_ejecucion)
            total_tiempo += tiempo_ejecucion

            resultado = {
                "tamanio": tamaño,
                "semilla": tamaño,
                "ejecucion": i + 1,
                "tiempo de ejecucion": tiempo_ejecucion,
                "oferta seleccionada": oferta,
                "mejor oferta": mejor_oferta
            }

            datos_json.append(resultado)

        promedio_tiempo = total_tiempo / promedios
        resultados.append((tamaño, promedio_tiempo))

    with open("ejercicio2/resultados.json", "w") as archivo:
        json.dump(datos_json, archivo, indent=4)

    return resultados

# Función para realizar el análisis de probabilidad
def analizar_ofertas():
    total_pruebas = 1000
    tamaño_lista = 1000
    aciertos = 0

    for semilla in range(total_pruebas):
        lista = generar_lista(tamaño_lista, semilla=semilla)
        seleccionada = elegir_mejor_oferta(lista)
        if seleccionada == max(lista):
            aciertos += 1

    porcentaje = (aciertos / total_pruebas) * 100
    return aciertos, total_pruebas, porcentaje

# Mostrar selección de ofertas de ejemplo
def mostrar_ofertas_de_ejemplo():
    ejemplo_ofertas = generar_lista(10, semilla=42)
    print("\n--- Ofertas de Ejemplo ---")
    print(f"Ofertas generadas: {ejemplo_ofertas}")
    oferta_seleccionada = elegir_mejor_oferta(ejemplo_ofertas)
    print(f"La oferta seleccionada es: {oferta_seleccionada}")
    print(f"La mejor oferta en la lista es: {max(ejemplo_ofertas)}\n")

# Mostrar análisis de tiempos de ejecución
def mostrar_tiempos_de_ejecucion():
    print("\n--- Resultados de Tiempos de Ejecucion ---")
    resultados = prueba_tiempos(promedios=5)  # Puedes cambiar el número de repeticiones
    for tamaño, duracion in resultados:
        print(f"Tamaño: {tamaño} -> Tiempo promedio: {duracion:.8f} segundos")

# Mostrar análisis de complejidad
def mostrar_analisis_de_complejidad():
    print("\n--- Analisis de Complejidad ---")
    aciertos, total_pruebas, porcentaje = analizar_ofertas()
    print(f"Aciertos: {aciertos}/{total_pruebas} ({porcentaje:.2f}%)")

def main():
    print("PROBLEMA 2 - Algoritmos Randomizados ")
    mostrar_ofertas_de_ejemplo()
    mostrar_tiempos_de_ejecucion()
    mostrar_analisis_de_complejidad()

main()
