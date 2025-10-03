from os import system, name


def limpiar_pantalla() -> None:

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def imprimir_palindromos(mínima_cantidad_palindromos: int, palindromos: list) -> None:

    print(f"Se han encontrado una cantidad mínima de {mínima_cantidad_palindromos} palíndromos.")
    print(f"Dichos palíndromos son: {', '.join(palindromos)}.")
    print("\n\n")
