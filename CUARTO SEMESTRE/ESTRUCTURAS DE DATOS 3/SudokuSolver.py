import math
from queue import Queue
import time


class SudokuSolver:

    def __init__(self, sudoku):
        # sudoku: la matriz que lo representa
        # crea una copia de la matriz
        self.sudoku = [row[:] for row in sudoku]
        # tamaño de fila y columna del sudoku Sudoku
        self.size = len(sudoku)
        # ancho de cada cuadrante
        self.width = int(math.sqrt(self.size))
        # número de pasos necesarios para resolver el Sudoku
        # self.steps = 0
        # indica si se ha encontrado una solución
        self.finished = False

    def getEmptyCells(self):
        # Devuelve una lista de las celdas vacías en el Sudoku (coordenadas de los 0)
        return [(i, j) for i in range(self.size) for j in range(self.size) if self.sudoku[i][j] == 0]

    def isValid(self, y, x, n):
        # Comprbamos si el valor n es válido para la celda (y,x) en el Sudoku
        # y: fila de la celda
        # x: columna de la celda
        # n: valor que se desea comprobar

        # Comprobamos que la fila no esté repetida
        for i in range(self.size):
            if self.sudoku[y][i] == n:
                return False
        # Comprobamos que la columna no esté repetida
        for i in range(self.size):
            if self.sudoku[i][x] == n:
                return False

        # Calculamos la posición (x,y) del grid
        gridX = (x//self.width)*self.width
        gridY = (y//self.width)*self.width
        # Comprobamos que el cuadrante no este repetido
        for i in range(self.width):
            for j in range(self.width):
                if self.sudoku[gridY+i][gridX+j] == n:
                    return False
        # Si el numeró no se repite en fila, columna y cuadrante es valido
        return True

    def printSudoku(self):
        # Imprime el Sudoku en la consola
        cont2 = 0
        if (self.width == 3):
            print("-------------------------")
        elif (self.width == 2):
            print("-------------")
        for i in self.sudoku:
            cont = 0
            print("|", end=" ")
            for j in i:
                print(j, end=" ")
                cont += 1
                if (cont % self.width == 0):
                    print("|", end=" ")
            cont2 += 1
            print()
            if (cont2 % self.width == 0):
                if (self.width == 3):
                    print("-------------------------")
                elif (self.width == 2):
                    print("-------------")
        print("\n")

    def solveSudokuBFS(self):
        # Se crea una cola para almacenar los posibles sudokus solucion
        queue = Queue()
        # Se agrega el tablero inicial a la cola
        queue.put(self.sudoku)

        while not queue.empty():
            # Se obtiene el primer elemento de la cola
            self.sudoku = queue.get()
            # Se obtienen las casillas vacías del tablero
            zeros = self.getEmptyCells()
            # Si no hay casillas vacías, entonces se ha resuelto el Sudoku
            if not zeros:
                return
            # Se obtienen las coordenadas de la primera casilla vacía
            y, x = zeros[0]
            # Se prueban los números posibles Sudoku
            for n in range(1, self.size+1):
                # Si el número es válido para la casilla vacía
                if self.isValid(y, x, n):
                    # Se crea una copia del sudoku actual
                    newSudoku = [row[:] for row in self.sudoku]
                    # Se actualiza la casilla vacía con el número válido
                    newSudoku[y][x] = n
                    # Se agrega el nuevo tablero a la cola
                    queue.put(newSudoku)

    def solveSudokuDFS(self):
        # Obtenemos todas las celdas vacías (valor 0)
        zeros = self.getEmptyCells()
        # Recorremos cada celda vacía
        for y, x in zeros:
            # Recorrer todos los números posibles
            for n in range(1, self.size+1):
                # Si el número es válido en esa posición del Sudoku
                if (self.isValid(y, x, n)):
                    # Incrementamos el contador de pasos
                    # self.steps+=1
                    # Colocar el número en la posición del Sudoku
                    self.sudoku[y][x] = n
                    # Llamada recursiva a la función 8(DFS)
                    self.solveSudokuDFS()
                    # Si no se ha terminado, volver a vaciar la celda
                    # si se quita se imprimirán mas soluciones diferentes
                    if (not self.finished):
                        self.sudoku[y][x] = 0
            # Salir del bucle for si la celda ya no está vacía
            return
        # Si no hay más celdas vacías, se ha encontrado una solución
        # Se marca como terminado
        self.finished = True


sudoku = [[4, 5, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 2, 0, 7, 0, 6, 3, 0],
          [0, 0, 0, 0, 0, 0, 0, 2, 8],
          [0, 0, 0, 9, 5, 0, 0, 0, 0],
          [0, 8, 6, 0, 0, 0, 2, 0, 0],
          [0, 2, 0, 6, 0, 0, 7, 5, 0],
          [0, 0, 0, 0, 0, 0, 4, 7, 6],
          [0, 7, 0, 0, 4, 5, 0, 0, 0],
          [0, 0, 8, 0, 0, 9, 0, 0, 0]]
sudoku2 = [[1, 0, 0, 0],
           [0, 0, 2, 0],
           [0, 3, 0, 0],
           [0, 0, 0, 0]]
sudoku3 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
           [6, 0, 0, 1, 9, 5, 0, 0, 0],
           [0, 9, 8, 0, 0, 0, 0, 6, 0],
           [8, 0, 0, 0, 6, 0, 0, 0, 3],
           [4, 0, 0, 8, 0, 3, 0, 0, 1],
           [7, 0, 0, 0, 2, 0, 0, 0, 6],
           [0, 6, 0, 0, 0, 0, 2, 8, 0],
           [0, 0, 0, 4, 1, 9, 0, 0, 5],
           [0, 0, 0, 0, 8, 0, 0, 0, 0]]
sudoku4 = [[4, 0, 8, 3, 6, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0, 0],
           [0, 7, 0, 9, 0, 8, 0, 0, 0],
           [3, 0, 0, 0, 5, 0, 0, 4, 7],
           [1, 0, 0, 0, 0, 6, 5, 0, 0],
           [8, 0, 0, 1, 0, 0, 0, 3, 0],
           [0, 0, 0, 4, 0, 0, 3, 0, 1],
           [0, 1, 0, 0, 8, 0, 0, 0, 0],
           [0, 2, 0, 0, 0, 0, 0, 0, 9]]
sudoku5 = [[0, 0, 0, 2, 0, 0, 0, 0, 0],
           [8, 0, 9, 0, 0, 0, 1, 0, 0],
           [0, 2, 0, 0, 0, 0, 0, 0, 0],
           [6, 0, 3, 0, 0, 9, 0, 0, 0],
           [0, 7, 0, 6, 0, 0, 0, 5, 0],
           [0, 0, 0, 0, 4, 0, 9, 0, 3],
           [0, 4, 0, 0, 8, 0, 0, 3, 0],
           [0, 0, 6, 9, 0, 0, 0, 7, 0],
           [0, 9, 5, 0, 0, 1, 0, 0, 2]]

Q = SudokuSolver(sudoku5)
Q2 = SudokuSolver(sudoku5)

print("\nNO RESUELTO")
Q.printSudoku()

print("RESUELTO CON DFS")
strTime = time.time()
Q.solveSudokuDFS()
endTime = time.time()
print("Tiempo de ejecución:", round(endTime - strTime, 3), end="s\n")
Q.printSudoku()

print("RESUELTO CON BFS")
strTime2 = time.time()
Q2.solveSudokuBFS()
endTime2 = time.time()
print("Tiempo de ejecución:",  round(endTime2 - strTime2, 3), end="s\n")
Q2.printSudoku()


'''
Q2 = SudokuSolver(sudoku2)
print("\nNO RESUELTO")
Q2.printSudoku()
print("RESUELTO CON BFS")
Q2.solveSudokuBFS()
Q2.printSudoku()

'''
'''
Q3 = SudokuSolver(sudoku3)
print("\nNO RESUELTO")
Q3.printSudoku()
print("RESUELTO")
Q3.solveSudoku()
print("Numero de soluciones:", Q3.solutions)

'''
