t = int(input())
for i in range(1,t+1):
    ymd = input()
    y = ymd[:4]
    m = ymd[4:6]
    d = ymd[6:]
    if int(m) == [1,3,5,7,8,10,12] :
        if int(d) > 31:
            print(f"#{i} -1")
        else:
            print(f"#{i} {y}/{m}/{d}")
    elif int(m) == 2:
        if int(d) > 28:
            print(f"#{i} -1")
        else:
            print(f"#{i} {y}/{m}/{d}")
    elif int(m) == [4,6,9,11]:
        if int(d) > 28:
            print(f"#{i} -1")
        else:
            print(f"#{i} {y}/{m}/{d}")
    elif int(m )== 0:
            print(f"#{i} -1")
    else:
        print(f"#{i} {y}/{m}/{d}")
