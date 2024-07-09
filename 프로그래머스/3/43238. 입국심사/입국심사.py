def solution(n, times):
    # 이분탐색 알고리즘 사용
    left = 0
    right = n*min(times)
    result = 0

    while left <= right:
        mid = (left+right)//2
        waitingMen = n  # 입국심사를 기다리는 사람들

        for time in times:
            waitingMen -= mid//time # 각 심사관이 mid 시간동안 응대할 수 있는 고객 수 차감
            if waitingMen <= 0:     # 모든 고객이 mid 시간 내에 입국심사를 끝낸 경우
                break
        
        if waitingMen > 0:  # mid 시간이 부족한 경우
            left = mid+1
        else:               # mid 시간이 충분한 경우
            right = mid-1
            result = mid
    
    return result