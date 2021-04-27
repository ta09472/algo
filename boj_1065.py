n = int(input())
cnt = 0
for i in range(1, n + 1):
    nums = list(map(int, str(i)))
    if i < 100:
        cnt += 1
    else:
        if nums[0] - nums[1] == nums[1] - nums[2]:
            cnt += 1
print(cnt)
