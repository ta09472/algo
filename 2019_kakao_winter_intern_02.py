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

import re
from collections import Counter

def solution(s):
    answer = []

    s = Counter(re.findall('\d+', s))
    tmp = sorted(s.items(), key=lambda x: x[1], reverse=True)

    for i in tmp:
        answer.append(i[0])

    answer = list(map(int, answer))

    return answer
