# 큐 알고리즘 FIFO 사용
from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)    # 큐 자료형으로 변환
    sec = 1             # 총 소요시간
    q = deque([])       # 현재 다리를 지나는 무게
    onTheBridge = 0     # 현재 다리 위 무게
    while 1:
        # 다리를 다 지난 트럭인 경우
        if len(q) > 0 and q[0][1] <= sec - bridge_length:
            onTheBridge -= q[0][0]
            q.popleft()
        # 다리에 트럭이 들어오는 경우
        if len(truck_weights) > 0 and truck_weights[0] <= weight-onTheBridge:
            q.append([truck_weights[0], sec])
            onTheBridge += truck_weights[0]
            truck_weights.popleft()
        
        # while문 종료 조건
        if len(q) == 0 and len(truck_weights) == 0:
            break
        else:
            sec += 1    # 소요시간 1초 증가

    return sec