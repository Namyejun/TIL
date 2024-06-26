from typing import Tuple
moves = [(0, 1), (-1, 0), (1, 0), (0, -1)]

def game(board, aloc, bloc,)-> Tuple[bool, int]:
    game_results = []
    
    if board[bloc[0]][bloc[1]] == 0:
        return True, 0
    if board[aloc[0]][aloc[1]] == 0:
        return False, 0
    
    for move in moves:
        next_aloc = (aloc[0]+move[0], aloc[1]+move[1])        
        try:
            if next_aloc[0] < 0 or next_aloc[1] < 0 :
                raise IndexError
            next_board = board[next_aloc[0]][next_aloc[1]]
        except IndexError:
            continue
        
        if next_board == 1:
            board[aloc[0]][aloc[1]] = 0
            win, game_length = game(board, bloc, next_aloc) # 다음 착수의 결과를 가져옴
            board[aloc[0]][aloc[1]] = 1 # 이런 스킬을 못쓰겠음;
            game_results.append((not win, game_length+1)) # 다음 착수의 결과는 이전 수와 a, b 위치가 바뀌므로 not 붙음
    
    if len(game_results) == 0: # 움직일 곳이 없으면
        return False, 0
    elif any(r[0] for r in game_results): # 하나라도 이기는 구석이 있으면 이긴다고 반환하고 가장 빨리 이기는 루트로
        return True, min(r[1] for r in game_results if r[0])
    else: # 이길 구석이 없으면 못이긴다고 하고 최대한 늦게 죽도록
        return False, max(r[1] for r in game_results)

def solution(board, aloc, bloc):
    return game(board, aloc, bloc)[1]