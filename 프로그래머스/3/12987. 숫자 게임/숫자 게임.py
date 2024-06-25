def solution(A, B):
    A.sort() ; B.sort()
    a, b = 0, 0 # A 리스트와 B 리스트의 인덱스값
    win = 0     # 승점

    while b < len(B):
        if A[a] < B[b]: # A의 최소값이 B의 최소값보다 작은 경우 B의 승점 1 추가
            a += 1 ; b += 1
            win += 1
        else:
            b += 1
    
    return win