from collections import deque

def solution(priorities, location):
    # priorities 배열을 가지고 [location, priority] 배열을 원소로 하는 큐 생성
    q = deque([])
    for i in range(len(priorities)):
        q.append([i, priorities[i]])
    
    # max 함수 대신 사용하기 위해 priorities 배열을 내림차순으로 정렬
    priorities.sort(reverse=True)
    
    # order = 프로세스가 실행되는 순서
    order = 0
    while 1:
        idx, priority = q.popleft()
        if priority == priorities[order]:   # 현재 프로세스의 우선도가 가장 높은 경우
            if idx == location:             # 내가 원하던 프로세스인 경우, 반복문 종료
                break
            else:
                order += 1                  # 현재 프로세스를 실행, order 1 증가
        else:
            q.append([idx, priority])       # 우선도가 가장 높지 않은 경우 맨 뒤에 추가
    
    return order+1