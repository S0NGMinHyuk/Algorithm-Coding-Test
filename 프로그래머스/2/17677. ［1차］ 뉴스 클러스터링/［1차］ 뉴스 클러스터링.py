def solution(str1, str2):
    str1 = str1.upper() ; str2 = str2.upper()   # 두 문자열 모두 대문자로 변경

    str1_dict = dict()
    str1_length = 0             # str1의 원소 개수
    for i in range(len(str1)-1):
        word = str1[i:i+2]
        if word.isalpha():      # 두 글자씩 떼어낸 문자가 영어일 경우 딕셔너리에 개수 추가
            str1_dict[word] = 1 if word not in str1_dict else str1_dict[word]+1 
            str1_length += 1    # 원소 개수 1 증가
    
    str2_length = 0             # str2의 원소 개수
    same = 0                    # 합집합 개수
    for i in range(len(str2)-1):
        word = str2[i:i+2]
        if word.isalpha():      # 두 글자씩 떼어낸 문자가 영어일 경우
            str2_length += 1    # 원소 개수 1 증가
            if word in str1_dict and str1_dict[word] > 0:   # 합집합인 경우 처리
                str1_dict[word] -= 1
                same += 1
    
    # str1과 str2가 모두 공집합인 경우 65536 출력
    return int(same / (str1_length + str2_length - same) * 65536) if (str1_length + str2_length - same) > 0 else 65536