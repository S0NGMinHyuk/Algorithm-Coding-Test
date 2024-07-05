# 스택  /   탐욕 알고리즘 사용
def solution(number, k):
    maxStack = len(number)-k  # stack의 최종 길이
    stack = []
    for n in number:
        # 내 앞의 자리 수가 나보다 작으면 제거 <- 위 내용만 지키기
        while len(stack) > 0 and k > 0 and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
    
    # number가 역순인 경우를 위해 슬라이싱
    return "".join(stack[:maxStack])