def solution(r1, r2):
    return getDotsInCircle(r2, True) - getDotsInCircle(r1, False)

# 반지름이 radius인 원 내부 점의 개수를 리턴하는 함수
def getDotsInCircle(radius, mode):
    result = 1  # (0, 0) 좌표의 점 추가
    for i in range(radius):
        dots = (radius**2-i**2)**0.5
        # 테두리에 걸치는 점도 추가
        if mode:                   
            result += int(dots)*4
        # 테두리에 걸치는 점은 제거
        else:
            result += (int(dots) if dots != int(dots) else int(dots)-1)*4
    return result