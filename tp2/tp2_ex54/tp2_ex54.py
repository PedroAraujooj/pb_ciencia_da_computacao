import multiprocessing
from multiprocessing import Pool
import sys
import random
import time
import matplotlib.pyplot as plt

def find_parallel(arr):
    inicio = time.time()
    with Pool() as pool:
        chunk_size = len(arr) // 4
        chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]
        results = pool.map(max, chunks)
    fim = time.time()
    return max(results), fim - inicio

def find_seq(arr):
    inicio = time.time()
    result = max(arr)
    fim = time.time()
    return result, fim - inicio

if __name__ == '__main__':
    tempo_paralell = [0]*5
    tempo_seq = [0]*5
    for i in range(5):
        array = [random.randint(0, 100) for _ in range(1000*(i+1))]
        result_parallel = find_parallel(array)
        result_seq = find_seq(array)

        tempo_paralell[i] = result_parallel[1]
        tempo_seq[i] = result_seq[1]

        print(f"Valor maximo na lista {i} sequencial: {result_seq[0]}, tempo: {tempo_seq[i]:.12f}")
        print(f"Valor maximo na lista {i} sequencial: {result_parallel[0]}, tempo: {tempo_paralell[i]:.12f}")

        plt.figure(figsize=(8, 6))
        plt.plot(tempo_seq, [1000*(i+1) for i in range(0, 5)], marker='o')
        plt.plot(tempo_paralell, [1000*(i+1) for i in range(0, 5)], marker='x')
        plt.title('Tamanho da lista x Tempo de Execução')
        plt.xlabel('Segundos')
        plt.ylabel('Tamanho da lista')
        plt.grid(True)
        plt.savefig("tp2_ex54.png")