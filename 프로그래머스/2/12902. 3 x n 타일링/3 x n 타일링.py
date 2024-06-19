def solution(n):    # 점화식 찾기 문제
    lst = [0]*5001  # 미리 배열 생성
    lst[2] = 3      # 배열 초기값 설정
    lst[4] = 11
    
    if n % 2 == 0:  # n이 짝수인 경우에만
        for i in range(6, n+1, 2):
            lst[i] = (lst[i-2]*4 - lst[i-4] + 1000000007) % 1000000007
            # lst[i-2]*4 보다 lst[i-4]가 더 큰 경우를 방지하기 위해 1000000007을 더함
    
    return lst[n]