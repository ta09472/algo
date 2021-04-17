T=int(input())

for i in range(T):
    str = list(input())
    if str == str[::-1]:
        result = 1
    else:
        result= 0
    print(f"#{i+1} {result}")
