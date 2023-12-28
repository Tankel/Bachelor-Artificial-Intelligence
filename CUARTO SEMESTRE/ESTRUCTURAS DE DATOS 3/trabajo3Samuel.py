from queue import PriorityQueue
from math import sqrt
import random
import itertools

class Heuristics:
    @staticmethod
    def heuristicOne(nodeA, nodeB):
        #Manhattan
        return abs(nodeA.row - nodeB.row) + abs(nodeA.col - nodeB.col)

    def heuristicTwo(nodeA, nodeB):
        #Euclidiana
        x = nodeA.row - nodeB.row
        y = nodeA.col - nodeB.col
        return sqrt(x*x + y*y)
    
    def heuristicThree(nodeA, nodeB):
        #Chebyshov
        return max(abs(nodeA.row - nodeB.row), abs(nodeA.col - nodeB.col))

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.heuristicValue = -1
        self.path = []
        self.distance = 0

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return (self.row == other.row and self.col == other.col)

    def __lt__(self, other):
        if not isinstance(other, Node):
            return False
        return self.heuristicValue + self.distance < other.heuristicValue + other.distance
    
    def __gt__(self, other):
        if not isinstance(other, Node):
            return False
        return self.heuristicValue + self.distance > other.heuristicValue + other.distance

class World:
    def __init__(self, world):
        self.world = world
        self.rows = len(self.world)
        self.cols = len(self.world[0])

        #Movement
        self.movement8 = [[-1, 0], [0, 1], [1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    
    def aStar(self, iniCol, iniRow, endCol, endRow, heuristicFunction):
        self.visitedMatrix = [[False] * self.cols for _ in range(self.rows)]
        
        pQueue = PriorityQueue()

        #Creamos el nodo origen y final
        source = Node(iniRow, iniCol)
        target = Node(endRow, endCol)

        #Metemos el vertice origen
        pQueue.put(source)

        while not pQueue.empty():
            currentNode = pQueue.get()
            if self.visitedMatrix[currentNode.row][currentNode.col] == True:
                continue

            self.visitedMatrix[currentNode.row][currentNode.col] = True

            #Comparar si currNode es el nodo target
            if currentNode == target:
                #currentNode.path.append(currentNode)
                #Retornamos el tamanio del path
                return len(currentNode.path)

            #Para cada movimiento
            for i in self.movement8:
                #Calcular la nueva casilla, 0 fila, 1 columna
                newNode = Node(currentNode.row + i[0], currentNode.col + i[1])

                #Comprobar que la nueva casilla este dentro del mundo
                #Comprobar que este libre
                #Comprobar que no este visitada
                if (newNode.col>=0) and (newNode.col<self.cols) and (newNode.row>=0) and (newNode.row<self.rows) and (self.visitedMatrix[newNode.row][newNode.col] is False) and (self.world[newNode.row][newNode.col]!='x'):
                    #Calcular la heuristica
                    newNode.heuristicValue = heuristicFunction(newNode, target)
                    #Copio el path del predecesor
                    newNode.path = currentNode.path.copy()
                    newNode.path.append(newNode)
                    newNode.distance = currentNode.distance + 1
                    #Agregar a la pQueue
                    pQueue.put(newNode)

        #Imprimir que no hay solucion
        return -1

#Arreglos de sumas y total de paths
#0 = Manhattan
#1 = Euclidiana
#2 = Chebyshov 

with open('matrix.txt', 'r') as f:
    worldMap = [[str(num) for num in line.split(',')] for line in f]

world = World(worldMap)
points = [[0, 0]] * 5
distances = [[0] * 5 for _ in range(5)]

for i in range(0, world.rows):
    for j in range(0, world.cols):
        if worldMap[i][j] == 'A':
            points[0] = [i, j]
        elif worldMap[i][j] == 'B':
            points[1] = [i, j]
        elif worldMap[i][j] == 'C':
            points[2] = [i, j]
        elif worldMap[i][j] == 'D':
            points[3] = [i, j]
        elif worldMap[i][j] == 'E':
            points[4] = [i, j]

print(points)

for i in range(5):
    for j in range(i+1, 5):
        distances[i][j] = world.aStar(points[i][1], points[i][0], points[j][1], points[j][0], Heuristics.heuristicTwo)
        distances[j][i] = distances[i][j]

print("\nMatriz de distancias")
for i in distances:
    print(i)

distance = 0
for i in range(5):
    if i+1 == 5:
        distance += distances[i][0]
        break
    distance += distances[i][i+1]
print("\nDistancia A-B-C-D-E-A =", distance)

nodes = [0, 1, 2, 3, 4]
permutations = list(itertools.permutations(nodes))
min = 100000000000000000
route = permutations[0]
distance = 0
for i in permutations:
    for j in range(0,5):
        if j+1 != 5:
            distance += distances[i[j]][i[j+1]]
    distance += distances[i[4]][i[0]]

    if distance < min:
        min = distance
        route = i

    distance = 0

print("\nRuta con distancia minima =", route)