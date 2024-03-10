# https://school.programmers.co.kr/learn/courses/30/lessons/92334
def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    idx_map = {}
    report_map = {}
    for i, j in enumerate(id_list): # 이름 넣으면 인덱스 나옴
        idx_map[j] = i
        report_map[j] = 0

    report_set = set(report)
    lst = [[0 for i in range(len(id_list))] for j in range(len(id_list))]
    for i in report_set:
        a, b = i.split(" ")
        report_map[b] += 1
        lst[idx_map[a]][idx_map[b]] += 1
    
    for i, j in report_map.items():
        if j >= k:
            for t in range(len(id_list)):
                if lst[t][idx_map[i]] > 0:
                    answer[t] += 1
    
    return answer

