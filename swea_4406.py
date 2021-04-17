import re
t = int(input())
for i in range(1,t+1):
    str = input()
    print(f'#{i}',(re.sub('a|e|i|o|u','',str)))
