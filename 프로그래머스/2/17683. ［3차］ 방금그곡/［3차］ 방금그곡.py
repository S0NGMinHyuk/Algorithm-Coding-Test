def solution(m, musicinfos):
    answer = []
    listen = getMelody(m)               # 들은 멜로디
    for order, info in enumerate(musicinfos):
        info = info.split(",")
        melody = getMelody(info[3])         # 노래 악보
        time = getTime(info[0], info[1])    # 노래 재생시간
        for i in range(time):
            idx = 0
            # 악보와 들은 노래의 음이 같으면 idx 1 증가
            while melody[(i + idx) % len(melody)] == listen[idx % len(listen)]: 
                idx += 1
                if idx == len(listen):      # 사용자가 들은 멜로디가 있는 경우
                    answer.append((time, order, info[2]))
                    break
    
    if len(answer) > 0:     # 정답 음악이 있는 경우, 재생 길이 > 나온 순서 순으로 정렬
        answer.sort(key=lambda x : (-x[0], x[1]))
        return answer[0][2]
    else:                   # 정답 음악이 없는 경우
        return "(None)"

# 시작 시간과 종료 시간 사이가 몇분인지 리턴하는 함수 (시간은 HH:MM 형태)
def getTime(start, end):
    start = list(map(int, start.split(":")))
    end = list(map(int, end.split(":")))
    return (end[0] - start[0]) * 60 + end[1] - start[1]

# 멜로디 문자열 m에서 각 음을 떼어내 리스트로 리턴하는 함수
def getMelody(m):
    index = 0
    melody = []
    while index < len(m)-1:
        if m[index+1] == "#":   # 다음 음이 #이면 같이 추가
            melody.append(m[index:index+2])
            index += 2
        else:
            melody.append(m[index])
            index += 1
    if index < len(m):          # 마지막 음이 #이 아닌 경우 추가
        melody.append(m[index])

    return melody