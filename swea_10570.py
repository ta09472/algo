t = int(input())
for _ in range(1,t+1):
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B + 1):
        root_num = i ** (1 / 2)
        if root_num == int(root_num):
            root_num = str(int(root_num))
            if str(i) == str(i)[::-1] and root_num == root_num[::-1]:
                cnt += 1

    print(f'#{_} {cnt}')
