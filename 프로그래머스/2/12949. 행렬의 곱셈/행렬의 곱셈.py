def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]   # 정답용 2차원 리스트 생성
    for row in range(len(arr1)):            # 첫번째 행렬의 행 탐색
        for column in range(len(arr2[0])):  # 두번째 행렬의 열 탐색
            for i in range(len(arr1[0])):   # 행렬곱 실행
                answer[row][column] += arr1[row][i] * arr2[i][column]
    return answer