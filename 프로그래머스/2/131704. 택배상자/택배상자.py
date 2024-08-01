from collections import deque

def solution(order):
    # 선입선출, 후입선출 자료구조 사용
    queue = deque(list(range(1, len(order)+1)))    
    stack = []
    
    # 실을 수 있는 상자 개수
    load = 0
    
    while load < len(order):
        # 보조 컨테이너에서 실을 수 있는 경우
        if len(stack) > 0 and stack[-1] == order[load]:
            load += 1
            stack.pop()
        # 메인 컨테이터에서 실을 수 있거나, 보조 컨테이너로 보내는 경우
        elif len(queue) > 0:
            if queue[0] == order[load]:
                load += 1
                queue.popleft()
            else:
                stack.append(queue.popleft())
        # 어떤 컨테이너에서도 실을 수 없는 경우
        else:
            break
    
    return load