from os import system, name


def limpiar_pantalla() -> None:

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def imprimir_resultados(resultados: list, cantidad_de_cuartetos: int) -> None:

    print(f"Cuartetos de números primos encontrados:\n")
    print(*resultados, sep = "\n")
    print(f"\nSe encontraron {cantidad_de_cuartetos} cuartetos de números primos.\n\n")


def elegir_opcion(texto: str, opcion_minima: int, opcion_maxima: int) -> int:

    while True:
        opcion: str = input(texto)
        if not opcion.isdigit() or int(opcion) < opcion_minima or int(opcion) > opcion_maxima:
            limpiar_pantalla()
            print("Ingresó algo que no es válido. Intente nuevamente.\n")
        elif int(opcion) >= opcion_minima and int(opcion) <= opcion_maxima:
            return int(opcion)
