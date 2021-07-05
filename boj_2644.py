from collections import deque
n = int(input())
s, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start, end):
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        v, cnt = queue.popleft()

        if v == end: # 종료 조건
            return cnt

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append((i,cnt+1))

    return -1

print(bfs(s,e))
