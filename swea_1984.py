t = int(input())
for i in range(1,t+1):
    num_list = sorted(list(map(int, input().split())))
    sumv = sum(num_list[1:9])
    avg = round(sumv/8)
    print(f"#{i} {avg}")
