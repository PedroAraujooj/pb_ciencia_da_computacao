from MinHeap import MinHeap



if __name__ == "__main__":

    lista_inteiros = [4, 10, 3, 5, 1]
    min_heap = MinHeap()
    min_heap.criar_heap_by_lista(lista_inteiros)
    print(f"Heap: ")
    min_heap.exibir_heap()

    print(f"\nHeap contêm 12?:")
    print(min_heap.buscar(12))
    print(f"Heap contêm 5?:")
    print(min_heap.buscar(5))
