import sys

# 상수 선언
DIRTY = 0
WALL = 1
CLEAN = 2

# 현재 칸의 상하좌우 4칸에 청소할 칸이 있는지 결과를 반환
def detectArea(graph, N, M, r, c):
    state = False

    if 0 <= r+1 < N and 0 <= c < M and graph[r+1][c] == DIRTY:
        state = True
    if 0 <= r-1 < N and 0 <= c < M and graph[r-1][c] == DIRTY:
        state = True
    if 0 <= r < N and 0 <= c+1 < M and graph[r][c+1] == DIRTY:
        state = True
    if 0 <= r < N and 0 <= c-1 < M and graph[r][c-1] == DIRTY:
        state = True
    
    return state


def solution():
    # 초기화 과정
    N, M = map(int, sys.stdin.readline().split())
    r, c, d = map(int, sys.stdin.readline().split())
    
    # 그래프 정보 저장
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    # 순서대로 북, 동, 남, 서 방향
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]


    cleanedBlock = 0
    while 1:
        # 현재 칸이 더러우면 청소
        if graph[r][c] == DIRTY:
            graph[r][c] = CLEAN
            cleanedBlock += 1

        # 청소할 칸이 있는 경우
        if detectArea(graph, N, M, r, c):   
            for _ in range(4):
                d = (d - 1) % 4                         # 반시계 방향으로 돌며
                if graph[r+dy[d]][c+dx[d]] == DIRTY:    # 앞 칸이 더러운 칸인 경우
                    r += dy[d]                          # 앞 칸으로 이동 후 for 문 탈출
                    c += dx[d]
                    break
        
        # 청소할 칸이 없는 경우
        else:                               
            # 갈 수 없는 경우 (벽으로 막힌 경우)
            if graph[r+dy[(d+2)%4]][c+dx[(d+2)%4]] == WALL: 
                break

            # 갈 수 있는 경우 뒤로 가기
            else:
                r = r + dy[(d+2)%4]
                c = c + dx[(d+2)%4]
    
    # 청소한 칸 개수 리턴
    return cleanedBlock

print(solution())