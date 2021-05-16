n = int(input())
ans = []
for i in range(n):
    ans.append(int(input()))
ans.sort(reverse=True)
ans = map(str, ans)
print(" ".join(ans))
