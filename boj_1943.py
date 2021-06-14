n = int(input())
def gcd(a,b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)

def lcd(a,b):
    return a * b // ans_gcd

for i in range(n):
    a, b = map(int, input().split())
    ans_gcd = gcd(a,b)
    ans_lcd = lcd(a,b)
    print(ans_lcd)
