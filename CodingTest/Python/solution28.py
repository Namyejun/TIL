# https://school.programmers.co.kr/learn/courses/30/lessons/118668

def solution(alp, cop, problems):
	maps = [[500 for _ in range(151)] for _ in range(151)]
	maps[alp][cop] = 0
	plans = [[[(1, 0, 1), (0, 1, 1)] for _ in range(151)] for _ in range(151)]
	for prob in problems:
		for i in range(151):
			for j in range(151):
				if i >= prob[0] and j > prob[1] or i > prob[0] and j >= prob[1]:
					plans[i][j].append((prob[2], prob[3], prob[4]))

	from collections import deque
	q = deque()
	q.append([alp, cop])
	mv = [[0, 1], [1, 0]]
	while q:
		x, y = q.popleft()
		
		for i, j in mv:
			nx = x + i
			ny = y + j
			if alp <= nx <= 150 and cop <= ny <= 150 and maps[nx][ny] == 500:
				lst = []
				for plan in plans[nx][ny]:
					lst.append(maps[nx - plan[0]][ny - plan[1]] + plan[2])
				maps[nx][ny] = min(lst)
				q.append([nx, ny])

	max_a = 0
	max_c = 0
	for a, c, _, _, _ in problems:
		if max_a < a:
			max_a = a
		if max_c < c:
			max_c = c
	
	answer = 999
	for i in range(max_a, 151):
		for j in range(max_c, 151):
			if answer > maps[i][j]:
				answer = maps[i][j]
	return answer

# 문제가 뭐냐면 이게 plans를 초기화 할 때 그냥 