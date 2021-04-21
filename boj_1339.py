words_list = [input().upper() for i in range(int(input()))]
dict = {}
nums = []
answer = 0
multipy = 9

for word in words_list: # 알파벳들을 딕셔너리에 넣기
    k = len(word)-1
    for alphabet in word:
        if alphabet in dict: # 알파벳이 기존 딕셔너리에 중복되는지 확인
            dict[alphabet] += pow(10,k)
        else:
            dict[alphabet] = pow(10,k)
        k -= 1

for value in dict.values(): # 밸류값만 가져와서 nums 리스트에 추가
    nums.append(value)
nums.sort(reverse = True)

for i in range(len(nums)):
    answer += nums[i] * multipy
    multipy -= 1

print(answer)
