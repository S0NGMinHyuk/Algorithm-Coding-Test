def solution(routes):
    routes.sort(key=lambda x: x[1])     # 차량 경로를 탈출지점 기준으로 오름차순 정렬
    camera = 0                          # 설치할 단속카메라 개수
    spot = -30001                       # 진입 지점이 -30000부터라서 -30001로 초기화
    for start, end in routes:
        if start > spot:
            camera += 1
            spot = end
    return camera