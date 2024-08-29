def solution(scores):
    result = 0
    wanho = scores[0]

    # 첫번째 점수에 대해서 내림차순, 두 번째 점수에 대해서 오름차순으로 정렬
    scores.sort(key=lambda x: (-x[0], x[1]))
    maxb = 0
    
    for a, b in scores:
        if wanho[0] < a and wanho[1] < b:
            return -1
        
        if b >= maxb:
            maxb = b
            if a + b > sum(wanho):
                result += 1
            
    return result+1