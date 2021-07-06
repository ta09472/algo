import sys
sys.setrecursionlimit(100001)

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(s):
    for v in graph[s]:
        if not parent[v]:
            parent[v] = s
            dfs(v)
dfs(1)
for i in range(2,n+1):
    print(parent[i])

from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(s):
    queue = deque()
    queue.append(s)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                parent[i] = v
                visited[i] = True
                queue.append(i)

bfs(1)
for i in range(2, n+1):
    print(parent[i])
