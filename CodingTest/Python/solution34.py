# https://school.programmers.co.kr/learn/courses/30/lessons/92343

def solution(info, edges):
    answer = []
    visit = [0 for i in range(len(info))]
    def dfs(s, w):
        if s > w:
            answer.append(s)
        else:
            return
        
        for i, j in edges:
            if visit[i] == 1 and visit[j] == 0:
                visit[j] = 1
                if info[j] == 0:
                    dfs(s + 1, w)
                else:
                    dfs(s, w + 1)
                visit[j] = 0
    visit[0] = 1
    dfs(1, 0)
    
    return max(answer)