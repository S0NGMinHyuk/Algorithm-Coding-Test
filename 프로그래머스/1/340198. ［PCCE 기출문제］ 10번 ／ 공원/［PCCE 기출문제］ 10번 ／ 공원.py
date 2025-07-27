def solution(mats, park):
    convert(park)
    size = getMaxSize(park)
    for n in sorted(mats, reverse=True):    # 갖고 있는 돗자리 중 최대 크기 리턴
        if size >= n:
            return n
    else:
         return -1   


def convert(park):  # 알파벳을 0, "-1"을 1로 변경
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "-1":
                park[i][j] = 1
            else:
                park[i][j] = 0
                

def getMaxSize(park):   # 깔 수 있는 가장 큰 정사각형 돗자리의 길이 리턴
    size = 1
    for i in range(1, len(park)):
        for j in range(1, len(park[i])):
            if park[i][j] != 0:
                park[i][j] = min(park[i-1][j], park[i][j-1], park[i-1][j-1]) + 1
            size = max(park[i][j], size)
    return size