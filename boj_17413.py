str = input()
tmp = ""
answer = ""
is_tag = False

for i in str:
    if i == '<':
        is_tag = True
        answer += tmp[::-1] + "<"
        tmp = ''
    elif i == '>':
        is_tag = False
        answer += ">"
    elif i == ' ':
        if is_tag:
           answer += ' '
        else:
           answer += tmp[::-1] + ' '
           tmp = ''
    else:
        if is_tag:
           answer += i
        else:
           tmp += i

answer += tmp[::-1]
print(answer)
