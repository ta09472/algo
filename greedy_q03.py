s = input()
flag = []
for idx, k in enumerate(s, start=1):
    if k != k-1:
        flag.append(k)
