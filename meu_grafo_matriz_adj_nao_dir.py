from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto (set) de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um conjunto (set) com os pares de vértices não adjacentes
        '''
        vert_nao_adj = set()
        for i in range(len(self.vertices)):
            for j in range(i + 1, len(self.vertices)):
                aresta = f"{self.vertices[i]}-{self.vertices[j]}"
                if len(self.arestas[i][j]) == 0:
                    vert_nao_adj.add(aresta)
        
        return vert_nao_adj

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        arestas = self.arestas
        for i in range(len(arestas)):
            if arestas[i][i]:
                return True
        return False
            


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        
        vertice = self.get_vertice(V)
        index_v = self.indice_do_vertice(vertice)
        grau = 0

        for j in range(index_v, len(self.vertices)):
            if j == index_v:
                grau += 2 * len(self.arestas[index_v][j])
            else:
                grau += len(self.arestas[index_v][j])
        
        for i in range(index_v):
            grau += len(self.arestas[i][index_v])
        
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.vertices)):
            for j in range(i, len(self.vertices)):
                if len(self.arestas[i][j]) > 1:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê um conjunto (set) que contém os rótulos das arestas que
        incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Um conjunto com os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        
        vertice = self.get_vertice(V)
        index_v = self.indice_do_vertice(vertice)
        arestas = set()

        for i in range(index_v, len(self.vertices)):
            atual = self.arestas[index_v][i]
            for a in atual:
                arestas.add(a)
        
        for j in range(index_v):
            atual = self.arestas[j][index_v]
            for a in atual:
                arestas.add(a)
        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco() or self.ha_paralelas():
            return False
        
        for i in range(len(self.vertices)):
            for j in range(i + 1, len(self.vertices)):
                if len(self.arestas[i][j]) == 0:
                    return False
        
        return True