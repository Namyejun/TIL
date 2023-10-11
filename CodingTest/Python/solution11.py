# https://school.programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
    answer = []
    for i in range(len(prices)):
        time = 0
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                time += 1
                answer.append(time)
                break
            else:
                time += 1
        else:
            answer.append(time)
    return answer