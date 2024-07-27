import matplotlib.pyplot as plt
import networkx as nx
from meu_grafo_lista_adj import *
# Função para visualizar um grafo


def visualizar_grafo(grafo):
    G = nx.Graph()
    for v in grafo.vertices:
        G.add_node(str(v))
    for a in grafo.arestas.values():
        G.add_edge(str(a.v1.rotulo), str(a.v2.rotulo))
    nx.draw(G, with_labels=True)
    plt.show()


# Exemplo de uso ['E', 'a2', 'C', 'a7', 'M', 'a8', 'T', 'a9', 'Z']
g_teste3 = MeuGrafo()
g_teste3.adiciona_vertice('A')
g_teste3.adiciona_vertice('B')
g_teste3.adiciona_vertice('C')
g_teste3.adiciona_vertice('D')
g_teste3.adiciona_vertice('E')
g_teste3.adiciona_vertice('F')
g_teste3.adiciona_aresta('a1', 'A', 'B')
g_teste3.adiciona_aresta('a2', 'A', 'C')
g_teste3.adiciona_aresta('a3', 'C', 'D')
g_teste3.adiciona_aresta('a4', 'B', 'D')
g_teste3.adiciona_aresta('a5', 'C', 'F')
g_teste3.adiciona_aresta('a6', 'D', 'E')
g_teste3.adiciona_aresta('a7', 'E', 'F')
visualizar_grafo(g_teste3)