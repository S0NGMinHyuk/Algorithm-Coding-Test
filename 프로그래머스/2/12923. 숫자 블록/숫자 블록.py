def solution(begin, end):
    answer = [0] * (end-begin+1)    # 정답 배열 생성
    
    for n in range(begin, end+1):
        k = 0 if n == 1 else 1      # 초기값 설정
        
        # 10**7 이내의 가능한 블록을 찾기
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                if n//i <= 10**7:
                    k = n//i
                    break
                else:
                    k = i
                    
        answer[n-begin] = k         # 값 저장
        
    return answer