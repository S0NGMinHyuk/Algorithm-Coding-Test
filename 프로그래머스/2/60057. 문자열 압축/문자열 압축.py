def solution(s):
    answer = len(s)
    for length in range(1, len(s)//2+1):
        comp_len = 0    # 압축된 문자열 길이
        index = 0       # 인덱스
        dup = 1         # 중복되는 횟수
        while index < len(s):
            # 문자열이 중복되는 경우
            if s[index : index+length] == s[index+length : index+2*length]:
                dup += 1
            # 문자열이 중복되지 않는 경우
            else:
                if dup == 1:
                    comp_len += len(s[index : index+length])
                else:
                    comp_len += len(s[index : index+length]) + len(str(dup))
                dup = 1                 # dup 초기화
            index += length             # index 위치 변경
            
        answer = min(answer, comp_len)  # answer 갱신
        
    return answer