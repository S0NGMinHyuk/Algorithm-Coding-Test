def solution(files):
    data = []
    for name in files:      
        info = [name]       # 파일 이름 저장
        toggle = True   
        start = 0
        for i in range(len(name)):
            if toggle and name[i].isdigit():
                info.append(name[start:i].upper())      # 파일 HEAD 저장
                start = i
                toggle = False
            elif not toggle and not name[i].isdigit():  
                info.append(int(name[start:i]))         # 파일 NUMBER 저장
                info.append(name[i:])                   # 파일 TAIL 저장
                break
        else:   # 파일의 TAIL이 없는 경우
            info.append(int(name[start:]))              # 파일 NUMBER 저장
            info.append("")                             # 파일 TAIL 저장

        # name의 데이터(info)를 data에 저장
        data.append(info)

    # HEAD, NUMBER 순으로 정렬 후 파일 이름만 출력
    data.sort(key = lambda x : (x[1], x[2]))
    return [info[0] for info in data]
