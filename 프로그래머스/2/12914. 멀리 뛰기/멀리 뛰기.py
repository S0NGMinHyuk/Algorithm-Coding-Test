# 점화식 찾기 문제
# f(n) = f(n-1) + f(n-2)
def solution(n):
    table = { 1 : 1, 2 : 2 }
    for i in range(3, n+1):
        table[i] = (table[i-1] + table[i-2]) % 1234567
    return table[n]