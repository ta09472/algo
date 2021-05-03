def dfs(x, y):
    global cnt # 함수 외부에서도 사용해야하는 변수이기때문에 전역변수 선언
    if x <= -1 or x >= n or y <= -1 or y >= n: # 22의 조건(좌표의 크기를 넘어가지 않는경우)
        return False
    if gragh[x][y] == 1: # 현재의 노드가 1인 경우 즉, 아파트가 존재하는 경우
        gragh[x][y] = "@"  # 현재 노드를 방문처리한다.
        cnt += 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False


n = int(input())
gragh = [list(map(int, input())) for _ in range(n)]
cnt = 0 # 단지내의 아파트 개수 증가
ans = []

# 모든 정점(좌표)을 확인해서 시작점이 될 수 있는지 확인(좌표의 크기 n을 넘어가거나 0보다 작지 않은 경우).조건을 만족하는 경우 dfs 탐색시작
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True: # 22의 조건을 만족한다면 함수 이하 실행
            ans.append(cnt)
            cnt = 0

print(len(ans)) # 총 단지의 수
ans.sort()
print("\n".join(map(str, ans)))
