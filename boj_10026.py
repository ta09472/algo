import sys
sys.setrecursionlimit(10000)

def dfs(x,y,c):
    visited[x][y] = True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if graph[nx][ny] == c:
                visited[nx][ny] = True
                dfs(nx,ny,c)

dx = [1,-1,0,0]
dy = [0,0,-1,1]

n = int(input())
graph = [list(input()) for _ in range(n)]
colors = ["R","G","B"]
tmp = []
tmp2 = []

for c in colors: # 일반인
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == c and not visited[i][j]:
                cnt += 1
                dfs(i,j,c)
    tmp.append(cnt)

for a in range(n):
    for b in range(n):
        if graph[a][b] != "B":
            graph[a][b] = "R"

for c in colors: # 색맹
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == c and not visited[i][j]:
                cnt += 1
                dfs(i,j,c)
    tmp2.append(cnt)

print(sum(tmp), sum(tmp2))
