def solution(s):
    # DFS 알고리즘 사용
    return dfs(s, [0, 0])

def dfs(s, answer):
    if s == "1":        # base case
        return answer
    
    answer[0] += 1                  # 변환 횟수 증가
    length = s.count("1")           # 0 제거 후 길이
    answer[1] += len(s) - length    # 제거한 0의 개수 추가
    return dfs(intToBinary(length), answer) # 재귀호출

# 숫자 n을 이진수 문자열로 변환하는 함수
def intToBinary(n):
    stack = []
    while n >= 2:
        stack.append(str(n%2))
        n = n // 2
    stack.append(str(n))
    return "".join(stack[::-1])