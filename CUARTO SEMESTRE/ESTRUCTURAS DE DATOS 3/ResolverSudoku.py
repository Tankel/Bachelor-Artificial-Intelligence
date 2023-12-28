# Resolver Sudoku: 1 informado, 1 no informado -> 2 no informado
import math

class SudokuSolver:
    def __init__(self):
        #self.solution = sudoku
        self.size = len(sudoku)
        self.rows = [[False]* self.size  for _ in range(self.size)]
        self.cols = [[False]* self.size  for _ in range(self.size)]
        self.grids = [[False]* self.size  for _ in range(self.size)]
        self.baseNumber = [[False]* self.size  for _ in range(self.size)]
        self.width = int(math.sqrt(self.size))
        self.values = range(1,10)

        '''
        self.size = size
        self.cont = 0
        # arreglos auxiliares
        self.row = [False] * size
        self.rightDiag = [False] * (size * 2)
        self.leftDiago = [False] * (size * 2)

        # arreglo para guardar las soluciones
        self.solution = [0] * size
        '''
    # recursivo par ecnontrar las soluciones
    def solveSudoku(self):
        global sudoku
        #print("AAAAAAAAAAA")
        for y in range(9):
            for x in range(9):
                #print("SOL",sudoku[y][x])
                if sudoku[y][x] == 0:
                    for n in range(1,10):
                        #print("i")
                        if (self.__isSquaredAttacked(y,x,n)):
                            #print(":((((((((()))))))))")
                            sudoku[y][x] = n
                            #self.printSolution()
                            self.solveSudoku()
                            sudoku[y][x] = 0
                    return
        self.printSolution()

    def __findSolutions(self, currentCol):
        if currentCol == self.size-1:
            self.printSolution()
            #self.cont += 1
            return

        # Rcorrer todas las filas de la columna actual
        for i in range(0, self.size):
            #print(i)
            for j in self.values:
                #print("\t",j)
                # comprobar si la casilla [i, currentCol] esta libre
                #print("----", self.__isSquaredAttacked(i, currentCol, j))
                #print(i, currentCol, self.solution[i][currentCol], self.baseNumber[i][currentCol])
                if (not self.__isSquaredAttacked(i, currentCol, j) and not self.baseNumber[i][currentCol]):
                    # Si esta libre, añadimos esta reina la solución
                    #print("a")
                    #print("row:", i, "col", currentCol, "Number:", j)
                    self.solution[i][currentCol] = j
                    #self.printSolution()
                    # Marcaos casilla como atacada
                    self.__setSquareAttacked(i, currentCol, True, j)
                    # Lamamos a la recursion con la siguiente columna
                    self.__findSolutions(currentCol+1)
                    #  Al terminar la recursion, marcamos la casilla como libre
                    self.__setSquareAttacked(i, currentCol, False, j)

    def __checkSudoku(self, currentCol):
        if currentCol == self.size-1:
            return
        for i in range(0, self.size):
            #print(self.baseNumber[i][currentCol])
            if (self.solution[i][currentCol] != 0):
                self.baseNumber[i][currentCol] = True
                #print(i, currentCol, self.solution[i][currentCol], self.baseNumber[i][currentCol])
                self.__setSquareAttacked(i, currentCol, True, self.solution[i][currentCol]-1)
                self.__checkSudoku(currentCol+1)
            else:
                self.baseNumber[i][currentCol] = False

    def checkSudoku(self):
        self.__checkSudoku(0)

    # Marcar casilla como atacada o libre
    def __setSquareAttacked(self, row, col, status, number):  # status atacada o libre
        grid = int(((row // self.width) * self.width) + (col // self.width))
        # Marcar fila como atacada
        self.rows[row][number] = status
        # Marcar columna  como atacada
        self.cols[col][number] = status
        # Marcar grid como atacada
        self.grids[grid][number] = status

    # Preguntar si casilla esta libre o atacada
    def __isSquaredAttacked(self, row, col, number):
        global sudoku
        #print("r", row, "c", col)
        for i in range(0,9):
            if sudoku[row][i] == number:
                #print("1NO SE PUEDE", number)
                return False
        for i in range(0,9):
            if sudoku[i][col] == number:
                #print("2NO SE PUEDE", number)
                return False
        gridX = (col//3)*3 # 5
        gridY = (row//3)*3 # 0
        for i in range(0,3):
            for j in range(0,3):
                if sudoku[gridY+i][gridX+j] == number:
                    #print("3NO SE PUEDE", number)
                    return False
        return True
        '''
        #print("Aaaaaaaaaa")
        grid = int(((row // self.width) * self.width) + (col // self.width))
        #print("Row:", row,"Col:",col,"grid:", grid, "N", number)
        #print(self.rows[row][number], self.cols[col][number], self.grids[grid][number], "grid:", grid)
        return bool(self.rows[row][number] or self.cols[col][number] or self.grids[grid][number])
        '''

    def findSolutions(self):
        self.__findSolutions(0)
    
    def printSolution(self):
        cont2=0
        print("-------------------------")
        for i in sudoku:
            cont = 0
            print("|", end=" ")
            for j in i:
                print(j, end=" ")
                cont+=1
                if(cont%3==0):
                    print("|", end=" ")
            cont2+=1
            print()
            if(cont2%3==0):
                print("-------------------------")
        print("\n")


sudoku = [[4, 5, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 2, 0, 7, 0, 6, 3, 0],
          [0, 0, 0, 0, 0, 0, 0, 2, 8],
          [0, 0, 0, 9, 5, 0, 0, 0, 0],
          [0, 8, 6, 0, 0, 0, 2, 0, 0],
          [0, 2, 0, 6, 0, 0, 7, 5, 0],
          [0, 0, 0, 0, 0, 0, 4, 7, 6],
          [0, 7, 0, 0, 4, 5, 0, 0, 0],
          [0, 0, 8, 0, 0, 9, 0, 0, 0]]

Q = SudokuSolver()
print("a")
Q.solveSudoku()
Q.printSolution()
#print("Total solutions:", Q.cont)
print("?")