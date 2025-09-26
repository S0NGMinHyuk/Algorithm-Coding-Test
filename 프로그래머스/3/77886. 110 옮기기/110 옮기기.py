def solution(s):
    answer = []
    for string in s:
        temp, count = divide110(string)
        result = buildNewNumber(temp, count)
        answer.append(result)
    return answer

# 기존 문자열에서 "110" 추출하고 남은 문자열과 "110"의 개수 리턴
def divide110(string):
    count = 0
    stack = []

    for i in range(len(string)):
        stack.append(string[i])
        if len(stack) >= 3:
            if stack[-3] == '1' and stack[-2] == '1' and stack[-1] == '0':
                count += 1
                for _ in range(3):
                    stack.pop()
            
    return stack, count

    
def buildNewNumber(string, count):
    if len(string) == 0:
        return "110" * count
    
    for i in range(1, len(string)):
        # 기존 문자열에서 "11"이 나오는 경우 앞에 "110"을 모두 추가
        if string[i-1] == string[i] == '1':
            return "".join(string[:i-1]) + "110"*count + "".join(string[i-1:])
    
    # 맨 뒤 값이 "0"이면 뒤에, "1"이면 앞에 "110"을 모두 추가
    if string[-1] == '1':
        return "".join(string[:-1]) + "110"*count + '1'
    else:
        return "".join(string) + "110"*count
    