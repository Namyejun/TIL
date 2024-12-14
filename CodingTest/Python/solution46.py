# 개인적인 생각으로는 dijkstra로 최단 거리 구해서 해당 루트에 S 껴있으면 그냥 두고 아니면 S에서 시작하는 루트 하나 더 만들기
import heapq
def solution(n, s, a, b, fares):
    maps = [[-1 for _ in range(n + 1)] for i in range(n + 1)]
    inf = 9999999999
    for c, d, f in fares:
        maps[c][d] = f
        maps[d][c] = f
    
    def dijkstra(start):
        dijk = [inf] * (n + 1)
        dijk[start] = 0
        q = []
        for x in range(1, len(maps[start])):
            if maps[start][x] != -1:
                heapq.heappush(q, [maps[start][x], x])
                dijk[x] = maps[start][x]

        while q:
            min_val, min_idx = heapq.heappop(q)
            for x in range(1, len(maps[min_idx])):
                if maps[min_idx][x] != -1:
                    if dijk[x] == inf:
                        dijk[x] = min_val + maps[min_idx][x]
                        heapq.heappush(q, [dijk[x], x])
                    elif dijk[x] > min_val + maps[min_idx][x]:
                        dijk[x] = min_val + maps[min_idx][x]
                        heapq.heappush(q, [dijk[x], x])
                    else:
                        pass
        return dijk
    
    dijk = [[inf] * (n + 1)]
    for i in range(1, n + 1):
        dijk.append(dijkstra(i))

    answer = 9999999999
    for i in range(1, n + 1):
        answer = min(answer, dijk[s][i] + dijk[i][a] + dijk[i][b])

    return answer