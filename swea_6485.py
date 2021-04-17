t = int(input())
for tc in range(1,t+1):
    N = int(input())
    bus_num = [0] * 5001

    for _ in range(N):
        a,b = map(int, input().split())

        for i in range(a,b+1):
            bus_num[i] += 1

    P = int(input())
    P_list = []

    for c in range(1,P+1):
        C = int(input())
        P_list.append(bus_num[C])
    print(f"#{tc}", " ".join(map(str,P_list)))
