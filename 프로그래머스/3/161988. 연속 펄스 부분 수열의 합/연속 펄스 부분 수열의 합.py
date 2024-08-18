def solution(sequence):
    s1 = makeList(sequence, True)
    s2 = makeList(sequence, False)
    return max(getMaximum(s1), getMaximum(s2))

# 부분수열의 최대합 리턴
def getMaximum(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > 0:
            arr[i] += arr[i-1]

    return max(arr)

# 펄스수열이 곱해진 수열 리턴
def makeList(sequence, mode):
    arr = list(sequence)
    if mode:
        for i in range(0, len(arr), 2):
            arr[i] *= -1
    else:
        for i in range(1, len(arr), 2):
            arr[i] *= -1
    return arr