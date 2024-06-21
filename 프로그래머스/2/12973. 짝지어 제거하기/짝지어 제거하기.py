# 스택 알고리즘 사용
def solution(s):
    stack = []
    for alphabet in s:
        # 앞의 알파벳과 다른 알파벳이면 스택에 추가
        if len(stack) == 0 or stack[-1] != alphabet:
            stack.append(alphabet)
        else:
            stack.pop() # 앞의 알파벳과 같으면 스택에서 제거
    
    return 0 if len(stack) else 1