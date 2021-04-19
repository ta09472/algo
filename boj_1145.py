a = list(map(int, input().split()))
n = 1
while True:
    cnt = 0 #
    for i in range(5):
        if n % a[i] == 0:
            cnt += 1
    if cnt >= 3:
        print(n)
        break
    n += 1


# 이하 내가 처음 제출 한 코드
# 오답인 이유 : 각각의 숫자들의 소인수 분해 한 값을 2차원 배열에 하나씩 넣으려고 했지만 실패
# 제곱수를 각각의 배열에 넣은 후 set 자료형으로 중복되는 수를 삭제하려고 했지만 실패

# 작동과정 :
# -> 입력받은 숫자들의 리스트 중 작은 순서대로 3개의 수만 가져옴
# -> 가져온 3개의 값들을 소인수 분해
# -> 소인수 분해한 결과를 가지고 최대 공배수를 구함
# -> 출력

# def multiply(arr): # 반복이 가능한 객체 전체 곱
#     ans = 1
#     for n in arr:
#         if n == 0:
#             return 0
#         ans *= n
#     return ans
#
# def prime(arr): # 리스트 객체에서 입력값을 받아와 소인수 분해한 결과를 new_list에 반환
#     for num in arr[:3]:
#         i = 2
#         while num!= 1:
#             if num % i == 0:
#                 num = num / i
#                 new_list.append(i)
#             else:
#                 i += 1
#     return new_list
#
# num_list = list(map(int, input().split())) # 입력
# num_list.sort() # 정렬
# new_list = []
#
# new_list = set(prime(num_list)) # set 형태로 감싸 중복되는 값 삭제
# print(multiply(new_list))
