n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
def solution(N, stages):
    tmp = []
    ans = []
    reached_player = len(stages)

    try:
        for player in range(1,n+1):
            tmp.append((player, stages.count(player) / reached_player))
            reached_player -= stages.count(player)
    except:
        ans.append((player, 0))

    tmp = sorted(tmp,key=lambda x: x[1],reverse=True)

    for i in tmp:
        ans.append(i[0])

    return ans
print(solution(n,stages))
