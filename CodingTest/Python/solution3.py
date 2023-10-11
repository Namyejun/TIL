# https://school.programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    answer = 0
    temp = 0
    citations.sort()
    for i in range(len(citations)):
        if i != 0 and citations[i - 1] == citations[i]:
            pass
        else:
            if citations[i] <= len(citations[i:]) and citations[i] >= len(citations[:i]):
                temp = citations[i]
                answer = citations[i]
            else:
                while True:
                    temp += 1
                    if temp <= len(citations[i:]) and temp >= len(citations[:i]):
                        answer = temp
                    else:
                        break
                break
    return answer