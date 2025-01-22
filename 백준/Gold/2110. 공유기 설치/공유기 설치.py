import sys

# 초기 입력값 처리 함수
def getHomeArr(n):
    arr = []
    for _ in range(n):
        arr.append(int(sys.stdin.readline()))
    return sorted(arr)


# homeArr 배열에서 n씩 거리를 두며 cnt개의 라우터를 깔 수 있는지 검사하는 함수
def isPromising(homeArr, n, cnt):
    left = right = 0
    while cnt > 0 and right < len(homeArr):
        if homeArr[right] - homeArr[left] >= n:
            cnt -= 1
            left = right
        right += 1
    
    return cnt == 0



def solution():
    homes, routers = map(int, sys.stdin.readline().split())
    homeArr = getHomeArr(homes)

    # 이분탐색으로 가장 먼 거리 찾기
    left = 0; right = homeArr[-1] - homeArr[0]
    while left <= right:
        mid = (left + right) // 2

        if isPromising(homeArr, mid, routers-1):    
            left = mid+1
        else:
            right = mid-1
    
    return right


print(solution())