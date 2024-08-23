class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    ''' Verifica se a pilha está vazia. '''
    return len(self.items) == 0
  
  def push(self, item):
    ''' Adiciona um item no topo da pilha. '''
    self.items.append(item)

  def pop(self):
    ''' Remove e retorna o item do topo da pilha. '''
    if (self.is_empty()):
      raise IndexError('A pilha está vazia!')
    return self.items.pop()
  
  def size(self):
    ''' Retorna o número de itens na pilha. '''
    return len(self.items)
  
  def peek(self):
    ''' Retorna o item do topo da pilha sem removê-lo. '''
    if (self.is_empty()):
      raise IndexError('A pilha está vazia!')
    return self.items[-1]
  
  def __str__(self):
    result = ''
    for i in reversed(self.items):
      result += f'\n|{i}|'
    return result