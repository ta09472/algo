n, k = map(int, input().split())
array = [int(input()) for _ in range(n)]
dp = [0 for _ in range(100001)]
dp[0] = 1
for i in array:
    for j in range(i, k+1):
        dp[j] += dp[j-i]
print(dp[k])
