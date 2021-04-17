t = int(input())
for i in range(1,t+1):
    n = int(input())
    n_earnlist = list(map(int, input().split()))
    mean = sum(n_earnlist) / n
    mean_low = []
    for j in n_earnlist:
        if j <= mean:
            mean_low.append(j)

    print(f"#{i} {len(mean_low)}")t = int(input())
for i in range(1,t+1):
    n = int(input())
    n_earnlist = list(map(int, input().split()))
    mean = sum(n_earnlist) / n
    mean_low = []
    for j in n_earnlist:
        if j <= mean:
            mean_low.append(j)

    print(f"#{i} {len(mean_low)}")
