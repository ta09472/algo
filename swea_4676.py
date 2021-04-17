t = int(input())
for i in range(1,t+1):
    str = list(input())
    n = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort(reverse=True)
    for k in range(n):
        str.insert(num_list[k], "-")
    print(f"#{i}", "".join(str))
