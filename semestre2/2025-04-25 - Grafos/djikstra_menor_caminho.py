import matplotlib
matplotlib.use("TkAgg")
import networkx as nx
import matplotlib.pyplot as plt
import heapq

def show_graph(adj_list, caminho=None):
    G = nx.Graph()

    # Adicionar arestas com pesos
    for u in adj_list:
        for v, peso in adj_list[u]:
            G.add_edge(u, v, weight=peso)

    pos = nx.spring_layout(G)  # Layout automático
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # Desenhar todos os nós e arestas
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=14)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

    # Se houver caminho, destacar arestas
    if caminho:
        edge_path = list(zip(caminho, caminho[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edge_path, edge_color='red', width=4)

    plt.title("Grafo com menor caminho em vermelho (Dijkstra)")
    plt.show()




def dijkstra(adj_list, inicio, destino):
    distancias = {v: float('inf') for v in adj_list}
    distancias[inicio] = 0
    predecessores = {v: None for v in adj_list}
    heap = [(0, inicio)]

    while heap:
        dist_atual, atual = heapq.heappop(heap)

        if atual == destino:
            break

        for vizinho, peso in adj_list[atual]:
            nova_dist = dist_atual + peso
            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                predecessores[vizinho] = atual
                heapq.heappush(heap, (nova_dist, vizinho))

    caminho = []
    atual = destino
    while atual is not None:
        caminho.insert(0, atual)
        atual = predecessores[atual]

    return caminho, distancias[destino]


# Grafo ponderado
adj_list = {
    "A": [("B", 2), ("C", 4)],
    "B": [("A", 2), ("D", 7), ("E", 3)],
    "C": [("A", 4), ("E", 1)],
    "D": [("B", 7), ("E", 2)],
    "E": [("B", 3), ("C", 1), ("D", 2)]
}

caminho, custo = dijkstra(adj_list, "A", "D")
print("Menor caminho de A até D:", caminho)
print("Custo total:", custo)
show_graph(adj_list)