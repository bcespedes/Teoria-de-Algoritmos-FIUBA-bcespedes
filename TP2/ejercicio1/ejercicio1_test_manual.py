import ejercicio1 as ej1
import utilidades as utilidades


def generar_datos() -> str:

    cadena: str = input("Ingrese una cadena para verificar la cantidad mínima de palíndromos (ingrese una cadena vacía para terminar la ejecución): ")
    utilidades.limpiar_pantalla()
    return cadena


def test_manual() -> None:

    utilidades.limpiar_pantalla()

    while True:
        cadena: str = generar_datos()

        if cadena == '':
            print("Se ha finalizado la ejecución.\n\n\n")
            break
        mínima_cantidad_palindromos, palindromos = ej1.encontrar_minimos_palindromos(cadena)

        print(f"Cadena generada manualmente: {cadena}.")
        utilidades.imprimir_palindromos(mínima_cantidad_palindromos, palindromos)


test_manual()