def solution(m, n, startX, startY, balls):
    return [getDistance(m, n, startX, startY, ball) for ball in balls]


def getDistance(m, n, x, y, ball):
    distance = m**2 + n**2
    
    # 오른쪽 벽에 튕기는 경우
    if not(ball[0] > x and ball[1] == y):
        distance = min(distance, (m*2-ball[0]-x)**2 + (ball[1]-y)**2)
    # 왼쪽 벽에 튕기는 경우
    if not(ball[0] < x and ball[1] == y):
        distance = min(distance, (ball[0]+x)**2 + (ball[1]-y)**2)
    # 위쪽 벽에 튕기는 경우
    if not(ball[0] == x and ball[1] > y):
        distance = min(distance, (ball[0]-x)**2 + (n*2-ball[1]-y)**2)
    # 아래쪽 벽에 튕기는 경우
    if not(ball[0] == x and ball[1] < y):
        distance = min(distance, (ball[0]-x)**2 + (ball[1]+y)**2)
        
    return distance