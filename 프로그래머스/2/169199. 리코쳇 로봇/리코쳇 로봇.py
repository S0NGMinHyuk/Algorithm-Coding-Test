def solution(board):
    from collections import deque
    
    # 시작위치와 목표지점 찾기
    start = getLocation(board, "R")
    GOAL = getLocation(board, "G")
    
    # BFS 알고리즘 사용 / [row, col, 횟수] 형태
    q = deque([[start[0], start[1], 0]])
    visited = set(tuple(start))
    
    while len(q) > 0:
        now = q.popleft()
        
        # 현재 위치가 목표지점인 경우
        if now[:2] == GOAL:
            return now[2]
        
        # 현재 위치에서 상하좌우로 갈 수 있는 지점을 q에 추가
        for i in range(4):
            newLocate = movePosition(board, now[:2], i)
            if newLocate not in visited:
                q.append([newLocate[0], newLocate[1], now[2]+1])
                visited.add(newLocate)
                # 중복 방지를 위해 visited에 저장
    
    # while문을 통과하면 목표지점에 도착할 수 없다는 뜻
    return -1


# board에서 mark의 좌표를 리턴하는 함수
def getLocation(board, mark):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == mark:
                return [i, j]
            
            
# board에서 now 좌표에 있을 때, direct 방향으로 이동한 좌표를 리턴하는 함수
def movePosition(board, now, direct):
    # 위쪽으로 이동
    if direct == 0:   
        for i in range(now[0]-1, -1, -1):
            if board[i][now[1]] == "D":     # 장애물에 부딪힌 경우, 이전 좌표 리턴
                return (i+1, now[1])
        return (0, now[1])                  # 맨 끝 좌표 리턴
    # 아래쪽으로 이동
    elif direct == 1:   
        for i in range(now[0]+1, len(board)):
            if board[i][now[1]] == "D":
                return (i-1, now[1])
        return (len(board)-1, now[1])
    # 왼쪽으로 이동
    elif direct == 2:     
        for i in range(now[1]-1, -1, -1):
            if board[now[0]][i] == "D":
                return (now[0], i+1)
        return (now[0], 0)
    # 오른쪽으로 이동
    elif direct == 3:   
        for i in range(now[1]+1, len(board[0])):
            if board[now[0]][i] == "D":
                return (now[0], i-1)
        return (now[0], len(board[0])-1)