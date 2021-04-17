t = int(input())
for tc in range(1,t+1):
    num_list = list(map(int, input().split()))
    answer = []
    for i in range(7):
        for j in range(i+1,7):
            for k in range(j+1,7):
                answer.append(num_list[i] + num_list[j] + num_list[k])
    answer = set(answer)

    print(f"#{tc} {sorted(answer, reverse = True)[4]}")
