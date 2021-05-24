n = int(input())
line = []
for i in range(n):
    x, y = map(int, input().split())
    line.append((x,y))
line.sort(key = lambda line: (line[0], line[1]))

start = line[0][0]
end = line[0][1]
ans = start - end

for i in range(1, n):  # 두번째부터 탐색
    if nList[i][0] <= e and nList[i][1] <= e:  # 현재 구간이 이전 구간에 포함되면
        continue
    ans += nList[i][1] - nList[i][0]  # 일단 구간 더해주기
    # 1. 구간의 일부가 겹칠때
    if nList[i][0] < e:
        ans -= (e - nList[i][0])  # 겹친 부분을 빼줌

    s = nList[i][0]  # 시작점 업데이트
    e = nList[i][1]  # 끝점 업데이트


print(ans)
