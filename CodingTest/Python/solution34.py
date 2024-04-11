# https://school.programmers.co.kr/learn/courses/30/lessons/92343
result = []
def solution(info, edges):
    answer = 0

    tree = [[] for i in range(len(info))]
    for i, j in edges:
        tree[i].append(j)

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