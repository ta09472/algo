from itertools import combinations
array = [int(input()) for _ in range(9)]
tmp = list(combinations(array,7))
ans = []
result = 0

for i in tmp:
    result = sum(i)
    if result == 100:
        ans = i
        break
    else:
        result = 0

for k in sorted(list(ans)):
    print(k)
