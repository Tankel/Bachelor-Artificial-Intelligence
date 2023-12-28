from queue import Queue
from collections import defaultdict


class GraphMat:
    def __init__(self, nVertex):
        self.nVertex = nVertex
        self.adjMatrix = [[0]*self.nVertex for _ in range(self.nVertex)]
        self.visited = [False] * nVertex

    def addEdge(self, a, b):
        self.adjMatrix[a][b] = 1
        self.adjMatrix[b][a] = 1

    def printAdjMatrix(self):
        #print(self.adjMatrix)
        for i in range(0, self.nVertex):
            print(self.adjMatrix[i])
        print()

    def __dfs(self, startVertex):
        # comprobar que no este visitado
        if (self.visited[startVertex]):
            return
        # imprimir el valor del nodo
        print(startVertex, end="\t")
        self.visited[startVertex] = True

        # para cada nodo conexo
        for i in range(0, self.nVertex):
        # si no estas visitado, movemos a ese nodo
            if (self.adjMatrix[startVertex][i]==1):
                self.__dfs(i)

    def dfs(self, startVertex):
        self.restoreVisited()
        self.__dfs(startVertex)

    def bfs(self, startVertex):
        self.restoreVisited()
        self.visited = [False] * self.nVertex

        # incializamos la cola para el bfs
        queue = Queue()
        
        # metemos a la cola el nodo orgien
        queue.put(startVertex)

        # lo marcamos para siempre
        self.visited[startVertex] = True

        # mientras haya nodos no explorados 
        while not queue.empty():
            # obtenemos el nodo siguiente
            currNode = queue.get()
            # imprimimos el nodo actial 
            print(currNode, end="\t")
            # para cada nodo conexo:
            for i in range(0, self.nVertex):
                # si no esta visitado, lo marcamos como visitado
                # y lo agregamos a la cola
                if(self.adjMatrix[currNode][i]==1 and not self.visited[i]):
                    self.visited[i] = True
                    queue.put(i)
    def restoreVisited(self):
        self.visited = [False] * self.nVertex


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
        print(startVertex, end="\t")
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
        queue = Queue()
        
        # metemos a la cola el nodo orgien
        queue.put(startVertex)

        # lo marcamos para siempre
        self.visited[startVertex] = True

        # mientras haya nodos no explorados 
        while not queue.empty():
            # obtenemos el nodo siguiente
            currNode = queue.get()
            # imprimimos el nodo actial 
            print(currNode, end="\t")
            # para cada nodo conexo:
            for i in self.adjList[currNode]:
                # si no esta visitado, lo marcamos como visitado
                # y lo agregamos a la cola
                if(not self.visited[i]):
                    self.visited[i] = True
                    queue.put(i)

    def restoreVisited(self):
        self.visited = [False] * self.nVertex


gm = GraphMat(6)
gm.addEdge(0, 2)
gm.addEdge(1, 3)
gm.addEdge(2, 3)
gm.addEdge(4, 3)
gm.addEdge(2, 5)
#gm.printAdjMatrix()
print("Adjacency Matrix\n\tDFS:\t", end="")
gm.dfs(0)
print("\n\tBFS:\t",end="")
gm.bfs(0)

print()
gl = GraphList(6)
gl.addList(0, 2)
gl.addList(1, 3)
gl.addList(2, 3)
gl.addList(4, 3)
gl.addList(2, 5)
#gl.printAdjList()
print("\nAdjacency list\n\tDFS:\t", end="")
gl.dfs(0)
print("\n\tBFS:\t",end="")
gl.bfs(0)
