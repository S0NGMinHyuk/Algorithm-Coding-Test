def solution(n, wires):
    # 전력망의 정보를 가진 2차원 배열 생성
    graph = [[0]*(n+1) for _ in range(n+1)]
    for w in wires:
        graph[w[0]][w[1]] = 1
        graph[w[1]][w[0]] = 1
    
    # 각각의 전력망이 끊어진 경우의 송전탑의 개수차이를 구하고 최소값 리턴
    result = n
    for w in wires:
        result = min(result, getDiff(graph, w))
    return result

# 선입선출 자료구조 사용
from collections import deque

def getDiff(graph, wire):
    # wire 전력망 끊기
    graph[wire[0]][wire[1]] = 0
    graph[wire[1]][wire[0]] = 0
    
    # 1번 노드부터 시작해서 이어진 노드를 visited 집합에 저장
    visited = set([1])
    q = deque([1])
    while len(q) > 0:
        now = q.popleft()
        for i in range(len(graph)):
            if graph[now][i] == 1 and i not in visited:
                visited.add(i)
                q.append(i)
                
    # wire 전력망 복구하기
    graph[wire[0]][wire[1]] = 1
    graph[wire[1]][wire[0]] = 1
    
    # 송전탑 개수 차이를 리턴
    return abs(len(graph)-1 - len(visited)*2)
    