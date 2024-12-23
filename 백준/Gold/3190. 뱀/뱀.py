import sys
from collections import deque

APPLE = 1
SNAKE = 2

def makeGraph(N):
    graph = [[0]*N for _ in range(N)]
    loop = int(sys.stdin.readline())

    for _ in range(loop):
        r, c = map(int, sys.stdin.readline().split())
        graph[r-1][c-1] = APPLE

    return graph


def getInfo():
    info = []
    loop = int(sys.stdin.readline())

    for _ in range(loop):
        info.append(list(sys.stdin.readline().split()))
        info[-1][0] = int(info[-1][0])
    
    return info


def solution():
    N = int(sys.stdin.readline())
    graph = makeGraph(N)
    info = getInfo()
    
    # 순서대로 우, 하, 좌, 상
    direct = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    timer = 0
    index = 0
    body = deque([[0, 0]])
    graph[0][0] = SNAKE
    while 1:
        pos = body[-1]
        if 0 <= pos[0] + dy[direct] < N and 0 <= pos[1] + dx[direct] < N:
            if graph[pos[0] + dy[direct]][pos[1] + dx[direct]] == APPLE:
                body.append([pos[0] + dy[direct], pos[1] + dx[direct]])
                graph[pos[0] + dy[direct]][pos[1] + dx[direct]] = SNAKE
            elif graph[pos[0] + dy[direct]][pos[1] + dx[direct]] == 0:
                body.append([pos[0] + dy[direct], pos[1] + dx[direct]])
                graph[pos[0] + dy[direct]][pos[1] + dx[direct]] = SNAKE
                graph[body[0][0]][body[0][1]] = 0
                body.popleft()
            else:
                return timer + 1
        else: 
            return timer + 1
            
        timer += 1
        if index < len(info) and timer == info[index][0]:
            if info[index][1] == "D":
                direct += 1
            elif info[index][1] == "L":
                direct -= 1
            direct %= 4
            index += 1
    
    return

print(solution())