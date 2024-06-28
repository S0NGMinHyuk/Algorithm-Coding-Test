def solution(phone_book):
    phone_book.sort()   # 문자열 정렬을 하면 자기 앞에 오는 문자열만 내 접두어인지 검사하면 된다.
    for i in range(len(phone_book)-1):
        if checkFront(phone_book[i], phone_book[i+1]):  # 접두어가 있으면 false 리턴
            return False
    return True     # 접두어가 없으면 true 리턴

# 문자열 a가 문자열 b의 접두어인지 결과를 반환하는 함수
# 접두어면 true, 아니면 false 리턴
def checkFront(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True