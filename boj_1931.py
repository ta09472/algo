n = int(input())
x_list = []
for i in range(n):
    start, end = map(int, input().split())
    x_list.append((start,end))
x_list = sorted(x_list, key = lambda x_list: (x_list[0], x_list[1]))
cnt = 0
k = 0
for i, j in x_list:
    if i >= k:
        cnt += 1
        k = j
print(cnt)
