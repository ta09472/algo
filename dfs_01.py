def dfs(x,y):
    if (x <= -1 or x >= n) or (y <= -1 or y >= m): # 주어진 범위를 벗어나는 경우 즉시 종료
        return False
    if icebox[x][y] == 0: # 현재 노드를 아직 방문하지 않았다면
        icebox[x][y] = 1 # 해당 노드를 방문처리
        dfs(x - 1, y) # 상하좌우 모두 재귀적으로 호출
        dfs(x + 1, y)
        dfs(x , y - 1)
        dfs(x , y + 1)
        return True
    return False

n, m = map(int, input().split())
icebox = [list(map(int, input())) for i in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True: # 현재위치에서 dfs 탐색 실시
            cnt += 1
print(cnt)
