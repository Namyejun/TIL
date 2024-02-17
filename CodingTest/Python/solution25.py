# https://school.programmers.co.kr/learn/courses/30/lessons/258707

def solution(coin, cards):
    answer = 1
    
    idx_of_cards = [i for i in range(len(cards))]
    pair_of_cards = [(len(cards) - i + 1) for i in cards]
    idx_of_pairs = []
    for i in range(len(pair_of_cards)):
        for j in range(len(cards)):
            if pair_of_cards[i] == cards[j]:
                idx_of_pairs.append(j)

    dist = []
    for i in range(len(cards)): # 각 짝과의 거리를 저장하는 배열
        dist.append(idx_of_pairs[i] - idx_of_cards[i])

    print(dist)

    couple = 0 # 제출할 수 있는 짝의 수
    deck = set() # 현재 보유하고 있는 카드
    for i in range(len(cards)//3): # 1/3 전에 애들
        deck.add(i) # 카드 획득
        if dist[i] < 0: # 이전에 짝이 있으면 실행
            deck.remove(i)
            deck.remove(i + dist[i])
            couple += 1

    for i in range(len(cards)//3, len(cards)): # 1/3 이후
        pass
        

    return answer