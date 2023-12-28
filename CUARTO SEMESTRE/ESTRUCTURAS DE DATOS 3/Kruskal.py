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

    def kruskal(self):
        pq = PriorityQueue()

        mst = Graph(self.nVertex)

        dsu = DSU(self.nVertex)

        for i in range(0, self.nVertex):
            for conn in self.adjList[i]:
                nodoA = i
                nodoB, peso = conn
                # obtener el peso
                # obtener el arista al que se conecta
                pq.put((peso, nodoA, nodoB))

        while not pq.empty():
            currEdge = pq.get()

            # obtener nodoA, nodoB y peso
            peso, nodoA, nodoB = currEdge

            if dsu.pathCompression(nodoA) != dsu.pathCompression(nodoB):
                mst.addEdge(nodoA, nodoB, peso)
                dsu.unionByRank(nodoA, nodoB)

        return mst
    
g = Graph(7)
g.addEdge(0, 4, 1)
g.addEdge(5, 3, 3)
g.addEdge(5, 4, 2)
g.addEdge(4, 6, 6)
g.addEdge(1, 6, 8)
g.addEdge(4, 3, 4)
g.addEdge(4, 2, 5)
g.addEdge(1, 2, 7)

mst = g.kruskal()
print("Peso total:", g.getWeight())
print("Peso con kruskal:", mst.getWeight())
print("Lista de adyacencia: ")
for i in range(0, mst.nVertex):
    print(i, "->" , mst.adjList[i])

