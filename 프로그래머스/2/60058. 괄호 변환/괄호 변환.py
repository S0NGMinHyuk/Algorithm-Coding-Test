def solution(p):
    answer = dfs(p) # 재귀함수 호출
    return answer

def dfs(p):
    # 입력이 빈 문자열일 경우, 빈 문자열을 반환
    if p == "":
        return p
    
    count = 0
    index = 0
    while index < len(p):
        count += 1 if p[index] == "(" else -1      
        if count == 0:  # 최초의 균형잡힌 괄호 문자열
            index += 1
            break
        index += 1
    
    u, v = p[:index], p[index:] # 문자열 p를 u와 v로 분할
    if isPerfect(u):            # u가 올바른 괄호 문자열인 경우
        return u + dfs(v)
    else:                       # u가 올바른 괄호 문자열이 아닌 경우
        return "(" + dfs(v) + ")" + convert_U(u)

# u가 올바른 괄호 문자열인지 검사하는 함수    
def isPerfect(u):
    stack = []
    for i in u:
        if i == "(":
            stack.append("(")
        elif i == ")" and len(stack) > 0:
            stack.pop()
        else:
            return False
        
    return True

# 4번 과정을 거친 u를 반환하는 함수
def convert_U(u):
    answer = ""
    for i in range(1, len(u)-1):
        answer += "(" if u[i] == ")" else ")"
    return answer