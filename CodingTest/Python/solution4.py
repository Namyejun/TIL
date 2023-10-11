# https://school.programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1
    lst = {}
    for cloth in clothes:
        if cloth[1] not in lst.keys():
            lst[cloth[1]] = 1
        else:
            lst[cloth[1]] += 1

    lst = list(lst.values())
    for l in lst:
        answer *= (l+1)
    return answer - 1