import heapq

class SudokuSolver:
    def __init__(self, sudoku):
        self.size = 9
        self.width = int(self.size**0.5)
        self.sudoku = [row[:] for row in sudoku]
        self.steps = 0
        self.solutions = 0

    '''
    def getRow(self, row):
        """Retorna la fila i del sudoku"""
        return self.sudoku[row]

    def getColumn(self, col):
        """Retorna la columna j del sudoku"""
        return [self.sudoku[i][col] for i in range(self.size)]

    def getBox(self, row, col):
        """Retorna la caja 3x3 en la que se encuentra la casilla (i,j)"""
        box_row = (row // self.width) * self.width
        box_col = (col // self.width) * self.width
        return [self.sudoku[i][j] for i in range(box_row, box_row + self.width) for j in range(box_col, box_col + self.width)]
    '''


    '''
    def isValid(self, y, x, n):
        """Retorna True si el valor es válido para la celda dada"""
        rowVal = self.getRow(y)
        colVal = self.getColumn(x)
        boxVal = self.getBox(y, x)
        if n in rowVal or n in colVal or n in boxVal:
            return False
        return True
        
    def isSolved(self):
        for y in range(self.size):
            for x in range(self.size):
                if self.sudoku[y][x] == 0:
                    return False
        return True
    
    '''

    def solveSudokuBFS(self):
        queue = []
        # Add all empty squares to the queue with their respective number of possible values as the priority
        for y in range(self.size):
            for x in range(self.size):
                if self.sudoku[y][x] == 0:
                    num_possibilities = len(self.getPossibleValues(y, x))
                    heapq.heappush(queue, (num_possibilities, y, x))
        # Start the search
        self.search(queue)
        
    def search(self, queue):
        if not queue:
            return
        # Pop the next box to fill from the priority queue
        num_possibilities, y, x = heapq.heappop(queue)
        # Try filling the box with each possible value
        for value in self.getPossibleValues(y, x):
            # Save the current state of the sudoku
            backup = [row[:] for row in self.sudoku]
            self.steps += 1
            self.sudoku[y][x] = value
            # If the sudoku is solved, print the solution and return
            if self.isSolved():
                self.solutions += 1
                print("Numero de pasos:", self.steps)
                #self.steps = 0
                self.printSudoku()
                return
            # Otherwise, add all empty squares to the priority queue with their respective number of possible values as the priority
            for i in range(self.size):
                for j in range(self.size):
                    if self.sudoku[i][j] == 0:
                        num_possibilities = len(self.getPossibleValues(i, j))
                        heapq.heappush(queue, (num_possibilities, i, j))
            # Recursively continue the search
            self.search(queue)
            # Restore the previous state of the sudoku
            self.sudoku = [row[:] for row in backup]

    def getPossibleValues(self, y, x):
        used_values = set()
        for i in range(self.size):
            used_values.add(self.sudoku[y][i])
            used_values.add(self.sudoku[i][x])
        gridX = (x//self.width)*self.width
        gridY = (y//self.width)*self.width
        for i in range(self.width):
            for j in range(self.width):
                used_values.add(self.sudoku[gridY+i][gridX+j])
        possible_values = set(range(1, self.size+1)) - used_values
        return possible_values

    def isSolved(self):
        for y in range(self.size):
            for x in range(self.size):
                if self.sudoku[y][x] == 0:
                    return False
        return True

    def printSudoku(self):
        for row in self.sudoku:
            print(row)
        print()



sudoku = [[4, 5, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 2, 0, 7, 0, 6, 3, 0],
          [0, 0, 0, 0, 0, 0, 0, 2, 8],
          [0, 0, 0, 9, 5, 0, 0, 0, 0],
          [0, 8, 6, 0, 0, 0, 2, 0, 0],
          [0, 2, 0, 6, 0, 0, 7, 5, 0],
          [0, 0, 0, 0, 0, 0, 4, 7, 6],
          [0, 7, 0, 0, 4, 5, 0, 0, 0],
          [0, 0, 8, 0, 0, 9, 0, 0, 0]]


Q = SudokuSolver(sudoku)
Q.solveSudokuBFS()

'''
there is one little trick to improve the the solver by magnitudes, iterate over all fields and find the one with the least possible values according to the 3 constraints (row, colom, box) 
if you feel fance only try those values (but it just reduces runtime costs by some small amount)
that way you have much less guessing and the search tree almost collapses to a list
there is one little trick to improve the the solver by magnitudes, iterate over all fields and find the one with the least possible values according to the 3 constraints (row, colom, box) 
if you feel fance only try those values (but it just reduces runtime costs by some small amount)
that way you have much less guessing and the search tree almost collapses to a list
'''