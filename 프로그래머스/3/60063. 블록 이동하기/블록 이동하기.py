from collections import deque

def solution(board):
    answer = 0
    N = len(board)
    goal = (N-1, N-1)
    visited = set([((0, 0), (0, 1))])
    
    bot = [(0, 0), (0, 1), True, 0] # left, right, status, time
    q = deque([bot])
    while len(q) > 0:
        left, right, status, time = q.popleft()
        if left == goal or right == goal:
            answer = time
            break
        
        if status == True: # 가로인 경우
            # 오른쪽으로 이동
            if right[1]+1 < N and board[right[0]][right[1]+1] == 0:
                newRight = (right[0], right[1]+1)
                if (right, newRight) not in visited:
                    visited.add((right, newRight))
                    q.append([right, newRight, status, time+1])      
            # 왼쪽으로 이동
            if left[1] > 0 and board[left[0]][left[1]-1] == 0:
                newLeft = (left[0], left[1]-1)
                if (newLeft, left) not in visited:
                    visited.add((newLeft, left))
                    q.append([newLeft, left, status, time+1])
            # 기계를 위쪽으로 세우기
            if left[0] > 0 and board[left[0]-1][left[1]] == 0 and board[right[0]-1][right[1]] == 0:
                upLeft = (left[0]-1, left[1]); upRight = (right[0]-1, right[1])
                if (upLeft, left) not in visited:  # 왼쪽 위로 세우기
                    visited.add((upLeft, left))
                    q.append([upLeft, left, not status, time+1]) 
                if (upRight, right) not in visited: # 오른쪽 위로 세우기
                    visited.add((upRight, right))
                    q.append([upRight, right, not status, time+1]) 
                if (upLeft, upRight) not in visited: # 위쪽으로 이동
                    visited.add((upLeft, upRight))
                    q.append([upLeft, upRight, status, time+1])
            # 기계를 아래쪽으로 세우기
            if left[0]+1 < N and board[left[0]+1][left[1]] == 0 and board[right[0]+1][right[1]] == 0:
                downLeft = (left[0]+1, left[1]); downRight = (right[0]+1, right[1])
                if (left, downLeft) not in visited:
                    visited.add((left, downLeft))
                    q.append([left, downLeft, not status, time+1])
                if (right, downRight) not in visited:
                    visited.add((right, downRight))
                    q.append([right, downRight, not status, time+1])
                if (downLeft, downRight) not in visited: # 아래쪽으로 이동
                    visited.add((downLeft, downRight))
                    q.append([downLeft, downRight, status, time+1])
                        
        else: # 세로인 경우
            # 아래쪽으로 이동
            if right[0]+1 < N and board[right[0]+1][right[1]] == 0: 
                newRight = (right[0]+1, right[1])
                if (right, newRight) not in visited:
                    visited.add((right, newRight))
                    q.append([right, newRight, status, time+1])
            # 위쪽으로 이동
            if left[0] > 0 and board[left[0]-1][left[1]] == 0:
                newLeft = (left[0]-1, left[1])
                if (newLeft, left) not in visited:
                    visited.add((newLeft, left))
                    q.append([newLeft, left, status, time+1])
            # 기계를 왼쪽으로 눕히기
            if left[1] > 0 and board[left[0]][left[1]-1] == 0 and board[right[0]][right[1]-1] == 0:
                downLeft = (left[0], left[1]-1); downRight = (right[0], right[1]-1)
                if (downLeft, left) not in visited:   # 위쪽을 축으로 눕히기
                    visited.add((downLeft, left))
                    q.append([downLeft, left, not status, time+1])
                if (downRight, right) not in visited: # 아래쪽을 축으로 눕히기
                    visited.add((downRight, right))
                    q.append([downRight, right, not status, time+1])
                if (downLeft, downRight) not in visited: # 왼쪽으로 이동
                    visited.add((downLeft, downRight))
                    q.append([downLeft, downRight, status, time+1])
            # 기계를 오른쪽으로 눕히기
            if left[1]+1 < N and board[left[0]][left[1]+1] == 0 and board[right[0]][right[1]+1] == 0:
                upLeft = (left[0], left[1]+1); upRight = (right[0], right[1]+1)
                if (left, upLeft) not in visited:   # 위쪽을 축으로 눕히기
                    visited.add((left, upLeft))
                    q.append([left, upLeft, not status, time+1])
                if (right, upRight) not in visited: # 아래쪽을 축으로 눕히기
                    visited.add((right, upRight))
                    q.append([right, upRight, not status, time+1])
                if (upLeft, upRight) not in visited: # 오른쪽으로 이동
                    visited.add((upLeft, upRight))
                    q.append([upLeft, upRight, status, time+1])
        
    return answer