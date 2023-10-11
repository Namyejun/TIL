# https://school.programmers.co.kr/learn/courses/30/lessons/42626
def solution(scoville, K):
    answer = 0
    import heapq
    heapq.heapify(scoville)
    while True:
        if len(scoville) <= 1 and scoville[0] < K:
            answer = -1
            break
        if scoville:
            first = heapq.heappop(scoville)
            if first >= K:
                break
        if scoville:
            second = heapq.heappop(scoville)
        new_food = first + second * 2
        heapq.heappush(scoville, new_food)
        answer += 1
    return answer