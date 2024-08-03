def solution(k, ranges):
    # 정적분 값을 저장하는 배열 생성
    value = []
    while k != 1:
        if k % 2 == 0:
            value.append((k*1.5) / 2)
            k /= 2
        else:
            value.append((4*k+1) / 2)
            k = k*3 + 1
    
    # 원하는 범위의 값을 result 배열에 추가
    result = []
    for r in ranges:
        if len(value)+r[1] >= r[0]: # 범위가 유효한 경우
            n = 0
            for i in range(r[0], len(value)+r[1]):
                n += value[i] 
        else:
            n = -1
        result.append(n)
    
    return result