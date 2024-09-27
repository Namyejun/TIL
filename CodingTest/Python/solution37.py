def solution(diffs, times, limit):
    answer = 0
    
    low = 1
    high = 100000;
    
    while True:
        mid = (low + high) // 2
        if low >= high:
            if calc_cost(diffs, times, mid) <= limit:
                answer = mid
            break
        else: 
            if calc_cost(diffs, times, mid) <= limit:
                answer = mid
                high = mid
            else:
                low = mid + 1
    return answer
    
    
def calc_cost(diffs, times, level):
    cost = 0
    for i in range(0, len(diffs)):
        if diffs[i] <= level:
            cost += times[i]
        else:
            cost += (diffs[i] - level) * (times[i] + times[i - 1]) + times[i]
    
    return cost
