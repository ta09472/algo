from collections import deque
dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]

n, m = map(int, input().split())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)] # 방문여부 확인


def bfs(x,y):
    queue = deque() # 큐 생성 (11-13은 정점의 초기 설정임  함수 밖에서도 정의 가능)
    graph[x][y] = True # 현재 정점(vertex)을 방문처리(True) 처리
    queue.append((x,y)) # 큐에 현재 정점을 삽입
    while queue: # 큐가 비어있지 않을 때까지 반복
        x, y = queue.popleft() # 큐에 마지막으로 들어간 정점의 좌표 위치를 x,y에 할당하고 삭제한다.
        for i in range(4):
            nx = x + dx[i] # 상하좌우 검사하기 위한 과정
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 입력보다 크기가 크거나 작은 경우, 무시
                continue
            if graph[nx][ny] == 0: # 입력에서 0은 벽, 무시
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False: # 정점의 값이 1(길이 뚫려있는 경우)이고 아직 정점을 방문하지 않은 경우(False)
                visited[nx][ny] = True # 해당 정점을 방문처리 한다 (False -> True)
                graph[nx][ny] = graph[x][y] + 1 # 위의 조건을 만족했을 경우 해당 정점의 value를 +1한다. (start에서 해당 정점까지의 거리)
                queue.append((nx, ny)) # 해당 정점을 큐에 추가한다.
    return graph[n - 1][m - 1] # n,m의 value를 반환한다.
print(bfs(0,0)) # 초기 start 정점 입력
