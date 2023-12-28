import time

class NQueenSolver:
    def __init__(self, size):
        self.size = size 
        self.cont = 0
        #arreglos auxiliares
        self.row = [False] * size
        self.rightDiag = [False] * (size * 2)
        self.leftDiago = [False] * (size * 2)

        # arreglo para guardar las soluciones
        self.solution = [0] * size 
    
    # recursivo par ecnontrar las soluciones
    def __findSolutions(self, currentCol):
        if currentCol == self.size:
            print(self.solution)
            self.cont += 1
            return
        
        # Rcorrer todas las filas de la columna actual
        for i in range (0, self.size):
            #comprobar si la casilla [i, currentCol] esta libre
            if(not self.__isSquaredAttacked(i,currentCol)):
                # Si esta libre, añadimos esta reina la solución
                self.solution[currentCol] = i
                # Marcaos casilla como atacada
                self.__setSquareAttacked(i, currentCol, True)
                # Lamamos a la recursion con la siguiente columna
                self.__findSolutions(currentCol+1)
                #  Al terminar la recursion, marcamos la casilla como libre
                self.__setSquareAttacked(i, currentCol, False)

    # Marcar casilla como atacada o libre
    def __setSquareAttacked(self, row, col, status): #status atacada o libre
        # Marcar fila como atacada
        self.row[row]= status
        # Marcar diagonal derecha como atacada
        self.rightDiag[row+col] = status
        # Marcar diagonal izquierda como atacada
        self.leftDiago[self.size+row-col] = status

    # Preguntar si casilla esta libre o atacada 
    def __isSquaredAttacked(self, row, col):
        # si no esta atacado retornamos 
        return self.row[row] or self.rightDiag[row + col] or self.leftDiago[self.size + (row - col)]
    
    def findSolutions(self):
        self.__findSolutions(0)

start_time = time.time()

N = 8
print("N:", N)
Q = NQueenSolver(N)
Q.findSolutions()
print("Total solutions:",Q.cont)

end_time = time.time()
total_time = end_time - start_time

print("Total time taken:", total_time, "seconds")