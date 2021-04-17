n,m,k = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort(reverse=True)
answer = (n_list[0] * k) + n_list[1]
print(answer)
