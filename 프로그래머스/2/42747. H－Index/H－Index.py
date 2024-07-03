def solution(citations):
    citations.sort(reverse=True)    # 내림차순으로 정렬
    answer = 0
    if len(citations) == 1:         # 논문이 1개인 경우 예외처리
        if citations[0] > 0:
            answer = 1
    
    for i in range(len(citations)):
        if citations[i] == i+1:     # i+1회 인용된 논문이 i+1개인 경우
            answer = i+1
            break
        elif citations[i] < i+1:    # i회 이상 인용된 논문이 i개인 경우
            answer = i
            break
        else:
            None
    else:                           # 논문의 최소 인용 횟수가 논문 개수보다 큰 경우
        answer = len(citations)        
    return answer