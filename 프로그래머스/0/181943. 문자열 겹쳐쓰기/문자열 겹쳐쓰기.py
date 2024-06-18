def solution(my_string, overwrite_string, s):
    answer = ''
    i = 0
    while(i < len(my_string)):
        if i >= s and i < s + len(overwrite_string):
            answer += overwrite_string[i-s]
        else:
            answer += my_string[i]
        i += 1
    return answer