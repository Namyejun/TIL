# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    
    stack_ptr = 0
    for i in s:
        if i == "(":
            stack_ptr += 1
        elif i == ")":
            stack_ptr -= 1
        if stack_ptr < 0:
            answer = False
            return answer
    if stack_ptr != 0:
        answer = False
    return answer