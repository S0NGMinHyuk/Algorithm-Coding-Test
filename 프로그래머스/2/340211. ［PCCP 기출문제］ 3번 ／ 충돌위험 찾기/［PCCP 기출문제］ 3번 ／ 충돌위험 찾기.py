from itertools import zip_longest

OUT = (-1, -1)

def solution(points, routes):
    answer = 0
    everyRoutes = []    # 각 로봇별 동선을 저장
    for route in routes:
        everyRoutes.append(getRoute(points, route))
    
    for col in zip_longest(*everyRoutes, fillvalue=OUT):   # 각 초마다 충돌이 발생하는 회수를 answer에 추가
        answer += countCrash(col)
    return answer
    
    
def getRoute(points, path) -> list: # 로봇이 가야하는 path에 따른 전체 동선을 리턴
    route = []
    route.append(tuple(points[path[0] - 1]))  # 시작 위치 추가
    for i in range(len(path) - 1):
        route.extend(findPath(points[path[i]-1], points[path[i + 1]-1]))
    route.append(OUT)  # 마지막에 OUT을 추가하여 밖으로 나간 로봇을 표시
    return route


def findPath(start, end) -> list:   # start 좌표에서 end 좌표로 가는 동선 리턴
    path = []
    while start[0] != end[0]:           # 위아래로 먼저 이동
        if start[0] < end[0]:
            start = (start[0] + 1, start[1])
        else:
            start = (start[0] - 1, start[1])
        path.append(start)
    while start[1] != end[1]:           # 좌우로 이동
        if start[1] < end[1]:
            start = (start[0], start[1] + 1)
        else:
            start = (start[0], start[1] - 1)
        path.append(start)
    return path


def countCrash(col) -> int: # 현재 시간에 충돌이 일어나는 칸의 개수를 리턴
    crash = 0
    visited = dict()
    for point in col:
        if point == OUT:    # 밖으로 나간 로봇은 제외
            continue
        if point in visited:
            visited[point] += 1
            if visited[point] == 2: # 충돌 발생 시 crash 증가
                crash += 1
        else:
            visited[point] = 1
    return crash