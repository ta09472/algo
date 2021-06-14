n = int(input())
arr = list(map(int, input().split()))
arr.sort()
group = []
cnt = 0
for idx, k in enumerate(arr):
    group.append(k)
    if len(group) >= k:
        cnt += 1
        group = []
print(cnt)
