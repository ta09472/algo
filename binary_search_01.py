# import sys
# n = int(input())
# lst = set(list(map(int, input().split())))
# m = int(input())
# request = sorted(list(map(int, input().split())))
#
# for i in request:
#     if i in lst:
#         print("yes", end = " ")
#     else:
#         print("no", end = " ")

n = int(input())
w_item = sorted(list(map(int, input().split())))
m = int(input())
request = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1
    return None

for i in request:
    ans = binary_search(w_item, i,0,n-1)
    if ans != None:
        print("yes", end = " ")
    else:
        print("no", end = " ")
