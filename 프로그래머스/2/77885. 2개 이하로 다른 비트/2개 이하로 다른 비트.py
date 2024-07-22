def solution(numbers):
    answer = []
    for x in numbers:
        arr = list('0'+bin(x)[2:])          # 숫자를 이진수 배열로 변경
        index = ''.join(arr).rfind('0')     # 마지막 0의 위치
        arr[index] = '1'                    # 마지막 0의 위치를 1로 변경
        if x % 2 != 0:                      # x가 홀수인 경우
            arr[index+1] = '0'              # 마지막 0의 위치 다음 값을 0으로 변경
        answer.append(int(''.join(arr), 2)) # 2진수를 10진수로 변환
    return answer