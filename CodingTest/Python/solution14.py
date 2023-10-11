# https://school.programmers.co.kr/learn/courses/30/lessons/42839
def solution(numbers):
    answer = 0
    # lst = [i for i in range(2, 10000000)]
    # for i in range(3200):
    #     for j in range(2, 3200):
    #         if i*j > 9999999:
    #             break
    #         if i*j in lst:
    #             lst.remove(i*j)
        
    lst = set()
    from itertools import permutations
    import math
    for i in range(1, len(numbers) + 1):
        temp = permutations(numbers, i)
        for t in temp:
            lst.add(int("".join(t)))
    
    for i in lst:
        b = True
        if i >= 2:
            for j in range(2, int(math.sqrt(i)) + 3):
                if i == j:
                    break
                else:
                    if i % j == 0:
                        b = False
                        break
                    else:
                        continue
        else:
             b = False           
        if b:
            print(i)
            answer += 1
            
                    
                
    return answer