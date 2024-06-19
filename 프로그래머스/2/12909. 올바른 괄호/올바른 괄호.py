def solution(s):
    stack = []
    for i in s:
        if i == "(":    # 오른쪽 괄호면 stack에 추가
            stack.append(i)
        else:           # 왼쪽 괄호면 stack에서 오른쪽 괄호 하나 제거
            if len(stack) > 0:
                stack.pop()
            else:
                return False    # 스택이 비어있다면 잘못된 문자열인 경우
    
    # for문 종료 후 stack이 비어있다면 True, 아니라면 False 리턴
    return True if len(stack) == 0 else False