import sys
n = int(input())
lst = set(list(map(int, input().split())))
m = int(input())
request = sorted(list(map(int, input().split())))

for i in request:
    if i in lst:
        print("yes", end = " ")
    else:
        print("no", end = " ")
