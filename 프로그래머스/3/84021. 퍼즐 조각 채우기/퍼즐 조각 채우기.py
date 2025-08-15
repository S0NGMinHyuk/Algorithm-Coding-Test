from collections import deque, defaultdict

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(game_board, table):
    answer = 0
    holes = getHoles(game_board)
    blocks = getBlocks(table)
    for b in blocks:
        for h in holes[len(b)]:
            if match(b, h):
                answer += len(b)
                holes[len(b)].remove(h)
                break
    return answer


def getHoles(board) -> dict:
    holes = defaultdict(list)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                hole = findHole(board, i, j)
                holes[len(hole)].append(hole)
    return holes
                    
                    
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
    return list(sorted(hole))


def getBlocks(table) -> list:
    blocks = list()
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == 1:
                blocks.append(findBlock(table, i, j))
    return blocks


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
    return list(sorted(block))


def match(block, hole) -> bool:
    for _ in range(4):
        gap = (block[0][0]-hole[0][0], block[0][1]-hole[0][1])
        for b, h in zip(block, hole):
            if (b[0]-h[0], b[1]-h[1]) != gap:
                break
        else:
            return True
        block = rotate(block)
    return False


def rotate(block):
    pivot = block[0]
    newBlock = []
    for r, c in block:
        nr, nc = r-pivot[0], c-pivot[1]
        newBlock.append((pivot[0]+nc, pivot[1]-nr))
    return list(sorted(newBlock))
    