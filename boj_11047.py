n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.reverse()
cnt = 0
while True:
    if k == 0:
        break
    for i in coin:
        cnt += k // i
        k %= i
print(cnt)
