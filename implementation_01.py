n = int(input())
cmd = list(input().split())
now_x, now_y = 1, 1

for k in cmd:
    if k == "L" and now_y > 1:
        now_y -= 1
    if k == "R" and now_y < 5:
        now_y += 1
    if k == "U" and now_x > 1:
        now_x -= 1
    if k == "D" and now_x < 5:
        now_x += 1
print(now_x,now_y)
