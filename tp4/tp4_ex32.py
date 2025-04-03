import time
import random
import matplotlib.pyplot as plt
from ListaAdjacencia import Grafo


def gerar_arestas_aleatorias(num_vertices, num_arestas):
    vertices = [chr(65 + i) for i in range(num_vertices)]
    arestas = set()
    while len(arestas) < num_arestas:
        v1, v2 = random.sample(vertices, 2)
        arestas.add((v1, v2))
    return list(arestas)


def testar_tempos_dfs():
    tamanhos = [10, 50, 100, 200, 500, 700, 1000]
    tempos = []

    for tamanho in tamanhos:
        num_arestas = tamanho * 5
        arestas = gerar_arestas_aleatorias(tamanho, num_arestas)

        grafo = Grafo()
        grafo.criar_grafo_by_arestas(arestas)

        inicio = time.time()
        for _ in range(100):
            ordem = grafo.dfs(arestas[0][0])
        fim = time.time()

        tempo_execucao = (fim - inicio)/100
        tempos.append(tempo_execucao)
        print(f"\nGrafo com {tamanho} vértices: {tempo_execucao:.6f} segundos. Ordem de visita: \n {ordem}")

    return tamanhos, tempos


def plotar_grafico(tamanhos, tempos):
    plt.plot(tamanhos, tempos, marker='o')
    plt.title("Tempo de execução da DFS por tamanho do grafo")
    plt.xlabel("Número de vértices")
    plt.ylabel("Tempo (s)")
    plt.grid(True)
    plt.savefig("tp4_ex32.png")


if __name__ == "__main__":

    grafo = Grafo()

    arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"),
               ("D", "E")]
    grafo.criar_grafo_by_arestas(arestas)

    print(grafo.dfs("A"))

    print("========================== Análise do tempo")
    tamanhos, tempos = testar_tempos_dfs()
    plotar_grafico(tamanhos, tempos)
