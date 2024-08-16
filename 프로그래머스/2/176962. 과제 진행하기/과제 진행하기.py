def solution(plans):
    plans.sort(key=lambda x: x[1])
    stop = []       # 미뤄둔 숙제 스택
    now = 0         # 현재시각
    result = []     # 완료한 숙제 스택
    
    for sub, start, running in plans:
        # 데이터 형태 변경
        start = convertTime(start)
        running = int(running)
        
        # 시간이 남으면 미뤄둔 숙제 하기
        while now < start and len(stop) > 0:
            redo = stop.pop()
            if redo[2] <= start-now:        # 미룬 숙제를 끝낼 수 있는 경우
                now += redo[2]
                result.append(redo[0])
            else:                           # 미룬 숙제를 끝내지 못하는 경우
                redo[2] -= start-now
                stop.append(redo)
                now = start
        
        # 일단 지금 숙제는 미루기
        stop.append([sub, start, running])
        now = start
    
    # 미뤄둔 숙제를 끝내기
    for info in reversed(stop):
        result.append(info[0])
    
    return result
        

# HH:MM 형태의 시간을 분으로 변경해 리턴하는 함수
def convertTime(time):
    time = list(map(int, time.split(":")))
    return time[0]*60 + time[1]