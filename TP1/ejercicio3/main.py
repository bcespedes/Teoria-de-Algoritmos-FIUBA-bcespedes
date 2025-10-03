from ejercicio3 import suma_encadenada_minima, time

def main():
    seguir = True
    while seguir:
        numero:int = int(input("Ingrese un número para buscar su cadena mínima (0 para salir): "))
        if (numero == 0):
            seguir = False
        else: 
            t1 = time.time()
            resultado = suma_encadenada_minima(numero)
            t2 = time.time()
            print(resultado)
            print(f"Longitud: {len(resultado)-1}")
            print(t2 - t1)
            print()
main()