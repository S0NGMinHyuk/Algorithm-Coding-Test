def solution(n, k):
    cnt = 0     # 소수 개수
    temp = 0    # 변환된 숫자 내 임시 숫자 변수
    for num in convert(n, k):
        if num > 0:                 # 0이 아니면 temp값 뒤에 추가
            temp = temp*10 + num
        else:                       # 0이면 소수인지 검사 후 temp 초기화
            cnt += isPrime(temp)
            temp = 0
    else:
        cnt += isPrime(temp)        # 마지막 값에 대해서도 소수 검사 후 리턴
        
    return cnt

# 정수 n을 k진수 배열로 변환하는 함수
def convert(n, k):
    stack = []
    while n > 0:
        n, rest = divmod(n, k)
        stack.append(rest)
    return stack[::-1]

# 정수 n이 소수인지 판별하는 함수
def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return 0
    return 1 if n > 1 else 0