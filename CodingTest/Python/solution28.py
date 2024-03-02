# https://school.programmers.co.kr/learn/courses/30/lessons/118668

def solution(alp, cop, problems):
	max_a = 0
	max_c = 0
	for problem in problems:
		max_a = max(max_a, problem[0])
		max_c = max(max_c, problem[1])
	dp = [[9999 for _ in range(max_c + 1)] for _ in range(max_a + 1)]
	
	alp = min(alp, max_a)
	cop = min(cop, max_c)
	dp[alp][cop] = 0
	for i in range(alp, max_a + 1):
		for j in range(cop, max_c + 1):
			# 문제 풀이 없이 공부하는 방법
			if i < max_a:
				dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
			if j < max_c:
				dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
			# 문제 풀이로 공부하는 방법
			for problem in problems:
				if i >= problem[0] and j >= problem[1]:
					a = min(i + problem[2], max_a)
					c = min(j + problem[3], max_c)
					dp[a][c] = min(dp[a][c], dp[i][j] + problem[-1])
					
	return dp[max_a][max_c]

# BFS로 하면 효율성 박살난대