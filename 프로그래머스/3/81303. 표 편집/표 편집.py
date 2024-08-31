def solution(n, k, cmd):
    # 모든 노드를 가진 연결리스트 생성
    link = dict()
    for i in range(n):
        if i == 0:
            link[i] = [None, i+1]
        elif i == n-1:
            link[i] = [i-1, None]
        else:
            link[i] = [i-1, i+1]
    
    # 현재 노드와 삭제된 노드를 저장하는 스택 선언
    curr = k
    deleted = []
    
    # 명령어에 따른 기능 수행
    for c in cmd:
        if len(c) > 1:      # 행 이동 명령어인 경우
            direct, move = c.split()
            move = int(move)
            while move > 0:
                curr = link[curr][0 if direct == "U" else 1]
                move -= 1
        else:
            if c == "C":    # 행 삭제 명령어인 경우, 연결리스트 끊고 curr 이동하기
                deleted.append(curr)
                if link[curr][0] == None:   # 맨 앞 노드인 경우
                    link[link[curr][1]][0] = link[curr][0]
                    curr = link[curr][1]
                elif link[curr][1] == None: # 맨 뒤 노드인 경우
                    link[link[curr][0]][1] = link[curr][1]
                    curr = link[curr][0]
                else:                       # 사이에 낀 노드인 경우
                    link[link[curr][1]][0] = link[curr][0]
                    link[link[curr][0]][1] = link[curr][1]
                    curr = link[curr][1]
            elif c == "Z":  # 행 복구 명령어인 경우, 연결리스트 잇기
                revive = deleted.pop()
                if link[revive][0] == None:     # 맨 앞 노드인 경우
                    link[link[revive][1]][0] = revive
                elif link[revive][1] == None:   # 맨 뒤 노드인 경우
                    link[link[revive][0]][1] = revive
                else:                           # 사이에 낀 노드인 경우
                    link[link[revive][1]][0] = revive
                    link[link[revive][0]][1] = revive
    
    # 모든 명령어 수행 수 결과 리턴하기
    result = ["O"]*n
    for i in deleted:
        # 삭제된 행은 "X"로 변경
        result[i] = "X" 
    
    return "".join(result)