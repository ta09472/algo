n = int(input())
cnt = 0
for i in range(n+1):
    for k in range(60):
        for l in range(60):
            check = str(i) + str(k) + str(l)
            if "3" in check:
                cnt += 1
print(cnt)
