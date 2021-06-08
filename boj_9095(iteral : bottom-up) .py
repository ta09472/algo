t = int(input())
dp = [0] * 10001
dp[1] = 1 # 초기 값
dp[2] = 2 # 초기 값
dp[3] = 4 # 초기 값
for _ in range(t):
    n = int(input())
    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])
