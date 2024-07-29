# 누적합 알고리즘 사용

def solution(board, skill):
    # 누적합 계산을 위한 배열 생성 및 값 찍기
    graph = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for info in skill:
        if info[0] == 1:    # 공격인 경우, 데미지를 음수로 변경
            info[-1] *= -1
        graph[info[1]][info[2]] += info[-1]
        graph[info[3]+1][info[4]+1] += info[-1]        
        graph[info[1]][info[4]+1] += -info[-1]        
        graph[info[3]+1][info[2]] += -info[-1] 

    # 누적합 진행 (오른쪽으로 진행 후 아래쪽으로 진행)
    for i in range(len(graph)):
        for row in range(1, len(graph[0])):
            graph[i][row] += graph[i][row-1]
    for i in range(len(graph[0])):
        for col in range(1, len(graph)):
            graph[col][i] += graph[col-1][i]
    
    # 파괴되지 않은 건물 카운트
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]+graph[i][j] > 0: cnt += 1
            
    return cnt