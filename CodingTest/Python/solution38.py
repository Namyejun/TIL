import math
<<<<<<< HEAD
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
    
=======

def solution(expressions):
    answer = []
    
    exp_map = dict()
    
    for exp in expressions:
        exp_map[exp] = ["!", "!"]
        for i in range(2, 10):
            exp_map[exp].append(chk_exp(exp, i))
    
    cand = set([2,3,4,5,6,7,8,9])
    for exp in expressions:
        tmp_cand = set()
        cand_lst = exp_map[exp]
        for i in range(len(cand_lst)):
            if cand_lst[i] == "!":
                pass
            else:
                tmp_cand.add(i)
        cand = cand & tmp_cand
    
    for exp in expressions:
        exp_lst = exp_map[exp]
        if exp[-1] == "X":
            b = "*"
            for i in cand:
                if b == "*":
                    b = exp_lst[i]
                elif b == exp_lst[i]:
                    b = exp_lst[i]
                else:
                    answer.append(exp.replace("X", "?"))
                    break
            else:
                answer.append(exp.replace("X", b))
    
    return answer
    
def chk_exp(exp, i):
    n1, op, n2, _, ans = exp.split(" ")
    
    tmp = 0
    tmp1 = 0
    tmp2 = 0
    
    for k, n in enumerate(reversed(n1)):
        if int(n) >= i:
            return "!"
        tmp1 += int(n)*math.pow(i, k)

    for k, n in enumerate(reversed(n2)):
        if int(n) >= i:
            return "!"
        tmp2 += int(n)*math.pow(i, k)
    
    if ans != "X":
        for n in ans:
            if int(n) >= i:
                return "!"

>>>>>>> c8eebc14911b24dbb90e98b5b15d144e1672f1c7
    if op == "+":
        tmp = tmp1 + tmp2
    else:
        tmp = tmp1 - tmp2
<<<<<<< HEAD
    
    tmp = int(tmp)
    
    ans = ""
    if tmp == 0: return 0
    
    while tmp != 0:
        r = tmp % n
        q = tmp // n
        ans = str(r) + ans
        tmp = q
    
    return ans
=======
        
    tmp = int(tmp)
    
    ret = ""
    if tmp == 0: return "0"
    
    while tmp != 0:
        r = tmp % i
        q = tmp // i
        ret = str(r) + ret
        tmp = q
    
    if ans == "X":
        return ret
    elif ans == ret:
        return ret
    else:
        return "!"
>>>>>>> c8eebc14911b24dbb90e98b5b15d144e1672f1c7
