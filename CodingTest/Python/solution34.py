# https://school.programmers.co.kr/learn/courses/30/lessons/92343

def solution(info, edges):
    answer = 0

    tree = [[] for i in range(len(info))]
    for i, j in edges:
        tree[i].append(j)

    return answer

def dfs(tree, explorerable, lst):
    for i in explorerable:
        new_lst = lst[:]
        new_lst.append(i)
        new_exp = explorerable[:]
        new_exp += tree[i]