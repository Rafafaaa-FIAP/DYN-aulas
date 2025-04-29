import matplotlib
matplotlib.use("TkAgg")
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def show_graph(adj_list, path=None):
    G = nx.Graph()

    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)  # posição "bonita"

    # Desenho do grafo
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500,
            font_size=16)

    # Se caminho fornecido, destacar
    if path:
        edge_path = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edge_path, edge_color='red', width=4)

    plt.title("Menor caminho em vermelho (BFS)")
    plt.show()

def bfs_menor_caminho(adj_list, inicio, destino):
    visitados = set()
    fila = deque([inicio])
    predecessores = {inicio: None}


    while fila:
        print('Predecessores: ', predecessores)
        atual = fila.popleft()

        if atual == destino:
            break

        for vizinho in adj_list[atual]:
            if vizinho not in predecessores:
                predecessores[vizinho] = atual
                fila.append(vizinho)

    # Reconstruir o caminho
    caminho = []
    atual = destino
    while atual is not None:
        caminho.insert(0, atual)
        atual = predecessores.get(atual)

    return caminho

# Lista de adjacência
adj_list = {
    "A": ["B", "C"],
    "B": ["A", "E"],
    "C": ["A", "D"],
    "D": ["C", "E"],
    "E": ["B", "D"]
}

# Executar busca
caminho = bfs_menor_caminho(adj_list, "A", "E")
print("Menor caminho de A até E:", caminho)

# Mostrar grafo com caminho
show_graph(adj_list, path=caminho)
