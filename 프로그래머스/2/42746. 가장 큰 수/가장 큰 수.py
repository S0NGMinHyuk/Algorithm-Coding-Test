def solution(numbers): 
    numbers = list(map(str, numbers))   # 숫자를 문자열로 변경
    # 최대값이 1000이므로 x*3을 해서 비교 (9 -> 999)
    numbers.sort(key = lambda x : x*3, reverse = True) 
    
    # numbers가 [0, 0] 인 경우를 대비해 숫자로 바꿨다가 다시 문자로 변경
    return str(int(''.join(numbers)))