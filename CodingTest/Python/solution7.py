# https://school.programmers.co.kr/learn/courses/30/lessons/87946
def solution(k, dungeons):
    answer = -1
    from itertools import permutations
    lst = permutations(dungeons, len(dungeons))
    answer_lst = []
    for item in lst:
        temp_k = k
        cnt = 0
        for dungeon in item:
            if temp_k >= dungeon[0]:
                temp_k -= dungeon[1]
                cnt += 1
            else:
                if cnt == 0:
                    cnt = -1
                break
        answer_lst.append(cnt)
    return max(answer_lst)