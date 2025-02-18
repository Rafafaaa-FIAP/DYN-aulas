class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)

raiz = NodoArvore(3)
raiz.esquerda = NodoArvore(5)
raiz.direita = NodoArvore(1)
print(raiz)