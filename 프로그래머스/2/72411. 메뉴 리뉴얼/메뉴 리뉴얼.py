def solution(orders, course):
    answer = []
    
    # 각 메뉴 개수에 대해 getMenu 함수 실행
    for c in course:
        answer += getMenu(orders, c)

    # 결과를 정렬해서 출력
    return sorted(answer)

# 리스트의 모든 조합을 찾는 모듈 호출
from itertools import combinations  

def getMenu(orders, c):
    candidate = dict()      # 신메뉴 후보군
    newMenu = []            # 신메뉴 리스트
    frequency = 2           # 최소 2회 이상 등장한 메뉴
    for order in orders:
        # 해당 주문에서 가능한 모든 조합에 대해 실행
        for union in list(combinations(order, c)):  
            union = "".join(sorted(union))
            candidate[union] = 1 if union not in candidate else candidate[union]+1
            
            # 가장 많이 주문된 조합인 경우
            if candidate[union] > frequency:
                frequency = candidate[union]
                newMenu = [union]
            elif candidate[union] == frequency:
                newMenu.append(union)

    # 신메뉴 조합 리턴
    return newMenu