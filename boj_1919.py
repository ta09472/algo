str1 = input()
str2 = input()
cnt = 0
for i in range(97,123):
    cnt += abs(str1.count(chr(i)) - str2.count(chr(i))) # 서로 다른 문자의 수
print(cnt)
