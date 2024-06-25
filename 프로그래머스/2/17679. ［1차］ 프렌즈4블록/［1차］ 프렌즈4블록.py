def solution(m, n, board):
    answer = 0
    table = [list(board[i]) for i in range(len(board))] # 2차원 배열로 변환

    while 1:    
        discard = boom(m, n, table) # 2x2 형태로 붙어있는 블록 개수를 리턴 + table에 '0'으로 마크
        if discard:                 # 없어지는 블록이 있는 경우
            answer += discard       # 제거할 블록 개수 추가
            rebuild(m, n, table)    # table 재구성
        else:       # 없어지는 블록이 없는 경우
            break   # 반복문 종료

    return answer

# 2x2 형태로 붙어있는 블록 개수를 리턴 + table에 '0'으로 마크
def boom(m, n, table):
    deleteDict = set()  # '0'으로 변경할 위치를 저장하는 집합
    for col in range(m-1):
        for row in range(n-1):
            # 2x2가 모두 같고 '0'이 아닌 경우, deleteSet에 추가
            if table[col][row] != '0' and table[col][row] == table[col+1][row] == table[col][row+1] == table[col+1][row+1]:
                deleteDict.add((col, row))
                deleteDict.add((col+1, row))
                deleteDict.add((col, row+1))
                deleteDict.add((col+1, row+1))
    # deleteSet에 있는 위치를 '0'으로 변경
    for col, row in deleteDict:
        table[col][row] = '0'

    return len(deleteDict)  # 붙어있는 불록 개수 리턴

# 블록이 제거되어 위에서 떨어져야 할 블록 재구성하는 함수
def rebuild(m, n, table):
    for row in range(n):
        stack = []
        for col in range(m-1, -1, -1):  # 열을 아래부터 보며 '0'이 아닌 경우 stack에 추가
            if table[col][row] != '0':
                stack.append(table[col][row])
                table[col][row] = '0'   # 스택에 추가 후 자기 자리를 '0'으로 변경
        
        for i in range(len(stack)):     # 맨 아래열부터 선입선출로 table 갱신
            table[m-1-i][row] = stack[i]
    return