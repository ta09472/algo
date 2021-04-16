def power(n,m):
    if m == 0:
        return 1
    else:
        return n * power(n,m-1)

for i in range(10):
    t = int(input())
    n, m = map(int, input().split())
    print(f"#{t} {power(n,m)}")
