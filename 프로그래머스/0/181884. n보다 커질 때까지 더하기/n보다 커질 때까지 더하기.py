def solution(numbers, n):
    answer = 0
    index = 0
    
    # 원소의 총합이 n 이하이고, index가 배열의 길이보다 작은 경우
    while answer <= n and index < len(numbers):
        answer += numbers[index]
        index += 1
        
    return answer