# 레벨 3 - n+1 카드게임
def solution(coin, cards):
    answer = 1
    origin_hands = set(cards[:len(cards)//3])
    add_hands = set()
    idx = len(cards)//3

    while 1:
        if idx >= len(cards):
            break
        add_hands.add(cards[idx])
        add_hands.add(cards[idx+1])
        idx += 2

        isFound = False
        if len(origin_hands) > 0:
            for num in origin_hands:
                if len(cards)-num+1 in origin_hands:
                    origin_hands.discard(num)
                    origin_hands.discard(len(cards)-num+1)
                    answer += 1
                    isFound = True
                    break
        else:
            break
        
        if isFound:
            continue

        if len(add_hands) > 0 and coin >= 1:
            for num in origin_hands:
                if len(cards)-num+1 in add_hands:
                    origin_hands.discard(num)
                    add_hands.discard(len(cards)-num+1)
                    coin -= 1
                    answer += 1
                    isFound = True
                    break
        if isFound:
            continue
        
        if len(add_hands) > 0 and coin >= 2:
            for num in add_hands:
                if len(cards)-num+1 in add_hands:
                    add_hands.discard(num)
                    add_hands.discard(len(cards)-num+1)
                    coin -= 2
                    answer += 1
                    isFound = True
                    break
        if isFound:
            continue

        break

    return answer