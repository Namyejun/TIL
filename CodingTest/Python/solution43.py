from collections import deque
from copy import deepcopy
def solution(maze):
    n = len(maze)
    m = len(maze[0])
    
    rvisit = [[0 for _ in range(m)] for _ in range(n)]
    bvisit = [[0 for _ in range(m)] for _ in range(n)]
    
    rstart = [-1, -1, 0]
    bstart = [-1, -1, 0]
    
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                rstart = [i, j]
            if maze[i][j] == 2:
                bstart = [i, j]
    
    rvisit[rstart[0]][rstart[1]] = 1
    bvisit[bstart[0]][bstart[1]] = 1
    
    q = deque()
    
    q.append([rstart, bstart, rvisit, bvisit, 0])

    while q:
        rs, bs, rvt, bvt, cnt = q.popleft()
        rx, ry = rs
        bx, by = bs
        rnv = deepcopy(rvt)
        bnv = deepcopy(bvt)
        rnv[rx][ry] = 1
        bnv[bx][by] = 1
        
        if maze[rx][ry] == 3 and maze[bx][by] == 4:
            return cnt
            
        if maze[rx][ry] == 3:
            for dx, dy in move:
                bnx, bny = bx + dx, by + dy
                if (0 <= bnx < n and 0 <= bny < m) and not((bnx == rx and bny == ry) or (bnv[bnx][bny] == 1) or (maze[bnx][bny] == 5)):
                    q.append([[rx, ry], [bnx, bny], rnv, bnv, cnt + 1])
        
        elif maze[bx][by] == 4:
            for dx, dy in move:
                rnx, rny = rx + dx, ry + dy
                if (0 <= rnx < n and 0 <= rny < m) and not((rnx == bx and rny == by) or (rnv[rnx][rny] == 1) or (maze[rnx][rny] == 5)):
                    q.append([[rnx, rny], [bx, by], rnv, bnv, cnt + 1])
        
        else:
            for rdx, rdy in move:
                rnx, rny = rx + rdx, ry + rdy
                if (0 <= rnx < n and 0 <= rny < m) and not((rnv[rnx][rny] == 1) or (maze[rnx][rny] == 5)):
                    for bdx, bdy in move:
                        bnx, bny = bx + bdx, by + bdy
                        if (0 <= bnx < n and 0 <= bny < m) and not((rnx == bnx and rny == bny) or ((rnx,rny) == (bx, by) and (rx, ry) == (bnx, bny)) or (bnv[bnx][bny] == 1) or (maze[bnx][bny] == 5)):
                            q.append([[rnx, rny], [bnx, bny], rnv, bnv, cnt + 1])
            
    return 0