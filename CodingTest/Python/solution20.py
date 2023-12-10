# https://school.programmers.co.kr/learn/courses/30/lessons/150366
def solution(commands):
    answer = []
    table = {}

    for r in range(1, 51):
        for c in range(1, 51):
            table[(r, c)] = ""

    for command in commands:
        print(command)
        c = list(command.split())
        if c[0] == "UPDATE":
            if len(c[1:]) == 3:
                update1(table, int(c[1]), int(c[2]), c[3])
            elif len(c[1:]) == 2:
                update2(table, c[1], c[2])
        elif c[0] == "MERGE":
            merge(table, int(c[1]), int(c[2]), int(c[3]), int(c[4]))
        elif c[0] == "UNMERGE":
            unmerge(table, int(c[1]), int(c[2]))    
        elif c[0] == "PRINT":
            return_val = print_str(table, int(c[1]), int(c[2]))
            if return_val == "":
                return_val ="EMPTY"
            answer.append(return_val)

    return answer

def update1(table, r, c, value):
    for merge_idx in table.keys():
        if (r, c) in merge_idx or (r, c) == merge_idx:
            table[merge_idx] = value
            break
    
def update2(table, value1, value2):
    for key in table.keys():
        if table[key] == value1:
            table[key] = value2

def merge(table, r1, c1, r2, c2):
    if r1 == r2 and c1 == c2:
        return
    key1 = (r1, c1)
    key2 = (r2, c2)
    for key in table.keys():
        if (r1, c1) in key or (r1, c1) == key:
            key1 = key
        if (r2, c2) in key or (r2, c2) == key:
            key2 = key
    if key1 == key2:
        return
    r1_c1_str = table.pop(key1)
    r2_c2_str = table.pop(key2)
    result_str = ""
    if len(r1_c1_str) != 0:
        result_str = r1_c1_str
    elif len(r2_c2_str) != 0:
        result_str = r2_c2_str
    else:
        pass
    
    lst = []
    if type(key1[0]) == type((3,4)):
        for key in key1:
            lst.append(key)
    else:
        lst.append(key1)
    if type(key2[0]) == type((3,4)):
        for key in key2:
            lst.append(key)
    else:
        lst.append(key2)
    key = tuple(lst)
    table[key] = result_str

def unmerge(table, r, c):
    keys = table.keys()
    for key in keys:
        if (r, c) in key:
            result_str = table.pop(key)
            for x, y in key:
                table[(x, y)] = ""
                if x == r and y == c:
                    table[(x, y)] = result_str
            break

def print_str(table, r, c):
    for key in table.keys():
        if (r, c) in key or (r, c) == key:
            return table[key]
            