t = int(input())
for i in range(1, t+1):
    d,l,n = map(int,input().split())
    total_damage = d * (n + (n*(n-1) /2) * l/100)
    print(f"#{i} {round(total_damage)}")
