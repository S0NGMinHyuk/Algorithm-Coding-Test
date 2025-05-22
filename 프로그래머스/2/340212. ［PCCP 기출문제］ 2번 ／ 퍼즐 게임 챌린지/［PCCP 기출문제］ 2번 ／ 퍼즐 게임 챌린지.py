def solution(diffs, times, limit):
    left, right = 1, max(diffs)
    while(left <= right):   # 이진탐색으로 최소 level 찾기
        if left == right: break
        mid = (left + right) // 2
        if isPossible(diffs, times, limit, mid):
            right = mid
        else:
            left = mid+1
    return left


def isPossible(diffs, times, limit, level): # 현재 레벨로 깰 수 있는지 여부 리턴
    total = 0
    for i in range(len(diffs)):
        if total > limit: break # 이미 못깨는 경우 break
        
        # 문제당 소요시간 업데이트
        if diffs[i] <= level:
            total += times[i]
        else:
            total += (diffs[i] - level) * (times[i] + times[i-1]) + times[i]
    
    return total <= limit # 깰 수 있는지 여부 리턴