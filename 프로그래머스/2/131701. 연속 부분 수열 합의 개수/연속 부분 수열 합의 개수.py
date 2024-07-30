# 재귀가 너무 깊으면 런타임 에러가 뜰 수 있다.
import sys
sys.setrecursionlimit(1000000)

def solution(elements):
    result = set()
    # 각 숫자를 시작으로 순열 생성
    for i in range(len(elements)):
        result |= set(dfs(elements, i, []))
    
    return len(result)

def dfs(arr, start, result):
    # Base Case / 연속순열을 한 바퀴 돈 경우
    if len(result) == len(arr):
        return result
    
    start %= len(arr)
    result.append(result[-1]+arr[start] if len(result) > 0 else arr[start])
    return dfs(arr, start+1, result)