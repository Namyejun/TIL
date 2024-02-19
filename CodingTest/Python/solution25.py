# https://school.programmers.co.kr/learn/courses/30/lessons/258707

def solution(coin, cards):
    answer = 0
    deck = set()
    A = cards[:len(cards)//3]
    B = cards[len(cards)//3:]
    # 가진 덱에 짤 수 있는 조합이 있는지 확인하고
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == len(cards) + 1 and A[i] not in deck and A[j] not in deck:
                deck.add(A[i])
                deck.add(A[j])
                answer += 1
    # 없으면 A랑 B랑 조합해서 있는지 확인하고
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] + B[j] == len(cards) + 1 and A[i] not in deck and B[j] not in deck and coin >= 1:
                deck.add(A[i])
                deck.add(B[j])
                answer += 1
                coin -= 1   
    # 그것 마저 없다면 B만 가지고 확인
    for i in range(len(B)):
        for j in range(i + 1, len(B)):
            if B[i] + B[j] == len(cards) + 1 and B[i] not in deck and B[j] not in deck and coin >= 2:
                deck.add(B[i])
                deck.add(B[j])
                answer += 1
                coin -= 2
        
    return answer