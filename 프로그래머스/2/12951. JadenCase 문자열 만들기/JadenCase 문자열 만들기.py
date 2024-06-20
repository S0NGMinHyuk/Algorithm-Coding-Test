def solution(s):
    s = list(s.lower()) # 문자열 s를 모두 소문자로 변경 및 리스트로 변환
    for i in range(len(s)):
        if i == 0:  # 첫 단어 대문자로 변경
            s[i] = s[i].upper()
        if s[i] == " " and i < len(s)-1:    # 공백문자 다음 문자를 대문자로 변경
            s[i+1] = s[i+1].upper()
    return "".join(s)   # 리스트를 문자열로 변경