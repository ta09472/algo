s = list(map(str, input()))
t = list(map(str, input()))
while True:
    if len(s) == len(t):
        break

    if t[-1] == "A":
        t.pop()
    elif t[-1] == "B":
        t.pop()
        t = t[::-1]

if s == t:
    print(1)
else:
    print(0)
