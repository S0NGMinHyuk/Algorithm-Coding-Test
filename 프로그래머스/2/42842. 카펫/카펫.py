def solution(brown, yellow):
    # 카펫의 가로세로가 될 수 있는 width, height를 탐색
    for i in range(3, int((brown+yellow)**0.5)+1):
        if (brown+yellow) % i == 0:
            width, height = (brown+yellow)//i, i
            # width, height 내부에 노란색 격자의 수가 가능한지 체크
            for j in range(1, height):
                # 가능하다면 [width, height] 리턴
                if yellow == (width-j)*(height-j):
                    return [width, height]