# https://school.programmers.co.kr/learn/courses/30/lessons/92334
def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    report_map = {i:0 for i in id_list}
    report_set = set(report)
    for i in report_set:
        a, b = i.split(" ")
        report_map[b] += 1
    
    for i in report_set:
        a, b = i.split(" ")
        if report_map[b] >= k:
            answer[id_list.index(a)] += 1
    return answer

