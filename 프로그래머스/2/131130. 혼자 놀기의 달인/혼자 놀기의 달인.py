def solution(cards):
    visited = set()     # 이미 연 상자 집합
    box = []            # 각 놀이 횟수마다 열 수 있는 상자 개수
    
    for i in range(len(cards)):     # 첫 번째 상자부터 열기
        cnt = 0
        curr = i
        while cards[curr] not in visited:   # 계속해서 열 수 있는 상자 열기
            visited.add(cards[curr])
            curr = cards[curr] - 1
            cnt += 1
        box.append(cnt)
    
    box.sort(reverse=True)          # 열 수 있는 상자 중 최대값 두개 곱하기
    return box[0]*box[1]