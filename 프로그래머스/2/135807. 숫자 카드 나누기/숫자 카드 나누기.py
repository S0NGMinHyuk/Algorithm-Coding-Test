def solution(arrayA, arrayB):
    # 각 배열의 최대공약수 구하기
    gcdA = gcd(arrayA)
    gcdB = gcd(arrayB)
    
    # 각 최대공약수가 상대 배열을 못 나누는 경우, result에 추가
    result = [0]
    for n in arrayA:
        if n % gcdB == 0:
            break
    else:
        result.append(gcdB)
        
    for n in arrayB:
        if n % gcdA == 0:
            break
    else:
        result.append(gcdA)
    
    # result의 최대값 리턴 
    return max(result)


# 배열의 최대공약수를 반환하는 함수
def gcd(arr):
    m = arr[0]
    for n in arr[1:]:
        while n != 0:
            m, n = n, m%n
    return m