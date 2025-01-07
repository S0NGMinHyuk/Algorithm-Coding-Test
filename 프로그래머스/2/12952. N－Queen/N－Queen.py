# 백트래킹 알고리즘 ( DFS 사용 )
def solution(n):
    position = []   # 퀸을 놓는 위치를 담은 리스트
    return nQueen(0, position, n)

# table에 퀸을 놓는 함수 (재귀 호출)
def nQueen(row, position, n):
    if row == n:    # 재귀 종료 base case
        return 1
    
    answer = 0
    for col in range(n):
        if isPossible(row, col, position):  # 현재 자리가 퀸을 놓을 수 있는지 검사
            position.append([row, col])     # 현재 자리에 퀸 놓기
            answer += nQueen(row+1, position, n)    # 다음 행에 대해 재귀 실행
            position.pop()                  # 현재 자리에 놓은 퀸 제거
    
    return answer

# position의 row, col 자리에 퀸을 놓을 수 있는지 검사하는 함수
def isPossible(row, col, position):
    for r, c in position:   # 이미 퀸이 놓인 자리 [r, c]
        if col == c or abs(row-r) == abs(col-c):    # 위나 대각선에 퀸이 있는 경우
            return False                            # 퀸을 놓을 수 없다.
    
    return True # 모든 자리를 무사히 통과하면 퀸을 놓을 수 있다.