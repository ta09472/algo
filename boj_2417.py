n = int(input())
start = 1
end = n
while start <= end:
    mid = (start + end) // 2
    ans = 0
    if mid**2 >= n:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
print(ans)
