def solution(numbers):
    answer = []
    for num in numbers:
        binary = getBinary(num)
        answer.append(int(isPossible(binary))) 
    return answer


# 이진트리로 표현이 가능한지 여부를 리턴하는 함수
def isPossible(binary) -> bool:
    if len(binary) == 1: # base case
        return True
    
    mid = len(binary) // 2
    if binary[mid] == 0: # 중간값이 0이면, 모두 0이어야 트리로 표현 가능
        return sum(binary) == 0
    else: # 중간값이 1이면, 좌우가 모두 트리로 표현이 가능한 경우에만 True 리턴
        left = binary[:mid]
        right = binary[mid+1:]
        return isPossible(left) and isPossible(right)


# 10진수의 값을 2진수 리스트로 리턴하는 함수
def getBinary(num) -> list:
    lst = list()
    length = 2
    while num > 0:
        lst.append(num%2)
        num = num // 2
        if len(lst) == length:
            length *= 2
    for _ in range(len(lst), length-1): # 리스트 길이를 (2**n)-1로 맞추기
        lst.append(0)
    return lst[::-1]
