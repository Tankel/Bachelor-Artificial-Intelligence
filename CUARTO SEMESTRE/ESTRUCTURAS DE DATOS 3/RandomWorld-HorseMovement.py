from queue import PriorityQueue
import math
import random


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
        self.heuritcValue = -1
        self.path = []

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        
        return self.row == other.row and self.col == other.col
        #return (self.heuritcValue == other.heuritcValue)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return (self.heuritcValue < other.heuritcValue)

    def __gt__(self, other):
        return (self.heuritcValue > other.heuritcValue)

    '''
    def __le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return (self > other) or (self == other)
    '''
class World:
    def __init__(self):
        #creamos mundo aleatorio
        self.world = self.createRandomWorld(10, 10, 50, 50, 5, 40)
        self.rows = len(self.world)
        self.cols = len(self.world[0])
        # 8 movimientos del caballo: L
        self.HorseMovement = [[-1, -2], [-1, 2], [1, -2], [1, 2],
                              [-2, 1], [-2, -1], [2, 1], [2, -1]]

    def createRandomWorld(self, minRows, minCols, maxRows, maxCols, minPercentageObstacles, maxPercentageObstacles):
        cols = random.randint(minRows, maxRows)
        rows = random.randint(minCols, maxCols)

        world = [['.'] * cols for _ in range(rows)]

        percentageObstacles = random.randint(minPercentageObstacles, maxPercentageObstacles)
        amountObstacles = cols * rows * percentageObstacles // 100


        while amountObstacles > 0:
            row = random.randint(0, rows - 1)
            col = random.randint(0, cols -1)

            if (row, col) == (rows-1, 0) or (row, col) == (0, cols-1):
                continue

            if world[row][col] != 'x':
                world[row][col] = 'x'
                amountObstacles -= 1

        return world
    def bestFirstSearch(self, iniRow, iniCol, endRow, endCol, heuristic):
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
        self.visitedMatrix[iniRow][iniCol] = True

        # mientras haya nodos no explorados
        while not pq.empty():
            # obtenemos el nodo siguiente
            currNode = pq.get()
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

                return len(currNode.path)
            
            for i in self.HorseMovement:
                # i[0] -> mov de fila
                # i[1] -> mov de columna
                # calcular nueva casilla currNode.row + mov
                casilla = [currNode.row + i[0], currNode.col +i[1]]
                # comprobar que la nueva casilla este dentro del mundo
                # Despues, compruebo que este libre
                # despues, compruebo que no esta visitada
                if(casilla[0] >= 0 and casilla[1] >= 0 and casilla[0] < self.rows and casilla[1] < self.cols
                    and self.world[casilla[0]][casilla[1]] == '.' and not self.visitedMatrix[casilla[0]][casilla[1]]):
                    #print("currNodeeee:",casilla[0], casilla[1])
                    #print("target nodeeee:",target.row,target.col)
                    # Marcar como visitado
                    self.visitedMatrix[casilla[0]][casilla[1]] = True
                    # Crear un nuevo nodo
                    newNode = Node(casilla[0], casilla[1])
                    # Calcular la heuristica para el nuevo nodo
                    newNode.heuritcValue = heuristic(newNode, target)
                    #print(newNode.heuritcValue)
                    #print("h:",newNode.heuritcValue,"- ",newNode.row,newNode.col)
                    # copio el path de currNode
                    newNode.path = currNode.path.copy()
                    # newNode.path = currNode.path
                    # Agreagamos a la ruta
                    newNode.path.append(newNode)
                    # Agregamos el nuevo nodo a la pq
                    pq.put(newNode)

        #imprimir que no hay solución
        # print("No hay solución")
        #terminamos
        
        return -1


worldMap = [['.', 'x', '.', 'x', '.', '.'],
            ['.', '.', '.', 'x', '.', 'x'],
            ['.', 'x', '.', '.', '.', '.'],
            ['.', '.', '.', 'x', 'x', '.'],
            ['x', 'x', '.', '.', 'x', '.'],
            ['.', '.', '.', 'x', '.', '.']]

# promedio de las distancias
AverageManhattanDis = 0
AverageChebyshovDist = 0
AverageEuclideanDist = 0

# numero de casos no fallidos
ManhattanTest = 0
ChebyshovTest = 0
EuclideanTest = 0

for i in range(1,100):
    # creamos nuevo mundo
    world = World()

    # r es la distancia de la esquina iferiori a izquierda hacia la superior derecha
    r = world.bestFirstSearch(world.rows-1, 0, 0, world.cols-1,heuristic.heuristicManhattanDist)  
    # si es -1 no se encontró solución
    if (r!=-1):
        AverageManhattanDis += r
        ManhattanTest += 1

    r = world.bestFirstSearch(world.rows-1, 0, 0, world.cols-1,heuristic.heuristicChebyshovDist)  
    if (r!=-1):
        AverageChebyshovDist += r
        ChebyshovTest += 1

    r = world.bestFirstSearch(world.rows-1, 0, 0, world.cols-1,heuristic.heuristicEuclideanDist)  
    if (r!=-1):
        AverageEuclideanDist += r
        EuclideanTest += 1

AverageManhattanDis /= ManhattanTest
AverageChebyshovDist /= ChebyshovTest
AverageEuclideanDist /= EuclideanTest

print("Promedio de la distancia Manhattan:",round(AverageManhattanDis,2))
print("Promedio de la distancia Chebyshov:",round(AverageChebyshovDist,2))
print("Promedio de la distancia Euclidean:",round(AverageEuclideanDist,2))


