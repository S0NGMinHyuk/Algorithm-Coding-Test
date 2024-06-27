def solution(msg):
    # 기존 알파벳 26개를 딕셔너리에 추가
    code = dict()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(alphabet)):
        code[alphabet[i]] = i+1
    
    answer = [] 
    idx = 0
    while idx < len(msg):
        key = msg[idx]
        while key in code:      # 현재 문자가 code에 있으면 다음 알파벳도 key에 추가
            value = code[key]   # 현재 key의 코드번호 저장
            idx += 1
            if idx == len(msg): # 두 번째 while문 종료 조건
                break
            key += msg[idx]
        code[key] = len(code)+1 # 새로운 key를 code에 추가
        answer.append(value)
    return answer