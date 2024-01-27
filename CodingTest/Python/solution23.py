# https://school.programmers.co.kr/learn/courses/30/lessons/258711

def solution(edges):
    answer = [0,0,0,0]
    max_node = 0
    for edge in edges:
        if max_node < edge[0]:
            max_node = edge[0]
        if max_node < edge[1]:
            max_node = edge[1]
    first = [0 for i in range(max_node + 1)]
    total = [0 for i in range(max_node + 1)]
    for edge in edges:
        first[edge[0]] += 1
        total[edge[0]] += 1
        total[edge[1]] += 1
    
    max_cnt = -1
    max_idx = 0
    for i in range(1, max_node + 1):
        if first[i] > max_cnt and total[i] == first[i]:
            max_cnt = first[i]
            max_idx = i
    
    for edge in edges:
        if edge[0] == max_idx:
            total[edge[1]] -= 1
    
    answer[0] = max_idx
    
    cnt = 0
    for i in range(1, max_node + 1):
        if first[i] == 0:
            cnt += 1
    
    answer[2] = cnt
    
    cnt = 0
    for i in range(1, max_node + 1):
        if total[i] == 4:
            cnt += 1
    
    answer[3] = cnt
    
    answer[1] = max_cnt - answer[2] - answer[3]
                
    return answer