t = int(input())
for i in range(1,t+1):
    n, k = map(int, input().split())
    total_score_list = []
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for j in range(1, n+1):
        mid_score, final_score, report_score = map(int, input().split())
        total_score = mid_score * 0.35 + final_score * 0.45 + report_score * 0.20
        total_score_list.append(total_score)
    k_index = total_score_list[k-1]
    total_score_list.sort(reverse=True)
    rank = total_score_list.index(k_index) // (n//10)
    k_grade = grade[rank]
    print(f"#{i} {k_grade}")
