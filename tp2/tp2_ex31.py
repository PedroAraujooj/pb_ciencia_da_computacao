class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
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

    def remove(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(20)
    linked_list.insert_at_beginning(30)
    linked_list.insert_at_beginning(40)
    linked_list.insert_at_end(50)
    linked_list.insert_at_end(60)
    linked_list.insert_at_beginning(5)
    print("Lista após inserções:")
    linked_list.traverse()

    linked_list.remove(20)
    print("Lista após remoção de 20:")
    linked_list.traverse()

    linked_list.remove(50)
    print("Lista após remoção de 50:")
    linked_list.traverse()


