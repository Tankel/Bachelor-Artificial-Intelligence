"""
Value code for each piece is as follows:
    - pawn = 1 for white, -1 for black
    - bishop =  2 for white, -2 for black
    - knight =  3 for white, -3 for black
    - rook =  4 for white, -4 for black

* It is recommended to store the direction of movement of both your pawn and opponent's pawn.

"""

import copy
import random
import time
import math

class TTCPlayer:
    # valuesCode is a list containing the value code that you must use to represent your pieces over the board.
    # The sign of the value code will tell you if you are playing as white or black pieces.
    # The values are in the order: pawn, bishop, knight, rook
    def __init__(self, name):
        self.name = name
        self.pawnDirection = 1
        self.currentTurn = 1
        self.maxCaptures = 5
        self.board = [[0] * 4 for _ in range(4)]

        self.piecesOnBoard = [0] * 5

    def setColor(self, piecesColor):
        self.piecesCode = [0, 1, 2, 3, 4]
        self.piecesCode = [x*piecesColor for x in self.piecesCode]
        self.piecesColor = piecesColor

    def __updatePawnDirection(self, board):
        # If the pawn is in the limit of the board, it should reverse
        if self.piecesColor in board[0]:
            self.pawnDirection = 1
        
        # If the pawn is in the start of the board, it should go forward
        if self.piecesColor in board[3]:
            self.pawnDirection = -1

    def __sameSign(self, a, b):
        return ((a < 0 and b < 0) or (a > 0  and b > 0))
    
    def __isInsideBoard(self, row, col):
        return (row >= 0 and row < 4 and col >= 0 and col < 4)

        # Function to check whether a movement was a movement or not
    
     # If it was a movement, it also checks if it was a capture or not.   
    
    def __wasPieceMovement(self, oldBoard, newBoard):
        changedSquares = []

        for i in range(4):
            for j in range(4):
                if oldBoard[i][j] != newBoard[i][j]:
                    changedSquares.append((i, j))

        if len(changedSquares) != 2:
            return False, False
        
        def areChangesFromCapture(row1, col1, row2, col2):
            return (newBoard[row1][col1] == 0
                    and oldBoard[row2][col2] != 0 
                    and newBoard[row2][col2] == oldBoard[row1][col1])
        
        def areChangesFromMovement(row1, col1, row2, col2):
            return (newBoard[row1][col1] == 0
                    and newBoard[row2][col2] == oldBoard[row1][col1])
        
        wasMovement = (areChangesFromMovement(changedSquares[0][0], changedSquares[0][1], changedSquares[1][0], changedSquares[1][1]) 
                or areChangesFromMovement(changedSquares[1][0], changedSquares[1][1], changedSquares[0][0], changedSquares[0][1]))
        
        wasCapture = (areChangesFromCapture(changedSquares[0][0], changedSquares[0][1], changedSquares[1][0], changedSquares[1][1]) 
                or areChangesFromCapture(changedSquares[1][0], changedSquares[1][1], changedSquares[0][0], changedSquares[0][1]))

        return (wasMovement, wasCapture)

    def __getPawnValidMovements(self, position, board, pawnDirection):
        validMovements = []
        
        row = position[0]
        col = position[1]

        # Move 1 to the front
        newRow = row + pawnDirection
        if self.__isInsideBoard(newRow, col) and board[newRow][col] == 0:
            validMovements.append((newRow, col))

        # Attack to the left
        newCol = col - 1
        if self.__isInsideBoard(newRow, newCol) and board[newRow][newCol] != 0 and not self.__sameSign(board[newRow][newCol], board[row][col]):
            validMovements.append((newRow, newCol))

        # Attack to the right
        newCol = col + 1
        if self.__isInsideBoard(newRow, newCol) and board[newRow][newCol] != 0 and not self.__sameSign(board[newRow][newCol], board[row][col]):
            validMovements.append((newRow, newCol))

        return validMovements
    
    def __getBishopValidMovements(self, position, board):
        validMovements = []

        row = position[0]
        col = position[1]

        # To check whether I already encountered a piece in this diagonal or not
        # 0 -> Up-Left Diagonal
        # 1 -> Up-Right Diagonal
        # 2 -> Down-Left Diagonal
        # 3 -> Down-Right Diagonal
        diagEncounteredPiece = [False] * 4

        # Describe the direction of the movement for the bishop in the same
        # order as described above
        movDirection = [[-1, -1],
                     [-1, 1],
                     [1, -1],
                     [1, 1]]

        # A bishop can move at most 3 squares
        for i in range(1,4):
            # Check 4 directions of movement
            for j in range(4):
                newCol = col + i * movDirection[j][0]
                newRow = row + i * movDirection[j][1]

                # If I haven't found a piece yet in this direction and its inside the board
                if not diagEncounteredPiece[j] and self.__isInsideBoard(newRow, newCol):
                    # If the proposed square its occupied
                    if board[newRow][newCol] != 0:
                        # If the piece that occupies the square its from the opponent, then its a valid movement
                        if not self.__sameSign(board[row][col], board[newRow][newCol]):
                            validMovements.append((newRow, newCol))
                        diagEncounteredPiece[j] = True
                    else: # If not, just append the movement
                        validMovements.append((newRow, newCol))

        return validMovements

    def __getKnightValidMovements(self, position, board):
        validMovements = []

        row = position[0]
        col = position[1]


        # Describe the movements of the knight
        movements = [[-2, 1],
                     [-1, 2],
                     [1, 2],
                     [2, 1],
                     [2, -1],
                     [1, -2],
                     [-1, -2],
                     [-2, -1]]
        
        # Loop through all possible movements
        for move in movements:
            newRow = row + move[0]
            newCol = col + move[1]

            # For the knight we just need to check if the new square is valid and it is not occupied by a piece of the same color
            if self.__isInsideBoard(newRow, newCol) and not self.__sameSign(board[row][col], board[newRow][newCol]):
                validMovements.append((newRow, newCol))

        return validMovements

    def __getRookValidMovements(self, position, board):
        validMovements = []

        row = position[0]
        col = position[1]

        # Checks whether or not I have found a piece in this direction
        # 0 - Up
        # 1 - Right
        # 2 - Down
        # 3 - Left
        dirPieceEncountered = [False] * 4

        # Describe the direction of movement for the rook
        # The order is the same as described above
        movDirection = [[-1, 0],
                        [0, 1],
                        [1, 0],
                        [0, -1]]
        
        # The rook can move maximum 3 squares
        for i in range(1, 4):
            # Loop through all possible movements
            for j in range(4):
                newRow = row + i * movDirection[j][0]
                newCol = col + i * movDirection[j][1]

                if not dirPieceEncountered[j] and self.__isInsideBoard(newRow, newCol):
                    if board[newRow][newCol] != 0:
                        if not self.__sameSign(board[newRow][newCol], board[row][col]):
                            validMovements.append((newRow, newCol))
                        dirPieceEncountered[j] = True
                    else:
                        validMovements.append((newRow, newCol))

        return validMovements        

    def __getValidMovements(self, pieceCode, position, board):
        if abs(pieceCode) == 1:
            return self.__getPawnValidMovements(position, board, self.pawnDirection)
        elif abs(pieceCode) == 2:
            return self.__getBishopValidMovements(position, board)
        elif abs(pieceCode) == 3:
            return self.__getKnightValidMovements(position, board)
        elif abs(pieceCode) == 4:
            return self.__getRookValidMovements(position, board)
        else:
            print("Piece ", pieceCode, " not recognized")
            return []

    def __getAllValidMoves(self, player, board):
        validMoves = []

        for row in range(4):
            for col in range(4):
                piece = board[row][col]

                # Verificar si la pieza pertenece al jugador actual
                if (piece > 0 and player > 0) or (piece < 0 and player < 0):
                    position = (row, col)
                    moves = self.__getValidMovements(piece, position, board)

                    # Agregar los movimientos válidos a la lista
                    validMoves.extend([(position, move) for move in moves])

        return validMoves


    def __movePiece(self, board):
        #print(self.name, "::moveRandomPiece")
        piece = 0

        while(self.piecesOnBoard[piece] != 1): 
            piece = random.randint(1, 4)
        
        pieceCode = self.piecesCode[piece]
        row = -1
        col = -1

        for i in range(4):
            for j in range(4):
                if board[i][j] == pieceCode:
                    row = i
                    col = j

                    i = 4
                    break

        validMovements = self.__getValidMovements(pieceCode, (row, col), board)
        if len(validMovements) == 0:
            return board
        
        #newRow, newCol = self.bestMoveAB(pieceCode, validMovements, board)
        newRow, newCol = validMovements[random.randint(0, len(validMovements)-1)]

        board[row][col] = 0
        board[newRow][newCol] = pieceCode

        return board

    def __updatePiecesOnBoard(self, board):
        self.piecesOnBoard = [0] * 5

        for i in range(4):
            for j in range(4):
                if self.__sameSign(board[i][j], self.piecesColor):
                    self.piecesOnBoard[abs(board[i][j])] = 1

    # que estrategia usar para sacar piezas?
    def __putPiece(self, board):
        piece = -1
        while(piece == -1 or self.piecesOnBoard[piece] != 0):
            piece = random.randint(1, 4)

        newRow = random.randint(0, 3)
        newCol = random.randint(0, 3)

        while (board[newRow][newCol] != 0):
            newRow = random.randint(0, 3)
            newCol = random.randint(0, 3)

        board[newRow][newCol] = piece * self.piecesColor

        return board

    def play(self, board):
        start = time.time()
        self.currentTurn += 1
        self.__updatePiecesOnBoard(board)

        originalBoard = copy.deepcopy(board)

        # We put a limit since there can be a really rare case when the only valid movement is a capture
        # And if in that moment it happens that you can no longer make any capture, it will cicle. That's why we put a limit.
        for _ in range(1000):

            if self.currentTurn < 3:
                newBoard = self.__putPiece(board)
            elif sum(self.piecesOnBoard) == 0: # There are no pieces on the board
                newBoard = self.__putPiece(board)
            elif sum(self.piecesOnBoard) == 4: # All the pieces are on the board
                newBoard = self.__movePiece(board)
            else:
                if random.randint(0, 1) == 0:
                    newBoard = self.__putPiece(board)
                else:
                    newBoard = self.__movePiece(board)

            _, wasCapture = self.__wasPieceMovement(originalBoard, newBoard)

            if wasCapture:
                if self.availableCaptures > 0:
                    self.availableCaptures -= 1
                else:
                    board = copy.deepcopy(originalBoard)
                    continue

            if newBoard != originalBoard:
                break
        
        self.__updatePawnDirection(newBoard)
        print("Time taken: ", time.time() - start)
        #print(newBoard, flush=True)

        #return utils.updateSyncBoard(syncBoard, newBoard)
        return newBoard       

    def reset(self):
        self.pawnDirection = -1
        self.piecesOnBoard = [0] * 5
        self.currentTurn = -1
        self.availableCaptures = 5

    #bestMove with optimization
    def bestMoveAB(self, pieceCode, validMovements, board):
        bestMove = validMovements[0]  # Initialize the best move as the first valid movement
        maxEval = -math.inf

        for move in validMovements:
            newBoard = copy.deepcopy(board)  # Create a deep copy of the board for each valid movement
            newBoard[move[0]][move[1]] = pieceCode  # Make the move on the new board

            eval = self.minimaxAB(newBoard, 0, -math.inf, math.inf, False)  # Calculate the evaluation using minimax

            if eval > maxEval:
                maxEval = eval
                bestMove = move

        return bestMove
    
    def minimaxAB(self, board, depth, alpha, beta, maximizingPlayer):
        # Evaluar el estado del tablero si se alcanzó la profundidad máxima o el juego ha terminado
        if self.evaluatePosition(board, self.piecesColor * -1):
            return self.evaluate(board)

        if maximizingPlayer:
            maxEval = -math.inf
            validMoves = self.__getAllValidMoves(board, self.piecesColor)
            
            for move in validMoves:
                newBoard = copy.deepcopy(board)
                self.makeMove(newBoard, move)
                
                eval = self.minimaxAB(newBoard, depth + 1, alpha, beta, False)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                
                if beta <= alpha:
                    break
            
            return maxEval
        else:
            minEval = math.inf
            validMoves = self.__getAllValidMoves(board, -self.piecesColor)
            
            for move in validMoves:
                newBoard = copy.deepcopy(board)
                self.makeMove(newBoard, move)
                
                eval = self.minimaxAB(newBoard, depth + 1, alpha, beta, True)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                
                if beta <= alpha:
                    break
            
            return minEval

    def makeMove(self, move, board):
        # Desempaqueta el movimiento en posición inicial y posición final
        (startRow, startCol), (endRow, endCol) = move

        # Obtiene la pieza en la posición inicial
        piece = board[startRow][startCol]

        # Realiza el movimiento actualizando el tablero
        board[startRow][startCol] = 0  # Vacía la posición inicial
        board[endRow][endCol] = piece  # Coloca la pieza en la posición final

        return board

    def evaluatePosition(self, board, color):
        lrDiagSum = 0
        rlDiagSum = 0
        for i in range(4):
            # Check diagonal left-right, up-down
            if self.__sameSign(board[i][i], color):
                lrDiagSum += 1

            # Check diagonal right-left, up-down
            if self.__sameSign(board[i][3-i], color):
                rlDiagSum += 1

            rowSum = 0
            colSum = 0
            # Loop to check all squares in a row or column
            for j in range(4):
                # Check row i
                if self.__sameSign(board[i][j], color):
                    rowSum += 1

                # Check column i
                if self.__sameSign(board[j][i], color):
                    colSum += 1

            # If the sum is 4, we have 4-pieces in a row
            if rowSum == 4 or colSum == 4:
                return True
            
        # If the sum is 4, we have 4-pieces in a row   
        if lrDiagSum == 4 or rlDiagSum == 4:
            return True
        
        return False
    
    def evaluate(self, board):
        score = 0

        # Verificar filas
        for row in board:
            score += self.evaluateLine(row)

        # Verificar columnas
        for col in range(4):
            column = [board[row][col] for row in range(4)]
            score += self.evaluateLine(column)

        # Verificar diagonales principales
        diagonal1 = [board[i][i] for i in range(4)]
        score += self.evaluateLine(diagonal1)

        # Verificar diagonales secundarias
        diagonal2 = [board[i][4 - 1 - i] for i in range(4)]
        score += self.evaluateLine(diagonal2)

        return score

    def evaluateLine(self, line):
        score = 0
        playerPieces = set()
        opponentPieces = set()

        for piece in line:
            if piece > 0:
                playerPieces.add(piece)
            elif piece < 0:
                opponentPieces.add(piece)

        # Calcular puntuación basada en la cantidad de piezas del jugador y del oponente
        score += len(playerPieces)
        score -= len(opponentPieces)

        return score