from os import system, name


def limpiar_pantalla() -> None:

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def imprimir_paradas(paradas: list) -> None:

    if paradas == []:
        print("No se pudo completar el recorrido con las distancias establecidas.")
    else:
        print(f"Lista de paradas en base a las distancias: {paradas}.")
    print("\n\n")
