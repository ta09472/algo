from collections import deque

def dfs(v):
    visited_dfs[v] = True # 현재노드의 방문처리
    print(v, end = ' ') # 해당 노드 출력
    for i in gragh[v]: # 각각의 리스트를 순회하면서 인접한 노드를 모두 방문
        if not visited_dfs[i] : # 방문한 노드가 False 방문하지 않은 경우에는 dfs 호출
            dfs(i)

def bfs(v):
    q = deque() # bfs를 실행할 큐 초기화
    q.append(v) # 큐에 시작노드 삽입
    visited_bfs[v] = True # 해당노드를 방문처리
    print(v, end = " ") # 해당 노드 출력
    while q: # 큐가 아무것도 남아있지 않을때까지 반복
        v = q.popleft() # 가장 마지막에 넣은 요소를 꺼낸다.
        for i in gragh[v]: # 각각의 리스트를 순회하면서 인접한 노드를 모두 방문
            if not visited_bfs[i]: # 방문한 노드가 False 방문하지 않은 경우에 아래 동작들을 수행
                q.append(i) # i와 인접한 노드를 모두 큐에 추가
                visited_bfs[i] = True # 큐에 추가한 모든 노드를 방문처리
                print(i, end = " ") # 큐에 있는 요소들을 하나씩 출력


n, m, v = map(int, input().split(' '))

gragh = [[] for _ in range(n+1)] # 헷갈리지 않도록 0번째 인덱스는 비우고 사용
visited_dfs = [False] * (n+1) # dfs의 방문여부를 확인 할 트루 폴스 리스트
visited_bfs = [False] * (n+1) # bfs의 방문여부를 확인 할 트루 폴스 리스트

for _ in range(m):
    x, y = map(int, input().split(' '))
    gragh[x].append(y) # 인접리스트로 표현함. 각각의 인덱스의 요소들은 인접한 노드를 표현하고 있음
    gragh[y].append(x) # 양방향 그래프 이므로 x와 y를 각각 리스트에 추가해준다

dfs(v)
print()
bfs(v)
