from collections import deque

def bfs(x,y,w):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > w :
                visited[nx][ny] = True
                queue.append((nx,ny))

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
                bfs(i,j,k)
    ans = max(ans, cnt)
print(ans)
