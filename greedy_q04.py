n = int(input())
arr = sorted(list(map(int, input().split())))
x = 1
for i in arr:
    if x < i:
        print(x)
        break
    else:
        x += i
