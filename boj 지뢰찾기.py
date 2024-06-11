import sys
input = sys.stdin.readline

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

def isFinished(x, y):
    finished = True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        #if mineBoard[nx][0][ny] == '*':
        if gameBoard[nx][0][ny] != 'x' or mineBoard[nx][0][ny] == '*':
            finished = False
            break
    
    return finished

def NumOfMines(x, y):
    mines = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if mineBoard[nx][0][ny] == '*':
            mines += 1

    return mines

N = int(input())
mineBoard = [list(map(str, input().split())) for _ in range(N)]
gameBoard = [list(map(str, input().split())) for _ in range(N)]

ansBoard = [['.'] * N for _ in range(N)]

viewMines = False

for i in range(N):
    for j in range(N):
        if gameBoard[i][0][j] == 'x' and mineBoard[i][0][j] == '*':
            viewMines = True
            break
    if viewMines:
        break

for i in range(N):
    for j in range(N):
        if viewMines and mineBoard[i][0][j] == '*':
            ansBoard[i][j] = '*'
            continue

        if gameBoard[i][0][j] == 'x':
            # if mineBoard[i][0][j] == '*':
            #     viewMines = True
            #     ansBoard[i][j] = '*'
            # else:

            if isFinished(i, j):
                ansBoard[i][j] = '0'
            else:
                ansBoard[i][j] = str(NumOfMines(i, j))
            
#print(ansBoard)

# for i in ansBoard:
#     print(*i)

for i in range(N):
    for j in range(N):
        print(ansBoard[i][j], end='')
    print()