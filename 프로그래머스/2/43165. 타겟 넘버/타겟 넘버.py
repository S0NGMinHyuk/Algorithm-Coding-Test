def solution(numbers, target):
    return dfs(numbers, target, 0, 0)

# DFS 알고리즘 사용
def dfs(numbers, target, index, current):
    # numbers 숫자를 사용해 target을 만들었으면 1, 아니면 0 리턴 (base case)
    if index == len(numbers):  
        return 1 if current == target else 0
    
    # 현재 인덱스 값을 더한 경우와 뺀 경우를 모두 실행 후 답 리턴
    answer = 0
    answer += dfs(numbers, target, index+1, current+numbers[index])
    answer += dfs(numbers, target, index+1, current-numbers[index])
    return answer