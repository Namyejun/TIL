# https://school.programmers.co.kr/learn/courses/30/lessons/150365?language=python3
from collections import deque

# dlru
def solution(n, m, x, y, r, c, k):
    answer = ''

    if distance(x,y,r,c) > k or (k - distance(x,y,r,c))%2==1:
        return 'impossible'

    move = [[1,0,'d'], [0,-1,'l'], [0,1,'r'], [-1,0,'u']]

    lst = []
    q = deque()        
    q.append([x, y, ''])
    while q:
        tx, ty, log = q.popleft()
        if (tx, ty) == (r - 1, c - 1) and (k-len(log))%2==1:
            return 'impossible'
        elif len(log) == k and tx == r and ty == c:
            return log
        elif len(log) < k:
            for i in range(4):
                nx, ny, direction = tx + move[i][0], ty + move[i][1], move[i][2]

                if not (1 <= nx <= n) or not (1 <= ny <= m):
                    pass
                else:
                    if distance(nx, ny, r, c) + len(log) + 1 > k:
                        continue
                    q.append([nx, ny, log + direction])
                    break # 이걸 넣을 수 있는게 바로 위에 if문 써서 아니겠다 싶은 애를 바로 걸러내서임

def distance(x, y, r, c):
    return abs(x - r) + abs(y - c)