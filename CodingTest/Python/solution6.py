# https://school.programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    ans_lst = []
    lst = list(enumerate(priorities))
    while lst:
        idx, prior = lst.pop(0)
        for i, j in lst:
            if prior < j:
                lst.append((idx, prior))
                break
        else:
            ans_lst.append(idx)

    return ans_lst.index(location) + 1