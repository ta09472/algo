n, m = map(int,input().split())
num_list = []
answer = []
for i in range(n):
    num_list.append(list(map(int,input().split())))
    answer.append(min(num_list[i]))
print(max(answer))
