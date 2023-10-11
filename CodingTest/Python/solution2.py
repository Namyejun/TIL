# https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(2, total//2):
        if total % i == 0:
            j = total // i
            if (i - 2) * (j - 2) == yellow:
                answer.append(max(i,j))
                answer.append(min(i,j))
                break
        
    return answer