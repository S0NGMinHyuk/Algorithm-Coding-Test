def solution(rows, columns, queries):
    # 이차원 행렬 생성
    arr = [list(range(1 + r*columns, (r+1)*columns+1)) for r in range(rows)]
    result = []

    # 쿼리에 맞춰 행렬 회전 및 최소값 갱신
    for q in queries:
        arr, mini = spin(arr, q)
        result.append(mini)
    
    # 최소값 반환
    return result

# 행렬을 회전시키며 최소값을 구하는 함수
def spin(arr, query):
    # 쿼리가 인덱스에 맞도록 1씩 감소
    for i in range(4):
        query[i] -= 1
    
    pos = [query[0], query[1]]      # 현재 위치
    prev = arr[query[0]][query[1]]  # 이전 값
    mini = arr[query[0]][query[1]]  # 최소값
    
    direct = 0                      # 회전 방향
    dx = [1, 0, -1, 0]              # 각 방향 별 x 변경값
    dy = [0, 1, 0, -1]              # 각 방형 별 y 변경값
    
    while 1:
        # 진행방향 변경이 필요한지 검사
        if direct == 0 and pos[1] == query[3]:
            direct += 1
        elif direct == 1 and pos[0] == query[2]:
            direct += 1
        elif direct == 2 and pos[1] == query[1]:
            direct += 1
        elif direct == 3 and pos[0] == query[0]:
            break
        
        # 현재 위치 변경 및 값 변경
        pos[0] += dy[direct]; pos[1] += dx[direct]
        prev, arr[pos[0]][pos[1]] = arr[pos[0]][pos[1]], prev
        mini = min(mini, prev)
    
    # 회전한 배열과 최소값 반환
    return arr, mini