import numpy as np
import random
import time
import json

COULOMB = 8.9875517923e9

def generar_particulas(n):
    random.seed(6)
    return [random.randint(-100, 100) for _ in range(n)]
    
def fuerza_coulomb(q, j, i):
    distancia = j - i
    if distancia == 0:
        return 0
    return COULOMB * (q[j] * q[i]) / (distancia ** 2)

def calcular_fuerzas(particulas, izquierda, derecha):
    if izquierda == derecha:
        return [0]
    
    mitad = (izquierda + derecha) // 2
    fuerza_izquierda = calcular_fuerzas(particulas, izquierda, mitad)
    fuerza_derecha = calcular_fuerzas(particulas, mitad + 1, derecha)
    
    fuerzas = fuerza_izquierda + fuerza_derecha
    
    for j in range(izquierda, mitad + 1):
        for i in range(mitad + 1, derecha + 1):
            fuerza = fuerza_coulomb(particulas, j, i)
            fuerzas[i - izquierda] += fuerza
            fuerzas[j - izquierda] -= fuerza
    
    return fuerzas

def calcular_fuerzas_coulomb(particulas):
    return calcular_fuerzas(particulas, 0, len(particulas) - 1)

def prog(n):
    t1 = time.time()
    particulas = generar_particulas(n)
    fuerzas = calcular_fuerzas_coulomb(particulas)
    t2 = time.time()
    
    resultado = {
        "cantidad_particulas": n,
        "tiempo_ejecucion": t2 - t1,
        "particulas": particulas,
        "fuerzas": fuerzas
    }
    
    with open(f"resultado_{n}.json", "w") as f:
        json.dump(resultado, f, indent=1, separators=(',', ':'))
    
    print(f"Tiempo de ejecución para {n} partículas: {t2-t1} segundos")

prog(2000)
prog(4000)
prog(6000)
prog(8000)
prog(10000)