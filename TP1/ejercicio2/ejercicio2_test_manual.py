import ejercicio2 as ej2
import utilidades as utilidades

def generar_datos() -> list:

    distancias: list = []

    utilidades.limpiar_pantalla()
    while True:
        distancia: str = input("Ingrese un valor mayor a 0 de distancia (0 para terminar la ejecución): ")
        if not distancia.isdigit():
            utilidades.limpiar_pantalla()
            print("Ingresó algo que no es válido. Intente nuevamente.\n")
        elif int(distancia) > 0:
            utilidades.limpiar_pantalla()
            print(f"Se introdujo el valor {int(distancia)} en la lista.\n")
            distancias.append(int(distancia))
        elif int(distancia) == 0:
            break

    return distancias


def test_manual() -> None:

    distancias: list = generar_datos()

    utilidades.limpiar_pantalla()

    if distancias == []:
        print("No se introdujo ningún valor de distancia.\n\n\n")
        return
    paradas: list = ej2.planificar_paradas(distancias)

    print(f"Lista de distancias generada manualmente: {distancias}.")
    utilidades.imprimir_paradas(paradas)


test_manual()
