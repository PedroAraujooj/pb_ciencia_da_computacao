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
