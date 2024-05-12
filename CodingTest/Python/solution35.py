# https://school.programmers.co.kr/learn/courses/30/lessons/92344

def solution(board, skill):
    answer = 0
    
    # 누적합 배열 선언
    # 그니까 누적합으로 하여금 skill을 압축할 수 있는 배열을 만드는 거임
    temp = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            temp[r1][c1] -= degree 
            temp[r1][c2 + 1] += degree
            temp[r2 + 1][c1] += degree
            temp[r2 + 1][c2 + 1] -= degree
        else:
            temp[r1][c1] += degree 
            temp[r1][c2 + 1] -= degree
            temp[r2 + 1][c1] -= degree
            temp[r2 + 1][c2 + 1] += degree

    # 행 방향 누적합
    for i in range(len(board) + 1):
        for j in range(1, len(board[0]) + 1):
            temp[i][j] = temp[i][j - 1] + temp[i][j]
            
    # 열 방향 누적합
    for i in range(len(board[0]) + 1):
        for j in range(1, len(board) + 1):
            temp[j][i] = temp[j - 1][i] + temp[j][i]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + temp[i][j] > 0:
                answer += 1
    return answer