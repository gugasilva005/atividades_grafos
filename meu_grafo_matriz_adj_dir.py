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
        n_adjacentes = set()
        vertices = [str(vertice) for vertice in self.vertices]

        for vertice in vertices:
            v_adj = set()
            for aresta_str in sorted(self.arestas_sobre_vertice_dir(vertice)):
                aresta = self.get_aresta(aresta_str)
                v1 = str(aresta.v1)
                v2 = str(aresta.v2)

                if v2 == vertice:
                    continue
                v_adj.add(v1 if v1 != vertice else v2)
            
            for vert in vertices:
                if vert not in v_adj and vert != vertice:
                    n_adjacentes.add(f'{vertice}-{vert}')
        
        return n_adjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        vertices = [str(vertice) for vertice in self.vertices]
        str_arestas = [
            aresta for vertice in vertices for aresta in
            self.arestas_sobre_vertice_dir(vertice)]

        for str_aresta in str_arestas:
            aresta = self.get_aresta(str_aresta)
            if aresta.v1 == aresta.v2:
                return True
        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        
        arestas = self.arestas_sobre_vertice_dir(V)
        count = 0

        for rotulo_aresta in arestas:
            aresta = self.get_aresta(rotulo_aresta)
            if str(aresta.v1) == V:
                count += 1
            if str(aresta.v2) == V:
                count += 1
        
        return count


    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for linha in self.arestas:
            for obj in linha:
                if len(obj) > 1:
                    return True
        return False

    def arestas_sobre_vertice_dir(self, V):
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
    
    def dijkstra(self, U, V):

        if not self.existe_rotulo_vertice(U) or not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        
        vertices = {}
        
        def get_pi(v):
            return vertices[v]['pi']
        def get_phi(v):
            return vertices[v]['phi']
        def get_beta(v):
            return vertices[v]['beta']
       
        for vertice in self.vertices:
            vertice_str = str(vertice)
            if vertice_str == U:
                vertices.update({vertice_str: {'beta': 0.0, 'phi': 1, 'pi': None}})
            else:
                vertices.update({vertice_str: {'beta': inf, 'phi': 0, 'pi': None}})

        w = U
        v_n_visitados: set[str] = {str(vert) for vert in self.vertices}

        while True:
            if (w == V):
                v_n_visitados.remove(w)
                break

            arestas: list[str] = sorted(self.arestas_sobre_vertice_dir(w))
            for aresta in arestas:
                obj_a = self.get_aresta(aresta)
                v_adj = str(obj_a.v2)
                if get_beta(v_adj) > get_beta(w) + obj_a.peso:
                    vertices[v_adj]['beta'] = obj_a.peso + get_beta(w)
                    vertices[v_adj]['pi'] = w
            
            menor = None
            for vertice in v_n_visitados:
                if not get_phi(vertice) and (menor is None or get_beta(vertice) < get_beta(menor)):
                    menor = vertice
            
            if menor is not None:
                w = menor 
                vertices[w]['phi'] = 1
            
        atual = w
        caminho: list[str] = list()
        while atual != U:
            caminho.append(atual)
            atual = get_pi(atual)
            
        caminho.append(U)
        return caminho[::-1]
    
    def bellman_ford(self, U, V):
        if not self.existe_rotulo_vertice(U) or not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        vertices = {}

        def get_pi(v):
            return vertices[v]['pi']
        def get_phi(v):
            return vertices[v]['phi']
        def get_beta(v):
            return vertices[v]['beta']
        
        for vertice in self.vertices:
            vertice_str = str(vertice)
            if vertice_str == U:
                vertices.update({vertice_str: {'beta': 0.0, 'phi': 1, 'pi': None}})
            else:
                vertices.update({vertice_str: {'beta': inf, 'phi': 0, 'pi': None}})
        
        qtd_vertices = len(self.vertices)
        v_alterados: set[str] = set()
        v_alterados.add(U)

        for x in range(qtd_vertices):
            ultimos_vertices: set[str] = set()

            for vertice in v_alterados:
                arestas = sorted(list(self.arestas_sobre_vertice_dir(vertice)))

                for aresta in arestas:
                    obj_a = self.get_aresta(aresta)
                    v_adj = str(obj_a.v2)

                    new_beta = get_beta(vertice) + obj_a.peso
                    if get_beta(v_adj) > new_beta:
                        vertices[v_adj]['beta'] = new_beta
                        vertices[v_adj]['pi'] = vertice
                        ultimos_vertices.add(v_adj)
            
            if not ultimos_vertices:
                atual = V
                caminho = list()

                while atual != U:
                    caminho.append(atual)
                    atual = get_pi(atual)
                
                caminho.append(U)
                return caminho[::-1]
            v_alterados = ultimos_vertices
        
        return False
