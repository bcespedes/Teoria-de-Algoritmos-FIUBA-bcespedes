import os
import time 
from ejercicio3 import suma_encadenada_minima

RUTA_BASE = os.path.dirname(os.path.abspath(__file__))
MODO = "w"
MENSAJE_PRINCIPAL = "Ingrese hasta que numero N se va generar las mediciones ( 0 para salir ): "
MENSAJE_ERROR_1 = "Ingrese un numero valido."
MENSAJE_ERROR_2 = "Ingrese un numero mayor a 0."
MINIMO = 0
SALIDA = "0"

def generar_resultados(n):
    with open(os.path.join(RUTA_BASE, str(n)+".txt"), MODO) as archivo:
        for i in range(1, n + 1):
            t1 = time.time()
            resultado = suma_encadenada_minima(i)
            t2 = time.time()
            tiempo_resultado = t2 - t1
            linea = (f"N = {str(i).rjust(3)}: {str(resultado).ljust(50)} | longitud = {str(len(resultado)).rjust(2)} | tiempo = {tiempo_resultado} seg\n")
            archivo.write(linea)

def main():
    entrada_usuario = input(MENSAJE_PRINCIPAL)

    while entrada_usuario != SALIDA:
        if not entrada_usuario.isdigit():
            print(MENSAJE_ERROR_1)
        else:
            numero = int(entrada_usuario)
            if numero <= MINIMO:
                print(MENSAJE_ERROR_2)
            else:
                generar_resultados(numero)
        entrada_usuario = input(MENSAJE_PRINCIPAL)
main()
