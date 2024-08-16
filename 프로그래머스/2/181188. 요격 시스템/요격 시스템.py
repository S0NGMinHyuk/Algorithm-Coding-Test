def solution(targets):
    # 먼저 나오고, 짧은 미사일 순으로 정렬
    targets.sort(key=lambda x: (x[0], x[1]-x[0]))
    
    bomb = 0    # 미사일 개수
    line = 0    # 날리는 위치
    
    for info in targets:
        if info[0] >= line:     # 요격 위치 이후에 나오는 미사일인 경우
            bomb += 1
            line = info[1]
        else:                   # 요격 위치 이전에 끝나는 미사일인 경우
            if info[1] < line:
                line = info[1]
            
    return bomb