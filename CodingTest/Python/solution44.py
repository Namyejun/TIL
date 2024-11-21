from itertools import combinations as cb

def solution(orders, course):
    answer = []

    d = {}
    for order in orders:
        order = sorted(order)
        for num in course:
            for i in cb(order, num):
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
    
    cand = {i:[] for i in course}

    for k, v in d.items():
        if len(k) in cand:
            cand[len(k)].append([v, ''.join(k)])

    answer = []
    for k, v in cand.items():
        tmp = sorted(v, reverse=True)
        if tmp and tmp[0][0] >= 2:
            mv = tmp[0][0]
            answer.append(tmp[0][1])
            for n, s in tmp[1:]:
                if n == mv:
                    answer.append(s)
                else:
                    break
    return sorted(answer)