def solution(play_time, adv_time, logs):
    play_time = convert2int(play_time)
    adv_time = convert2int(adv_time)
    timezone = [0] * (100*60*60)
    
    # 누적합 사용
    for log in logs:
        log = log.split("-")
        start = convert2int(log[0])
        end = convert2int(log[1])
        timezone[start] += 1
        timezone[end] -= 1 
    for i in range(1, len(timezone)):
        timezone[i] += timezone[i-1]
    
    # 투포인터 사용
    left = 0
    right = 0
    top = 0
    current = 0
    answer = 0
    while right < play_time:
        current += timezone[right]
        if right - left == adv_time: # 광고 길이와 같다는 건 초과했다는 뜻
            current -= timezone[left]
            left += 1
        if current > top: # answer 갱신
            top = current
            answer = left
        right += 1
    
    return convert2string(answer)

# hh:mm:ss 형태의 시간을 초로 변환하는 함수
def convert2int(time):
    hour, minute, second = map(int, time.split(":"))
    return second + minute*60 + hour*60*60

# 초 형태의 시간을 hh:mm:ss로 변환하는 함수
def convert2string(time):
    hour = time // (60*60)
    time %= 60*60
    minute = time // 60
    time %= 60
    return f"{hour:02}:{minute:02}:{time:02}"
