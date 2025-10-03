import random

COULOMB = 1

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
    particulas = generar_particulas(n)
    fuerzas = calcular_fuerzas_coulomb(particulas)
    print("Particulas = ", particulas, "\nFuerzas = ", fuerzas)

print("Programa de prueba con elementos reducidos, los set de datos grandes se encuentran en la carpeta resultados\n------------------------------------")
prog(5)
prog(10)
prog(20)
