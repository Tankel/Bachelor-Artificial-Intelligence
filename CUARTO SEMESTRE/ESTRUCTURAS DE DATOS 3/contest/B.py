from queue import Queue
from collections import defaultdict

class GraphList:
    def __init__(self, nVertex):
        self.nVertex = nVertex
        self.adjList = defaultdict(list)
        self.visited = [False] * nVertex

    def addList(self, a, b):
        self.adjList[a].append(b)
        self.adjList[b].append(a)

    def printAdjList(self):
        print(self.adjList)
    
    def __dfs(self, startVertex):
        # comprobar que no este visitado
        if (self.visited[startVertex]):
            return
        # imprimir el valor del nodo
        print(startVertex, end=" ")
        self.visited[startVertex] = True

        # para cada nodo conexo
        for i in self.adjList[startVertex]:
        # si no estas visitado, movemos a ese nodo
                self.__dfs(i)

    def dfs(self, startVertex):
        self.restoreVisited()
        self.__dfs(startVertex)

    def bfs(self, startVertex):
        self.restoreVisited()
        # incializamos la cola para el bfs
        # queue = Queue()
        list<int> a 
        
        # metemos a la cola el nodo orgien
        a.insert(startVertex)

        # lo marcamos para siempre
        self.visited[startVertex] = True

        # mientras haya nodos no explorados 
        while not a.empty():
            # obtenemos el nodo siguiente
            currNode = a.get()
            # imprimimos el nodo actial 
            print(currNode, end="\t")
            # para cada nodo conexo:
            for i in self.adjList[currNode]:
                # si no esta visitado, lo marcamos como visitado
                # y lo agregamos a la cola
                if(not self.visited[i]):
                    self.visited[i] = True
                    a.insert(i)
                    a.sort()

    def restoreVisited(self):
        self.visited = [False] * self.nVertex

n, m = input().split()
n = int(n)
m = int (m)
gl = GraphList(n+1)
for i in range(0, m):
    a, b = input().split()
    a = int(a)
    b = int (b)
    gl.addList(a, b)
gl.dfs(1)



