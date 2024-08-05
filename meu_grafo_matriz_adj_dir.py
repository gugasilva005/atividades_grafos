from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *
from math import inf

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        pass

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        v = self.get_vertice(V)
        indiceVertice = self.indice_do_vertice(v)
        arestas = set()

        for j in range(len(self.arestas)):
            arestas.update(self.arestas[indiceVertice][j])

        for j in range(len(self.arestas)):
            arestas.update(self.arestas[j][indiceVertice])

        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass

    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        :return: Uma lista de listas que representa a matriz de alcançabilidade de Warshall associada ao grafo
        '''
        E = []
        for i in range(len(self.vertices)):
            linha = []
            for j in range(len(self.vertices)):
                if len(self.arestas[i][j]) >= 1:
                    linha.append(1)
                else:
                    linha.append(0)
            E.append(linha)
        
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                for k in range(len(self.vertices)):
                    E[i][j] = E[i][j] or (E[i][k] and E[k][j])
                
        return E
    
    def dijkstra(self, I, F):
        beta = {}
        phi = {}
        pi = {}
        w = I
        for n in self.vertices:
            v = str(n)
            beta[v] = inf
            phi[v] = 0
            pi[v] = 0
        beta[I] = 0
        phi[I] = 1
        w = I
        while True:
            sobre = self.arestas_sobre_vertice(w)
            if w == F:
                break
            for x in sobre:
                contrario = ""
                if w == x.v1.rotulo:
                    contrario = x.v2.rotulo
                else:
                    contrario = x.v1.rotulo
                if beta[contrario] > beta[w] + x.peso and phi[contrario] == 0:
                    beta[contrario] = beta[w] + x.peso
                    pi[contrario] = w
            menor = inf
            for i in beta:
                if beta[i] < menor and phi[i] == 0:
                    menor = beta[i]
            w = list(beta.keys())[list(beta.values()).index(menor)]
            phi[w] = 1
        r = F
        caminho = []
        while True:
            caminho.append(r)
            if r == I:
                return caminho
            r = pi[r]