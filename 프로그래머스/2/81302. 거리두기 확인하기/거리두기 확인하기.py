def solution(places):
    result = []
    # 각 교실마다 거리두기를 체크 후 결과를 result에 추가
    for room in places:
        result.append(isGood(room))
    return result

# room에서 P가 있는 위치를 기준으로 checkSit 함수를 실행 후 거리두기 결과를
def isGood(room):
    for col in range(5):
        for row in range(5):
            if room[col][row] == "P":
                if checkSit(room, col, row) == False:
                    return 0
    return 1

# 현재 위치의 상하좌우를 보고 적절한 작업을 실행하는 함수
# 상하좌우 중 X인 경우는 스킵, P인 경우 False 리턴,
# O인 경우 isClear 함수 실행 및 결과에 따라 False 리턴 혹은 continue 실행
def checkSit(room, col, row):
    dcol = [-1, 1, 0, 0]
    drow = [0, 0, -1, 1]
    
    for i in range(4):
        # 배열 범위 제한
        if col+dcol[i] >= 0 and col+dcol[i] < 5 and row+drow[i] >= 0 and row+drow[i] < 5:
            target = room[col+dcol[i]][row+drow[i]]
            if target == "X":
                continue
            elif target == "P": # 거리두기 안지킨 경우
                return False
            elif target == "O":
                if isClear(room, col+dcol[i], row+drow[i]) == False:
                    return False
        else:
            continue
    # 거리두기를 잘 지킨 경우
    return True

# 현재 칸의 상하좌우 칸에 사람이 2명 이상인지 검사하는 함수
def isClear(room, col, row):
    dcol = [-1, 1, 0, 0]
    drow = [0, 0, -1, 1]
    man = 0
    
    for i in range(4):
        # 배열 범위 제한
        if col+dcol[i] >= 0 and col+dcol[i] < 5 and row+drow[i] >= 0 and row+drow[i] < 5:
            target = room[col+dcol[i]][row+drow[i]]
            if target == "P":   # 사람인 경우, man 1 증가
                man += 1
        else:
            continue
    
    # 사람이 1명 이하면 True, 초과면 False 리턴
    return True if man < 2 else False