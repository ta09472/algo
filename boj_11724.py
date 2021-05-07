def dfs(s):
    visited[s] = True
    for edge in graph[s]:
        if not visited[edge]:
            dfs(edge)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0

for i in range(m): # 연결 리스트 작성
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for k in range(1, n + 1):# 모든 정점을 확인하며
    if not visited[k]: # 아직 방문하지 않은 정점이 있다면 함수 호출 후 cnt의 수를 1 증가시킨다.
        dfs(k)
        cnt += 1

print(cnt)
