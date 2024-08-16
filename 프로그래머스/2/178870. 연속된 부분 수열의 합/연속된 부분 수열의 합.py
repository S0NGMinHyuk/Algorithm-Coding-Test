# 투포인터 알고리즘 사용
def solution(sequence, k):
    result = None           # 결과값
    left, right = 0, 0      # 투포인터 인덱스 / 시작값 0, 0
    total = sequence[0]     # 시작값
    
    while True:    
        if total > k:
            total -= sequence[left]
            left += 1
        else:
            if total == k and (result == None or right-left < result[1]-result[0]):
                result = [left, right]
            
            right += 1
            if right == len(sequence):
                break
            total += sequence[right]
    
    return result