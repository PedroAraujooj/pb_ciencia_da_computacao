import math
import random
import time
import matplotlib.pyplot as plt


def plotar_grafico(tamanhos, tempos):
    plt.plot(tamanhos, tempos, marker='o')
    plt.title("Tempo de execução do Vizinho Mais Próximo por quantidade de itens")
    plt.xlabel("Número de itens")
    plt.ylabel("Tempo (s)")
    plt.grid(True)
    plt.savefig("tp5_ex22.png")

def gerar_itens_aleatorios(quantidade):
    itens = {}
    for i in range(1, quantidade + 1):
        coordenada1 = random.randint(1, quantidade * 2)
        coordenada2 = random.randint(1, quantidade * 2)
        itens[f'item{i}'] = (coordenada1, coordenada2)
    return itens


def distancia(a, b):
    x1, y1 = a
    x2, y2 = b
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def tsp_vizinho_mais_proximo(cidades, inicio='A'):
    nao_visitadas = set(cidades.keys())
    rota = [inicio]
    nao_visitadas.remove(inicio)

    atual = inicio

    while nao_visitadas:
        proxima, dist_min = None, float('inf')
        for c in nao_visitadas:
            d = distancia(cidades[atual], cidades[c])
            if d < dist_min:
                dist_min = d
                proxima = c
        rota.append(proxima)
        nao_visitadas.remove(proxima)
        atual = proxima

    rota.append(inicio)
    return rota


if __name__ == "__main__":
    cidades = {
        'A': (0, 0),
        'B': (1, 5),
        'C': (5, 2),
        'D': (6, 6),
        'E': (8, 3)
    }
    cidade_inicial = 'A'
    rota_encontrada = tsp_vizinho_mais_proximo(cidades, inicio=cidade_inicial)
    print("Rota encontrada:", " -> ".join(rota_encontrada))

    print("========================== Análise do tempo")
    tamanhos = [8, 64, 128, 256, 512, 1024, 2048, 4096]
    tempos = []
    for i in tamanhos:
        quantidade_itens = i
        itens = gerar_itens_aleatorios(quantidade_itens)
        inicio = time.time()
        for _ in range(100):
            resultado = tsp_vizinho_mais_proximo(itens, inicio=next(iter(itens)))
        fim = time.time()
        tempo = (fim - inicio) / 100
        tempos.append(tempo)
        print("Rota encontrada:", " -> ".join(resultado))
        print(f"Tempo de execução com {i} cidades : {tempo:.6f}")
    plotar_grafico(tamanhos, tempos)
