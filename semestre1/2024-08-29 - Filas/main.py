
from deque import Deque
import unittest

class Atendimento:
    def __init__(self):
        self.fila_padrao = Deque()
        self.fila_prioritaria = Deque()

    def enfileirar_elemento(self, pessoa):
        if (pessoa['idade'] <= 65):
            self.fila_padrao.enqueue_rear(pessoa)
        else:
            self.fila_prioritaria.enqueue_rear(pessoa)

    def ajustar_filas(self):
        pass


class TestDeque(unittest.TestCase):
    def setUp(self):
        self.atendimento = Atendimento()

    def test_enfileirar_varias_pessoas(self):
        pessoas = [
            {'nome': 'João', 'idade': 30},
            {'nome': 'Maria', 'idade': 70},
            {'nome': 'Ana', 'idade': 65},
            {'nome': 'Carlos', 'idade': 80}
        ]
        for pessoa in pessoas:
            self.atendimento.enfileirar_elemento(pessoa)

        self.assertEqual(self.atendimento.fila_padrao.size(), 2)
        self.assertEqual(self.atendimento.fila_prioritaria.size(), 2)
        self.assertEqual(self.atendimento.fila_padrao.peek_front(), pessoas[0])
        self.assertEqual(self.atendimento.fila_prioritaria.peek_front(), pessoas[1])
        self.assertEqual(self.atendimento.fila_prioritaria.peek_rear(), pessoas[3])