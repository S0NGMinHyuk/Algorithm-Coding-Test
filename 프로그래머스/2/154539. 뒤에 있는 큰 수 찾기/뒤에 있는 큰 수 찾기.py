def solution(numbers):
    result = [-1]*len(numbers)
    stack = []  # 스택 알고리즘 사용

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:    # 앞의 숫자보다 큰 수일 경우
            result[stack.pop()] = numbers[i]

        stack.append(i) # 스택에 추가

    return result