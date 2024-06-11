import sys
sys.setrecursionlimit(10**5)

R, C = map(int, input().split())

# 무슨 차이?
#area = [list(map(str, input())) for _ in range(R)]
area = [list(input()) for _ in range(R)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0] # 우 좌 하 상

gotcha_sheep = set()
gotcha_wolves = set()
visited = set()
wolves = 0
sheep = 0

g_wolves = 0
g_sheep = 0

# def Wander(x, y, 늑대, 양)으로 받아서 맨 마지막에 (늑대, 양)을 리턴하려고 한다면 dfs의 맨 끝을 알아야 할 것 같은데, 알 수 있을까? 모르겠어서 글로벌변수 처리함 일단
# nx, ny 문이 아무데도 못가고 끝났다면 될까? ==> 다른 막다른 길도 많을 것이므로 안될 것 같음
# bfs를 썼어야 했을까? ==> (?)
def Wander(x, y):
    global wolves
    global sheep

    visited.add((x, y))

    if area[x][y] == 'o' and (x, y) not in gotcha_sheep:
        gotcha_sheep.add((x, y))
        sheep += 1
    elif area[x][y] == 'v' and (x, y) not in gotcha_wolves:
        gotcha_wolves.add((x, y))
        wolves += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<R and 0<=ny<C and area[nx][ny] != '#':
            if (nx, ny) not in visited:
                Wander(nx, ny)

for i in range(R):
    for j in range(C):
        if area[i][j] == 'o' and (i, j) not in gotcha_sheep or area[i][j] == 'v' and (i, j) not in gotcha_wolves:

            if area[i][j] == 'o':
                sheep += 1 
                gotcha_sheep.add((i, j))
            else:
                wolves += 1
                gotcha_wolves.add((i, j))

            Wander(i, j)

            if wolves >= sheep:
                g_wolves += wolves
            else :
                g_sheep += sheep

            wolves = 0
            sheep = 0
        
        


print(g_sheep, g_wolves)
