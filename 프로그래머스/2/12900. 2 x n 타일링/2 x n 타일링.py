def solution(n):    # solution(n) = solution(n-1) + solution(n-2)
    dict = {1 : 1, 2 : 2}
    for i in range(3, n+1):
        dict[i] = (dict[i-1] + dict[i-2]) % 1000000007
    return dict[n]