import sys
sys.setrecursionlimit(10000)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    global cnt
    graph[x][y] = 2
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
            dfs(nx,ny)


m, n, k = map(int,sys.stdin.readline().split())
graph = [[0] * n for _ in range(m)]
ans = []
cnt = 0

for i in range(k):
    x1,y1,x2,y2 = list(map(int, sys.stdin.readline().split()))
    for k in range(y1,y2):
        for l in range(x1,x2):
            graph[k][l] = 1

for r in range(m):
    for c in range(n):
        if graph[r][c] == 0:
            cnt = 0
            dfs(r,c)
            ans.append(cnt)
ans.sort()
print(len(ans))
for a in ans:
    print(a, end = " ")
