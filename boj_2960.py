N, K = map(int, input().split())
cnt = 0
nums = [True] * (N + 1)
for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if nums[j] != False:
            nums[j] = False
            cnt += 1
            if cnt == K:
                print(j)
