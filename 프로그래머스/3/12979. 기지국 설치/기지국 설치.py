def solution(n, stations, w):
    answer = 0
    for i in range(len(stations)+1):
        if i == 0:  # 첫 번째 아파트부터 처음 나오는 기지국 사이에 필요한 기지국 개수 추가
            answer += getNeededStations(stations[i], w, True)
        elif i == len(stations):    # 마지막 기지국부터 마지막 아파트 사이에 필요한 기지국 개수 추가
            answer += getNeededStations(n - stations[-1] + 1, w, True)
        else:   # 기자국과 기지국 사이에 필요한 기지국 개수 추가
            answer += getNeededStations(stations[i] - stations[i-1] + 1, w, False)

    return answer


# 연속된 area칸 안에 도달범위가 scope인 기지국을 몇개 세워야 하는지 리턴하는 함수
def getNeededStations(area, scope, side):
    area -= scope + 1 if side else scope*2+2    # area = 기지국이 필요한 아파트 개수 
    if area <= 0:   # 음수 예외처리
        return 0
    div, mod = divmod(area, scope*2 +1)
    return div if mod == 0 else div+1   # 나머지가 0이면 몫만, 0이 아니면 몫+1을 리턴