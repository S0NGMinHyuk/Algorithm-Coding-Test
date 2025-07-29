#BFS 알고리즘 + DP 알고리즘 사용
from collections import deque

def solution(board):
    # 각 블록까지 경주로를 짓는 비용과 방향 정보를 가진 2차원 배열 생성 및 초기값 세팅
    grid = [[[0, set()] for _ in range(len(board))] for _ in range(len(board))]
    grid[-1][-1] = [1, set(["U", "D", "L", "R"])]
    
    # 상하좌우 순서
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    direct = ["U", "D", "L", "R"]
    
    # 목표 위치부터 BFS 알고리즘을 따라 경주로 건설
    q = deque([[len(board)-1, len(board)-1]])
    while len(q) > 0:
        y, x = q.popleft()
        for i in range(4):
            # 범위를 벗어나는 칸인지 검사 + 벽인지 검사 후 이동 가능하면 cost 계산
            if 0 <= y+dy[i] < len(board) and 0 <= x+dx[i] < len(board) and board[y+dy[i]][x+dx[i]] == 0:
                cost = grid[y][x][0] + (100 if direct[i] in grid[y][x][1] else 600)
                # 건설 비용이 더 저렴한 방법인 경우, 비용 및 방향 갱신
                if grid[y+dy[i]][x+dx[i]][0] == 0 or cost < grid[y+dy[i]][x+dx[i]][0]:
                    grid[y+dy[i]][x+dx[i]][1] = set(direct[i])
                    grid[y+dy[i]][x+dx[i]][0] = cost
                    q.append([y+dy[i], x+dx[i]])
                # 동일한 건설비용인 경우, 방향만 추가
                elif grid[y+dy[i]][x+dx[i]][0] == cost:
                    grid[y+dy[i]][x+dx[i]][1].add(direct[i])
    
    # 시작 지점의 건설비용 리턴
    return grid[0][0][0] - 1