from collections import deque

def solution(maps):
    # 상하좌우 움직임 리스트
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    VISITED = -1
    N, M = len(maps), len(maps[0])

    queue = deque([[0, 0, 1]])    # 큐에 시작 [x위치, y위치, 이동 횟수] 추가
    maps[0][0] = VISITED

    # BFS 알고리즘
    while len(queue) > 0:   
        x, y, move = queue.popleft()

        if y == N - 1 and x == M - 1:    # 결승점에 도달한 경우
            return move
        
        for i in range(4):  # 현재 위치의 상하좌우 탐색
            nx, ny = x+dx[i], y+dy[i]
            if nx >= 0 and ny >= 0 and nx < M and ny < N:
                if maps[ny][nx] > 0: # 2차원 배열 범위를 벗어나지 않고, 벽이 아닌 경우 큐에 추가
                    queue.append([nx, ny, move+1])
                    maps[ny][nx] = VISITED    # 큐에 중복 추가를 막기 위해 큐에 추가할 때 VISITED 처리
    
    # 결승점에 도달하지 못한 경우
    return -1
