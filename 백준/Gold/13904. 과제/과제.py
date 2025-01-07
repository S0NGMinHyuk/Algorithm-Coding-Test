import sys
from heapq import heappop, heappush

# 과제 정보를 "남은 일수 : [점수들]" 형태의 딕셔너리로 리턴하는 함수
def getInfo():
    n = int(sys.stdin.readline())
    info = dict()

    for _ in range(n):
        expDate, score = list(map(int, sys.stdin.readline().split()))
        if expDate not in info: info[expDate] = [score]
        elif expDate in info:   info[expDate].append(score)

    return info


def solution():
    info = getInfo()    # 과제 정보 받기
    scoreList = []      # 웅찬이가 받을 점수 배열
    now = 1             # 현재 날짜

    for expTime in sorted(info.keys()):
        for score in sorted(info[expTime], reverse=True):
            if expTime < now:                   # 만료 기간이 지난 경우
                if score > scoreList[0]:        # 이미 했던 과제 중 점수가 더 낮은 게 있다면
                    heappop(scoreList)          # 해당 과제를 하지 말고
                    heappush(scoreList, score)  # 이번 과제를 수행
            
            elif expTime >= now:                # 아직 만료 기간이 남은 경우
                heappush(scoreList, score)      # 해당 과제 수행
                now += 1                        # 과제를 수행했으니 now 날짜 1 증가
    
    return sum(scoreList)   # 수행한 과제 점수의 총합 리턴

print(solution())