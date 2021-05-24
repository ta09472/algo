n, m = map(int, input().split())
lst = [int(input()) for _ in range(n)]

start = 1
end = max(lst)
while start <= end: # 반목문 종료조건
    cnt = 0 # 선의 개수
    mid = (start + end) // 2

    for i in lst: # 랜선 분할시키
        cnt += i // mid

    if cnt >= m: # 목표 개수보다 분할시킨 선의 개수가 많다면 시작지점을 바꿔서 다시 이진탐색 시작
        start = mid + 1
    else: # 목표 개수보다 적다면 끝지점을 바꿔서 다시 이진탐색 시작
        end = mid - 1
print(end)
