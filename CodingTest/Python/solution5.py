# https://school.programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    import math
    answer = []
    stck = []
    
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        if len(stck) == 0:
            stck.append(day)
        else:
            if stck[0] >= day:
                stck.append(day)
            else:
                answer.append(len(stck))
                stck = []
                stck.append(day)
    else:
        if len(stck) != 0:
            answer.append(len(stck))
                
    return answer