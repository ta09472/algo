array = [1, 5, 2, 6, 3, 7, 4]
cmds= [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for cmd in commands:
        tmp = sorted(array[cmd[0]-1:cmd[1]])
        answer.append(tmp[cmd[2]-1])
    return answer
print(solution(array,cmds))
