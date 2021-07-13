from collections import deque

dc = [1,-1,0,0]
dr = [0,0,-1,1]

def solution(places):
    tmp = []
    answer = []

    for place in places:
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    visited = [[False] * 5 for _ in range(5)]
                    tmp.append(bfs(i,j,visited, place))

        if 0 in tmp:
            answer.append(0)
        else:
            answer.append(1)
        print(tmp)
        tmp = []

    return answer

def bfs(r, c, visited,place):

    queue = deque()
    queue.append((r,c,0))
    visited[r][c] = True

    while queue:
        r, c, cnt = queue.popleft()

        if place[r][c] == "P" and 0 < cnt <= 2:
            return 0

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < 5 and 0 <= nc < 5 and (place[nr][nc] == "O" or place[nr][nc] == "P"):
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr,nc,cnt+1))

    return 1
# 
# places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
#         ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
#         ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
#         ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
#         ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
#
# print(solution(places))
