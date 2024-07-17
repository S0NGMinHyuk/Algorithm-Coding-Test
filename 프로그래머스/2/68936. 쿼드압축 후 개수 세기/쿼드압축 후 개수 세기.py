def solution(arr):
    answer = dfs(arr, [0, 0])   # dfs 알고리즘 사용
    return answer

def dfs(arr, answer):
    if len(arr) == 1:           # base case / 한 칸 짜리 배열로 압축된 경우
        if arr[0][0] == 0:      # 0만 있던 경우, 0 증가
            answer[0] += 1
        elif arr[0][0] == 1:    # 1만 있던 경우, 1 증가
            answer[1] += 1
        return answer
    
    NOT_COMP = 2    # 압축이 안되는 경우, 2로 표기
    newArr = [[0]*(len(arr)//2) for _ in range(len(arr)//2)]    # 2n x 2n인 arr를 n x n배열로 압축한다.
    
    for col in range(0, len(arr), 2):
        for row in range(0, len(arr), 2):
            # 압축이 가능한 경우, 해당 값으로 newArr에 압축
            if arr[col][row] == arr[col+1][row] == arr[col][row+1] == arr[col+1][row+1]:
                newArr[col//2][row//2] = arr[col][row]
            else:
                # 압축이 불가능한 경우, NOT_COMP로 압축 후 0과 1 개수를 answer에 추가
                newArr[col//2][row//2] = NOT_COMP
                if arr[col][row] == 0:
                    answer[0] += 1
                elif arr[col][row] == 1:
                    answer[1] += 1
                if arr[col+1][row] == 0:
                    answer[0] += 1
                elif arr[col+1][row] == 1:
                    answer[1] += 1
                if arr[col][row+1] == 0:
                    answer[0] += 1
                elif arr[col][row+1] == 1:
                    answer[1] += 1
                if arr[col+1][row+1] == 0:
                    answer[0] += 1
                elif arr[col+1][row+1] == 1:
                    answer[1] += 1
    # 압축된 newArr 배열로 재귀호출 후 결과를 리턴
    return dfs(newArr, answer)