def solution(n, left, right):
    # num 자리의 숫자는 행과 열 중 더 큰 값 + 1이다.
    return [1+max(num//n, num%n) for num in range(left, right+1)]