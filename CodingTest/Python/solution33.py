# https://school.programmers.co.kr/learn/courses/30/lessons/92342#qna
# https://school.programmers.co.kr/questions/25527


# import sys
# sys.setrecursionlimit(10**7)

ryon_lst = []

def solution(n, info):
    answer = []
    min_inv = [info[i] + 1 for i in range(11)]
    lst = [0 for i in range(11)]
    dfs(0, n, lst, min_inv)
    result = []
    
    for r in ryon_lst:
        result.append([calc(info, r), r])
    A = sorted(result, reverse = True)
    if A[0][0] > 0:
        t = 0
        max_lst = []
        while A[t][0] == A[0][0]:
            min_point = -1
            for i in reversed(range(11)):
                if A[t][1][i] != 0:
                    min_point = (10 - i)
                    break
            max_lst.append([min_point, A[t][1]])
            t += 1
        
        B = sorted(max_lst)
        if sum(B[0][1]) != n:
            B[0][1][-1] += n - sum(B[0][1])
        return B[0][1]
    else:
        return [-1]
        
    return answer
    
def dfs(i, k, lst, min_inv):
    if i == 11 or k == 0:
        ryon_lst.append(lst)
        return
    new_lst = lst[:]
    dfs(i + 1, k, new_lst, min_inv)
    if k - min_inv[i] >= 0:
        new_lst[i] += min_inv[i]
        dfs(i + 1, k - min_inv[i], new_lst, min_inv)

def calc(apeach, ryon):
    a = 0
    r = 0
    for i in range(11):
        if apeach[i] == 0 and ryon[i] == 0:
            continue
        
        if apeach[i] >= ryon[i]:
            a += (10 - i)
        else:
            r += (10 - i)
    
    return r - a