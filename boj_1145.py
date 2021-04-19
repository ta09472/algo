a = list(map(int, input().split()))
n = 1
while True:
    cnt = 0 #
    for i in range(5):
        if n % a[i] == 0:
            cnt += 1
    if cnt >= 3:
        print(n)
        break
    n += 1
