from tp5.GrafoAlgoritmoPrim import GrafoAlgoritmoPrim

if __name__ == "__main__":

    verticesAndArestas = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 4)],
        'C': [('A', 3), ('B', 1), ('D', 5)],
        'D': [('B', 4), ('C', 5)]

    }
    grafo = GrafoAlgoritmoPrim()
    grafo.grafo = verticesAndArestas
    grafo.imprimir('A')
