import math

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

    if op == "+":
        tmp = tmp1 + tmp2
    else:
        tmp = tmp1 - tmp2

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