from queue import Queue

def get_row(sudoku, row):
    """Retorna la fila i del sudoku"""
    return sudoku[row]

def get_column(sudoku, col):
    """Retorna la columna j del sudoku"""
    return [sudoku[i][col] for i in range(9)]

def get_box(sudoku, row, col):
    """Retorna la caja 3x3 en la que se encuentra la casilla (i,j)"""
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    return [sudoku[i][j] for i in range(box_row, box_row+3) for j in range(box_col, box_col+3)]

def get_empty_cells(sudoku):
    """Retorna la lista de celdas vacías en el sudoku"""
    return [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def is_valid(sudoku, row, col, value):
    """Retorna True si el valor es válido para la celda dada"""
    row_values = get_row(sudoku, row)
    col_values = get_column(sudoku, col)
    box_values = get_box(sudoku, row, col)
    if value in row_values or value in col_values or value in box_values:
        return False
    return True

def solve_sudoku_bfs(sudoku):
    """Resuelve el sudoku utilizando BFS"""
    queue = Queue()
    queue.put(sudoku)
    while not queue.empty():
        current = queue.get()
        empty_cells = get_empty_cells(current)
        if not empty_cells:
            return current
        row, col = empty_cells[0]
        for value in range(1, 10):
            if is_valid(current, row, col, value):
                new_sudoku = [row[:] for row in current]
                new_sudoku[row][col] = value
                queue.put(new_sudoku)

sudoku = [[4, 5, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 2, 0, 7, 0, 6, 3, 0],
          [0, 0, 0, 0, 0, 0, 0, 2, 8],
          [0, 0, 0, 9, 5, 0, 0, 0, 0],
          [0, 8, 6, 0, 0, 0, 2, 0, 0],
          [0, 2, 0, 6, 0, 0, 7, 5, 0],
          [0, 0, 0, 0, 0, 0, 4, 7, 6],
          [0, 7, 0, 0, 4, 5, 0, 0, 0],
          [0, 0, 8, 0, 0, 9, 0, 0, 0]]

solution = solve_sudoku_bfs(sudoku)

for row in solution:
    print(row)