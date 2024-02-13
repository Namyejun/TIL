# https://school.programmers.co.kr/learn/courses/30/lessons/258707

def solution(coin, cards):
    answer = 0
    
    idx_of_cards = [i for i in range(len(cards))]
    pair_of_cards = [(len(cards) - i + 1) for i in cards]
    idx_of_pairs = []
    for i in range(len(pair_of_cards)):
        for j in range(len(cards)):
            if pair_of_cards[i] == cards[j]:
                idx_of_pairs.append(j)
    
    print(cards)
    print(pair_of_cards)
    print()
    print(idx_of_cards)
    print(idx_of_pairs)

    deck = cards[:len(cards)//3]

    return answer