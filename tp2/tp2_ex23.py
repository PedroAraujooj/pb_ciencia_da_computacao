import time
import random
def quickselect(array, low, high, k):
    if low == high:
        return array[low]
    pivot_index = partition(array, low, high)
    if k == pivot_index:
        return array[k]
    elif k < pivot_index:
        return quickselect(array, low, pivot_index - 1, k)
    else:
        return quickselect(array, pivot_index + 1, high, k)

def partition(array, low, high):
    pivot = array[high]
    i = low
    for j in range(low, high):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i

if __name__ == "__main__":
    for i in range(10):
        print(f"Lista {i + 1}")
        lista = [random.randint(1, 1000) for _ in range(10000)]
        k1 = quickselect(lista.copy(), 0, len(lista) - 1, 0)
        print(f"O {1}º menor elemento do array é: {k1}")
        k5 = quickselect(lista.copy(), 0, len(lista) - 1, 4)
        print(f"O {5}º menor elemento do array é: {k5}")
        k10 = quickselect(lista.copy(), 0, len(lista) - 1, 9)
        print(f"O {10}º menor elemento do array é: {k10}")
        k15 = quickselect(lista.copy(), 0, len(lista) - 1, 14)
        print(f"O {15}º menor elemento do array é: {k15}")
        k20 = quickselect(lista.copy(), 0, len(lista) - 1, 19)
        print(f"O {20}º menor elemento do array é: {k20}")

