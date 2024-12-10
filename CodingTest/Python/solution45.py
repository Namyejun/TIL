from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    
    d = {}

    for i in info:
        tmp_i= i.split(" ")
        cond = tmp_i[:-1]
        score = int(tmp_i[-1])

        # 위에서 택한 정보에 부합하는 조건을 싹다 만들어줌
        for x in range(5):
            comb = list(combinations([0,1,2,3], x))
            for c in comb:
                tmp_c = cond[:]
                for y in c:
                    tmp_c[y] = '-'
                if ''.join(tmp_c) in d:
                    d[''.join(tmp_c)].append(score)
                else:
                    d[''.join(tmp_c)] = [score]

    for v in d.values():
        v.sort()

    for q in query:
        q = q.replace("and ", "")
        tmp_q = q.split(" ")
        cond = tmp_q[:-1]
        score = int(tmp_q[-1])
        if ''.join(cond) in d:
            lst = d[''.join(cond)]
            answer.append(len(lst) - bisect_left(lst, score))
        else:
            answer.append(0)
    return answer