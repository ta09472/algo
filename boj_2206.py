from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global dist
    queue = deque()
    queue.append([0, 0, 1])
    dist = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    dist[0][0][1] = 1

    while queue:
        x, y, wall = queue.popleft()
        if x == n - 1 and y == m - 1:
            return dist[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and wall == 1:
                    dist[nx][ny][0] = dist[x][y][1] + 1
                    queue.append([nx, ny, 0])
                elif graph[nx][ny] == 0 and dist[nx][ny][wall] == 0:
                    dist[nx][ny][wall] = dist[x][y][wall] + 1
                    queue.append([nx, ny, wall])

    return -1


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
print(bfs())
