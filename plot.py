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
grafo1 = MeuGrafo()
grafo1.adiciona_vertice("E")
grafo1.adiciona_vertice("C")
grafo1.adiciona_vertice("M")
grafo1.adiciona_vertice("T")
grafo1.adiciona_vertice("Z")
grafo1.adiciona_aresta('a2', 'E', 'C')
grafo1.adiciona_aresta('a7', 'C', 'M')
grafo1.adiciona_aresta('a8', 'M', 'T')
grafo1.adiciona_aresta('a9', 'T', 'Z')
visualizar_grafo(grafo1)