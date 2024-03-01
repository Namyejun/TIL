# https://school.programmers.co.kr/learn/courses/30/lessons/118668

def solution(alp, cop, problems):
	answer = 0
	maps = [[500 for _ in range(151)] for _ in range(151)]
	maps[0][0] = 0
	plans = [[[(1, 0, 1), (0, 1, 1)] for _ in range(151)] for _ in range(151)]
	for prob in problems:
		for i in range(151):
			for j in range(151):
				if i > prob[0] and j >prob[1]:
					plans[i][j].append((prob[2], prob[3], prob[4]))
	
	for x in range(301):
		for i in range(x + 1):
			if i > 151:
				continue
	
			for j in range(x  + 1 - i):
				if j > 151:
					continue
				maps[i][j] = min()
					

	return answer