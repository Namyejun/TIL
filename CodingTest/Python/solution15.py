# https://school.programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    answer = []
    
    tables = {}
    
    for i, genre in enumerate(genres):
        if genre not in tables.keys():
            tables[genre] = [plays[i], []]
            tables[genre][1].append([i, plays[i]])
        else:
            tables[genre][0] += plays[i]
            tables[genre][1].append([i, plays[i]])

    lists = list(tables.values())
    lists.sort(key=lambda x: x[0], reverse= True)
    for i in lists:
        for k, j in enumerate(sorted(i[1], key = lambda x : x[1], reverse= True)):
            if k > 1:
                break
            answer.append(j[0])
    
    return answer