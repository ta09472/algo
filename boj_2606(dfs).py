def dfs(v):
    visited[v] = True
    ans.append(v)
    for i in graph[v]:
        if not visited[i]:
            ans.append(i)
            dfs(i)


v = int(input())
e = int(input())

graph = [[] for _ in range(v+1)]
visited = [False for _ in range(v+1)]
ans = []

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
print(len(set(ans)) - 1)
