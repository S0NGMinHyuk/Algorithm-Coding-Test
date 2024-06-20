def solution(n, s):
    if n > s:   # 최고의 집합 생성 불가 조건
        return [-1]
    
    # 최고의 집합 생성 방법
    answer = [s//n] * n 
    for i in range(s-sum(answer)):
        answer[i] += 1
    
    # 오름차순으로 리턴
    return answer[::-1]