def solution(A,B):
    answer = 0
    A.sort()                # A를 오름차순으로 정렬
    B.sort(reverse=True)    # B를 내림차순으로 정렬
    for a, b in zip(A, B):  # A와 B의 같은 인덱스 자리 값을 곱해서 추가
        answer += a*b
    return answer