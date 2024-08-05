def solution(k, d):
    DISTANCE = d**2     # 원점에서 떨어질 수 있는 최대거리
    dots = 0            # 점의 개수
    
    # (0, 0)에서 x좌표를 k씩 (d, 0)까지 진행
    for i in range(0, d+1, k):
        available = (DISTANCE - i**2)**0.5  # x좌표가 i일 때 가능한 최대 y좌표
        dots += available // k + 1          # (i, 0)에서 (i, available)까지의 점 개수
    
    return dots
        