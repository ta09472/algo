def water(t):
    for i in range(1,t+1):
        P,Q,R,S,W = map(int,input().split())
        A = W * P
        if W <= R:
            B = Q
        else:
            B = Q + (W-R) * S
        if A < B:
            print(f"#{i} {A}")
        elif A > B:
            print(f"#{i} {B}")
t = int(input())
water(t)
