T = int(input())
for i in range(T):
    numbers = list(map(int, input().split()))
    odd_nums = [num for num in numbers if num % 2 == 1]
    print("#{} {}".format(i+1, sum(odd_nums)))
