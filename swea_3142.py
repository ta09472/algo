t = int(input())
for i in range(1,t+1):
    n,m = map(int, input().split())
    twin_horn = n - m
    unicon = m - twin_horn
    print(f"#{i} {unicon} {twin_horn}")
