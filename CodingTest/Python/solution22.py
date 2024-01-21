# https://school.programmers.co.kr/learn/courses/30/lessons/258712?language=python3
def solution(friends, gifts):
    answer = 0
    lst = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    
    # 선물 기록
    for i in gifts:
        A, B = i.split(" ")
        A = friends.index(A)
        B = friends.index(B)

        lst[A][B] += 1
    
    # 선물 지수
    lst2 = []
    for i in range(len(friends)):
        give = 0
        take = 0
        for j in range(len(friends)):
            if i != j:
                give += lst[i][j]
                take += lst[j][i]
        lst2.append(give - take)

    # 최대값 계산
    sol = [0 for i in range(len(friends))]
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i == j:
                pass
            else:
                if lst[i][j] > lst[j][i]:
                    sol[i] += 1
                elif lst[i][j] == lst[j][i]:
                    if lst2[i] > lst2[j]:
                        sol[i] += 1
                    elif lst2[i] == lst2[j]:
                        pass
                    else:
                        pass
                else:
                    pass
    return max(sol)
