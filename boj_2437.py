n = int(input())
sinker_list = list(map(int, input().split()))
sinker_list.sort()

target = 1
for i in sinker_list:
    if target < i:
        break
    else:
        target += i
print(target)
