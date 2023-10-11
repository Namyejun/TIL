# https://school.programmers.co.kr/learn/courses/30/lessons/172927

m = {0:{"diamond":1, "iron":1, "stone":1},
     1:{"diamond":5, "iron":1, "stone":1},
     2:{"diamond":25, "iron":5, "stone":1}}
def solution(picks, minerals):
    global answer
    answer = 99999
    dfs(0, picks, minerals)
    
    return answer

def dfs(score, picks, minerals):
    global answer
    if sum(picks) == 0 or len(minerals) == 0:
        answer = min(answer, score)
    else:
        for i in range(3):
            if picks[i] == 0:
                pass
            else:
                temp_picks = picks[:]
                temp_picks[i] -= 1
                temp_score = 0
                if len(minerals) < 5:
                    for j in range(len(minerals)):
                        temp_score += m[i][minerals[j]]
                    dfs(score + temp_score, temp_picks, [])
                else:
                    for j in range(5):
                        temp_score += m[i][minerals[j]]
                    dfs(score + temp_score, temp_picks, minerals[5:])