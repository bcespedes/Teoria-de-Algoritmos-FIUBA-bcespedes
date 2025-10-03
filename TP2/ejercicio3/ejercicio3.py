from Grafo import grafo
from Herramientas import utilidades, generar_antenas
import algoritmo_Edmons_Karp
from time import time

FUENTE = "FUENTE"
SUMIDERO = "SUMIDERO"
GRUPOS = ["A", "B"]


def crear_grafo_antenas(matriz_distancias, distancia_maxima, 
                        grupo_k_backups, grupo_b_antenas):
    
    g = grafo.Grafo(es_dirigido=True)
    g.agregar_vertice(SUMIDERO)
    g.agregar_vertice(FUENTE)
    for i in range(1, len(matriz_distancias) + 1):
        for grupo in GRUPOS:
            grupo_antena = grupo + str(i)
            g.agregar_vertice(grupo_antena)
            if grupo == "A":
                g.agregar_arista(FUENTE, grupo_antena, grupo_k_backups)
            else:
                g.agregar_arista(grupo_antena, SUMIDERO, grupo_b_antenas)
    
    for i in range(len(matriz_distancias)):
        for j in range(len(matriz_distancias[0])):
            if i != j and matriz_distancias[i][j] < distancia_maxima:
                g.agregar_arista(GRUPOS[0] + str(i+1), GRUPOS[1] + str(j+1), 1)
            
    return g

def main():
    
    #-------------- INICIALIZACION Y CREACION DEL GRAFO--------------------------------------------------------------------------------#
    prueba_antenas = "25Antenas"
    D_maximo, grupo_k_backups, grupo_b_antenas, matriz_distancias = generar_antenas.leer_archivo_txt(f"TP2/ejercicio3/pruebastxt/{prueba_antenas}.txt")
    #D_maximo, grupo_k_backups, grupo_b_antenas, matriz_distancias = generar_antenas.leer_archivo_txt(f"TP2/ejercicio3/ejemplo_seguimiento.txt")
    #Descomentar el de arriba y comentar el de arriba las pruebas para ejecutar el ejemplo de seguimiento del informe
    grafo_antenas = crear_grafo_antenas(matriz_distancias, D_maximo, grupo_k_backups, grupo_b_antenas)

    #-------------- APLICACION DEL ALGORITMO EDMONS-KARP--------------------------------------------------------------------------------#
    inicio = time()
    flujo_resultante = algoritmo_Edmons_Karp.flujo(grafo_antenas, FUENTE, SUMIDERO)
    fin = time()
    
    total_flujo = utilidades.calcular_flujo_total(flujo_resultante, FUENTE)
    n = len(matriz_distancias)
    print(f"Flujo total: {total_flujo} (esperado: {n * grupo_k_backups})")
    
    #-------------- VERIFICACION SI HAY O NO SOLUCION--------------------------------------------------------------------------------#
    if total_flujo == n * grupo_k_backups:
        solucion = utilidades.extraer_solucion(flujo_resultante)
        archivo = "TP2/ejercicio3/" + prueba_antenas + "Resultado.txt"
        utilidades.escribir_solucion(archivo, solucion, fin - inicio, total_flujo)
    else:
        print("No existe solución posible.")
    
main()