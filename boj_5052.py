t = int(input())
for tc in range(t):
    n = int(input())
    phone = []
    for i in range(n):
        phone.append(input())
    phone.sort()
    for k in range(n-1):
        if phone[k] == phone[k+1][0:len(phone[k])]:
            print("NO")
            break
        else:
            print("YES")
            break
    print(phone)
    # phone = sorted(phone, key = lambda x: len(x))
    # for idx, k in enumerate(phone):
    #     if str(k) in phone:
    #         print("NO")
    #         break
    #     else:
    #         print("YES")
    #         break
