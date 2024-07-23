def solution(word):
    answer = 0
    aeiou = 'AEIOU'

    for i, num in enumerate(word):
        if i == 0:
            answer += aeiou.index(num) *781 +1
        elif i == 1:
            answer += aeiou.index(num) *156 +1
        elif i == 2:
            answer += aeiou.index(num) *31 +1
        elif i == 3:
            answer += aeiou.index(num) *6 +1
        else:
            answer += aeiou.index(num) +1
    
    return answer