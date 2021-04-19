t = int(input())
for i in range(t):
    n = int(input())
    answer_list = []
    num_list = list(map(int, input().split()))
    num_list.sort()
    answer = 0
    for k in range(2,n):
        answer = max(answer,abs(num_list[k] - num_list[k - 2]))
    print(answer)
