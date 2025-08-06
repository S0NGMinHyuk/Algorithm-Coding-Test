def solution(n, cores):
    if n <= len(cores):
        return n
    
    # 이분탐색으로 n값보다 적게 작업을 진행하는 시간의 최대값(right) 구하기
    left = 0
    right = 10000 * n
    while left <= right:
        mid = (left + right) // 2
        jobs = len(cores)
        for c in cores:
            jobs += mid // c
            if jobs >= n:
                break
        
        if jobs >= n:
            right = mid-1
        else:
            left = mid+1
    
    # n값보다 적게 작업하는 시간(right)동안 작업한 총량(jobs) 구하기
    jobs = len(cores)
    for c in cores:
        jobs += right // c
    
    # right+1 시간 때 작업하는 코어 중 n번째 작업을 하는 코어 번호를 리턴
    for i in range(len(cores)):
        if (right+1) % cores[i] == 0: # 작업을 하는 코어인 경우
            jobs += 1
            if jobs == n:
                return i+1