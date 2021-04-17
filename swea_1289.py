t = int(input())
for i in range(1, t + 1):
    cnt = 0
    memory = list(map(int, input().strip()))
    default = 0

    for k in memory:
        if default != k:
            cnt += 1
            default = k

    print(f"#{i} {cnt}")
