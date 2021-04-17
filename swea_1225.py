for i in range(1,11):
    t = int(input())
    pwd = list(map(int, input().split()))
    n = 1
    while True:
        if pwd[0] - n <= 0:
            pwd = pwd[1:]
            pwd.append(0)
            break
        else:
            back = pwd[0] - n
            pwd = pwd[1:]
            pwd.append(back)
            n += 1
        if n > 5:
            n = 1

    print(f"#{t}", *pwd, sep = " ")
