
def binary_search(array, target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

t = int(input())
for tc in range(t):
    n = int(input())
    array = sorted(list(map(int, input().split())))
    m = int(input())
    req_array = list(map(int, input().split()))

    for target in req_array:
        print(binary_search(array,target))
# 되도록 함수 써서 제출
