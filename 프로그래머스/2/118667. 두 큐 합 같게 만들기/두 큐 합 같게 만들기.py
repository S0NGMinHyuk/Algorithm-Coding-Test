# 선입선출 알고리즘 사용
from collections import deque

def solution(queue1, queue2):
    MAXLEN = (len(queue1) + len(queue2)) * 2    # 최대 반복횟수.
    one = sum(queue1) ; two = sum(queue2)       # 각 큐의 총합
    q1 = deque(queue1)
    q2 = deque(queue2) 
    
    # 총합이 더 큰 큐에서 값을 빼서 총합이 더 작은 큐에 더한다.
    cnt = 0
    while cnt <= MAXLEN and one != two:
        if one < two:
            num = q2.popleft()
            q1.append(num)
            two -= num ; one += num
        else:
            num = q1.popleft()
            q2.append(num)
            one -= num ; two += num
        cnt += 1
    
    # 최대 반복횟수인 경우는 실패한 경우
    return cnt if cnt <= MAXLEN else -1