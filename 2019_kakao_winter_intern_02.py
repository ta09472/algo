def solution(s):
    answer = []
    tmp = []
    s = s[2:-2]
    s = s.split("},{")
    s = sorted(s, key = lambda x: len(x))

    for k in s:
        if k != ",":
            tmp.append(k.split(","))


    for idx, value in enumerate(tmp):
        for j in range(len(value)):
            if tmp[idx][j] not in answer:
                answer.append(tmp[idx][j])

    answer = list(map(int, answer))

    return answer



s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))
