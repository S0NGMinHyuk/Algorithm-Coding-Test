def solution(matrix):           # DP 알고리즘 사용
    def calculate(left, right): # matrix[left]와 matrix[right]의 행렬곱을 구하는 최소 곱셈 연산 리턴
        result = float("inf")
        for mid in range(left, right):
            temp = dp[left][mid] + dp[mid+1][right] # (left, mid)까지의 곱셈과 (mid+1, right)까지의 곱셈 연산 구하기
            temp += matrix[left][0] * matrix[mid][1] * matrix[right][1] # 행렬곱 연산 더하기
            result = min(result, temp)
        return result # 최소 곱셈 연산 리턴

    # dp[a][b]는 a번째 행렬과 b번째 행렬의 행렬곱의 최소 곱셈 연산값
    dp = [[float("inf")] * len(matrix) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        dp[i][i] = 0
    
    arange = 1 # 행렬 범위
    while arange < len(matrix):
        for i in range(len(matrix)-arange):
            dp[i][i+arange] = calculate(i, i+arange)
        arange += 1
    return dp[0][-1]