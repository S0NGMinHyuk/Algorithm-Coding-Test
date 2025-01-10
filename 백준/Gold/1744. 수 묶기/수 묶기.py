import sys

POSITIVE = 0
NEGATIVE = 1

# 입력값 처리 함수
def init():
    loop = int(sys.stdin.readline())
    arr = [[], []]

    for _ in range(loop):
        n = int(sys.stdin.readline())
        if n > 0:   arr[POSITIVE].append(n) # 양수 저장
        else:       arr[NEGATIVE].append(n) # 0, 음수 저장
    
    # 음수는 내림차순, 양수는 오름차순으로 정렬
    arr[NEGATIVE].sort(reverse=True)
    arr[POSITIVE].sort()

    return arr  # 양수 배열과 음수 배열을 가진 2차원 배열 리턴


def getValue(arr):
    value = 0

    while len(arr) > 0:
        if len(arr) == 1:       # 값이 하나만 남으면
            value += arr[-1]    # 해당 값을 value에 더하고
            break               # 반복문 종료

        a = arr.pop()           # 뒤에서 값을 두개 가져와서
        b = arr.pop()           # 합과 곱 중에 더 큰 것을
        value += max(a*b, a+b)  # value에 추가

    return value


def solution():
    arr = init()
    return getValue(arr[POSITIVE]) + getValue(arr[NEGATIVE])


print(solution())