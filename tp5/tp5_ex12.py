from tp5.GrafoAlgoritmoPrim import GrafoAlgoritmoPrim
import time
import random
import matplotlib.pyplot as plt


def gerar_arestas_aleatorias(grafo_grande, num_vertices, num_arestas):
    nodes = [f"C{i}" for i in range(num_vertices)]
    for no in nodes:
        grafo_grande.grafo[no] = []
    for _ in range(num_arestas):
        u = random.choice(nodes)
        v = random.choice(nodes)
        if u != v:
            peso = random.randint(1, 1000)
            grafo_grande.adicionar_aresta(u, v, peso)


def testar_tempos_prim():
    tamanhos = [10, 50, 100, 200, 500, 700, 1000]
    tempos = []

    for tamanho in tamanhos:
        num_arestas = tamanho * 5
        grafo = GrafoAlgoritmoPrim()
        gerar_arestas_aleatorias(grafo, tamanho, num_arestas)

        inicio = time.time()
        for _ in range(100):
            pai = grafo.prim("C0")
        fim = time.time()

        tempo_execucao = (fim - inicio) / 100
        tempos.append(tempo_execucao)
        print(f"\nGrafo com {tamanho} vértices: {tempo_execucao:.6f} segundos. Ordem de visita: \n {pai}")

    return tamanhos, tempos


def plotar_grafico(tamanhos, tempos):
    plt.plot(tamanhos, tempos, marker='o')
    plt.title("Tempo de execução do prim por tamanho do grafo")
    plt.xlabel("Número de vértices")
    plt.ylabel("Tempo (s)")
    plt.grid(True)
    plt.savefig("tp5_ex12.png")


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

    print("========================== Análise do tempo")
    tamanhos, tempos = testar_tempos_prim()
    plotar_grafico(tamanhos, tempos)
