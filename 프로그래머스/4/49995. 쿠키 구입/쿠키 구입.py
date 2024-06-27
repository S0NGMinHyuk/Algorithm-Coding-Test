def solution(cookie):
    answer = 0
    for i in range(len(cookie)-1):
        left, right = i, i+1                        # 투포인터 알고리즘
        lsum, rsum = cookie[left], cookie[right]    # 해당 위치의 과자 한 개만 주는 것으로 시작
        while 1:
            if lsum == rsum:                        # 양쪽의 합이 같을 때 answer 갱신 후 right 1 추가
                answer = lsum if lsum > answer else answer
                right += 1
                if right >= len(cookie):
                    break
                rsum += cookie[right]
            elif lsum < rsum:                       # lsum이 작으면 left 1 감소 후 해당 자리 값 추가
                left -= 1
                if left < 0:
                    break
                lsum += cookie[left]
            else: # lsum > rsum:                    # rsum이 작으면 right 1 증가 후 해당 자리 값 추가
                right += 1
                if right >= len(cookie):
                    break
                rsum += cookie[right]
    return answer