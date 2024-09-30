import math
import copy
def solution(expressions):
    answer = []
    
    for exp in expressions:
        exp = exp.split(" ")
        n1, op, n2, ans = exp[0], exp[1], exp[2], exp[4]
        tmp_cand = set()
        if ans == "X":
            tmp_cand = find_cand(n1) & find_cand(n2)
        else:
            tmp_cand = find_cand(n1) & find_cand(n2) & find_cand(ans)
            tmp_cand2 = copy.deepcopy(tmp_cand)
            for i in tmp_cand:
                if calc_nmal(n1, op, n2, i) != ans:
                    tmp_cand2.remove(i)
            tmp_cand = tmp_cand2
            
        print(tmp_cand)
                
        

def find_cand(n):
    cand = set()
    if n == "X":
        return set([i for i in range(2, 10)])
    else:
        return_val = set()
        for i in n:
            return_val.add(int(i))
        return return_val
        
def calc_nmal(n1, op, n2, n):
    tmp = 0

    tmp1 = 0
    for i, j in enumerate(reversed(n1)):
        tmp1 += int(j)*math.pow(n, i)
    
    tmp2 = 0
    for i, j in enumerate(reversed(n2)):
        tmp2 += int(j)*math.pow(n, i)
    
    if op == "+":
        tmp = tmp1 + tmp2
    else:
        tmp = tmp1 - tmp2
    
    tmp = int(tmp)
    
    ans = ""
    if tmp == 0: return 0
    
    while tmp != 0:
        r = tmp % n
        q = tmp // n
        ans = str(r) + ans
        tmp = q
    
    return ans
