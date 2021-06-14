n = input()
ans = 0
for idx,k in enumerate(n):
    if (int(k) == 0 or int(k) == 1) or idx == 0 or (ans == 0 or ans == 1):
        ans += int(k)
    else:
        ans *= int(k)
print(ans)
