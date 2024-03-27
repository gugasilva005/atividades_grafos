from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        todos_nao_adjacentes: set[str] = set()
        all_vert: set[str] = set()
        
        for v in self.vertices:
            all_vert.add(v.rotulo)
            
        for v in self.vertices:
            adjacentes: set[str] = set()
            adjacentes.add(v.rotulo)
            for a in self.arestas.values():
                if a.v1 == v:
                    adjacentes.add(a.v2.rotulo)
                elif a.v2 == v:
                    adjacentes.add(a.v1.rotulo)
            
            nao_adjacentes = all_vert - adjacentes
            for n_adjacentes in nao_adjacentes:
                par_v = f'{v.rotulo}-{n_adjacentes}'
                if par_v[::-1] not in todos_nao_adjacentes:
                    todos_nao_adjacentes.add(par_v)
        return todos_nao_adjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.arestas:
            if self.arestas[a].v1 == self.arestas[a].v2:
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

        count = 0
        for a in self.arestas.values():
            if a.v1.rotulo == V:
                count += 1
            if a.v2.rotulo == V:
                count += 1
        return count

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        vertices_vistos = [(aresta.v1, aresta.v2) for aresta in self.arestas.values()]
        
        lista_vertices = len(vertices_vistos)
        for i in range(lista_vertices):
            incidencia = vertices_vistos[i]
            for j in range(i + 1, lista_vertices):
                if incidencia == vertices_vistos[j]:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        incidencia_V = list()
        for aresta_rotulo, aresta in self.arestas.items():
            if aresta.v1.rotulo == V or aresta.v2.rotulo == V:
                incidencia_V.append(aresta_rotulo)
        return set(incidencia_V)

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco() or self.ha_paralelas():
            return False
        
        total_v = len(self.vertices)
        if total_v > 1 and len(self.arestas) == 0:
            return False
        for a in self.arestas:
            if (self.grau(self.arestas[a].v1.rotulo) != total_v - 1) or (self.grau(self.arestas[a].v2.rotulo) != total_v - 1):
                return False
        return True
    
    def dfs(self, V=''):
        novo_grafo = MeuGrafo() # Retorno do Novo Grafo
        
        if self.ha_laco():
            return False
        if not self.existe_rotulo_vertice(V): # Verificação da raiz
            raise VerticeInvalidoError
        novo_grafo.adiciona_vertice(V)
        
        def percorre_grafo(raiz):
            arestas_vertices: str = sorted(list(self.arestas_sobre_vertice(raiz))) # Arestas incidentes da atual raiz
            
            for a in arestas_vertices:
                v_1 = str(self.arestas[a].v1)
                v_2 = str(self.arestas[a].v2)
                
                if novo_grafo.existe_rotulo_vertice(v_1) and novo_grafo.existe_rotulo_vertice(v_2):
                    continue
                
                prox = v_1 if v_1 != raiz else v_2
                novo_grafo.adiciona_vertice(prox)
                novo_grafo.adiciona_aresta(self.arestas[a])
                percorre_grafo(prox)
        
        percorre_grafo(V)
        
        if len(self.vertices) != len(novo_grafo.vertices):
            return False
        
        print(novo_grafo)
        return novo_grafo
    
    def bfs(self, V=''):
        novo_grafo = MeuGrafo()
    
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        if self.ha_laco():
            raise ValueError
        
        novo_grafo.adiciona_vertice(V)
        prox_v: str = list()
        
        prox_v.append(V)
        while prox_v:
            vert_atual = prox_v.pop(0)
            arestas_vertices: str = sorted(list(self.arestas_sobre_vertice(vert_atual)))
            
            for a in arestas_vertices:
                v_1 = str(self.arestas[a].v1)
                v_2 = str(self.arestas[a].v2)
                
                if novo_grafo.existe_rotulo_vertice(v_1) and novo_grafo.existe_rotulo_vertice(v_2):
                    continue
                
                prox = v_1 if v_1 != vert_atual else v_2
                novo_grafo.adiciona_vertice(prox)
                novo_grafo.adiciona_aresta(self.arestas[a])
                prox_v.append(prox)
        
        if len(self.vertices) != len(novo_grafo.vertices):
            raise ValueError
        
        return novo_grafo
    
    def ha_ciclo(self):
        if (len(self.vertices) <= 2) and not (self.ha_laco()) \
            and not (self.ha_paralelas()) or (not len(self.arestas)):
            return False
        
        vertices_grafo = sorted([str(a) for a in self.vertices])

        v_raiz = vertices_grafo[0]
        ciclo = list()
        ciclo_encontrado = [False]
        arestas_visitadas = set()

        def percorre_grafo(raiz, verificacao):
            arestas: str = sorted(list(self.arestas_sobre_vertice(raiz)))

            ciclo.append(raiz)
            for a in arestas:
                v_1 = str(self.arestas[a].v1)
                v_2 = str(self.arestas[a].v2)

                if verificacao[0]:
                    return
                if a in arestas_visitadas:
                    continue
                if v_1 in ciclo and v_2 in ciclo:
                    ciclo.append(a)
                    ciclo.append(v_2 if v_1 == raiz else v_1)
                    verificacao = True
                    return
                
                arestas_visitadas.add(a)
                prox = v_1 if v_1 != raiz else v_2
                ciclo.append(a)
                percorre_grafo(prox, verificacao)
            if not verificacao[0]:
                if raiz != v_raiz:
                    ciclo.pop()
                ciclo.pop()
        percorre_grafo(v_raiz, ciclo_encontrado)

        if not ciclo:
            return False
        
        comeco_ciclo = ciclo.index(ciclo[-1])
        ciclo = ciclo[comeco_ciclo:]

        return ciclo
    
    def caminho(self, n):
        if n < 1:
            return False
        
        vertices = sorted([str(v) for v in self.vertices])
        vertices_visitados = list()
        arestas_visitadas = list()
        caminho = list()
        count = 0

        def percorre_grafo(raiz, tam):
            nonlocal count
            arestas: str = sorted(list(self.arestas_sobre_vertice(raiz)))

            caminho.append(raiz)
            for a in arestas:
                v_1 = str(self.arestas[a].v1)
                v_2 = str(self.arestas[a].v2)

                if v_1 in caminho and v_2 in caminho:
                    continue
                if count == tam:
                    break
                if a in arestas_visitadas:
                    continue

                arestas_visitadas.append(a)
                vertices_visitados.append(v_1)
                vertices_visitados.append(v_2)
                count += 1
                prox = v_1 if v_1 != raiz else v_2
                caminho.append(a)
                percorre_grafo(prox, n)
            if count != n:
                if len(caminho) > 1:
                    caminho.pop()
                caminho.pop()
                if len(arestas_visitadas) > 0:
                    arestas_visitadas.pop()
                if count > 0:
                    count -= 1
        
        for i in vertices:
            if caminho:
                break
            percorre_grafo(i, n)
            vertices_visitados.clear()
    
        return caminho if caminho else False
    
    def conexo(self):
        raiz = str(self.vertices[0])
        dfs = self.dfs(raiz)
        return False if not dfs else True
        
        

        
if __name__ == '__main__':
    g_p = MeuGrafo()
    g_p.adiciona_vertice("J")
    g_p.adiciona_vertice("C")
    g_p.adiciona_vertice("E")
    g_p.adiciona_vertice("P")
    g_p.adiciona_vertice("M")
    g_p.adiciona_vertice("T")
    g_p.adiciona_vertice("Z")
    g_p.adiciona_aresta('a1', 'J', 'C')
    g_p.adiciona_aresta('a2', 'C', 'E')
    g_p.adiciona_aresta('a3', 'C', 'E')
    g_p.adiciona_aresta('a4', 'P', 'C')
    g_p.adiciona_aresta('a5', 'P', 'C')
    g_p.adiciona_aresta('a6', 'T', 'C')
    g_p.adiciona_aresta('a7', 'M', 'C')
    g_p.adiciona_aresta('a8', 'M', 'T')
    g_p.adiciona_aresta('a9', 'T', 'Z')
    print(g_p.ha_ciclo())