def solution(m, n, puddles):
    # m x n 크기의 2차원 배열 생성 (초기값 0)
    graph = [[0]*m for _ in range(n)]
    
    # 웅덩이 위치는 -1으로 변경 (pubbles가 행렬이 아니라 열행이라고..?)
    PUDDLE = -1
    for p in puddles:
        graph[p[1]-1][p[0]-1] = PUDDLE
    
    # 아래로만 가는 경우와 왼쪽으로만 가는 경우 초기값 세팅
    for i in range(m):
        if graph[0][i] == PUDDLE:
            break
        graph[0][i] = 1
    for i in range(n):
        if graph[i][0] == PUDDLE:
            break
        graph[i][0] = 1
    
    # 모든 칸에 대해
    for i in range(1, n):
        for j in range(1, m):
            # 웅덩이 칸이면 skip
            if graph[i][j] == PUDDLE:
                continue
            # 왼쪽 칸과 위쪽 칸의 값을 합치기
            graph[i][j] = max(graph[i-1][j], 0) + max(graph[i][j-1], 0)
            graph[i][j] %= 1000000007
    
    # 학교 위치의 값을 리턴
    return graph[-1][-1]
            