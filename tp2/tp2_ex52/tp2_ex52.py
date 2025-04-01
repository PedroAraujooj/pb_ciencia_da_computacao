import time
from multiprocessing import Process, Value
import matplotlib.pyplot as plt

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_subtree(node, target, found):
    if node is None or found.value:
        return
    if node.value == target:
        found.value = True
        return
    search_subtree(node.left, target, found)
    search_subtree(node.right, target, found)

def parallel_search(root, target):
    inicio = time.time()
    if root.value == target:
        fim = time.time()
        return True, fim - inicio
    found = Value('b', False)
    left_proc = Process(target=search_subtree, args=(root.left, target, found))
    right_proc = Process(target=search_subtree, args=(root.right, target, found))

    left_proc.start()
    right_proc.start()
    left_proc.join()
    right_proc.join()

    fim = time.time()
    if found.value == 1:
        return True, fim - inicio
    else:
        return False, fim - inicio


def search_aux(current, value):
    if current is None:
        return False
    if current.value == value:
        return True
    if value < current.value:
        return search_aux(current.left, value)
    else:
        return search_aux(current.right, value)

def search(current, value):
    inicio = time.time()
    result = search_aux(current, value)
    fim = time.time()
    return result, fim - inicio



if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(18)
    root.left.left.left = Node(1)
    root.left.left.right = Node(4)
    root.left.right.left = Node(6)
    root.left.right.right = Node(8)
    root.right.left.left = Node(11)
    root.right.left.right = Node(13)
    root.right.right.left = Node(16)
    root.right.right.right = Node(20)
    root.left.left.left.left = Node(0)
    root.left.left.left.right = Node(2)
    root.right.right.right.left = Node(19)
    root.right.right.right.right = Node(21)

    tempos_paralell = [0]*5
    tempos_seq = [0]*5

    tempos_paralell[0] = parallel_search(root, 10)[1]
    tempos_seq[0] = search(root, 10)[1]

    tempos_paralell[1] = parallel_search(root, 5)[1]
    tempos_seq[1] = search(root, 5)[1]

    tempos_paralell[2] = parallel_search(root, 3)[1]
    tempos_seq[2] = search(root, 3)[1]

    tempos_paralell[3] = parallel_search(root, 1)[1]
    tempos_seq[3] = search(root, 1)[1]

    tempos_paralell[4] = parallel_search(root, 0)[1]
    tempos_seq[4] = search(root, 0)[1]

    plt.figure(figsize=(8, 6))
    plt.plot(tempos_seq, [i for i in range(1, 6)], marker='o')
    plt.plot(tempos_paralell, [i for i in range(1, 6)], marker='x')
    plt.title('Número de camadas x Tempo de Execução')
    plt.xlabel('Segundos')
    plt.ylabel('Número de camadas')
    plt.grid(True)
    plt.savefig("tp2_ex52.png")



