import sys
from heapq import heappop, heappush

# 초기 입력값 처리 함수
def init():
    garbage = int(sys.stdin.readline())
    roads = list(map(int, sys.stdin.readline().split()))
    towns = list(map(int, sys.stdin.readline().split()))
    return towns, roads


def solution():
    towns, roads = init()
    gasCost = []
    totalCost = 0

    # 새로운 마을에 갈 때마다 해당 가격의 주유소 값을 gasCost에 추가.
    # 다음 마을로 갈 수 있는 양만 지나온 마을 중 제일 저렴한 가격으로 주유
    for i in range(len(roads)):
        heappush(gasCost, towns[i])
        totalCost += gasCost[0] * roads[i]
    
    return totalCost


print(solution())