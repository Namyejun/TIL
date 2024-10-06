def solution(points, routes):
    answer = 0
    
    points = [[]] + points
    robots = []

    # 로봇들 움직이는 루트 기록
    for i in range(len(routes)):
        robot = []
        
        sx, sy = points[routes[i][0]]
        robot.append([sx, sy])
        
        for j in range(1, len(routes[i])):
            ex, ey = points[routes[i][j]]
            
            while ex != sx:
                if ex - sx > 0:
                    sx += 1
                else:
                    sx -= 1
                robot.append([sx, sy])
            while ey != sy:
                if ey - sy > 0:
                    sy += 1
                else:
                    sy -= 1
                robot.append([sx, sy])

        robots.append(robot)

    # 일단 로봇마다의 경로는 구해놓음. 이제 시간에 따라서 충돌 구하면 됨
    empty = 0
    while len(routes) != empty:
        # 충돌 위치 체크
        crash_point = dict()
        for i in range(len(robots)):
            if len(robots[i]) != 0:
                r, c = robots[i].pop(0)
                if len(robots[i]) == 0:
                    empty += 1
                if (r, c) in crash_point:
                    crash_point[(r, c)] += 1
                else:
                    crash_point[(r, c)] = 1
        
        for i in crash_point.values():
            if i >= 2:
                answer += 1

    return answer