# https://school.programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    time = 0
    total = sum(truck_weights)
    while total != 0:
        if truck_weights and sum(bridge[:-1]) + truck_weights[0] <= weight:
            temp = truck_weights.pop(0)
            total -= bridge.pop()
            bridge = [temp] + bridge
            time += 1
        else:
            idx = 0
            for i in reversed(range(bridge_length)):
                if bridge[i] != 0:
                    idx = i
                    break
            total -= bridge[idx - bridge_length]
            bridge = [0 for _ in range(bridge_length - idx)] + bridge[:idx - bridge_length]
            if truck_weights and sum(bridge) + truck_weights[0] <= weight:
                bridge[0] = truck_weights.pop(0)
            time += bridge_length - idx
    answer = time
    return answer