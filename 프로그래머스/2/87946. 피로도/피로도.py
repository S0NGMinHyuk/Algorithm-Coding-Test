def solution(k, dungeons):
    return dfs(k, dungeons, set())  # DFS 알고리즘 사용


def dfs(hp, stages, clear):
    if len(stages) == 0:    # Base Case
        return len(clear)   # 모든 던전을 클리어한 경우, 클리어한 던전 개수 리턴
    
    result = len(clear)
    for i in range(len(stages)):
        # 깨지 않은 맵 중 깰 수 있는 맵에 대해 재귀 실행
        if i not in clear and hp >= stages[i][0]:
            result = max(result, dfs(hp-stages[i][1], stages, clear|{i}))
    
    # 현재 재귀함수에서 가장 많이 깬 맵 개수를 리턴
    return result
    