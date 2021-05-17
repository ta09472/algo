n = int(input())
lista = list(map(int, input().split()))
listb = list(map(int, input().split()))
lista.sort()
key = []
ans = 0
for idx, k in enumerate(sorted(listb, reverse=True)):
    key.append(k)

for j in range(n):
    ans += key[j] * lista[j]
print (ans)
