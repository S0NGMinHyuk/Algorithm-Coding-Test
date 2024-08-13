def solution(board):
    # 틱택토가 잘못되는 경우
    # 1. O와 X가 모두 이긴 경우
    # 2. O와 X의 차이가 1이 아닌 경우
    # 3. 이기는 경우가 2개인 경우
    cnt_O = getCount(board, "O")    # O가 둔 횟수
    cnt_X = getCount(board, "X")    # X가 둔 횟수
    win_O = isWin(board, "O")       # O가 이기는 경우의 수
    win_X = isWin(board, "X")       # X가 이기는 경우의 수
    
    if win_O > 0 and win_X == 0 and cnt_O-cnt_X == 1:      # 선공이 이기는 경우
        return 1
    elif win_O == 0 and win_X > 0 and cnt_O-cnt_X == 0:    # 후공이 이기는 경우
        return 1
    elif win_O+win_X == 0 and 0 <= cnt_O-cnt_X <= 1:        # 무승부인 경우
        return 1
    else:
        return 0
        
        
# mark가 board에 몇개 있는지 리턴하는 함수
def getCount(board, mark):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == mark:
                cnt += 1
    return cnt

# board에서 mark가 이기는 경우의 개수를 리턴
def isWin(board, mark):
    win = 0
    for i in range(3):
        # 가로, 세로 검사
        if board[i][0] == board[i][1] == board[i][2] == mark:
            win += 1
        if board[0][i] == board[1][i] == board[2][i] == mark:
            win += 1
    
    # 대각선 검사
    if board[0][0] == board[1][1] == board[2][2] == mark:
        win += 1
    if board[0][2] == board[1][1] == board[2][0] == mark:
        win += 1
        
    return win
    