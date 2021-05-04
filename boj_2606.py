from collections import deque

def bfs(s):
    global cnt
    queue = deque()
    visited[s] = True
    queue.append(s)
    while queue:
        v = queue.popleft()
        for i in gragh[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt

v = int(input())
e = int(input())
visited = [False] * (v + 1)
gragh = [[] for _ in range(v+1)]
cnt = 0

for _ in range(e):
    x, y = map(int, input().split(" "))
    gragh[x].append(y)
    gragh[y].append(x)

print(bfs(1))
