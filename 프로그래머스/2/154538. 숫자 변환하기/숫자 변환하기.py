# BFS 알고리즘 사용
from collections import deque

def solution(x, y, n):  
    q = deque([[y, 0]]) 
    
    while len(q) > 0:
        num, cnt = q.popleft()
        if num == x:    # y에서 x를 만든 경우, 연산 횟수 리턴
            return cnt
        else:           # y에서 x를 갈 수 있는 가능성이 있는 연산을 q에 추가
            if num%2 == 0 and num/2 >= x:
                q.append([num/2, cnt+1])
            if num%3 == 0 and num/3 >= x:
                q.append([num/3, cnt+1])
            if num-n >= x:
                q.append([num-n, cnt+1])
    
    return -1   # y에서 x를 만들 수 없다면 -1 리턴