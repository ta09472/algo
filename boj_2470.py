n = int(input())
array = sorted(list(map(int, input().split())))

start_idx = 0 # 용액 a에 접근하기 위한 인덱스
end_idx = n-1 # 용액 b에 접근하기 위한 인덱스
val = abs(array[start_idx] + array[end_idx]) # 초기 값
a = start_idx # 용액 a
b = end_idx # 용액 b

while start_idx < end_idx:
    total = array[start_idx] + array[end_idx]
    if abs(total) < val:
        a = start_idx
        b = end_idx
        val = abs(total)

        if total == 0:
            break

    if total > 0:
        end_idx -= 1
    else:
        start_idx += 1
print(array[a], array[b])
