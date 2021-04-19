n = int(input())
answer = list(input())
for i in range(n - 1):
    check = list(input())
    for j in range(len(answer)):
        if answer[j] != check[j]:
            answer[j] = '?'
print("".join(answer))
