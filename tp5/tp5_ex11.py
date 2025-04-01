from tp5.GrafoPonderado import GrafoPonderado

if __name__ == "__main__":

    verticesAndArestas = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]

    }
    grafo = GrafoPonderado()
    grafo.vertices = verticesAndArestas
    distancias, predecessore = grafo.dijkstra('A')
    print("Distâncias a partir de A:")
    for vertice, distancia in distancias.items():
        print(f"{vertice}: {distancia}")
