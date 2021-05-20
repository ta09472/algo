import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    cnt = 1
    lists = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    lists.sort(key = lambda lists: (lists[0]))
    min_n = lists[0][1]
    for i in range(1,n):
        if lists[i][1] < min_n:
            min_n = lists[i][1]
            cnt += 1
    print(cnt)
