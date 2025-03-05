class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)

def pre_ordem(raiz):
    if not raiz:
        return

    # Visita nodo corrente.
    print(raiz.chave)
    # Visita filho da esquerda.
    pre_ordem(raiz.esquerda)
    # Visita filho da direita.
    pre_ordem(raiz.direita)

# raiz = NodoArvore(3)
# raiz.esquerda = NodoArvore(5)
# raiz.direita = NodoArvore(1)
# pre_ordem(raiz)

def insere(raiz, nodo):
    # Insere um nodo em uma árvore binária de pesquisa.
    # Nodo deve ser inserido na raiz.
    if raiz is None:
        raiz = nodo
    # Nodo deve ser inserido na subárvore direita.
    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)
    # Nodo deve ser inserido na subárvore esquerda.
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)

raiz = NodoArvore(40)
for chave in [20,60,50,70,10,30]:
    nodo = NodoArvore(chave)
    insere(raiz, nodo)
print(raiz)
