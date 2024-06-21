# Merge Sort의 변형 로직 - divide & conquer 알고리즘
def solution(arr):
    if len(arr) > 2:    # 배열 길이가 2 초과면 divide
        return lcm(solution(arr[:len(arr)//2]), solution(arr[len(arr)//2:]))
    elif len(arr) == 2: # 배열 길이가 2 이하면 conquer
        return lcm(arr[0], arr[1])
    elif len(arr) == 1:
        return arr[0]

# 최소공배수를 리턴하는 함수
def lcm(a, b):
    multi = a*b

    # 최대공약수를 찾는 방법. b가 0일 때 a가 최대공약수
    while b > 0:    
        div, mod = divmod(a, b)
        a, b = b, mod
    
    # a와 b의 최대공배수 = a * b / gcd(a, b)
    return multi // a