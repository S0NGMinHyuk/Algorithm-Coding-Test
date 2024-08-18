def solution(n, t, m, timetable):
    timetable.sort(reverse=True)
    
    bustime = 9*60              # 버스시간
    capacity = m                # 탈 수 있는 인원
    answer = bustime + (n-1)*t  # 초기값은 맨 마지막 차의 출발시간으로 설정
    

    while timetable:
        man = convertTime(timetable.pop(), True)
        while man > bustime and n > 0:      # 맨 앞 사람의 도착시간이 버스 출발시간 이후인 경우
            n -= 1                          # 현재 버스 출발
            bustime += t                    # 다음 버스 출발시간으로 변경
            capacity = m                    # 탑승가능인원 초기화
        
        capacity -= 1           # 맨 앞사람 탑승
        if capacity == 0:       # 승객이 모두 찼을 경우
            if n > 1:           # 마지막 버스가 아니면 버스 보내기
                n -= 1
                bustime += t
                capacity = m
            elif n == 1:        # 마지막 버스인 경우, 콘이 현재사람보다 1분 일찍 도착하게 변경 후 종료
                answer = man-1
                break
            else:               # 이미 버스가 없는 경우, 반복문 종료
                break
    
    # 콘의 도착시간을 리턴
    return convertTime(answer, False)
            
    
# HH:MM <-> 분 으로 변경하는 함수
def convertTime(time, mode):
    if mode:
        time = list(map(int, time.split(":")))
        return time[0]*60 + time[1]
    else:
        hour = str(time//60)
        minute = str(time%60)
        if len(hour) == 1:
            hour = "0"+hour
        if len(minute) == 1:
            minute = "0"+minute
        return hour+":"+minute