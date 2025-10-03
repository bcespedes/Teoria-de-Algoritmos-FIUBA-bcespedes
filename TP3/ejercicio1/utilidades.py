from os import system, name


def limpiar_pantalla() -> None:

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def imprimir_subconjuntos(lista_de_numeros: list, numero_objetivo: int, subconjunto_aproximado: list) -> None:

    print(f"Lista de números disponibles (ya ordenada): {lista_de_numeros}.")
    print(f"El valor más próximo al número {numero_objetivo} es {sum(subconjunto_aproximado)}.")
    print(f"Se obtiene sumando los números de la siguiente lista: {subconjunto_aproximado}.")