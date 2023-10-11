# https://school.programmers.co.kr/learn/courses/30/lessons/42628
def solution(operations):
    answer = []
    import heapq
    
    min_q = []
    max_q = []

    for oper in operations:
        c, d = oper.split()
        if c == "I":
            heapq.heappush(min_q, int(d))
            heapq.heappush(max_q, -int(d))
        elif c == "D":
            if d == "-1":
                if min_q and max_q:
                    temp = heapq.heappop(min_q)
                    max_q.remove(-temp)
            elif d == "1":
                if min_q and max_q:
                    temp = heapq.heappop(max_q)
                    min_q.remove(-temp)
    if min_q and max_q:
        answer = [-heapq.heappop(max_q), heapq.heappop(min_q)]
    else:
        answer = [0, 0]
    return answer