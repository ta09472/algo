n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)
for i in range(n-1,-1,-1):
    if i + array[i][0] <= n:
        dp[i] = max(dp[i+1], array[i][1] + dp[i + array[i][0]])
    else:
        dp[i] = dp[i+1]
print(max(dp))
