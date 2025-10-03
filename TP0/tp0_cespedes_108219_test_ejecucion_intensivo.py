import tp0_cespedes_108219_utilidades as utilidades
import tp0_cespedes_108219_primera_solucion as primera_solucion
import tp0_cespedes_108219_segunda_solucion as segunda_solucion


def ejecutar_pruebas_intensivas(solucion_ingresada: int, numero_de_iteraciones: int, limite: int, funcion_a_probar) -> None:

    tiempos_de_ejecucion: list = []
    utilidades.limpiar_pantalla()

    for i in range(numero_de_iteraciones):
        utilidades.limpiar_pantalla()

        tiempo_de_ejecucion: float = funcion_a_probar(limite)

        tiempos_de_ejecucion.append(tiempo_de_ejecucion)

    print(f"Resultados obtenidos para n = {limite} (SOLUCIÓN {solucion_ingresada}):\n")

    if numero_de_iteraciones > 1:
        print(f"\tMenor tiempo de ejecución registrado tras {numero_de_iteraciones} iteraciones: {min(tiempos_de_ejecucion)} segundos.\n")
        print(f"\tPromedio: {sum(tiempos_de_ejecucion) / len(tiempos_de_ejecucion)} segundos.\n\n")
    elif numero_de_iteraciones == 1:
        print(f"\tTiempo de ejecución: {tiempos_de_ejecucion[0]} segundos.\n\n")


def test_tiempos_de_ejecucion_intensivo() -> None:

    while True:

        print("Este programa realiza pruebas intensivas sobre las dos soluciones propuestas.\n\n")
        solucion_ingresada: int = utilidades.elegir_opcion("Ingrese la solución que desea probar intensivamente (1 / 2) (0 para finalizar la ejecución): ", 0, 2)
        if solucion_ingresada == 0:
            break

        numero_de_iteraciones: int = utilidades.elegir_opcion("\nIngrese la cantidad de iteraciones a ejecutar para esta solución (1 a 1000): ", 1, 1000)

        limite: int = utilidades.elegir_opcion("\nIngrese el valor límite de n (hasta 1000M). Ingrese 0 para usar el valor por defecto (1M): ", 0, 1000000000)
        if limite == 0:
            limite = 1000000

        if solucion_ingresada == 1:
            ejecutar_pruebas_intensivas(solucion_ingresada, numero_de_iteraciones, limite, primera_solucion.encontrar_cuartetos_de_numeros_primos)
        elif solucion_ingresada == 2:
            ejecutar_pruebas_intensivas(solucion_ingresada, numero_de_iteraciones, limite, segunda_solucion.encontrar_cuartetos_de_numeros_primos)

    print("\n\nSe finalizó la ejecución del programa.")


test_tiempos_de_ejecucion_intensivo()
