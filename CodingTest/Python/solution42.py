def solution(bandage, health, attacks):
    answer = 0
    
    current = [0, health, 0]
    time = [0 for i in range(1001)]
    for t, d in attacks:
        time[t] = d
    
    for i in range(1, attacks[-1][0] + 1):
        current[0] += 1
        current[2] += 1
        
        if time[i] != 0:
            current[1] -= time[i]
            if current[1] <= 0:
                return -1
            current[2] = 0
        else:
            heal = 0
            if current[2] == bandage[0]:
                heal = bandage[2] + bandage[1]
                current[2] = 0
            else:
                heal = bandage[1]
            if current[1] + heal >= health:
                current[1] = health
            else:
                current[1] += heal
    answer = current[1]
    return answer