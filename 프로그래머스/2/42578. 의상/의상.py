def solution(clothes):
    closet = dict()     # 해시 자료구조 사용
    for cloth, body in clothes: # 옷의 종류별 개수를 저장
        if body in closet:
            closet[body] += 1
        else:
            closet[body] = 1
    
    # 옷 종류별로 입거나 안입거나 선택할 수 있으므로 value+1을 곱한다.
    answer = 1
    for value in closet.values():
        answer *= value+1
    
    return answer-1     # 모든 종류의 옷을 안입는 경우의 수를 빼고 리턴