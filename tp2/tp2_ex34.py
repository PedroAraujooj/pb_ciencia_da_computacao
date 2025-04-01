class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def remove(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next
        if current is None:
            return
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.head:
            self.head = current.next

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.head
        if not current:
            print("None")
            return
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")
    def sort(self):
        if self.head is None or self.head.next is None:
            return
        flag = True
        while flag:
            flag = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    flag = True
                current = current.next

def mesclar_lista(list1, list2):
    new_list = DoublyLinkedList()
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data <= current2.data:
            new_list.insert_at_end(current1.data)
            current1 = current1.next
        else:
            new_list.insert_at_end(current2.data)
            current2 = current2.next

    while current1:
        new_list.insert_at_end(current1.data)
        current1 = current1.next

    while current2:
        new_list.insert_at_end(current2.data)
        current2 = current2.next

    return new_list

if __name__ == "__main__":
    print("Lista 1 ================================")

    dll = DoublyLinkedList()

    dll.insert_at_beginning(10)
    dll.insert_at_beginning(20)
    dll.insert_at_end(30)
    dll.insert_at_end(40)
    dll.insert_at_end(5)
    dll.insert_at_end(9)

    print("Percorrendo lista 1 da frente para trás:")
    dll.traverse_forward()

    print("Ordenando a lista 1 com Bubble Sort")
    dll.sort()
    print("Lista 1 ordenada (forward):")
    dll.traverse_forward()
    print("Lista 1 ordenada (backward):")
    dll.traverse_backward()

    print("Lista 2 ================================")

    dll2 = DoublyLinkedList()

    dll2.insert_at_beginning(14)
    dll2.insert_at_beginning(25)
    dll2.insert_at_end(2)
    dll2.insert_at_end(8)
    dll2.insert_at_end(39)
    dll2.insert_at_end(17)

    print("Percorrendo lista 2 da frente para trás:")
    dll2.traverse_forward()

    print("Ordenando a lista 2 com Bubble Sort")
    dll2.sort()
    print("Lista 2 ordenada (forward):")
    dll2.traverse_forward()
    print("Lista 2 ordenada (backward):")
    dll2.traverse_backward()

    print("Mescla  ================================")
    nova_lista = mesclar_lista(dll, dll2)
    nova_lista.traverse_forward()




