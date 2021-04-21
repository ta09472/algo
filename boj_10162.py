t = int(input())
answer = [0,0,0]
while True:
    if t < 10:
        break
    if t >= 300:
        answer[0] += (t // 300)
        t %= 300
    elif t >= 60:
        answer[1] += (t // 60)
        t %= 60
    elif  t >= 10:
        answer[2] += (t // 10)
        t %= 10

if t != 0:
    print(-1)
else:
    print(*answer, sep = " ")
