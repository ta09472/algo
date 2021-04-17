t = int(input())
for i in range(1,t+1):
    n = int(input())
    sum_list = []
    for j in range(n):
        p, x = map(float, input().split())
        sum_list.append(p*x)
    print(f"#{i} {sum(sum_list)}")
