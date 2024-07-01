# 스택 알고리즘 사용
def solution(prices):
    answer = [0] * len(prices)          # 정답 리스트
    stack = [0]                         # 0번째 인덱스 값 저장
    for i in range(1, len(prices)):     # 1번째 인덱스부터 n-1 인덱스까지 반복
        while len(stack) > 0 and prices[stack[-1]] > prices[i]: # 내 가격보다 떨어진 경우
            answer[stack[-1]] = i - stack[-1]                   # answer 배열의 해당 인덱스값 변경
            stack.pop()                                         # stack에서 제거
        stack.append(i)
    for i in stack:                     # stack에 남은 인덱스는 끝까지 살아남은 주식 가격
        answer[i] = len(prices) - i - 1 # answer 배열의 해당 인덱스값 변경
    
    return answer