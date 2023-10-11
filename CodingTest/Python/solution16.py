# https://school.programmers.co.kr/learn/courses/30/lessons/42627
def solution(jobs):
    answer = 0
    import heapq
    jobs.sort()
    print(jobs)
    cnt = len(jobs)
    time = 0
    temp = []
    while True:
        while jobs and time >= jobs[0][0]:
            at, rt = jobs.pop(0)
            heapq.heappush(temp, (rt, at))
        if temp:
            rt, at = heapq.heappop(temp)
            answer += (time - at + rt)
            time += rt
        else:
            time += 1

        if not jobs and not temp:
            break
    return answer // cnt