def solution(points, routes):
    answer = 0
    # 포인트의 시작 번호가 1번부터 시작되므로  0번 인덱스 추가
    points = [[]] + points
    
    # 로봇이 기억할 것은 본인의 현재 위치와 다음에 향할 곳
    robots = []

    # 로봇s 초기화
    # 다음에 향할 곳은 포인트 도착 시 route의 앞 부분을 pop하는 방식
    for i in range(len(routes)):
        robots.append([points[routes[i][0]], routes[i][1:], 0])
    
    while chk_finished(robots):
        move(robots, points)
        answer += chk_crash(robots)
    
    return answer
    
# 로봇 움직이는 메서드와 모든 로봇이 움직인 후 충돌 개수 확인하는 메서드 두 개 필요

#로봇 움직이는 메서드로 아예 로봇 리스트와 어떤 로봇인지 받아옴
def move(robots, points):
    for i in range(len(robots)):
        robot = robots[i]

        state = robot[2]
        cur_r, cur_c = robot[0][0], robot[0][1]
        dest_r, dest_c = points[robot[1][0]][0], points[robot[1][0]][0][1]

        if state != 0:
            if dest_r - cur_r < 0:
                cur_r -= 1
            elif dest_r - cur_r > 0:
                cur_r += 1
            else:
                if dest_c - cur_c < 0:
                    cur_c -= 1
                elif dest_c - cur_c > 0:
                    cur_c += 1
                else:
                    state = 1
        
        robots[i] = [[cur_r, cur_c], robot[1][1:], state]

# 끝났는지 확인
def chk_finished(robots):
    chk = 1
    for robot in robots:
        chk *= robot[2]
    
    if chk:
        return True
    else:
        return False

# 충돌 체크 메서드
def chk_crash(robots):
    # 숫자 세기
    cnt = 0
    # 충돌 위치 체크
    crash_dic = dict()

    for robot in robots:
        # 1은 이미 도착해서 사라진 로봇이라 뺌
        if robot[2] != 1:
            if crash_dic.get(robot[0]) != None:
                crash_dic[robot[0]] = 1
            else:
                crash_dic[robot[0]] += 1
    
    return len(crash_dic.keys())


# main    