from MinHeap import MinHeap



if __name__ == "__main__":

    lista_inteiros = [4, 10, 3, 5, 1]
    min_heap = MinHeap()
    min_heap.criar_heap_by_lista(lista_inteiros)

    print(f"Heap antes da adição:")
    min_heap.exibir_heap()

    print(f"Heap após da adição:")
    min_heap.insert(6)
    min_heap.exibir_heap()
