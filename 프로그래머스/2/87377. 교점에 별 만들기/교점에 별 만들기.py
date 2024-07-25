def solution(line):
    dots = []   # 교점을 저장하는 리스트
    top, bot, left, right = None, None, None, None  # 상하좌우 최대 좌표값 저장
    
    # 모든 직선에 대해 교점 구하기
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            dot = getDot(line[i], line[j])
            
            # 교점이 정수가 아닌 경우
            if dot == False:
                continue
            
            # 교점 리스트에 추가 및 상하좌우 최대 좌표값 저장
            dots.append(dot)
            top = max(top, dot[1]) if top != None else dot[1]
            bot = min(bot, dot[1]) if bot != None else dot[1]
            right = max(right, dot[0]) if right != None else dot[0]
            left = min(left, dot[0]) if left != None else dot[0]
    
    # 별을 찍을 2차원 리스트 생성
    graph = [["."]*(right-left+1) for _ in range(top-bot+1)]
    
    # 교점에 대해 좌표값을 적절하게 이동시키고 2차원 리스트에 별 찍기
    for dot in dots:
        dot[0] -= left
        dot[1] -= bot
        graph[dot[1]][dot[0]] = "*"
    
    # 2차원 리스트를 문자열 리스트로 변경하기
    for i in range(len(graph)):
        graph[i] = "".join(graph[i])
    
    # 리스트를 뒤집어서 리턴
    return graph[::-1]
            
    
# [x, y] 좌표 리턴
def getDot(a, b):
    # 두 직선이 평행하지 않고, 교점이 있는 경우
    if (a[0]*b[1] - a[1]*b[0]) != 0:
        x = (a[1]*b[2] - a[2]*b[1]) / (a[0]*b[1] - a[1]*b[0])
        y = (a[2]*b[0] - a[0]*b[2]) / (a[0]*b[1] - a[1]*b[0])
        # x, y 좌표가 정수인 경우
        if x == int(x) and y == int(y):
            return [int(x), int(y)]
        
    return False