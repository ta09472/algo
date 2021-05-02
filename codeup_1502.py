n = int(input())
list = [[0 for i in range(n)] for j in range(n)]
cnt = 0
for k in range(n):
    for l in range(len(list[k])):
        cnt += 1
        list[l][k] = cnt

for k in range(n):
    for l in range(n):
        print(list[k][l], end= " ")
    print()
