from collections import deque
def solution(rc, operations):
    answer = []
    N = len(rc)
    M = len(rc[0])
    l_col = deque([rc[i][0] for i in range(N)])
    r_col = deque([rc[i][M - 1] for i in range(N)])
    row = deque([deque(rc[i][1:M - 1]) for i in range(N)])
    
    for op in operations:
        if op == "ShiftRow":
            l_col.rotate(1)
            r_col.rotate(1)
            row.rotate(1)
        else:
            row[0].appendleft(l_col.popleft())
            row[-1].append(r_col.pop())
            l_col.append(row[-1].popleft())
            r_col.appendleft(row[0].pop())
    
    for i in range(N):
        answer.append([l_col[i]] + list(row[i]) + [r_col[i]])
    
    return answer

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))