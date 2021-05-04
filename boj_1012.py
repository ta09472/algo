def dfs(x, y):
    global cnt
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if gragh[x][y] == 1:
        gragh[x][y] = 0 # 조건에 부합하면  1 -> 0 으로 바꿈
        cnt += 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

t = int(input())

for tc in range(t):
    n,m,k = map(int, input().split())
    visited = [[False] * (m) for _ in range(n)]
    gragh = [[0] * n for _ in range(m)]
    ans = []
    cnt = 0
    for i in range(k):
        x, y = map(int,input().split())
        gragh[y][x] = 1

    for i in range(m):
        for j in range(n):
            if dfs(i,j) == True:
                ans.append(cnt)
                cnt = 0
                
    print(len(ans))
