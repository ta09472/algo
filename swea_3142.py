t = int(input())
for i in range(1,t+1):
    n, m = map(int,input().split())
    twinhorn = n - m
    unicon = m - twinhorn
    print(f"#{i} {unicon} {twinhorn}")
