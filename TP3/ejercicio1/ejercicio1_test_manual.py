import ejercicio1 as ej1
import utilidades as utilidades


def elegir_numero_objetivo() -> int:

    numero_objetivo: int = 0

    while True:
        numero_objetivo: str = input("Ingrese un número objetivo mayor a 0 (0 para terminar la ejecución): ")
        if not numero_objetivo.isdigit() or int(numero_objetivo) < 0:
            utilidades.limpiar_pantalla()
            print("Ingresó algo que no es válido. Intente nuevamente.\n")
        elif int(numero_objetivo) == 0:
            utilidades.limpiar_pantalla()
            break
        elif int(numero_objetivo) > 0:
            utilidades.limpiar_pantalla()
            print(f"Se introdujo el valor {int(numero_objetivo)} como objetivo.\n")
            break
    
    return int(numero_objetivo)


def agregar_elementos_a_lista_de_numeros() -> list:

    lista_de_numeros: list = []

    while True:
        numero: str = input("Ingrese un valor mayor a 0 para introducirlo en la lista de números (0 para terminar la ejecución): ")
        if not numero.isdigit():
            utilidades.limpiar_pantalla()
            print("Ingresó algo que no es válido. Intente nuevamente.\n")
        elif int(numero) > 0:
            utilidades.limpiar_pantalla()
            print(f"Se introdujo el valor {int(numero)} en la lista.\n")
            lista_de_numeros.append(int(numero))
        elif int(numero) == 0:
            break

    return lista_de_numeros


def generar_datos() -> list:

    utilidades.limpiar_pantalla()

    numero_objetivo = elegir_numero_objetivo()

    if numero_objetivo == 0:
        return [], 0

    lista_de_numeros = agregar_elementos_a_lista_de_numeros()

    return lista_de_numeros, int(numero_objetivo)


def test_manual() -> None:

    lista_de_numeros, numero_objetivo = generar_datos()

    utilidades.limpiar_pantalla()

    if numero_objetivo == 0:
        print("No se introdujo ningún número objetivo.\n\n\n")
        return
    if lista_de_numeros == []:
        print("No se introdujo ningún número en la lista.\n\n\n")
        return
    subconjunto_aproximado, numero_objetivo = ej1.mejor_subconjunto_aproximado(lista_de_numeros, numero_objetivo)

    utilidades.imprimir_subconjuntos(lista_de_numeros, numero_objetivo, subconjunto_aproximado)
    print("\n\n")


test_manual()