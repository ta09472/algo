t = int(input())
def recursion(n):
    if n == 1: # 재귀함수 탈출 조건들(초기 조건)
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return recursion(n - 1) + recursion(n - 2) + recursion(n - 3)

for i in range(t):
    n = int(input())
    print(recursion(n))

#         f(n)
# f(n-1) f(n-2) f(n-3)
# .......
