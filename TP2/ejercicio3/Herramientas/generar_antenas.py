from random import randint, seed

SEMILLA = 10

def crear_matriz_distancias(cantidad_antenas: int):
    matriz = []
    seed(SEMILLA)
    for i in range(cantidad_antenas):
        fila = []
        for j in range(cantidad_antenas):
            if i == j:
                fila.append(0)
            elif (j < i):
                fila.append(matriz[j][i])
            else:
                fila.append(randint(1, cantidad_antenas))
        matriz.append(fila)        
        
    return matriz


def leer_archivo_txt(ruta_archivo):
    with open(ruta_archivo, 'r') as f:
        distancia_minima = int(f.readline().strip())
        k_backups = int(f.readline().strip())
        b_grupo_antenas = int(f.readline().strip())

        matriz = []
        for linea in f:
            fila = []
            linea = linea.strip()
            distancias = linea.split('|')
            for distancia in distancias[1:]:
                fila.append(int(distancia))
            matriz.append(fila)
    
    return distancia_minima, k_backups, b_grupo_antenas, matriz

def escribir_archivo_txt(archivo, distancia_minima, k_backups, 
                         b_grupo_antenas, matriz):
    with open(archivo, 'w') as f:
        f.write(f"{distancia_minima}\n")
        f.write(f"{k_backups}\n")
        f.write(f"{b_grupo_antenas}\n")
        
        for i in range(len(matriz)):
            nombre_antena = "Antena" + str(i+1)
            fila = matriz[i]

            distancias = []
            for distancia in fila:
                distancias.append(str(distancia))
    
            linea = '|'.join(distancias)
            f.write(f"{nombre_antena}|{linea}\n")

# def main():
#     cantidad_antenas = 450
#     distancia_maxima = 440
#     k = 427
#     b = 435
#     matriz = crear_matriz_distancias(cantidad_antenas)
#     escribir_archivo_txt(f"{cantidad_antenas}Antenas.txt", distancia_maxima, k, b, matriz)
# main()