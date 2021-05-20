n = int(input())
positive = []
negative = []
else_num = []

ans = 0
for i in range(n): # 음수 양수 별로 분류
    num = int(input())
    if num == 1:
        ans += 1
    elif num > 1:
        positive.append(num)
    elif num <= 0:
        negative.append(num)

positive.sort(reverse=True)
negative.sort()

if len(positive) % 2 == 0: # 양수가 짝수개 일경우 두개씩 곱한다.
  for i in range(0, len(positive), 2):
    ans += positive[i] * positive[i+1]

else: # 양수가 홀수개 일 경우 두개씩 곱한 후 남은 마지막 수 하나는 더한다
  for i in range(0, len(positive)-1, 2):
    ans += positive[i] * positive[i+1]
  ans += positive[len(positive)-1] # 마지막 수는 더한다.


if len(negative) % 2 == 0: # 음수가 짝수개 일 경우 두개씩 곱한다.
  for i in range(0, len(negative), 2):
    ans += negative[i] * negative[i+1]

else:  # 음수가 홀수개 일 경우 두개씩 곱한 후 남은 마지막 수 하나는 더한다
  for i in range(0, len(negative)-1, 2):
    ans += negative[i] * negative[i+1]
  ans += negative[len(negative)-1] # 마지막 수는 더한다.

print(ans)
