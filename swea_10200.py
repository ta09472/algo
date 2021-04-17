t = int(input())
for i in range(1,t+1):
    n,a,b = map(int, input().split())
    min_sub = a + b - n
    if min_sub < 0:
        min_sub = 0
    elif min_sub > 0:
        min_sub = a + b - n
    if a > b:
        max_sub = b
    elif a <= b:
        max_sub = a

    print(f"#{i} {max_sub} {min_sub}")
