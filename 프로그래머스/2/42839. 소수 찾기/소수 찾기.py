# 완전 탐색은 재귀함수를 고려해보기

def solution(numbers):
    # 문자열 속 숫자를 리스트 자료형으로 분리
    num_lst = list(numbers)
    answer = set(makeNum("", num_lst))  # 재귀 호출
    return len(answer)

# lst로 만들 수 있는 수를 재귀방식으로 모두 만드는 함수
def makeNum(num, lst):
    # 모든 숫자를 사용하지 않은 경우, 현재 숫자가 소수인지 검사 후 숫자 만들기
    if len(num) < len(lst): 
        # 현재 숫자가 소수인지 검사
        answer = [int(num)] if isPrime(num) else []
        # 재귀 호출로 이후 값 만들기
        for i in range(len(lst)):
            if lst[i] != None:
                temp = lst[i]
                lst[i] = None
                answer += makeNum(num+temp, lst)
                lst[i] = temp
        return answer
    # Base Case
    # 모든 숫자를 사용한 경우, 현재 숫자가 재귀인지 검사 후 리턴
    else:
        return [int(num)] if isPrime(num) else []

# num이 소수인지 검사하는 함수
def isPrime(num):
    if num == "":
        return False
    
    num = int(num)
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    
    return True