from collections import deque

dr = [0,0,-1,1]
dc = [1,-1,0,0]

m,n  = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
answer = []
queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j,0))

while queue:
    r,c,cnt = queue.popleft()
    visited[r][c] = True

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <=  nr < n and 0 <= nc < m and graph[nr][nc] != -1:
            if not visited[nr][nc]:
                graph[nr][nc] = 1
                visited[nr][nc] = True
                queue.append((nr,nc,cnt+1))
    answer.append(cnt)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            answer.append(-1)

if -1 in answer:
    print(-1)
else:
    print(max(answer))
