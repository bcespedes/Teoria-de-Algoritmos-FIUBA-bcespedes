from Grafo import Grafo
from Herramientas import utilidades

def test_camino_existe():
    g = Grafo(es_dirigido=True, vertices_init=["A", "B", "C"])
    g.agregar_arista("A", "B", 1)
    g.agregar_arista("B", "C", 1)

    camino = utilidades.obtener_camino(g, "A", "C")
    assert camino == ["A", "B", "C"]

def test_camino_no_existe_por_peso():
    g = Grafo(es_dirigido=True, vertices_init=["A", "B"])
    g.agregar_arista("A", "B", 0)

    camino = utilidades.obtener_camino(g, "A", "B")
    assert camino is None

def test_sin_conexion():
    g = Grafo(es_dirigido=True, vertices_init=["A", "B", "C"])
    g.agregar_arista("A", "B", 1)

    camino = utilidades.obtener_camino(g, "B", "C")
    assert camino is None
