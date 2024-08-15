
import matplotlib.pyplot as plt
import networkx as nx
from meu_grafo_lista_adj import *
# Função para visualizar um grafo


def visualizar_grafo(grafo, layout='spring'):
    G = nx.DiGraph()  # Usar DiGraph para grafos direcionados
    for v in grafo.vertices:
        G.add_node(str(v))
    for a in grafo.arestas.values():
        G.add_edge(str(a.v1.rotulo), str(a.v2.rotulo),
                   weight=a.peso, label=str(a.peso))

    plt.figure(figsize=(10, 5))  # Ajustar o tamanho da figura

    # Escolher o layout
    if layout == 'spring':
        pos = nx.spring_layout(G, k=0.5, iterations=50)
    elif layout == 'shell':
        pos = nx.shell_layout(G)
    elif layout == 'spectral':
        pos = nx.spectral_layout(G)
    elif layout == 'kamada_kawai':
        pos = nx.kamada_kawai_layout(G)
    else:
        pos = nx.spring_layout(G, k=0.5, iterations=50)

    nx.draw(G, pos, with_labels=True, node_size=400, node_color='lightblue', font_size=10, font_weight='bold',
            arrowsize=20)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels, font_color='red')

    plt.show()


grafo_drone_bellman = MeuGrafo()
grafo_drone_bellman.adiciona_vertice('A')
grafo_drone_bellman.adiciona_vertice('B')
grafo_drone_bellman.adiciona_vertice('C')
grafo_drone_bellman.adiciona_vertice('D')
grafo_drone_bellman.adiciona_vertice('E')
grafo_drone_bellman.adiciona_vertice('F')
grafo_drone_bellman.adiciona_vertice('G')
grafo_drone_bellman.adiciona_vertice('H')
grafo_drone_bellman.adiciona_vertice('I')
grafo_drone_bellman.adiciona_vertice('J')
grafo_drone_bellman.adiciona_vertice('K')
grafo_drone_bellman.adiciona_vertice('L')
grafo_drone_bellman.adiciona_vertice('M')
grafo_drone_bellman.adiciona_vertice('N')
grafo_drone_bellman.adiciona_vertice('O')
grafo_drone_bellman.adiciona_vertice('P')
grafo_drone_bellman.adiciona_vertice('Q')
grafo_drone_bellman.adiciona_vertice('R')
grafo_drone_bellman.adiciona_vertice('S')
grafo_drone_bellman.adiciona_vertice('T')
grafo_drone_bellman.adiciona_vertice('U')
grafo_drone_bellman.adiciona_vertice('V')
grafo_drone_bellman.adiciona_vertice('W')
grafo_drone_bellman.adiciona_vertice('X')
grafo_drone_bellman.adiciona_vertice('Y')
grafo_drone_bellman.adiciona_vertice('Z')
grafo_drone_bellman.adiciona_vertice('AA')
grafo_drone_bellman.adiciona_vertice('AB')
grafo_drone_bellman.adiciona_vertice('AC')
grafo_drone_bellman.adiciona_vertice('AD')
grafo_drone_bellman.adiciona_vertice('AE')
grafo_drone_bellman.adiciona_vertice('AF')
grafo_drone_bellman.adiciona_vertice('AG')
grafo_drone_bellman.adiciona_aresta('a1', 'A', 'B', 1)
grafo_drone_bellman.adiciona_aresta('a2', 'B', 'I', 1)
grafo_drone_bellman.adiciona_aresta('a3', 'I', 'J', 1)
grafo_drone_bellman.adiciona_aresta('a4', 'J', 'U', 1)
grafo_drone_bellman.adiciona_aresta('a5', 'U', 'V', 1)
grafo_drone_bellman.adiciona_aresta('a6', 'V', 'Y', 1)
grafo_drone_bellman.adiciona_aresta('a7', 'Y', 'X', 1)
grafo_drone_bellman.adiciona_aresta('a8', 'X', 'Z', 1)
grafo_drone_bellman.adiciona_aresta('a9', 'B', 'H', -1)
grafo_drone_bellman.adiciona_aresta('a10', 'A', 'C', 3)
grafo_drone_bellman.adiciona_aresta('a11', 'A', 'D', 2)
grafo_drone_bellman.adiciona_aresta('a12', 'D', 'E', 4)
grafo_drone_bellman.adiciona_aresta('a13', 'C', 'F', -2)
grafo_drone_bellman.adiciona_aresta('a14', 'E', 'F', 2)
grafo_drone_bellman.adiciona_aresta('a15', 'F', 'G', 3)
grafo_drone_bellman.adiciona_aresta('a16', 'H', 'G', 2)
grafo_drone_bellman.adiciona_aresta('a17', 'G', 'K', 2)
grafo_drone_bellman.adiciona_aresta('a18', 'F', 'L', 2)
grafo_drone_bellman.adiciona_aresta('a19', 'F', 'K', 3)
grafo_drone_bellman.adiciona_aresta('a20', 'E', 'M', 4)
grafo_drone_bellman.adiciona_aresta('a21', 'M', 'N', 3)
grafo_drone_bellman.adiciona_aresta('a22', 'L', 'O', 3)
grafo_drone_bellman.adiciona_aresta('a23', 'K', 'P', 2)
grafo_drone_bellman.adiciona_aresta('a24', 'K', 'I', 3)
grafo_drone_bellman.adiciona_aresta('a25', 'G', 'B', 2)
grafo_drone_bellman.adiciona_aresta('a26', 'J', 'Q', 3)
grafo_drone_bellman.adiciona_aresta('a27', 'Q', 'S', 7)
grafo_drone_bellman.adiciona_aresta('a28', 'S', 'AC', 2)
grafo_drone_bellman.adiciona_aresta('a29', 'AB', 'S', 3)
grafo_drone_bellman.adiciona_aresta('a30', 'O', 'U', 3)
grafo_drone_bellman.adiciona_aresta('a31', 'N', 'AA', 3)
grafo_drone_bellman.adiciona_aresta('a32', 'P', 'AA', 2)
grafo_drone_bellman.adiciona_aresta('a33', 'D', 'C', 2)
grafo_drone_bellman.adiciona_aresta('a34', 'R', 'Q', 3)
grafo_drone_bellman.adiciona_aresta('a35', 'P', 'R', 2)
grafo_drone_bellman.adiciona_aresta('a36', 'P', 'U', 4)
grafo_drone_bellman.adiciona_aresta('a37', 'U', 'R', 3)
grafo_drone_bellman.adiciona_aresta('a38', 'R', 'T', -1)
grafo_drone_bellman.adiciona_aresta('a39', 'T', 'W', 1)
grafo_drone_bellman.adiciona_aresta('a40', 'W', 'U', 2)
grafo_drone_bellman.adiciona_aresta('a41', 'V', 'AF', 2)
grafo_drone_bellman.adiciona_aresta('a42', 'T', 'AG', 2)
grafo_drone_bellman.adiciona_aresta('a43', 'T', 'AB', 1)
grafo_drone_bellman.adiciona_aresta('a44', 'Y', 'W', 3)
grafo_drone_bellman.adiciona_aresta('a45', 'AC', 'AD', 4)
grafo_drone_bellman.adiciona_aresta('a46', 'AD', 'X', 3)
grafo_drone_bellman.adiciona_aresta('a47', 'X', 'AE', 2)
visualizar_grafo(grafo_drone_bellman)
