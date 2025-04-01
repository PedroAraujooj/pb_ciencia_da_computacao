from collections import deque


class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}

    def criar_grafo_by_arestas(self, arestas):
        self.lista_adjacencia = {}
        for vertice1, vertice2 in arestas:
            if vertice1 not in self.lista_adjacencia:
                self.adicionar_vertice(vertice1)
            if vertice2 not in self.lista_adjacencia:
                self.adicionar_vertice(vertice2)
            self.lista_adjacencia[vertice1].append(vertice2)
            self.lista_adjacencia[vertice2].append(vertice1)  # Para grafos não direcionados

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            self.lista_adjacencia[vertice1].append(vertice2)
            self.lista_adjacencia[vertice2].append(vertice1)  # Para grafos não direcionados

    def mostrar_vizinhos(self, vertice):
        if vertice in self.lista_adjacencia:
            print(f"Vizinhos de {vertice}: {self.lista_adjacencia[vertice]}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")

    def mostrar_grafo(self):
        for vertice in self.lista_adjacencia:
            print(f"{vertice} -> {self.lista_adjacencia[vertice]}")

    def _dfs_ciclo(self, vertice, visitados, rec_stack):

        visitados.add(vertice)
        rec_stack.add(vertice)

        for vizinho in self.lista_adjacencia[vertice]:
            if vizinho not in visitados:
                if self._dfs_ciclo(vizinho, visitados, rec_stack):
                    return True
            elif vizinho in rec_stack:
                return True

        rec_stack.remove(vertice)
        return False

    def existe_ciclo(self):
        visitados = set()
        rec_stack = set()

        for vertice in self.lista_adjacencia:
            if vertice not in visitados:
                if self._dfs_ciclo(vertice, visitados, rec_stack):
                    return True
        return False

    def bfs_menor_distancia(self, inicio, destino):
        visitados = set()
        fila = deque()
        pais = {}

        fila.append(inicio)
        visitados.add(inicio)
        pais[inicio] = None

        while fila:
            vertice_atual = fila.popleft()

            if vertice_atual == destino:
                break

            for adj in self.lista_adjacencia[vertice_atual]:
                vizinho = adj

                if vizinho not in visitados:
                    visitados.add(vizinho)
                    pais[vizinho] = vertice_atual
                    fila.append(vizinho)

        caminho = []
        if destino in pais:
            vertice = destino
            while vertice is not None:
                caminho.append(vertice)
                vertice = pais[vertice]
            caminho.reverse()

        return caminho

    def bfs(self, inicio):
        visitados = set()
        fila = deque()
        ordem_visita = []

        fila.append(inicio)
        visitados.add(inicio)

        while fila:
            vertice_atual = fila.popleft()
            ordem_visita.append(vertice_atual)
            for vizinho in self.lista_adjacencia[vertice_atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)

        return ordem_visita

    def dfs(self, inicio, visitados=None, ordem_visita=None):
        if visitados is None:
            visitados = set()
        if ordem_visita is None:
            ordem_visita = []

        visitados.add(inicio)
        ordem_visita.append(inicio)

        for vizinho in self.lista_adjacencia[inicio]:
            if vizinho not in visitados:
                self.dfs(vizinho, visitados, ordem_visita)

        return ordem_visita
