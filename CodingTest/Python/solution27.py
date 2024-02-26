# https://school.programmers.co.kr/learn/courses/30/lessons/118667
from collections import deque
def solution(queue1, queue2):
	answer = 0
	queue1 = deque(queue1)
	queue2 = deque(queue2)
	l = len(queue1)*4
	sum1 = sum(queue1)
	sum2 = sum(queue2)
	if (sum1 + sum2) % 2 != 0:
		return -1
	while True:
		if sum1 > sum2:
			out = queue1.popleft()
			queue2.append(out)
			sum1 -= out
			sum2 += out
			answer += 1
		elif sum1 < sum2:
			out = queue2.popleft()
			queue1.append(out)
			sum2 -= out
			sum1 += out
			answer += 1
		else:
			break

		if answer == l:
			answer -= 1
			break
		
	return answer