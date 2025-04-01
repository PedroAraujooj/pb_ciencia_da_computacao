import time
import matplotlib.pyplot as plt


def permutacoes_aux(string, lista, prefixo=""):
    if len(string) == 0:
        lista.add(prefixo)
    else:
        for i in range(len(string)):
            ch = string[i]
            resto = string[:i] + string[i+1:]
            permutacoes_aux(resto, lista, prefixo + ch)

def permutacoes(string):
    lista = set()
    permutacoes_aux(string, lista)
    return lista

if __name__ == "__main__":
    print(permutacoes("ABC"))


