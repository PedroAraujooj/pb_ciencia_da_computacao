import random
import time
import matplotlib.pyplot as plt


def plotar_grafico(tamanhos, tempos):
    plt.plot(tamanhos, tempos, marker='o')
    plt.title("Tempo de execução da mochila gulosa por quantidade de itens")
    plt.xlabel("Número de itens")
    plt.ylabel("Tempo (s)")
    plt.grid(True)
    plt.savefig("tp5_ex21.png")


def gerar_itens_aleatorios(quantidade, peso_max=10, valor_max=100):
    itens = {}
    for i in range(1, quantidade + 1):
        peso = random.randint(1, peso_max)
        valor = random.randint(10, valor_max)
        itens[f'item{i}'] = (peso, valor)
    return itens


def mochila_gulosa(capacidade, itens):
    itens_ordenados = sorted(itens.items(), key=lambda item: item[1][1] / item[1][0], reverse=True)

    valor_total = 0
    peso_atual = 0

    for nome, (peso, valor) in itens_ordenados:
        if peso_atual + peso <= capacidade:
            peso_atual += peso
            valor_total += valor

    return valor_total


if __name__ == "__main__":
    itens = {'item1': (2, 40), 'item2': (3, 50), 'item3': (5, 100), 'item4': (4, 90)}
    capacidade = 8
    resultado = mochila_gulosa(capacidade, itens)
    print("Valor máximo possível na mochila:", resultado)

    print("========================== Análise do tempo")
    tamanhos = [8, 64, 128, 256, 512, 1024]
    tempos = []
    for i in tamanhos:
        quantidade_itens = i
        capacidade = i * 2
        itens = gerar_itens_aleatorios(quantidade_itens)
        inicio = time.time()
        for _ in range(100):
            resultado = mochila_gulosa(capacidade, itens)
        fim = time.time()
        tempo = (fim - inicio) / 100
        tempos.append(tempo)
        print(f"\nValor máximo possível na mochila com {i} itens: ", resultado)
        print(f"Tempo de execução: {tempo:.6f}")
    plotar_grafico(tamanhos, tempos)
