# https://school.programmers.co.kr/learn/courses/30/lessons/118669

def solution(n, paths, gates, summits):
    answer = []
    graph = [[0 for j in range(n + 1)] for i in range(n + 1)]
    for i, j, w in paths:
        graph[i][j] = w
        graph[j][i] = w


    for gate in gates:
        dist = ["inf" for i in range(n + 1)]
        visit = [0 for i in range(n + 1)]
        dist[gate] = 0

        for i in range(1, len(dist)):
            min_node = 0
            min_value = 99999999
            for j in range(1, len(dist)): # 최소 노드 찾기
                if visit[j] == 0 and dist[j] != "inf":
                    if min_value > dist[j]:
                        min_value = dist[j]
                        min_node = j
            visit[min_node] = 1

            for j in range(1, len(graph[min_node])):
                if graph[min_node][j] != 0 and dist[j] == "inf":
                    dist[j] = dist[min_node] + graph[min_node][j]
                elif graph[min_node][j] != 0 and dist[j] != "inf":
                    dist[j] = min(dist[j], dist[min_node] + graph[min_node][j])

        print(dist)
            


        
    return answer