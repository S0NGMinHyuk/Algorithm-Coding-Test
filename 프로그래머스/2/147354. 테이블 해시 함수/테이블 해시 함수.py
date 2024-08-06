def solution(data, col, row_begin, row_end):
    # 정해진 방법에 따라 튜플 정렬
    data.sort(key=lambda x: (x[col-1], -x[0]))
    
    # i번째 행의 튜플에 대해 각 컬럼의 값을 i 로 나눈 나머지들의 합을 XOR 연산
    result = 0
    for i in range(row_begin, row_end+1):
        value = 0
        for n in data[i-1]:
            value += n%i
        result ^= value
    
    # 결과 리턴
    return result
        