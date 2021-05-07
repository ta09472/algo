from collections import deque

def bfs(s):
    queue = deque()
    visited[s] = True
    queue.append(s)
    while queue:
        v = queue.popleft()
        for vertex in graph[v]:
            if not visited[vertex]:
                visited[vertex] = True
                queue.append(vertex)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for i in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)
