
from linkedList import LinkedList

# Exemplo de uso
lista = LinkedList()
lista.insert_at_end(10)
lista.insert_at_end(20)
lista.insert_at_end(30)
lista.insert_at_start(5)

lista.display() # Output esperado: 5 -> 10 -> 20 -> 30
print("Tamanho da lista:", lista.size()) # Output esperado: 4

lista.remove(20)
lista.display() # Output esperado: 5 -> 10 -> 30

nodo = lista.search(10)
print(f"Nó encontrado: {nodo.data}") if nodo else print("Nó não encontrado.")

lista.remove_first()
lista.display() # Output esperado: 10 -> 30

lista.remove_last()
lista.display() # Output esperado: 10
