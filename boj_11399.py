n = int(input())
waiting_time = list(map(int, input().split()))
waiting_time.sort()
answer = 0
for i in range(n):
    answer += waiting_time[i] * (n - i)
print(answer)
