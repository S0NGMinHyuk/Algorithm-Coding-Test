def solution(n, t, m, p):
    # m명이 t번 외칠 수 있는 길이만큼 숫자를 n진수 문자열로 변환
    result = ''
    num = 0
    while len(result) < m*t:    
        result += changeNum(num, n)
        num += 1

    # 만들어놓은 result 문자열에서 내 차례 값만 따로 모아서 리턴
    answer = ''
    for i in range(t):
        answer += result[i*m+p-1]
    return answer

# 숫자 num을 n진수 문자열로 변환하는 함수
def changeNum(num, n):
    number = "0123456789ABCDEF"
    stack = []
    while num >= n:
        num, mod = divmod(num, n)
        stack.append(mod)

    answer = number[num]
    for i in stack[::-1]:
        answer += number[i]
    
    return answer