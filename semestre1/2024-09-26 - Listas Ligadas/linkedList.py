
from node import Node

class LinkedList:
    def __init__(self):
        self.head = None # Cabeça da lista (primeiro nó)

    # Método para verificar se a lista está vazia
    def is_empty(self):
        return self.head is None

    # Método para adicionar um nó ao início da lista
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Método para adicionar um nó ao final da lista
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Método para buscar um nó na lista
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    # Método para remover um nó específico da lista
    def remove(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next
        print(f"Nó com dado {data} não encontrado.")

    # Método para exibir a lista
    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        print(" -> ".join(nodes))

    # Método para obter o tamanho da lista
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # Método para remover o primeiro nó da lista
    def remove_first(self):
        if not self.is_empty():
            self.head = self.head.next
        else:
            print("A lista está vazia.")

    # Método para remover o último nó da lista
    def remove_last(self):
        if self.is_empty():
            print("A lista está vazia.")
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None
