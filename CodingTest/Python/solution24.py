# https://school.programmers.co.kr/learn/courses/30/lessons/258709

from itertools import combinations
import bisect


def solution(dice):
    global X_lst

    answer = []

    num = [i for i in range(len(dice))]

    X_com = combinations(num, len(dice)//2)

    X_dict = {}

    for x in X_com:
        X = []
        for i in x:
            X.append(dice[i])
        X_lst = []
        X_dfs(X, 0, 0)
        X_lst = sorted(X_lst)
        X_dict[to_str(x)] = X_lst

    lst = []
    X_com = combinations(num, len(dice)//2)
    
    for a in X_com:
        A_lst = X_dict[to_str(a)]
        B_lst = X_dict[to_str(get_b(a, dice))]
        
        cnt = 0
        total = 0
        l = len(B_lst)
        for j in range(len(A_lst)):
            idx = bisect.bisect_left(B_lst, A_lst[j])
            cnt += idx
            total += l

        lst.append([cnt/total, a])
    lst = sorted(lst)
    for i in lst[-1][1]:
        answer.append(i + 1)
    return answer

def X_dfs(X, depth, sumation):
    global X_lst
    if depth == len(X):
        X_lst.append(sumation)
        return
    
    for i in range(6):
        new_sumation = sumation + X[depth][i]
        X_dfs(X, depth + 1, new_sumation)

def to_str(x):
    s = ""
    for i in x:
        s += str(i)
    return s

def get_b(a, dice):
    b = []
    for i in range(len(dice)):
        if i not in a:
            b.append(i)
    return b


# 이거 10C5해서 나오는 결과들 그거를 애초에 for 문 바깥에서 계산하자.
# 그니까 A_lst, B_lst를 둘 다 계산하지 말고
# A_lst 하나만 계산해서 B_lst는 그냥 A_lst 10c5에서 찾자.