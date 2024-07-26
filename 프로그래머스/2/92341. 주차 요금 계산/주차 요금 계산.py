def solution(fees, records):
    #  { 자동차 번호 : 총 주차시간 } 형태의 딕셔너리 생성
    parking = dict()
    
    for r in records:
        r = r.split()
        if r[2] == "IN":    # 입차인 경우, 입차 시간을 빼기
            if r[1] not in parking:
                parking[r[1]] = convertTime(r[0]) * (-1)
            else:
                parking[r[1]] -= convertTime(r[0])
        else:               # 출차인 경우, 출차 시간을 더하기
            parking[r[1]] += convertTime(r[0])
    
    answer = []
    # 차량 번호가 작은 순서대로 실행
    for car in sorted(parking.keys()):  
        if parking[car] <= 0:   # 출차하지 않은 경우, 23:59에 출차했다고 간주
            parking[car] += convertTime("23:59")
        
        parking[car] -= fees[0] # 기본 주차 시간 빼기
        cost = fees[1]
        while parking[car] > 0: # 누적 주차 시간만큼 추가요금 증가
            cost += fees[3]
            parking[car] -= fees[2]
        answer.append(cost)
    
    return answer

# HH:MM 형태의 문자열을 00:00부터 몇분이 지났는지 숫자형으로 변환하는 함수
def convertTime(time):
    time = list(map(int, time.split(":")))
    return time[0]*60 + time[1]