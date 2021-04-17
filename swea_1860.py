t = int(input())
for i in range(1,t+1):
    n,m,k = map(int,input().split())
    reached_sec = list(map(int, input().split()))
    reached_sec.sort()
    bread = 0
    idx = 0
    for c in range(reached_sec[-1]+1):
        if c != 0: # 0초 제외
            if c % m == 0:
                bread += k

        if c == reached_sec[idx]: # 손님이 올 시간이라면
            if bread == 0: # 남은 붕어빵이 없다면
                answer = "Impossible"
                break

            else:
                bread -= 1
                idx += 1

        if c == reached_sec[-1]:
            answer = "Possible"
    print(f"#{i} {answer}")
