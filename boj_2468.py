import sys
sys.setrecursionlimit(100000)

def dfs(x, y, h):
    visited[x][y]
    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]

        if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny]:
            if graph[nx][ny] > h:
                visited[nx][ny] = True
                dfs(nx, ny, h)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 1
max_height = max(map(max, graph))

for k in range(max_height):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > k:
                cnt += 1

                dfs(i,j,k)
    ans = max(ans, cnt)
print(ans)
