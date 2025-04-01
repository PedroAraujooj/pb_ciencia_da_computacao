class GrafoAlgoritmoPrim:
    def __init__(self):
        self.grafo = {}

    def adicionar_aresta(self, u, v, peso):
        if u not in self.grafo:
            self.grafo[u] = []
        if v not in self.grafo:
            self.grafo[v] = []
        self.grafo[u].append((v, peso))
        self.grafo[v].append((u, peso))

    def get_peso(self, u, v):
        for (vizinho, peso) in self.grafo[u]:
            if vizinho == v:
                return peso
        return float('inf')

    def prim(self, raiz):
        infinito = float('inf')
        vertices = list(self.grafo.keys())
        chave = {vertice: infinito for vertice in vertices}
        pai = {vertice: None for vertice in vertices}
        selecionado = {vertice: False for vertice in vertices}

        chave[raiz] = 0

        for _ in range(len(vertices)):
            u = min((v for v in vertices if not selecionado[v]),
                    key=lambda v: chave[v],
                    default=None)
            if u is None:
                break
            selecionado[u] = True

            for (vizinho, peso) in self.grafo[u]:
                if not selecionado[vizinho] and peso < chave[vizinho]:
                    chave[vizinho] = peso
                    pai[vizinho] = u

        print("\nArestas da Árvore Geradora Mínima:")
        return pai

    def imprimir(self, pai):
        pai = self.prim(pai)
        custo_total = 0
        for vertice, pai_vertice in pai.items():
            if pai_vertice is not None:
                peso = self.get_peso(vertice, pai_vertice)
                print(f"{pai_vertice} - {vertice} (Peso: {peso})")
                custo_total += peso
        print(f"Peso total da AGM: {custo_total}")
