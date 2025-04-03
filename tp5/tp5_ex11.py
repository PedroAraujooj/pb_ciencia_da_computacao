from tp5.GrafoPonderado import GrafoPonderado
import time
import random
import matplotlib.pyplot as plt


def gerar_arestas_aleatorias(grafo_grande, num_vertices, num_arestas):
    nodes = [f"C{i}" for i in range(num_vertices)]
    for no in nodes:
        grafo_grande.vertices[no] = []
    for _ in range(num_arestas):
        u = random.choice(nodes)
        v = random.choice(nodes)
        if u != v:
            peso = random.randint(1, 1000)
            grafo_grande.adicionar_arestas(u, v, peso)


def testar_tempos_dijkstra():
    tamanhos = [10, 50, 100, 200, 500, 700, 1000]
    tempos = []

    for tamanho in tamanhos:
        num_arestas = tamanho * 5
        grafo = GrafoPonderado()
        gerar_arestas_aleatorias(grafo, tamanho, num_arestas)

        inicio = time.time()
        for _ in range(100):
            distancias, predecessores = grafo.dijkstra("C0")
        fim = time.time()

        tempo_execucao = (fim - inicio) / 100
        tempos.append(tempo_execucao)
        print(f"\nGrafo com {tamanho} vértices: {tempo_execucao:.6f} segundos. Ordem de visita: \n {predecessores}")

    return tamanhos, tempos


def plotar_grafico(tamanhos, tempos):
    plt.plot(tamanhos, tempos, marker='o')
    plt.title("Tempo de execução do dijkstra por tamanho do grafo")
    plt.xlabel("Número de vértices")
    plt.ylabel("Tempo (s)")
    plt.grid(True)
    plt.savefig("tp5_ex11.png")


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

    print("========================== Análise do tempo")
    tamanhos, tempos = testar_tempos_dijkstra()
    plotar_grafico(tamanhos, tempos)
