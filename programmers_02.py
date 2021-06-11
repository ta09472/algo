a = int(input())
b = int(input())
if a <= b:
    start = a
    end = b
else:
    start = b
    end = a
ans = 0
for i in range(start,end+1):
    ans += i
print(ans)
