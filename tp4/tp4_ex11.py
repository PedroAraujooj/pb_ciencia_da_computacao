from MinHeap import MinHeap



if __name__ == "__main__":

    lista_inteiros = [4, 10, 3, 5, 1]
    minh_heap = MinHeap()
    minh_heap.criar_heap_by_lista(lista_inteiros)
    minh_heap.exibir_heap()