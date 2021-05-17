n = int(input())
x_list = []
for i in range(n):
    x, y = map(int, input().split())
    x_list.append((x,y))
x_list = sorted(x_list, key = lambda x_list: (x_list[0], x_list[1]))

for k in range(n):
    print(x_list[k][0], x_list[k][1])
