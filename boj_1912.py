n = int(input())
array = list(map(int, input().split()))

dp = [_ for _ in array]

for i in range(1, n):
    dp[i] = max(dp[i], dp[i - 1] + array[i])

print(max(dp))
