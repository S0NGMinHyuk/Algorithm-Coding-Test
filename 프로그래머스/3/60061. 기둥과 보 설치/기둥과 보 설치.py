PILLAR = 0
PAPER = 1

def solution(n, build_frame):
    graph = [[[0] * (n+1) for _ in range(n+1)] for _ in range(2)]
    info = set()
    
    def can_build(x, y, a): # 설치가 가능한지 여부를 반환하는 함수
        if a == PILLAR: # 기둥
            if y == 0:  # 바닥에 설차히는 경우
                return True
            if graph[PILLAR][y-1][x] == 1: # 아래에 기둥이 있는 경우
                return True
            if graph[PAPER][y][x] == 1: # 현재 자리에 보가 있는 경우
                return True
            if x > 0 and graph[PAPER][y][x-1]: # 왼쪽에 보가 있는 경우
                return True
            return False
        else: # 보
            if graph[PILLAR][y-1][x] == 1 or graph[PILLAR][y-1][x+1] == 1: # 밑에 기둥이 있는 경우
                return True
            if graph[PAPER][y][x-1] == 1 and graph[PAPER][y][x+1] == 1: # 양 옆에 보가 있는 경우
                return True
            return False
            
    def can_remove(x, y, a): # 철거가 가능한지 여부를 반환하는 함수
        if a == PILLAR: # 기둥
            if graph[PILLAR][y+1][x] == 1 and not can_build(x, y+1, PILLAR): # 내 위의 기둥이 무너지는 경우
                return False
            if graph[PAPER][y+1][x] == 1 and not can_build(x, y+1, PAPER):  # 내 위의 보가 무너지는 경우
                return False
            if x > 0 and graph[PAPER][y+1][x-1] == 1 and not can_build(x-1, y+1, PAPER): # 내 위의 보가 무너지는 경우
                return False
            return True # 철거가 가능한 경우
        else: # 보
            if graph[PILLAR][y][x] == 1 and not can_build(x, y, PILLAR): # 내 위의 기둥이 무너지는 경우
                return False
            if graph[PILLAR][y][x+1] == 1 and not can_build(x+1, y, PILLAR): # 내 위의 기둥이 무너지는 경우
                return False
            if x > 0 and graph[PAPER][y][x-1] == 1 and not can_build(x-1, y, PAPER): # 내 왼쪽 보가 무너지는 경우
                return False
            if graph[PAPER][y][x+1] == 1 and not can_build(x+1, y, PAPER): # 내 오른쪽 보가 무너지는 경우
                return False
            return True
            
    for b in build_frame:
        if b[-1] == 1: # 설치하는 경우
            if can_build(b[0], b[1], b[2]): # 설치가 가능하면 설치
                graph[b[2]][b[1]][b[0]] = 1
                info.add((b[0], b[1], b[2]))
        
        elif b[-1] == 0: # 철거하는 경우
            graph[b[2]][b[1]][b[0]] = 0 # 일단 철거
            info.remove((b[0], b[1], b[2]))
            if not can_remove(b[0], b[1], b[2]): # 철거가 안되면 다시 복구
                graph[b[2]][b[1]][b[0]] = 1
                info.add((b[0], b[1], b[2]))
    
    info = sorted(list(info))
    return [list(element) for element in info]