from Grafo import Grafo

def test_arista_direccion_correcta():
    g = Grafo(es_dirigido=True, vertices_init=["A", "B"])
    g.agregar_arista("A", "B", 5)

    assert g.estan_unidos("A", "B")
    assert not g.estan_unidos("B", "A")
    assert g.peso_arista("A", "B") == 5

def test_cambiar_peso_arista_dirigido():
    g = Grafo(es_dirigido=True, vertices_init=["X", "Y"])
    g.agregar_arista("X", "Y", 3)
    g.cambiar_peso("X", "Y", 8)

    assert g.peso_arista("X", "Y") == 8
