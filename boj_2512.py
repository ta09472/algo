n = int(input())
array = list(map(int, input().split()))
m = int(input())

start = 0
end = max(array)

ans = []
while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in array:
        if i > mid:
            total += mid

        elif i <= mid:
            total += i

    if total > m:
        end = mid - 1

    elif total <= m:
        ans.append(mid)
        start = mid + 1
print(max(ans))
