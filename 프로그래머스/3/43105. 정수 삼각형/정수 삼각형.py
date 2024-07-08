def solution(triangle):
    # 아래에서 위로 올라가기
    for i in range(len(triangle)-2, -1, -1):
        # 자기 자식값 2개 중 더 큰 값을 더하기
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    # 꼭대기 값 (최대값) 리턴
    return triangle[0][0]