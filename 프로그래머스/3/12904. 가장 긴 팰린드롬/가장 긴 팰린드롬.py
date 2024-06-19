def solution(s):
    for i in range(len(s), 0, -1):
        for j in range(len(s)-i+1):
            answer = checkPalindrome(s[j:j+i])
            if answer > 0:
                return answer
    
    return 1

def checkPalindrome(s):
    left, right = 0, len(s)-1
    while left < right:
        if s[left] == s[right]:
            left += 1 ; right -= 1
        else:
            return 0
    
    return len(s)