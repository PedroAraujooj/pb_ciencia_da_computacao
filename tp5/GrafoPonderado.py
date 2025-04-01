class GrafoPonderado:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def adicionar_arestas(self, vertice1, vertice2, peso):
        self.vertices[vertice1].append((vertice2, peso))
        self.vertices[vertice2].append((vertice1, peso))

    def dijkstra(self, origem):
        nao_visitados = list(self.vertices.keys())
        distancias = {v: float("inf") for v in self.vertices}
        distancias[origem] = 0
        predecessores = {}

        while nao_visitados:
            vertice_atual = min(nao_visitados, key=lambda v: distancias[v])
            if distancias[vertice_atual] == float("inf"):
                break

            for vizinho, peso in self.vertices[vertice_atual]:
                nova_dist = distancias[vertice_atual] + peso
                if nova_dist < distancias[vizinho]:
                    distancias[vizinho] = nova_dist
                    predecessores[vizinho] = vertice_atual

            nao_visitados.remove(vertice_atual)

        return distancias, predecessores
