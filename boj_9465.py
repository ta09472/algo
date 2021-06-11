t = int(input())

for test_case in range(t):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(2)]

    arr[0][1] = arr[0][1] + arr[1][0]
    arr[1][1] = arr[1][1] + arr[0][0]

    for k in range(2, n):
        arr[0][k] = arr[0][k] + max(arr[1][k - 1], arr[1][k - 2])
        arr[1][k] = arr[1][k] + max(arr[0][k - 1], arr[0][k - 2])

    ans = max(arr[0][n-1], arr[1][n-1])
    print(ans)
