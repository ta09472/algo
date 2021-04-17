T = int(input())

for test_case in range(1, T + 1):
    li = list(map(int, input().split()))
    result = round(sum(li) / len(li))
    print(f'#{test_case} {result}')
