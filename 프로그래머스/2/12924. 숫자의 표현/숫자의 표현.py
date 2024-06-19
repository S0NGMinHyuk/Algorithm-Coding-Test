def solution(n):
    answer = 1
    for i in range(1, n//2+1):  # n 절반 이하 값부터 시작
        temp = i
        for j in range(i+1, n+1):   # i 다음 값을 차례대로 더하기
            temp += j
            if temp < n:    # 여전히 작으면 continue
                continue
            elif temp == n: # n과 같으면 answer 1 증가하고 종료
                answer += 1
                break
            else:           # n 초과하면 종료
                break
    return answer