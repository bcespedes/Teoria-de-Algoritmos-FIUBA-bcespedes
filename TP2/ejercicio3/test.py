from Test.test_grafo_dirigido import (
    test_arista_direccion_correcta,
    test_cambiar_peso_arista_dirigido
)

from Test.test_recorrido_bfs import (
    test_camino_existe,
    test_camino_no_existe_por_peso,
    test_sin_conexion
)

from Test.test_flujo import (
    test_flujo_simple
)

def correr_todos_los_tests():
    print("Corriendo tests de Grafo dirigido...")
    test_arista_direccion_correcta()
    test_cambiar_peso_arista_dirigido()
    print("Tests de Grafo dirigido pasaron.\n")

    print("Corriendo tests de obtener_camino...")
    test_camino_existe()
    test_camino_no_existe_por_peso()
    test_sin_conexion()
    print("Tests de obtener_camino pasaron.\n")

    print("Corriendo tests de flujo máximo...")
    test_flujo_simple()
    print("Tests de flujo máximo pasaron.\n")

if __name__ == "__main__":
    correr_todos_los_tests()
    print("¡Todos los tests pasaron correctamente!")
