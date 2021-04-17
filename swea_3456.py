t = int(input())
for i in range(1,t+1):
    a,b,c = map(int, input().split())
    if a != b:
        d = a+b-c
    else:
        d = c
    print(f"#{i} {d}")
