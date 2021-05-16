n = int(input())
members = []
for i in range(n):
    age, name = input().split()
    members.append((int(age), name))
members.sort(key = lambda members: members[0])
for k in members:
    print(k[0], k[1])
