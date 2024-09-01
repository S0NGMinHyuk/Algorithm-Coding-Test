def solution(arr):
    for i in range(len(arr)):
        
        # 50 미만 홀수인 경우
        if arr[i] < 50 and arr[i] % 2 == 1:
            arr[i] *= 2
            
        # 50 이상 짝수인 경우
        elif arr[i] >= 50 and arr[i] % 2 == 0:
            arr[i] /= 2
            
    return arr