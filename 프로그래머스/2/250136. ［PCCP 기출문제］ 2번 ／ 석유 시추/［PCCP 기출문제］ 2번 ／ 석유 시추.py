def solution(land):
    visited = set()
    dataSet = [0]*len(land[0])
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1 and (i, j) not in visited:
                # 석유 발견 시 추출 및 dataSet에 추출할 수 있는 석유량 추가
                fuel, found, area = getFuel(land, [i, j])
                visited |= found
                for row in area:
                    dataSet[row] += fuel
    return max(dataSet)

                
# land 그래프 내 locate 좌표에서 이어진 석유 개수와 위치를 리턴하는 함수
def getFuel(land, locate):
    # BFS 알고리즘 사용
    from collections import deque
    q = deque([locate])
    visited = {tuple(locate)}
    area = {locate[1]}
    
    while len(q) > 0:
        now = q.popleft()
        for i in range(4):
            newLocate = getMoving(land, now, i)
            if newLocate and newLocate not in visited:
                q.append(newLocate)
                visited.add(newLocate)
                area.add(newLocate[1])
    
    return len(visited), visited, area


# land 그래프 내 now에서 i방향에 석유가 있으면 움직인 좌표를 리턴하는 함수
def getMoving(land, now, i):
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    
    if 0 <= now[0]+dy[i] < len(land) and 0 <= now[1]+dx[i] < len(land[0]):
        if land[now[0]+dy[i]][now[1]+dx[i]] == 1:
            return (now[0]+dy[i], now[1]+dx[i])

    return False