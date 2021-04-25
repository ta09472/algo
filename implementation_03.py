movement = [[-2,-1], [-1,-2], [1,-2], [2,-1], [2,1], [1,2], [-1,2], [-2,1]]
now = list(input())
now[0] = ord(now[0]) - 96
now[1] = int(now[1])
cnt = 0
for i in movement:
    if now[0] - i[0] >= 1 and now[1] - i[1] >= 1:
        cnt += 1
print(cnt)
