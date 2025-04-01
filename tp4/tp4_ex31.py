from ListaAdjacencia import Grafo

if __name__ == "__main__":

    grafo = Grafo()

    arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"),
               ("D", "E")]

    grafo.criar_grafo_by_arestas(arestas)

    grafo.mostrar_grafo()
