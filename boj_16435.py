n, l = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()
for i in range(n):
    if l >= heights[i]:
        l += 1
        continue
    elif l < heights[i]:
        break
print(l)
