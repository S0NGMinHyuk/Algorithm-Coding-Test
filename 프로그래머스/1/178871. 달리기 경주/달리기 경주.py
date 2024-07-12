def solution(players, callings):
    # 선수 이름 : 순위 정보를 가진 딕셔너리
    ranks = {players[i]: i for i in range(len(players))}
    
    for call in callings:
        pos = ranks[call]           # 불린 선수의 기존 순위
        front = players[pos-1]      # 불린 선수 앞의 선수 이름
        
        # players 배열에서 두 선수의 순서 변경, 두 선수의 순위도 변경
        players[pos], players[pos-1] = players[pos-1], players[pos]
        ranks[call] -= 1
        ranks[front] += 1
        
    return players