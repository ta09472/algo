n, c = map(int, input().split())
house = sorted([int(input()) for _ in range(n)])

start = 1
end = max(house) - min(house)
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    value = min(house)
    for i in range(1, n):
        if house[i] >= value + mid:
            cnt += 1
            value = house[i]
    if cnt >= c:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
print(ans)
