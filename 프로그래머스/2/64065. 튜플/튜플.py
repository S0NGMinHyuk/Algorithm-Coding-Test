def solution(s):
    # 문자열 s에서 튜플 부분의 문자열을 tuples에 추가
    tuples = []
    for i in range(len(s)-1):
        if s[i] == "{":
            index = i + 1
        elif s[i] == "}":
            tuples.append(s[index:i])
    
    # 길이가 짧은 순서로 튜플 정렬
    tuples.sort(key=lambda x: len(x))
    
    # 맨 앞의 튜플부터 없는 값을 answer에 추가
    answer = []
    for lst in tuples:
        lst = lst.split(",")
        for char in lst:
            if char not in answer:
                answer.append(char)
    
    # 문자 자료형을 숫자 자료형으로 변경
    return list(map(int, answer))