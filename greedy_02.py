n,m,k = map(int, input().split())
n_list = list(map(int, input().split()))
<<<<<<< HEAD

=======
>>>>>>> 3f7840d1d6e04cd7ae00f9cf78971715dbd44b38
n_list.sort(reverse=True)

cnt = m // (k+1) * k
cnt += m % (k+1)

answer = 0
answer += (cnt) * n_list[0]
answer += (m - cnt) * n_list[1]
print(answer)
