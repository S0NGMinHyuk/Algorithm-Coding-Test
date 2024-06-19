def solution(n):
    answer = 0
    while n > 0:
        n, mod = divmod(n, 3)   # 몫과 나머지 저장, 3진수 방식 사용
        if mod == 0:            # 나머지가 0일 경우, 예외처리
            n, mod = n-1, 4
        
        answer = answer*10 + mod
    
    return str(answer)[::-1]    # answer를 거꾸로 출력