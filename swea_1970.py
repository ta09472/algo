moneys = [50000,10000,5000,1000,500,100,50,10]
t = int(input())
for i in range(1,t+1):
    result = [0 for _ in range(8)]
    n = input()
    n = int(n) - int(n[-1])
    k = 0
    while True:
        result[k] = n // moneys[k]
        n %= moneys[k]
        if n == 0:
            break
        k+=1
    print(f'#{i}\n'+" ".join(map(str, result)))
