from collections import deque, defaultdict

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(game_board, table):
    answer = 0
    holes = getHoles(game_board) # 모든 빈 공간을 구하기
    blocks = getBlocks(table)    # 모든 퍼즐조각을 구하기
    for b in blocks:
        for h in holes[len(b)]:
            if match(b, h):      # 퍼즐조각이 들어갈 자리를 찾은경우
                answer += len(b) # answer 갱신
                holes[len(b)].remove(h) # 해당 빈 공간 삭제
                break
    return answer

# board에서 빈 공간을 찾아 딕셔너리로 리턴하는 함수
# key는 빈공간 크기, value는 빈공간의 좌표 배열이다.
def getHoles(board) -> dict:
    holes = defaultdict(list)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0: # 빈 공간을 발견한 경우
                hole = findHole(board, i, j) # 빈 공간 찾고 holes에 추가
                holes[len(hole)].append(hole)
    return holes
                    
# i, j 좌표가 속한 빈 공간의 좌표 배열을 리턴하는 함수 (BFS 사용)
def findHole(board, i, j) -> list:
    hole = [(i, j)]
    q = deque([(i, j)])
    board[i][j] = 1
    while len(q) > 0:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dx[i], c+dy[i]
            if 0 <= nr < len(board) and 0 <= nc < len(board) and board[nr][nc] == 0:
                hole.append((nr, nc))
                q.append((nr, nc))
                board[nr][nc] = 1
    return list(sorted(hole)) # 빈 공간의 좌표들을 정렬해서 리턴

# table에서 퍼즐조각을 찾아 배열로 리턴하는 함수
def getBlocks(table) -> list:
    blocks = list()
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == 1: # 퍼즐조각을 찾은 경우
                blocks.append(findBlock(table, i, j))
    return blocks

# i, j 좌표가 속한 퍼즐조각의 좌표 배열을 리턴하는 함수 (BFS 사용)
def findBlock(table, i, j) -> list:
    block = [(i, j)]
    q = deque([(i, j)])
    table[i][j] = 0
    while len(q) > 0:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dx[i], c+dy[i]
            if 0 <= nr < len(table) and 0 <= nc < len(table) and table[nr][nc] == 1:
                block.append((nr, nc))
                q.append((nr, nc))
                table[nr][nc] = 0
    return list(sorted(block)) # 퍼즐조각의 좌표들을 정렬해서 리턴

# block 배열이 hole 배열에 딱 맞는지 여부를 리턴하는 함수
def match(block, hole) -> bool:
    for _ in range(4):
        gap = (block[0][0]-hole[0][0], block[0][1]-hole[0][1])
        for b, h in zip(block, hole):
            if (b[0]-h[0], b[1]-h[1]) != gap: # 딱 맞지 않는 경우
                break
        else:
            return True
        block = rotate(block) # 블록 회전시키기
    return False

# 블록 배열을 시계방향으로 90도 회전시키는 함수
def rotate(block):
    pivot = block[0]
    newBlock = []
    for r, c in block:
        nr, nc = r-pivot[0], c-pivot[1]
        newBlock.append((pivot[0]+nc, pivot[1]-nr))
    return list(sorted(newBlock))
    