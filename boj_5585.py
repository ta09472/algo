n = int(input())
coin = [500,100,50,10,5,1]
k = 1000 - n
cnt = 0
while True:
    if k == 0:
        break
    for i in coin:
        cnt += k // i
        k %= i
print(cnt)
