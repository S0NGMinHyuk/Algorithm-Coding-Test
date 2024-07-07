def solution(record):
    userId = {} # 사용자 아이디에 따른 닉네임 저장
    log = []    # 채팅창 로그
    for info in record:
        info = info.split()         # 띄어쓰기로 구분
        if info[0] == "Enter":      # 사용자가 들어온 경우
            log.append([info[0], info[1]])
            userId[info[1]] = info[2]
        elif info[0] == "Leave":    # 사용자가 나간 경우
            log.append([info[0], info[1]])
        elif info[0] == "Change":   # 사용자가 닉네임을 변경한 경우
            userId[info[1]] = info[2]
    
    answer = []
    for command, uid in log:        # 로그에 따라 채팅창 출력
        if command == "Enter":
            answer.append(f"{userId[uid]}님이 들어왔습니다.")
        else:
            answer.append(f"{userId[uid]}님이 나갔습니다.")
            
    return answer