def solution(n):
    return hanoi(n, 1, 2, 3)    # 재귀 함수 호출

def hanoi(n, start, via, goal): # 3가지 변수 start, via, goal을 선언하는게 중요하다.
    if n == 1:  # 재귀 종료 조건
        return [[start, goal]]
    else:       # 재귀 반복 호출
        return hanoi(n-1, start, goal, via) + [[start, goal]] + hanoi(n-1, via, start, goal)