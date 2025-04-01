import time
import random

def quicksort_last(array):
    if len(array) <= 1:
        return array
    pivot = array[-1]
    menores = [x for x in array[:-1] if x <= pivot]
    maiores = [x for x in array[:-1] if x > pivot]
    return quicksort_last(menores) + [pivot] + quicksort_last(maiores)

def quicksort_mid(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    pivot = array[mid]
    resto = array[:mid] + array[mid+1:]
    menores = [x for x in resto if x <= pivot]
    maiores = [x for x in resto if x > pivot]
    return quicksort_mid(menores) + [pivot] + quicksort_mid(maiores)

def quicksort_first(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    menores = [x for x in array[1:] if x <= pivot]
    maiores = [x for x in array[1:] if x > pivot]
    return quicksort_first(menores) + [pivot] + quicksort_first(maiores)

def calcular_tempo(func, arr):
    inicio = time.time()
    func(arr)
    fim = time.time()
    return fim - inicio

if __name__ == "__main__":
    tempos = [0]*3
    for _ in range(10):
        listaMil = list(range(0, 1000))
        random.shuffle(listaMil)
        tempos[0] += calcular_tempo(quicksort_first, listaMil.copy())
        tempos[1] += calcular_tempo(quicksort_mid, listaMil.copy())
        tempos[2] += calcular_tempo(quicksort_last, listaMil.copy())
    tempos[0] = tempos[0]/10
    tempos[1] = tempos[1]/10
    tempos[2] = tempos[2]/10
    print(f"Tempo do quicksort com o pivot no inicio: {(tempos[0]):.6f} segundos")
    print(f"Tempo do quicksort com o pivot no meio: {(tempos[1]):.6f} segundos")
    print(f"Tempo do quicksort com o pivot no final: {(tempos[2]):.6f} segundos")