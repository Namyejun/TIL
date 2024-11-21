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



# import collections
# import itertools

# def solution(orders, course):
#     result = []

#     for course_size in course:
#         order_combinations = []
#         for order in orders:
#             order_combinations += itertools.combinations(sorted(order), course_size)

#         most_ordered = collections.Counter(order_combinations).most_common()
#         result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

#     return [ ''.join(v) for v in sorted(result) ]