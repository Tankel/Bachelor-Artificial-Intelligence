from queue import PriorityQueue
import math
import random
from itertools import permutations

class heuristic:
    @staticmethod
    def heuristicChebyshovDist(nodeA, nodeB):
        # distancai Chebyshov
        return max(abs(nodeA.row-nodeB.row), abs(nodeA.col-nodeB.col))

    def heuristicManhattanDist(nodeA, nodeB):
        # distancia Manhattan
        return abs(nodeA.row-nodeB.row) + abs(nodeA.col-nodeB.col)
    
    def heuristicEuclideanDist(nodeA, nodeB):
        # distancia Euclidiana
        return math.sqrt( abs(nodeA.row-nodeB.row)**2 + abs(nodeA.col-nodeB.col)**2)


class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.totalDist = -1
        self.path = []
        self.size = 0

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        
        return self.row == other.row and self.col == other.col
        #return (self.heuritcValue == other.heuritcValue)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return (self.totalDist < other.totalDist)

    def __gt__(self, other):
        return (self.totalDist > other.totalDist)

    '''
    def __le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return (self > other) or (self == other)
    '''
class World:
    def __init__(self):
        #creamos mundo aleatorio
        #self.world = self.createRandomWorld(10, 10, 50, 50, 5, 40)
        with open('matrix.txt', 'r') as f:
            self.world = [[str(num) for num in line.split(',')] for line in f]
        self.rows = len(self.world)
        self.cols = len(self.world[0])
        # 8 movimientos del caballo: L
        self.movement8 = [[-1, 0], [0, 1], [1, 0], [0, -1], [1,1], [-1,-1], [1,-1], [-1,1]]

    def searchLetter(self, letter):
        currNode = [0,0]
        while currNode[1]<self.cols-1:
            while currNode[0]<self.rows-1:
                if self.world[currNode[0]][currNode[1]] == letter:
                    return currNode
                currNode[0]+=1
            currNode[0] = 0
            currNode[1] +=1
            


    def bestFirstSearch(self, startPoint, targetPoint, heuristic):

        iniCoor = self.searchLetter(startPoint)
        endCoor = self.searchLetter(targetPoint)

        iniRow = iniCoor[0]
        iniCol = iniCoor[1]
        endRow = endCoor[0]
        endCol = endCoor[1]

        #print(startPoint, iniRow, iniCol)
        #print(targetPoint, endRow, endCol)
        
        # Incializamos la matriz de visitados
        self.visitedMatrix = [[False] * self.cols for _ in range(self.rows)]

        # incializamos la cola para el bfs
        pq = PriorityQueue()

        # creamos el nodo origen y final
        source = Node(iniRow, iniCol)
        target = Node(endRow, endCol)

        #metemos el vertice origen
        pq.put(source)

        # lo marcamos para siempre
        # self.visitedMatrix[iniRow][iniCol] = True

        # mientras haya nodos no explorados
        while not pq.empty():
            # obtenemos el nodo siguiente
            currNode = pq.get()
            if(self.visitedMatrix[currNode.row][currNode.col]):
                continue
            else:
                self.visitedMatrix[currNode.row][currNode.col] = True
            #agregamos a la ruta el de mayor prioridad
            # currNode.path.append(currNode)
            #pq.queue.clear()
            # comparar si currNode es el nodo target
            if currNode == target:
                # si es, lo agregamos al path de currNode
                # currNode.path.append(currNode) #no es necesario ya que al ser el mismo nodo ya se incluyo con la maxima prioridad
                # imprimimos el path
                
                '''
                print("_____________________")
                print("  PATH:    HEURISTIC:")
                print("  x ", " y ")
                for i in currNode.path:
                    print("[",i.col,",",i.row,"]    h:",i.heuritcValue)
                # terminamo
                print("Numero de movimientos:", len(currNode.path) -1)
                '''

                return currNode.size
            
            for i in self.movement8:
                #print(currNode.row, currNode.col)
                # i[0] -> mov de fila
                # i[1] -> mov de columna
                # calcular nueva casilla currNode.row + mov
                casilla = [currNode.row + i[0], currNode.col +i[1]]
                # comprobar que la nueva casilla este dentro del mundo
                # Despues, compruebo que este libre
                # despues, compruebo que no esta visitada
                if(casilla[0] >= 0 and casilla[1] >= 0 and casilla[0] < self.rows and casilla[1] < self.cols
                    and self.world[casilla[0]][casilla[1]] != 'x' and not self.visitedMatrix[casilla[0]][casilla[1]]):
                    #print("currNodeeee:",casilla[0], casilla[1])
                    #print("target nodeeee:",target.row,target.col)
                    # Marcar como visitado
                    #self.visitedMatrix[casilla[0]][casilla[1]] = True
                    # Crear un nuevo nodo
                    newNode = Node(casilla[0], casilla[1])
                    # Calcular ladistancia total con la heuristica mas el tamaño del path
                    newNode.totalDist = heuristic(newNode, target) + (currNode.size+1)
                    #print(newNode.totalDist)
                    #print(newNode.row, newNode.col)
                    #print(target.row, target.col)
                    #print("h:",newNode.heuritcValue,"- ",newNode.row,newNode.col)
                    # copio el path de currNode
                    newNode.path = currNode.path.copy()
                    newNode.size = currNode.size + 1
                    # newNode.path = currNode.path
                    # Agreagamos a la ruta
                    newNode.path.append(newNode)
                    # Agregamos el nuevo nodo a la pq
                    pq.put(newNode)

        #imprimir que no hay solución
        # print("No hay solución")
        #terminamos
        
        return -1 

world = World()

letters = ["A", "B", "C", "D", "E"]
distancias = [[0] * 5 for _ in range(5)]

n = len(letters)
print("\nMatriz de distancias:")
print("\tA\tB\tC\tD\tE")
for i in range(n):
    print(letters[i],end="\t")
    for j in range(n):
        distancias[i][j] = world.bestFirstSearch(letters[i],letters[j],heuristic.heuristicEuclideanDist)
        print(distancias[i][j],end="\t")
    print()
print()

dist = 0
for i in range(len(letters)-1):
    dist += distancias[i][i+1]
dist += distancias[4][0]
print("Distancia A-B-C-D-E-A:", dist, "\n")

distMin = [0] * 120

cont = 0
l = list(permutations(letters))
for i in l:
    for j in range(n-1):
        distMin[cont] += distancias[letters.index(i[j])][letters.index(i[j+1])]
    distMin[cont] += distancias[letters.index(i[4])][letters.index(i[0])]
    cont+=1
print("Distancia minima:", min(distMin), l[distMin.index(min(distMin))], "\n")
