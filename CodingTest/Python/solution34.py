# https://school.programmers.co.kr/learn/courses/30/lessons/92343
result = []
def solution(info, edges):
    answer = 0

    tree = [[] for i in range(len(info))]
    for i, j in edges:
        tree[i].append(j)

    dfs(info, tree, [0])

    return answer

def dfs(info, tree, explorerable, lst, s, w):
    if s <= w or not explorerable:
        result.append(s)
        return
    for i in explorerable:
        new_lst = lst[:]
        new_lst.append(i)
        new_exp = explorerable[:]
        new_exp += tree[i]
        if info[i] == 0:
            dfs(info, tree, new_exp, new_lst, s + 1, w)
        else:
            dfs(info, tree, new_exp, new_lst, s, w + 1)