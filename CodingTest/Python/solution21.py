# https://school.programmers.co.kr/learn/courses/30/lessons/150364

from collections import deque
import math
def solution(edges, target):
    answer = []
    edges = sorted(edges)
    target = [0] + target

    tree = [deque() for _ in range(len(edges) + 2)]

    for s, e in edges:
        tree[s].append(e)

    max_len = sum(target)
    change_leaf_node = []
    
    for _ in  range(max_len):
        idx = 1
        while True:
            if len(tree[idx]) == 0:
                break
            next_idx = tree[idx][0]
            tree[idx].rotate(-1)
            idx = next_idx
        change_leaf_node.append(idx)

    # 그냥 리프 노드에 도달하는 순서를 기록해놓고 어떤 순서로 넣을지 하면 될거같은데. 굳이 deque로 rotate 같은거 안하고
    # 순서 [4, 8, 7, 9, 4, 10, 7, 8, 4, 9, 7, 10, 4, 8]
    # 타겟 [0, 0, 0, 0, 3, 0, 0, 5, 1, 2, 3]
    min_visit_time = []
    for i in range(len(target)):
        min_visit_time.append(math.ceil(target[i] / 3))

    # 그 다음에 최소 몇 번 리프노드에 방문해야하는지 기록
    # 최소 방문 횟수 [0, 0, 0, 0, 1, 0, 0, 2, 1, 1, 1]

    # 그 다음은 순서를 처음부터 하나씩 체크하면서 최소 방문 횟수를 만족하는지 체크
    min_drop_order = []
    visit_cnt = []
    for i in range(1, len(change_leaf_node) + 1):
        temp_visit = [0 for _ in range(len(target))]
        for j in change_leaf_node[:i]:
            temp_visit[j] += 1
        
        b = True

        for j in range(len(target)):
            if temp_visit[j] > target[j]:
                return [-1]
            if temp_visit[j] < min_visit_time[j]:
                b = False
                break

        if b:
            min_drop_order = change_leaf_node[:i]
            visit_cnt = temp_visit
            break

    # print(change_leaf_node)
    # print(min_visit_time)
    # print(min_drop_order)
    # print(visit_cnt)
    # 타겟 [0, 0, 0, 0, 3, 0, 0, 5, 1, 2, 3]
    # 횟수 [0, 0, 0, 0, 2, 0, 0, 2, 1, 1, 1]
    # 최소 방문 횟수 만족하는 [4, 8, 7, 9, 4, 10, 7]
    order = []
    result = [[]]
    for i in range(1, len(target)):
        # print(target)
        # print(visit_cnt) # 얘네 두개가지고 할거임
        if target[i] == 0:
            result.append([])
        else:
            result.append(arrange(visit_cnt[i], target[i]))

    for i in min_drop_order:
        order.append(result[i].pop())

    return order


def arrange(x, y): # 4 7
    t = y
    return_val = []
    for i in range(x):
        if t - (x - i)*3 == 0:
            return_val += [3]*(x - i)
            break
        elif t - (x - i)*3 == -1:
            return_val.append(2)
            t -= 2
        else:
            return_val.append(1)
            t -= 1
    return list(reversed(return_val))