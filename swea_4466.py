t = int(input())
for i in range(1,t+1):
    n,k = map(int, input().split())
    score_list = list(map(int, input().split()))
    score_list.sort(reverse=True)
    result = 0
    for j in range(k):
        result += score_list[j]
    print(f"#{i} {result}")
