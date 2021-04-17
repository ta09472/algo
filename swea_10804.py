t = int(input())
for i in range(1,t+1):
    str = input()
    rev_str = str.maketrans("bdpq","dbqp")
    print(f"#{i} {str.translate(rev_str)[::-1]}")
