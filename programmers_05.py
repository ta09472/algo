import re
def solution(new_id):
    answer = ''

    new_id = new_id.lower()

    answer = re.sub("[^a-z\d\-\_\.]", "", new_id)

    answer = re.sub("\.\.+", ".", answer)

    answer = re.sub("^\.|\.$", "", answer)

    if answer == "":
        answer = "a"

    answer = re.sub("\.$","", answer[:15])

    if len(answer) <= 2:
        while True:
            if len(answer) == 3:
                answer += answer[-1]

    return answer
