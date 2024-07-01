def solution(progresses, speeds):
    answer = []     # 정답 리스트
    i = 0           # 맨 앞에 있는 작업 인덱스
    while i < len(progresses):  # 모든 프로그레스가 끝날 때까지 반복
        # time = 맨 앞에 있는 일을 끝내기 위해 필요한 시간 
        time = (100-progresses[i])/speeds[i]   
        if int(time) != time:
            time = int(time)+1
        
        cnt = 0
        # 맨 앞에 있는 작업을 배포할 때 같이 배포할 수 있는 작업인 경우
        while(progresses[i] + speeds[i]*time) >= 100:
            i += 1 ; cnt += 1  
            if i == len(progresses):
                break
            
        answer.append(cnt)
    
    return answer