from stack import Stack
import unittest

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

class TestVerificarParentesesBalanceados(unittest.TestCase):
  def test_balanceado_simples(self):
    self.assertTrue(verificar_parenteses_balanceados("(a + b) * (c + d)"))

  def test_desbalanceado_faltando_fechamento(self):
    self.assertFalse(verificar_parenteses_balanceados("((a + b) * c"))

  def test_balanceado_complexo(self):
    self.assertTrue(verificar_parenteses_balanceados("((a + b) * (c + d))"))

  def test_desbalanceado_fechamento_excedente(self):
    self.assertFalse(verificar_parenteses_balanceados("a + b) * (c + d)"))

  def test_vazio(self):
    self.assertTrue(verificar_parenteses_balanceados(""))

def decimal_para_binario(decimal: int) -> str:
  ''' Converte um número decimal para binário usando uma pilha. '''
  if decimal == 0:
    return "0"
  pilha = Stack()
  while decimal > 0:
    resto = decimal % 2
  pilha.push(resto)
  decimal = decimal // 2
  binario = ""
  while not pilha.is_empty():
    binario += str(pilha.pop())
  # Adicionar zeros à esquerda para completar 8 bits (se necessário)
  return binario.zfill(8)