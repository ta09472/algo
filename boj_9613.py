import itertools
def gcd(a,b):
    if b == 0:
        return a
    r = a % b
    return gcd(b,r)

t = int(input())
for i in range(t):
    num_list = list(map(int, input().split()))
    num_list = num_list[1:]
    ans = 0
    for a, b in itertools.combinations(num_list, 2):
        ans += gcd(a, b)
    print(ans)
