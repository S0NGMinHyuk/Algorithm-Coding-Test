# 선입선출 자료구조 사용
from collections import deque

def solution(expression):
    expression = strToExpr(expression)  # 문자열 식을 숫자와 연산자를 원소로 하는 리스트로 변환
    operator = deque(["+", "-", "*"])
    answer = dfs(expression, operator)  # DFS 알고리즘 사용
    return answer

# 재귀호출 알고리즘
def dfs(expr, operator):
    if len(expr) == 1:  # Base Case. 계산 결과의 절대값을 리턴
        return abs(expr[0])
    else:
        answer = 0      # 남은 연산자 중 맨 앞의 연산자를 우선순위로 재귀호출
        for _ in range(len(operator)):
            oper = operator.popleft()               # 맨 앞의 연산자
            temp_expr = calculate(list(expr), oper) # 맨 앞의 연산자를 우선순위로 수식 계산
            answer = max(answer, dfs(temp_expr, operator))  # 재귀 호출 및 최대값을 저장
            operator.append(oper)       # 맨 앞 연산자를 뒤에 다시 추가
    
    return answer

# expr 리스트에서 oper 연산자를 계산한 수식 리스트를 반환하는 함수
def calculate(expr, oper):
    i = 0
    while i < len(expr):
        if expr[i] == oper:
            if oper == "+":
                expr[i-1] += expr[i+1]
            elif oper == "-":
                expr[i-1] -= expr[i+1]
            elif oper == "*":
                expr[i-1] *= expr[i+1]
            expr = expr[:i] + expr[i+2:]
        else:
            i += 1
    return expr
            
# 문자열 식을 숫자와 연산자를 원소로 하는 리스트로 변환하는 함수
def strToExpr(s):
    lst = []
    operator = 0
    for i in range(len(s)):
        if not s[i].isdigit():  # 현재 인덱스값이 연산자인 경우
            lst.append(int(s[operator:i]))
            lst.append(s[i])
            operator = i + 1
    else:                       # 마지막 숫자값 추가
        lst.append(int(s[operator:]))
    
    return lst