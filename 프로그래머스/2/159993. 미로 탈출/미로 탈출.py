def solution(maps):
    start, lever, exit = getLocation(maps)
    first = getPath(maps, start, lever)     # 시작부터 레버까지의 최단거리
    second = getPath(maps, lever, exit)     # 레버부터 출구까지의 최단거리
    return first + second if first > 0 and second > 0 else -1   # 결과 리턴
        
# maps에서 시작, 레버, 종료 좌표를 리턴하는 함수
def getLocation(maps):
    found = 0
    start, lever, exit = None, None, None
    for col in range(len(maps)):
        for row in range(len(maps[0])):
            if maps[col][row] == "S":
                start = [col, row]
                found += 1
            elif maps[col][row] == "L":
                lever = [col, row]
                found += 1
            elif maps[col][row] == "E":
                exit = [col, row]
                found += 1
            
            if found == 3:
                return start, lever, exit

# start에서 goal까지 거리를 리턴하는 함수
from collections import deque
def getPath(maps, start, goal):
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    
    # start 좌표를 기준으로 시작 / [x좌표, y좌표, start부터의 거리]
    q = deque([[start[0], start[1], 0]])
    visited = set(tuple(start))
    
    while len(q) > 0:
        now = q.popleft()
        if now[0] == goal[0] and now[1] == goal[1]: # goal에 도착한 경우
            return now[2]
        else:
            # 상하좌우 탐색
            for i in range(4):  
                # maps 범위를 벗어나는지 검사
                if 0 <= now[0]+dy[i] < len(maps) and 0 <= now[1]+dx[i] < len(maps[0]):  
                    # 이동할 길이 통로인지, 처음 방문하는 좌표인지 검사
                    if maps[now[0]+dy[i]][now[1]+dx[i]] != "X" and tuple([now[0]+dy[i], now[1]+dx[i]]) not in visited:
                        q.append([now[0]+dy[i], now[1]+dx[i], now[2]+1])
                        visited.add(tuple([now[0]+dy[i], now[1]+dx[i]]))
    
    # while문이 종료되면 길이 없다는 것
    return 0
    