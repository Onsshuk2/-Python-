import math
import random
#EX1
def nsd(num1,num2):
    return math.gcd(num1,num2)
a=24
b=6
result=nsd(a,b)
print(result)
#EX2
def programNumber():
    return [random.randint(0, 9) for i in range(4)]

def checkGuess(secret, guess):
    bulls= 0
    cows=0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def bullsAndCows(secret, attempts=1):
    guess = [int(num) for num in input("Введіть чотиризначне число: ")]
    bulls, cows = checkGuess(secret, guess)
    print(f"Бики: {bulls}, Корови: {cows}")
    if bulls == 4:
        print(f"Вітаємо! Ви вгадали число за {attempts} спроб.")
    else:
        return bullsAndCows(secret, attempts + 1)

secretNumber = programNumber()
bullsAndCows(secretNumber)
       
    
#EX3
def isValidMove(x, y, path, n):
    return 0 <= x < n and 0 <= y < n and (x, y) not in path

def printBoard(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

def solveKnightTour(board, x, y, move_count, n, path):
    if move_count == n * n:
        printBoard(board, n)
        return True
    moves = [
        (2, 1), (1, 2),
        (-1, 2), (-2, 1),
        (-2, -1), (-1, -2),
        (1, -2), (2, -1)]
    for move in moves:
        next_x, next_y = x + move[0], y + move[1]
        if isValidMove(next_x, next_y, path, n):
            board[next_x][next_y] = move_count + 1
            path.append((next_x, next_y))
            if solveKnightTour(board, next_x, next_y, move_count + 1, n, path):
                return True
            board[next_x][next_y] = 0
            path.pop()
    return False

def knightTour(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[0][0] = 1
    path = [(0, 0)]
    if not solveKnightTour(board, 0, 0, 1, n, path):
        print("No solution exists.")

boardSize = 6  
knightTour(boardSize)

#EX4
def printBoard(board):
    for row in board:
        print(" ".join(map(str, row)))

def shuffleBoard():
    numbers = list(range(1, 16))
    random.shuffle(numbers)
    board = [numbers[i:i + 4] for i in range(0, len(numbers), 4)]
    return board

def getBlankPosition(board):
    for i, row in enumerate(board):
        if 0 in row:
            return i, row.index(0)

def make_move(board, move, blankPosition):
    board[blankPosition[0]][blankPosition[1]], board[move[0]][move[1]] = board[move[0]][move[1]], board[blankPosition[0]][blankPosition[1]]
    return getBlankPosition(board)

def isSolved(board):
    return all(board[i][j] == i * 4 + j + 1 for i in range(4) for j in range(4))

def playGame():
    board = shuffleBoard()
    blankPosition = getBlankPosition(board)
    while not isSolved(board):
        printBoard(board)
        move = tuple(map(int, input("Enter the number you want to move (row column): ").split()))
        if move == (0, 0):  
            break
        if 0 <= move[0] < 4 and 0 <= move[1] < 4 and board[move[0]][move[1]] != 0:
            blankPosition = make_move(board, move, blankPosition)
        else:
            print("Invalid move. Try again.")

    print("Congratulations! You solved the puzzle.")

def startGame():
    playGame()


startGame()


