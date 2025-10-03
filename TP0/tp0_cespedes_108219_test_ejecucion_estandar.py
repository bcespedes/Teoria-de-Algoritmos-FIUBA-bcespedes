import tp0_cespedes_108219_utilidades as utilidades
import tp0_cespedes_108219_primera_solucion as primera_solucion
import tp0_cespedes_108219_segunda_solucion as segunda_solucion


LIMITES: list = [
    200000, 400000, 600000, 800000, 1000000,
    1200000, 1400000, 1600000, 1800000, 2000000
]


def ejecutar_pruebas_estandar() -> None:

    resultados: list = []

    for limite in LIMITES:
        tiempo_de_ejecucion_primera_solucion: float = primera_solucion.encontrar_cuartetos_de_numeros_primos(limite)
        tiempo_de_ejecucion_segunda_solucion: float = segunda_solucion.encontrar_cuartetos_de_numeros_primos(limite)
        resultados.append((limite, tiempo_de_ejecucion_primera_solucion, tiempo_de_ejecucion_segunda_solucion))
        utilidades.limpiar_pantalla()

    for n, resultado_primera_solucion, resultado_segunda_solucion in resultados:
        print(f"Resultados obtenidos para n = {n}:\n")
        print(f"\tTiempo de ejecución (SOLUCIÓN 1): {resultado_primera_solucion} segundos.")
        print(f"\tTiempo de ejecución (SOLUCIÓN 2): {resultado_segunda_solucion} segundos.\n\n")


def test_tiempos_de_ejecucion_estandar() -> None:

    while True:

        lista_formateada: str = ", ".join(f"{limite}" for limite in LIMITES)

        print("Este programa mide los tiempos de ejecución de las dos soluciones propuestas para los siguientes valores: ")
        print(f"\t{lista_formateada}\n")
        opcion_ingresada: int = utilidades.elegir_opcion("Ingrese 1 para iniciar la ejecución o 0 para finalizar la ejecución: ", 0, 1)
        if opcion_ingresada == 0:
            break

        elif opcion_ingresada == 1:
            ejecutar_pruebas_estandar()

    print("\n\nSe finalizó la ejecución del programa.")

test_tiempos_de_ejecucion_estandar()
