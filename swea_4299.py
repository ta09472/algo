t = int(input())
for i in range(1,t+1):
    D,H,M = map(int, input().split())
    passing_D = (D - 11)*24*60
    passing_H = (H - 11)*60
    passing_M = M - 11
    result = passing_D + passing_H + passing_M
    if result < 0:
        print(f"#{i} -1")
    else:
        print(f"#{i} {result}")
