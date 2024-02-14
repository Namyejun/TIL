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
    
    print(cards)
    print(pair_of_cards)
    print()
    print(idx_of_cards)
    print(idx_of_pairs)

    card_set = set()
    submit = 0
    

    for i in range(len(cards)):
        if i < len(cards)//3:
            if pair_of_cards[i] in card_set: # 같은 짝이 패에 있을 때 제출목록으로 넘김
                card_set.pop(pair_of_cards[i])
                submit += 1
            else:
                card_set.add(cards)
        else:


            if i % 2 == 1 and submit > 0:
                submit -= 1
                answer += 1
            else:
                break

    return answer