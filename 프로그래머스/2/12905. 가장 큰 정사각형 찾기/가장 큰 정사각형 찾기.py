def solution(board):
    answer = 0  
    for arr in board:   # board의 행 또는 열의 길이가 1인 경우 예외처리
        if 1 in arr:
            answer = 1  # answer의 최소값을 1로 변경
    
    for column in range(1, len(board)):     # board의 0번째 행, 열은 skip
        for row in range(1, len(board[0])):
            if board[column][row] > 0:          # 현재 칸이 사각형인 경우
                board[column][row] = 1 + min(   # 현재 칸의 위쪽, 왼쪽, 왼쪽의 위쪽 값 중 최소값 +1 저장
                    board[column-1][row],       # (현재값의 위쪽)
                    board[column][row-1],       # (현재값의 왼쪽)
                    board[column-1][row-1])     # (현재값의 왼쪽의 위쪽)
            # answer 값 갱신
            answer = max(board[column][row], answer)
    
    return answer**2