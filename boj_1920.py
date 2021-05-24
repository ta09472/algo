n = int(input())
listn = list(map(int, input().split()))
m = int(input())
listm = list(map(int, input().split()))
for i in listm:
    if i in listn:
        print(1)
    else:
        print(0)
