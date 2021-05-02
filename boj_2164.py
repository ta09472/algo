from collections import deque
cardeck = deque()

n = int(input())
for i in range(1,n+1):
    cardeck.append(i)
while True:
    if len(cardeck) == 1:
        break
    cardeck.popleft()
    k = cardeck.popleft()
    cardeck.append(k)
print(cardeck[0]) 
