T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0] # 우 좌 하 상

def DFS(x, y):
    stack = [(x, y)]

    while stack:
        v = stack.pop()
        visited[v[0]][v[1]] = True

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if 0<=nx<N and 0<=ny<N:
                if maze[nx][ny] == '0' and not visited[nx][ny]:
                    stack.append((nx, ny))
                elif maze[nx][ny] == '3':
                    return 1

    return 0

def BFS(x, y):
    q = [(x, y)]

    while q:
        v = q.pop(0)
        visited[v[0]][v[1]] = True

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if 0<=nx<N and 0<=ny<N:
                if maze[nx][ny] == '0' and not visited[nx][ny]:
                    q.append((nx, ny))
                elif maze[nx][ny] == '3':
                    return 1

    return 0

for t in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                ans = BFS(i, j)
                #ans = DFS(i, j)
                break

        # 이거 안하는 방법?
        if ans:
            break

    print(f'#{t} {ans}')