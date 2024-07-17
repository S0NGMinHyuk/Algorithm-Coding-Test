def solution(a):
    MIN = min(a)
    answer = getCount(a, MIN) + getCount(a[::-1], MIN)
    return answer + 1 # 1은 MIN의 경우를 추가한 것.

def getCount(a, MIN):
    count = 0
    left = None
    for num in a:
        if num == MIN:
            break
        if left == None or num < left:
            left = num
            count += 1
    return count