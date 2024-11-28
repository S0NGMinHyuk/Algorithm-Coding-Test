def is_palindrome(s):
    return s == s[::-1]
 
def is_similary(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            temp1 = s[left+1:right+1]
            temp2 = s[left:right]
            return is_palindrome(temp1) or is_palindrome(temp2)
        left += 1
        right -= 1
    return False
 
T = int(input())
 
for i in range(T):
    s = input()
    
    if is_palindrome(s):
        print(0)
    elif is_similary(s):
        print(1)
    else:
        print(2)