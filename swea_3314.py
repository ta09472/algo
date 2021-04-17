t = int(input())
for i in range(1,t+1):
    score_list = list(map(int, input().split()))
    for _ in range(len(score_list)):
        if score_list[_] <= 40:
            score_list[_] = 40
    print(f"#{i} {sum(score_list) // 5}")
