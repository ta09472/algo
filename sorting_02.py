n = int(input())
ans = []
for i in range(n):
    v, k = map(str, input().split())
    ans.append((v,k))
def set(ans):
    return ans[1]

result = sorted(ans, key = set)
for t in range(len(ans)):
    print(result[t][0], end = " ")
