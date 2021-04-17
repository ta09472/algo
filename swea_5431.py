t = int(input())
for i in range(1,t+1):
    n,k = map(int, input().split())
    n_list = list(map(int, input().split()))
    student = [j for j in range(1,n+1)]
    for u in n_list:
        if u in student:
            student.remove(u)
    print(f"#{i}",*sorted(student),sep = " ")
