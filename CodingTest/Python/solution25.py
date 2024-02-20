# https://school.programmers.co.kr/learn/courses/30/lessons/258707

def solution(coin, cards):
    answer = 1
    deck = set()
    A = cards[:len(cards)//3]
    B_lst = cards[len(cards)//3:]
    B = []
    round = 1
    for i in range(0, len(B_lst), 2):
        round += 1
        B.append(B_lst[i])
        B.append(B_lst[i + 1])
        t = False
        # 가진 덱에 짤 수 있는 조합이 있는지 확인하고
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] + A[j] == len(cards) + 1 and A[i] not in deck and A[j] not in deck:
                    deck.add(A[i])
                    deck.add(A[j])
                    answer += 1
                    t = True
                    break
            if t:
                break
        if t:
            continue
        # 없으면 A랑 B랑 조합해서 있는지 확인하고
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] + B[j] == len(cards) + 1 and A[i] not in deck and B[j] not in deck and coin >= 1:
                    deck.add(A[i])
                    deck.add(B[j])
                    answer += 1
                    coin -= 1
                    t = True
                    break
            if t:
                break
        if t:
            continue
        # 그것 마저 없다면 B만 가지고 확인
        for i in range(len(B)):
            for j in range(i + 1, len(B)):
                if B[i] + B[j] == len(cards) + 1 and B[i] not in deck and B[j] not in deck and coin >= 2:
                    deck.add(B[i])
                    deck.add(B[j])
                    answer += 1
                    coin -= 2
                    t = True
                    break
            if t:
                break
        if t:
            continue
        if round > answer:
            break
    return answer