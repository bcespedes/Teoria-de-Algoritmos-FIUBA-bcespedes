import ejercicio1 as ej1
import utilidades as utilidades
from random import seed, choices
from string import ascii_letters


CANTIDAD_SETS: int = 10
LONGITUD_CADENA: int = 25


def generar_datos_aleatorios(semilla: int, longitud_cadena: int) -> str:

    seed(semilla)
    caracteres: str = ascii_letters
    cadena: str = ''.join(choices(caracteres, k = longitud_cadena))

    return cadena


def test_aleatorio() -> None:

    utilidades.limpiar_pantalla()

    with open("test_aleatorio.txt", "w") as archivo:
        for i in range(CANTIDAD_SETS):

            cadena: str = generar_datos_aleatorios(i, LONGITUD_CADENA)
            mínima_cantidad_palindromos, palindromos = ej1.encontrar_minimos_palindromos(cadena)

            print(f"Set aleatorio número {i + 1}:\n")
            print(f"Cadena generada aleatoriamente: {cadena}.")
            utilidades.imprimir_palindromos(mínima_cantidad_palindromos, palindromos)

            archivo.write(f"Set aleatorio número {i + 1}:\n\n")
            archivo.write(f"Cadena generada aleatoriamente: {cadena}.\n")
            archivo.write(f"Se han encontrado una cantidad mínima de {mínima_cantidad_palindromos} palíndromos.\n")
            archivo.write(f"Dichos palíndromos son: {', '.join(palindromos)}.\n\n\n")


test_aleatorio()