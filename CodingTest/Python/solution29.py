# https://school.programmers.co.kr/learn/courses/30/lessons/118669
import heapq
import math
def solution(n, paths, gates, summits):
    inf = math.inf
    
    graph = [[] for i in range(n + 1)]
    for path in paths:
        graph[path[0]].append([path[1], path[2]])
        graph[path[1]].append([path[0], path[2]])

    is_summit = [False] * (n + 1)
    for summit in summits:
        is_summit[summit] = True
    
    dist = [inf for i in range(n + 1)]
    q = []
    for gate in gates:
        dist[gate] = 0
        heapq.heappush(q, [0, gate])

    while q:
        d, i = heapq.heappop(q)
        if dist[i] < d or is_summit[i]:
            continue
        for j, new_d in graph[i]:
            new_d = max(dist[i], new_d)
            if dist[j] > new_d:
                dist[j] = new_d
                heapq.heappush(q, [new_d, j])

    answer = [0, inf]
    for summit in sorted(summits):
        if dist[summit] < answer[1]:
            answer[0] = summit
            answer[1] = dist[summit]

    return answer
# ['inf', 0, 3, 4, 3, 3, 3]
# ['inf', 4, 4, 0, 4, 4, 4]

#[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]	[1, 3]	[5]	[5, 3]