import ejercicio1 as ej1
import utilidades as utilidades
from time import time


LONGITUD_CADENA = [
    500, 1000, 1500, 2000, 2500,
    3000, 3500, 4000, 4500, 5000,
    5500, 6000, 7000, 7500, 8000,
    8500, 9000, 9500, 10000, 10500,
    11000, 11500, 12000, 12500, 13000,
    13500, 14000, 14500, 15000, 15500,
    16000, 16500, 17000, 17500, 18000,
    18500, 19000, 19500, 20000, 20500,
    21000, 21500, 22000, 22500, 23000,
    23500, 24000, 24500, 25000
]


def generar_datos(longitud_cadena: int) -> str:

    cadena_base: str = "ABACB"
    cadena_resultado: str = (cadena_base * ((longitud_cadena // len(cadena_base)) + 1))[:longitud_cadena]

    return cadena_resultado


def test_tiempo_de_ejecucion() -> None:

    utilidades.limpiar_pantalla()

    with open("test_tiempos_de_ejecucion.txt", "w") as archivo:
        for longitud_cadena in LONGITUD_CADENA:
            cadena: str = generar_datos(longitud_cadena)
            tiempo_inicial: float = time()
            _: tuple = ej1.encontrar_minimos_palindromos(cadena)
            tiempo_final: float = time()

            tiempo_de_ejecucion: float = tiempo_final - tiempo_inicial

            print(f"Para una cadena de longitud = {longitud_cadena}:")
            print(f"Tiempo de ejecución: {tiempo_de_ejecucion} segundos.")
            print("\n")

            archivo.write(f"{tiempo_de_ejecucion}\n")


test_tiempo_de_ejecucion()