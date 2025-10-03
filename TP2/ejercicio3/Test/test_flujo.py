from Grafo import Grafo
from algoritmo_Edmons_Karp import flujo

def test_flujo_simple():
    g = Grafo(es_dirigido=True, vertices_init=["S", "A", "B", "T"])
    g.agregar_arista("S", "A", 10)
    g.agregar_arista("A", "B", 5)
    g.agregar_arista("B", "T", 10)

    resultado = flujo(g, "S", "T")

    flujo_salida_fuente = sum(resultado[("S", v)] for v in g.adyacentes("S"))
    flujo_entrada_sumidero = sum(resultado[(u, "T")] for u in g.vertices if (u, "T") in resultado)

    print(resultado)

    assert flujo_salida_fuente == flujo_entrada_sumidero
    assert flujo_salida_fuente == 5
    assert resultado[("S", "A")] == 5
    assert resultado[("A", "B")] == 5
    assert resultado[("B", "T")] == 5