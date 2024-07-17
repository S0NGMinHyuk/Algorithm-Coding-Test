def solution(n):
    # 예외처리
    if n == 1:
        return [1]
    
    # 달팽이 값을 채울 2차원 배열 생성
    graph = [[0]*n for _ in range(n)]
    
    # Down, Right, Up&Left 방향
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    
    num = 1         # 시작값
    xy = [0, 0]     # 시작위치
    direct = 0      # 진행 방향
    
    while graph[xy[0]][xy[1]] == 0: # 현재 자리가 빈 자리인 경우
        graph[xy[0]][xy[1]] = num   # 현재 자리를 num으로 채우고 num 1 증가 
        num += 1

        if direct == 0:     # 아래쪽으로 가다가 방향을 바꾸는 경우
            if xy[0]+1 == n or graph[xy[0]+1][xy[1]] > 0:
                direct += 1
        elif direct == 1:   # 오른쪽으로 가다가 방향을 바꾸는 경우
            if xy[1] == xy[0] or graph[xy[0]][xy[1]+1] > 0:
                direct += 1
        elif direct == 2:   # 왼쪽 위로 가다가 방향을 바꾸는 경우
            if graph[xy[0]-1][xy[1]-1] > 0:
                direct += 1
        
        # 위치 이동
        direct = direct % 3
        xy[0] += dy[direct]
        xy[1] += dx[direct]
    
    # 2차원 배열에서 0을 제외한 값을 answer 리스트에 추가
    answer = []
    for lst in graph:
        for n in lst:
            if n > 0:
                answer.append(n)
            else:
                break
    
    return answer