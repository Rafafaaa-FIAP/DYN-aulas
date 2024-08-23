from stack import Stack
# import unittest

def verificar_parenteses_balanceados(expressao: str) -> bool:
  pilha = Stack()

  for c in expressao:
    if (c == '('):
      pilha.push('(')
    elif (c == ')'):
      if (pilha.is_empty()):
        return False
      else:
        pilha.pop()

  return pilha.is_empty()







# class TestVerificarParentesesBalanceados(unittest.TestCase):
#   def test_balanceado_simples(self):
#     self.assertTrue(verificar_parenteses_balanceados("(a + b) * (c + d)"))

#   def test_desbalanceado_faltando_fechamento(self):
#     self.assertFalse(verificar_parenteses_balanceados("((a + b) * c"))

#   def test_balanceado_complexo(self):
#     self.assertTrue(verificar_parenteses_balanceados("((a + b) * (c + d))"))

#   def test_desbalanceado_fechamento_excedente(self):
#     self.assertFalse(verificar_parenteses_balanceados("a + b) * (c + d)"))

#   def test_vazio(self):
#     self.assertTrue(verificar_parenteses_balanceados(""))

print(verificar_parenteses_balanceados("(a + b) * (c + d)"))
print(verificar_parenteses_balanceados("((a + b) * c"))
print(verificar_parenteses_balanceados("((a + b) * (c + d))"))
print(verificar_parenteses_balanceados("a + b) * (c + d)"))
print(verificar_parenteses_balanceados(""))