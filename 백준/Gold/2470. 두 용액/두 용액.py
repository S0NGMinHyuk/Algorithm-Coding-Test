import sys

def getArr():
    garbage = sys.stdin.readline()
    return sorted(list(map(int, sys.stdin.readline().split())))


def solution():
    arr = getArr()
    left = 0
    right = len(arr)-1

    gap = abs(arr[right] + arr[left])
    answer = [left, right]

    while left < right:
        temp = arr[right] + arr[left]
        if abs(temp) < gap:
            gap = abs(temp)
            answer = [left, right]

        if temp > 0:
            right -= 1
        else:
            left += 1
    
    for i in range(2):
        print(f"{arr[answer[i]]} ", end="")


solution()