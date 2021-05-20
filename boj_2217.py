n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort(reverse=True)
max_rope = 0
for i in range(n):
    if rope[i] * (i+1) > max_rope:
        max_rope = rope[i] * (i+1)
print(max_rope)
