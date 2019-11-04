from collections import defaultdict
import random
import heapq
#lista de prioridade
class MinHeap:
    #construtor
    def __init__(self):
        self._queue = []
        self._index = 0
    #inserindo na lista
    def insert(self, item, prioridade):
        heapq.heappush(self._queue, (-prioridade, self._index, item))
        self._index +=1
    #removendo da lista
    def remove(self):
        return heapq.heappop(self._queue)[-1]
    #pegando o tamanho da lista
    def get_length(self):
        return len(self._queue)


class Graph:
    #construtor para o grafo
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = {}

     #colocando aresta
    def addaresta(self,origem,destino,custo):
        self.graph[origem].append((destino,custo))
        self.vertices[origem] = origem
        self.vertices[destino] = destino

     #calculando menor caminho
    def dijkstra(self,origem,destino):
        # quantidade de vertices
        numero_vertices = len(self.vertices)
        #colocando todos NONE para ir trocando durante o percorrer
        p = [ 0 for i in range(numero_vertices)]


        #oridem sempre vai ser  0
        p[origem] = 0

        #criando a lista de prioridade
        min_heap = MinHeap()
        #adicionando a origem na lista
        min_heap.insert(origem,0)
        testando = min_heap.remove()
        for i in self.graph[testando]:
          teste =  random.choice(self.graph)

        print(teste)

        #enquanto o tamanho da lista for maior que 0
        while min_heap.get_length()>0:
            #remove o que já foi visitado
            u = min_heap.remove()
            #percorre o grafo
            for arestas in self.graph[u]:
                #custo da aresta e o vertice
                v,custo = arestas
                #relaxamento
            if(teste == arestas):
                    arestas = "",10000000
            else:
                if p[v] == 0 or p[v] > p[u] + custo:
                    #Calculando o valor para ser atualizado
                    p[v] = p[u] + custo
                    #atualizando o valor final
                    min_heap.insert(v,p[v])
         #retorna o caminho minimo
        return p[destino]



#Criando o grafo
G = Graph()

#adicionando as arestas ao grafo origem,destino,custo
G.addaresta(0,1,1)
G.addaresta(0,3,3)
G.addaresta(0,4,10)
G.addaresta(1,2,5)
G.addaresta(2,4,1)
G.addaresta(3,2,2)
G.addaresta(3,4,6)




comeco = int(input("Digite o Ponto de saida: "))
inicio = int(input("Digite o Ponto de chegada: "))

print(" Menor Caminho :",G.dijkstra(comeco,inicio))