import numpy as np
import soma_vetor_parallel
import time


def soma_paralela(arr):
    inicio = time.time()
    resultado = soma_vetor_parallel.soma_vetor_parallel(arr)
    print("Soma paralela :", resultado)
    fim = time.time()
    return fim - inicio


def soma_sequencial(arr):
    inicio = time.time()
    total = 0.0
    for i in range(len(arr)):
        total += arr[i]
    print("Soma sequenial :", total)
    fim = time.time()
    return fim - inicio


if __name__ == "__main__":
    arr = np.random.rand(1_000_000)
    print("Tempo de execução paralela: " + str(soma_paralela(arr.copy())))
    print("Tempo de execução sequencial: " + str(soma_sequencial(arr.copy())))