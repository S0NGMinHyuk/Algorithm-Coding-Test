# 투포인터 알고리즘 사용
def solution(gems):
    TOTAL = len(set(gems))  # 전체 보석 개수
    answer = None           # 정답 배열
    start, end = 0, 0       # 투포인터 시작값
    
    # 첫 번째 원소를 가진 채 시작
    hand = {gems[end]: 1}
    
    while end < len(gems):
        # 보석이 부족하면 end 다음 보석을 구매하기
        if len(hand) < TOTAL:       
            end += 1
            if end == len(gems):    # 반복문 종료조건
                break
            
            # 보석 구매 후 hand에 추가
            hand[gems[end]] = 1 if gems[end] not in hand else hand[gems[end]]+1  
        # 보석이 모두 있으면 start 보석을 판매하기
        else:                    
            # 현재가 가장 조금 구매하는 경우라면 answer 갱신
            if answer == None or end-start < answer[1]-answer[0]:
                answer = [start+1, end+1]
            
            # start 위치의 보석을 판매하고, 같은 종류의 보석이 없으면 key 삭제
            hand[gems[start]] -= 1
            if hand[gems[start]] == 0:
                hand.pop(gems[start])
            
            start += 1
    
    return answer 