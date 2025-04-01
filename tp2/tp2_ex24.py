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
    lista = [random.randint(1, 1000) for _ in range(10000)]
    k_mid = quickselect(lista.copy(), 0, len(lista) - 1, len(lista) // 2)
    print(f"A mediana do array é: {k_mid}")

