N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N

def dfs(start, dist):

    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            dfs(i, dist + W[start][i])
            visited = False







dfs(0)