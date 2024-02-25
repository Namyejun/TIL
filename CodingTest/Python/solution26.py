# https://school.programmers.co.kr/learn/courses/30/lessons/258705

def solution(n, tops):
	lst = [0 for i in range(len(tops)*2 + 2)] # 0 1 2 3 4 5 6 7 8 9
	dp = [1,1]
	for i in range(len(tops)):
		lst[2*i+2] = tops[i] # 0 1 2 3
	for i in range(2, len(lst)):
		if lst[i] == 1:
			dp.append((dp[i-1]*2 + dp[i-2])%10007)
		else:
			dp.append((dp[i-1] + dp[i-2])%10007)
	return dp[-1]%10007