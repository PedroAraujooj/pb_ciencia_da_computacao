from MinHeap import MinHeap



if __name__ == "__main__":

    lista_inteiros = [4, 10, 3, 5, 1]
    min_heap = MinHeap()
    min_heap.criar_heap_by_lista(lista_inteiros)

    print(f"Heap antes da remoção:")
    min_heap.exibir_heap()

    print(f"Heap após a remoção do nó raiz:")
    min_heap.pop()
    min_heap.exibir_heap()
