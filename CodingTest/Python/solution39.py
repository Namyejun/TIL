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
    print(robots)
        
    return answer
    
# 뭐가 틀렸을까요...
