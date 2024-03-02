# https://school.programmers.co.kr/learn/courses/30/lessons/118669

def solution(n, paths, gates, summits):
    answer = []
    graph = [[0 for j in range(n + 1)] for i in range(n + 1)]
    for i, j, w in paths:
        graph[i][j] = w
        graph[j][i] = w
    
    for summit in summits:
        pass
    return answer

# dp로 안되나??
# 2차원 배열로
