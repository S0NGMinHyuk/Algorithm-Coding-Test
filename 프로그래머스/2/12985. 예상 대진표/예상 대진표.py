def solution(n,a,b):
    answer = 0

    while a != b:
        a = (a+1) // 2 ; b = (b+1) // 2 # 다음라운드에서 자신의 번호 저장
        answer += 1                     # 라운드 추가

    return answer