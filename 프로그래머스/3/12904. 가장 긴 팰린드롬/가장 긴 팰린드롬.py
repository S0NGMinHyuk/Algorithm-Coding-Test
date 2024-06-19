# 문자열 길이를 하나씩 줄여가며 펠린드롬이 있는지 검사하는 방식
# n의 최대값이 2500이기 때문에 O(N^2) 시간복잡도 사용 가능
def solution(s):
    for i in range(len(s), 0, -1):
        for j in range(len(s)-i+1):
            answer = checkPalindrome(s[j:j+i])
            if answer > 0:
                return answer

# 펠린드롬 검사 함수. 성공시 문자열 길이, 실패시 0 리턴
def checkPalindrome(s): 
    left, right = 0, len(s)-1
    while left < right:
        if s[left] == s[right]:
            left += 1 ; right -= 1
        else:
            return 0
    
    return len(s)
