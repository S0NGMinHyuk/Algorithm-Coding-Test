def solution(schedules, timelogs, startday):
    answer = 0
    for goal, logs in zip(schedules, timelogs):
        goal = convertTime(goal) + 10       # 목표 시간
        logs = alignLogs(logs, startday)    # 출근 로그 정렬
        if isSuccess(goal, logs[:5]):       # 평일 출근을 성공했다면 answer 값 증가
            answer += 1
    
    return answer


def convertTime(time) -> int:  # 시간을 분으로 치환
    return (time // 100) * 60 + time % 100

def alignLogs(logs, startday) -> list:  # 로그가 월요일부터 시작하도록 재정렬
    return logs[7-startday+1:] + logs[:7-startday]

def isSuccess(goal, logs) -> bool:  # 평일동안 제시간 출근을 했는지 여부 리턴
    for l in logs:
        if convertTime(l) > goal:
            return False
    return True