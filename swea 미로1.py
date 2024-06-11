from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        v = q.popleft()

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if 0<=nx<T and 0<=ny<T:
                if maze[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif maze[nx][ny] == 3:
                    return 1

    return 0


def DFS(x, y):
    stack = [(x, y)]
    visited[x][y] = True

    while stack:
        v = stack.pop()
        #visited 놓는 최적의 위치 생각해보기
        #visited[v[0]][v[1]] = True

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if 0<=nx<T and 0<=ny<T:
                if maze[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                elif maze[nx][ny] == 3:
                    return 1

    return 0

T = 16
for t in range(1, 11):
    input()
    maze = [list(map(int, input())) for _ in range(T)]
    visited = [[False] * T for _ in range(T)]

    #print(f'#{t} {DFS(1, 1)}')
    print(f'#{t} {BFS(1, 1)}')
