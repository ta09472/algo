n = int(input())
for i in range(n):
    stack = list(map(str, input()))
    cnt = 0
    for k in stack:
        if k =="(":
            cnt += 1
        elif k ==")":
            cnt -= 1
        if cnt < 0:
            print("NO")
            break
    if cnt > 0:
        print("NO")
    elif cnt == 0:
        print("YES")
