def solution(rc, operations):
    before = ""
    lst = []
    for op in operations:
        if op != before:
            lst.append([op, 1])
        else:
            lst[-1][1] += 1
        before = op
    # print(*rc, sep="\n", end="\n")
    # print()
    for op in lst:
        if op[0] == "ShiftRow":
            rc = shift_row(rc, op[1])
        else:
            rc = rotate(rc, op[1])
        # print(*rc, sep="\n", end="\n")
        # print()
    return rc
        
    
def shift_row(arr, n):
    return_arr = []
    queue = deque()
    for i in arr:
        queue.append(i)
    
    queue.rotate(n % len(arr))
    while queue:
        return_arr.append(queue.popleft())
    return return_arr

from collections import deque
def rotate(arr, n):
    queue = deque()
    for i in range(len(arr[0])):
        queue.append(arr[0][i])
    for i in range(1, len(arr)):
        queue.append(arr[i][len(arr[0]) - 1])
    for i in reversed(range(len(arr[0]) - 1)):
        queue.append(arr[len(arr) - 1][i])
    for i in reversed(range(1, len(arr) - 1)):
        queue.append(arr[i][0])
    # print(queue)
    if n % (len(arr) * 4 - 4) == 0:
        return arr[:]
    elif n % (len(arr) * 4 - 4) // 2 >= (len(arr) * 4 - 4) // 2:
        queue.rotate(-((len(arr) * 4 - 4) - (n % (len(arr) * 4 - 4))))
    else:
        queue.rotate(n % (len(arr) * 4 - 4))
        
    return_arr = arr[:]
    for i in range(len(arr[0])):
        return_arr[0][i] = queue.popleft()
    for i in range(1, len(arr)):
        return_arr[i][len(arr[0]) - 1] = queue.popleft()
    for i in reversed(range(len(arr[0]) - 1)):
        return_arr[len(arr) - 1][i] = queue.popleft()
    for i in reversed(range(1, len(arr) - 1)):
        return_arr[i][0] = queue.popleft()
        
    return return_arr
# 시간초과 문제부터해결해보자