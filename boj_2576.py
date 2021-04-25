nums = []
for i in range(7):
    k = int(input())
    if k % 2 == 1:
        nums.append(k)
        
if len(nums) == 0:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))
