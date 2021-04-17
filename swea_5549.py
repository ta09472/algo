t = int(input())
for i in range(1,t+1):
    n = input()
    if int(n[-1]) % 2 == 1:
        print(f"#{i} Odd")
    elif int(n[-1]) % 2 == 0:
        print(f"#{i} Even")
