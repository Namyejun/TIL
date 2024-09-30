def solution(points, routes):
    answer = 0
    # 포인트의 시작 번호가 1번부터 시작되므로  0번 인덱스 추가
    points = [[]] + points
    
    # 로봇이 기억할 것은 본인의 현재 위치와 다음에 향할 곳
    robots = []

    # 로봇s 초기화
    # 다음에 향할 곳은 포인트 도착 시 route의 앞 부분을 pop하는 방식
    for i in range(len(routes)):
        robots.append([points[routes[i][0]], routes[i][1:]])
    

    
    
    return answer
    
# 로봇 움직이는 메서드와 모든 로봇이 움직인 후 충돌 개수 확인하는 메서드 두 개 필요

#로봇 움직이는 메서드로 아예 로봇 리스트와 어떤 로봇인지 받아옴
def move(robots):
    for robot in robots:
        cur_r, cur_c = robot[0][0], robot[0][1]
        dest = robot[1]
        

# main    