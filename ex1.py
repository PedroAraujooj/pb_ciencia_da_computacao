import time


def read_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


def insertion(arr):
    for i in range(1, len(arr)):
        ele = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > ele:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = ele


def calcular_media_bubble(arr):
    print(f"---------------------- Bubble Sort ----------------------")

    listaMediaTempo = [0] * 10
    arrays = []
    for i in range(1000, 10001, 1000):
        arrays.append(arr[:i])
    for _ in range(10):
        for id, array in enumerate(arrays):
            tempInicial = time.time()
            bubble(array)
            temp_final = time.time() - tempInicial
            listaMediaTempo[id] += temp_final
    for i in range(10):
        print(
            f"Bubble Sort - Ordenação de {1000 * (i + 1)} elementos: tempo médio = {(listaMediaTempo[i] / 10):.6f}s")


def calcular_media_selection(arr):
    print(f"---------------------- Selection Sort ----------------------")

    listaMediaTempo = [0] * 10
    arrays = []
    for i in range(1000, 10001, 1000):
        arrays.append(arr[:i])
    for _ in range(10):
        for id, array in enumerate(arrays):
            tempInicial = time.time()
            selection(array)
            temp_final = time.time() - tempInicial
            listaMediaTempo[id] += temp_final
    for i in range(10):
        print(
            f"Selection Sort - Ordenação de {1000 * (i + 1)} elementos: tempo médio = {(listaMediaTempo[i] / 10):.6f}s")


def calcular_media_insertion(arr):
    print(f"---------------------- Insertion Sort ----------------------")

    listaMediaTempo = [0] * 10
    arrays = []
    for i in range(1000, 10001, 1000):
        arrays.append(arr[:i])
    for _ in range(10):
        for id, array in enumerate(arrays):
            tempInicial = time.time()
            insertion(array)
            temp_final = time.time() - tempInicial
            listaMediaTempo[id] += temp_final
    for i in range(10):
        print(
            f"Insertion Sort - Ordenação de {1000 * (i + 1)} elementos: tempo médio = {(listaMediaTempo[i] / 10):.6f}s")


if __name__ == "__main__":
    file = 'pb_tp1.txt'
    list = read_file(file)

    calcular_media_bubble(list.copy())
    calcular_media_selection(list.copy())
    calcular_media_insertion(list.copy())
