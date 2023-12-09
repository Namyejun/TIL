# https://school.programmers.co.kr/learn/courses/30/lessons/150367
import sys
sys.setrecursionlimit(10000)
def solution(numbers):
    answer = []
    for number in numbers:
        bin_num = str(bin(number)[2:])
        con = 1
        while len(bin_num) > 2**con - 1:
            con += 1
        
        bin_tree = '0'*(2**con - 1 - len(bin_num))+bin_num
        
        
        if chk_valid(bin_tree) == "T":
            answer.append(1)
        else:
            answer.append(0)

    return answer

def chk_valid(bin_tree):
    if bin_tree == "0":
        return "F"
    if bin_tree == "1":
        return "T"
    
    if len(bin_tree) == 3:
        if bin_tree[1] == '0':
            if bin_tree[0] == '0' and bin_tree[2] == '0':
                return "ALL_ZERO"
            else:
                return "F"
        else:
            return "T"
    
    if bin_tree[len(bin_tree)//2] == "0":
        if chk_valid(bin_tree[:len(bin_tree)//2]) == "ALL_ZERO" and chk_valid(bin_tree[len(bin_tree)//2 + 1:]) == "ALL_ZERO":
            return "ALL_ZERO"
        else:
            return "F"
    else:
        if chk_valid(bin_tree[:len(bin_tree)//2]) == "F" or chk_valid(bin_tree[len(bin_tree)//2 + 1:]) == "F":
            return "F"
        else:
            return "T"
    
    