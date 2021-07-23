from collections import deque

def bfs(s):
    queue = deque()
    queue.append((s,0))
    visited[s] = True
    while queue:
        v, depth = queue.popleft()
        if depth == 2:
            break
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append((i,depth+1))
    return depth

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)

for i in visited:
    if i:
        cnt += 1
print(cnt-1)
