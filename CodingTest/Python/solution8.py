# https://school.programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    answer = True
    min_len = 20
    lst = {}
    phone_book.sort(key = lambda x : len(x))
    for num in phone_book:
        min_len = min(min_len, len(num))
        for i in range(min_len, len(num) + 1):
            if num[0:i] in lst.keys():
                return False
        else:
            lst[num] = 0
    return answer