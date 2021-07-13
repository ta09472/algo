import re
def solution(s):
    answer = s
    answer = re.sub("zero","0", answer)
    answer = re.sub("one","1", answer)
    answer = re.sub("two","2", answer)
    answer = re.sub("three","3", answer)
    answer = re.sub("four","4", answer)
    answer = re.sub("five","5", answer)
    answer = re.sub("six","6", answer)
    answer = re.sub("seven","7", answer)
    answer = re.sub("eight","8", answer)
    answer = re.sub("nine","9", answer)

    return answer

# num_dic = {"zero":"0",
#             "one":"1",
#             "two":"2",
#             "three":"3",
#             "four":"4",
#             "five":"5",
#             "six":"6",
#             "seven":"7",
#             "eight":"8",
#             "nine":"9"}
#
# def solution(s):
#     answer = s
#     for key, value in num_dic:
#         answer = answer.replace(key, value)
#     return int(answer)
# s = 123
# print(solution(s))
