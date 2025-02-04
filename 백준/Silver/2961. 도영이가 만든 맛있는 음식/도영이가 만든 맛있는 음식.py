import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def backTracking(index, balance):
    if index == n:
        if balance != [1, 0]:
            global GAP
            GAP = min(GAP, abs(balance[0] - balance[1]))
        return
    
    temp = [balance[0] * foods[index][0], balance[1] + foods[index][1]]
    backTracking(index+1, temp)
    backTracking(index+1, balance)


if __name__ == '__main__':
    GAP = float("inf")
    n = int(input())
    foods = [list(map(int, input().split())) for _ in range(n)]

    backTracking(0, [1, 0])
    print(GAP)