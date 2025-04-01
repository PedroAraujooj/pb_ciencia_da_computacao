import multiprocessing
from multiprocessing import Pool
import sys
import random
import time
import matplotlib.pyplot as plt

class ItemMochila:
    def __init__(self, nome, peso, valor):
        self.nome = nome
        self.peso = peso
        self.valor = valor
def knapsack(itens, w):
    n = len(itens)
    memo = [[0] * (w + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, w + 1):
            if itens[i - 1].peso > w:
                memo[i][w] = memo[i - 1][w]
            else:
                incluir = itens[i - 1].valor + memo[i - 1][w - itens[i - 1].peso]
                excluir = memo[i - 1][w]
                memo[i][w] = max(incluir, excluir)
    return memo[n][w]

if __name__ == '__main__':
    itens1 = [
        ItemMochila("Item1", peso=2, valor=3),
        ItemMochila("Item2", peso=3, valor=4),
        ItemMochila("Item3", peso=4, valor=5),
        ItemMochila("Item4", peso=5, valor=6)
    ]
    valor_maximo1 = knapsack(itens1, 5)
    print("Valor máximo que pode ser carregado exemplo1 :", valor_maximo1)

    itens2 = [
        ItemMochila("Item1", peso=9, valor=3),
        ItemMochila("Item2", peso=8, valor=8),
        ItemMochila("Item3", peso=1, valor=12),
        ItemMochila("Item4", peso=5, valor=3)
    ]
    valor_maximo2 = knapsack(itens2, 12)
    print("Valor máximo que pode ser carregado exemplo2 :", valor_maximo2)

    itens3 = [
        ItemMochila("Item1", peso=12, valor=3),
        ItemMochila("Item2", peso=5, valor=4),
        ItemMochila("Item3", peso=10, valor=5),
        ItemMochila("Item4", peso=9, valor=6),
        ItemMochila("Item5", peso=7, valor=7)
    ]
    valor_maximo3 = knapsack(itens3, 25)
    print("Valor máximo que pode ser carregado exemplo3 :", valor_maximo3)