s = list(map(str, input()))
t = list(map(str, input()))
while True:
    if len(s) == len(t):
        break

    if t[-1] == "A":
        t.pop()
    elif t[-1] == "B":
        t.pop()
        t.reverse()

if s == t:
    print(1)
else:
    print(0)



# 12
# list.reverse(값을 반환하지 않고 원래의 리스트를 변경한다)list[::-1]과 같다.
# + reversed(list)는 원래의 리스트는 변경하지 않고 값만 반환한다.
