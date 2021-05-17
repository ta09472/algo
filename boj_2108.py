import sys
from collections import Counter
n = int(sys.stdin.readline())
list = []

for i in range(n):
    list.append(int(sys.stdin.readline()))

print(round(sum(list) / n))

list.sort()
print(list[n//2])

cnt = Counter(list).most_common()
if len(cnt)> 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(max(list) - min(list))
