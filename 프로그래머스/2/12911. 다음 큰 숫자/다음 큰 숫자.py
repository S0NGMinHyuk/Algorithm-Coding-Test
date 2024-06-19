def solution(n):
    cnt = bin(n)[2:].count('1')     # 2진수로 변경하는 함수 + 1의 개수를 세는 함수
    while True:
        n += 1
        if cnt == bin(n)[2:].count('1'):    # n을 1씩 증가하며 cnt와 같은 수가 나오면 return
            return n