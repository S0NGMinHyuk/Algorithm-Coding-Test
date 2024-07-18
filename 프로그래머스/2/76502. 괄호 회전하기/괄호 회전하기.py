# 선입선출 큐 사용
from collections import deque

def solution(s):
    answer = 0
    s = deque(list(s))
    
    # 괄호 문자열을 회전시키며 올바른 괄호 문자열이면 answer 1 증가
    for _ in range(len(s)):
        if isCorrect(s):
            answer += 1
        s.appendleft(s.pop())

    return answer

# 괄호문자열 s가 올바른 괄호문자열인지 검사하는 함수. stack 자료구조 사용
def isCorrect(s):
    stack = []
    for char in s:
        if char == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                return False
        elif char == "}":
            if len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            else:
                return False
        elif char == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                return False
        # 왼쪽 괄호 종류인 경우
        else:   
            stack.append(char)
            
    # 반복문을 통과하고 스택이 비어있으면 올바른 괄호 문자열
    return len(stack) == 0