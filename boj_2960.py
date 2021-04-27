n, k = map(int, input().split())
cnt = 0
nums = [True for _ in range(n+1)]
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if nums[j] == True:
            nums[j] = False
            cnt = cnt + 1
            if cnt == k:
                print(j)
                break
