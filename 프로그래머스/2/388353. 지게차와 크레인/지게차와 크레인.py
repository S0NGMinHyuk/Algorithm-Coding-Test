BORDER = "0"
INSIDE = "1"

def solution(storage, requests):
    answer = len(storage) * len(storage[0])
    storage = makeMargin(storage)
    
    for request in requests:
        boxes = findBox(storage, request)
        answer -= len(boxes)
        removeBox(storage, boxes)
        clearStorage(storage)
    
    return answer


def makeMargin(arr):    # 배열의 상하좌우에 한칸씩 모서리("0")를 추가하는 함수
    temp = [[BORDER] * (len(arr[0])+2)]
    for row in arr:
        temp.append([BORDER] + list(row) + [BORDER])
    temp.append([BORDER] * (len(arr[0])+2))
    return temp


def findBox(storage, request):  # 제거해야하는 컨테이너의 좌표를 리턴하는 함수
    target = request[0]
    boxes = []
    for i in range(1, len(storage) - 1):
        for j in range(1, len(storage[0]) - 1):
            if storage[i][j] == target:
                if len(request) == 1 and not isBorder(storage, i, j):
                    continue
                else:
                    boxes.append((i, j))
    return boxes
    
    
def removeBox(storage, boxes):  # 제거해야하는 박스를 제거하는 함수.
    for i, j in boxes:
        if isBorder(storage, i, j):
            storage[i][j] = BORDER
        else:
            storage[i][j] = INSIDE
            

def isBorder(storage, i, j):    # 현재 좌표가 테두리와 맞닿아있는지 여부 리턴
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for k in range(4):
        if 0 <= i + dx[k] < len(storage) and 0 <= j + dy[k] < len(storage[0]):
            if storage[i + dx[k]][j + dy[k]] == BORDER:
                return True
    return False


def clearStorage(storage):      # 컨테이너 제거 후 Border를 재탐색하는 함수
    for i in range(1, len(storage)-1):
        for j in range(1, len(storage[0])-1):
            if storage[i][j] == INSIDE and isBorder(storage, i, j):
                inside2border(storage, i, j)
                

def inside2border(storage, i, j):   # INSIDE 였던 칸이 BORDER가 되는 경우를 모두 찾아서 변환하는 함수
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    storage[i][j] = BORDER
    for k in range(4):
        ni, nj = i + dx[k], j + dy[k]
        if 0 <= ni < len(storage) and 0 <= nj < len(storage[0]) and storage[ni][nj] == INSIDE:
            inside2border(storage, ni, nj)