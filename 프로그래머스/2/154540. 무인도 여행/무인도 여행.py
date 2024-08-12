def solution(maps):
    island = []         # 각 섬에서 머무를 수 있는 날짜 배열
    visited = set()     # 방문한 섬 좌표를 저장하는 집합
    
    # 모든 칸을 돌기
    for col in range(len(maps)):
        for row in range(len(maps[0])):
            # X가 아니고 처음 도착하는 섬인 경우
            # 해당 섬에서 머무를 수 있는 날짜를 island에 추가 + visited에 방문한 섬으로 체크
            if maps[col][row] != "X" and tuple([col, row]) not in visited:
                visited, food = getFood(maps, col, row, visited)
                island.append(food)
    
    # 지낼 수 있는 날짜를 오름차순으로 정렬해서 리턴
    return sorted(island) if len(island) > 0 else [-1]


def getFood(maps, col, row, visited):
    # BFS 알고리즘 사용
    from collections import deque
    
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    
    q = deque([[col, row]])
    food = int(maps[col][row])      # 현재 좌표부터 식량 카운팅
    visited.add(tuple([col, row]))  # 방문 좌표에 추가

    while len(q) > 0:
        y, x = q.popleft()
        for i in range(4):
            # 현재 좌표의 상하좌우를 살펴서 이어진 부분이 있으면 q에 추가 및 식량 카운팅
            if 0 <= y+dy[i] < len(maps) and 0 <= x+dx[i] < len(maps[0]):
                if maps[y+dy[i]][x+dx[i]] != "X" and tuple([y+dy[i], x+dx[i]]) not in visited:
                    food += int(maps[y+dy[i]][x+dx[i]])
                    q.append([y+dy[i], x+dx[i]])
                    visited.add(tuple([y+dy[i], x+dx[i]]))
    
    # 갱신된 visited와 이번 섬의 총 식량 리턴
    return visited, food