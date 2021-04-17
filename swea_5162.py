t = int(input())
for i in range(1,t+1):
    a,b,c = map(int, input().split())
    answer = 0
    if a >= b:
        chaep_bread = b
    else:
         chaep_bread = a
    answer = c // chaep_bread

    print(f"#{i} {answer}")
