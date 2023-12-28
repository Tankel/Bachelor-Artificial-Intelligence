from queue import PriorityQueue
from UnionFind import DSU
from collections import defaultdict


class Graph:
    def __init__(self, nVertex):
        self.nVertex = nVertex
        self.adjList = defaultdict(list)
        self.totalWeight = 0

    def addEdge(self, a, b, peso):
        self.adjList[a].append((b, peso))
        self.adjList[b].append((a, peso))
        self.totalWeight += peso

    def getWeight(self):
        return self.totalWeight

    def prim(self):
        pq = PriorityQueue()
        mst = Graph(self.nVertex)

        visited = self.nVertex * [False]
        
        pq.put((0,-1,0))

        while not pq.empty():
            currEdge = pq.get()

            peso, nodoA, nodoB = currEdge

            if(visited[nodoB]):
                continue

            visited[nodoB] = True

            if nodoA != -1:
                mst.addEdge(nodoA, nodoB, peso)

            #Agregamos los nodos adyacentes que no estan visitados
            for conn in self.adjList[nodoB]:
                nodoC, peso = conn
                if(not visited[nodoC]):
                    pq.put((peso, nodoB, nodoC))

        return mst
    
g = Graph(6)
g.addEdge(0, 1, 1)
g.addEdge(0, 2, 2)
g.addEdge(1, 3, 4)
g.addEdge(1, 2, 3)
g.addEdge(2, 4, 6)
g.addEdge(2, 3, 5)
g.addEdge(3, 5, 7)
g.addEdge(4, 5, 8)

mst = g.prim()
print("Peso total:", g.getWeight())
print("Peso con prim:", mst.getWeight()) #20
print("Lista de adyacencia: ")
for i in range(0, mst.nVertex):
    print(i, "->" , mst.adjList[i])
