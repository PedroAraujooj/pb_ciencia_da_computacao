import multiprocessing
from multiprocessing import Pool
import sys
import random
import time
import matplotlib.pyplot as plt

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)

def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    with Pool() as pool:
        sorted_left, sorted_right = pool.map(merge_sort, [left, right])
    return merge(sorted_left, sorted_right)

if __name__ == '__main__':
    tempo_paralell = [0]*5
    tempo_seq = [0]*5
    for i in range(5):
        array = [random.randint(0, 100) for _ in range(1000*(i+1))]

        inicio_paralell = time.time()
        parallel_result = parallel_merge_sort(array.copy())
        fim_paralell = time.time()
        tempo_paralell[i] = fim_paralell - inicio_paralell

        inicio_seq = time.time()
        seq_result = merge_sort(array.copy())
        fim_seq = time.time()
        tempo_paralell[i] = fim_seq - inicio_seq

        plt.figure(figsize=(8, 6))
        plt.plot(tempo_seq, [1000*(i+1) for i in range(0, 5)], marker='o')
        plt.plot(tempo_paralell, [1000*(i+1) for i in range(0, 5)], marker='x')
        plt.title('Tamanho da lista x Tempo de Execução')
        plt.xlabel('Segundos')
        plt.ylabel('Tamanho da lista')
        plt.grid(True)
        plt.savefig("tp2_ex53.png")