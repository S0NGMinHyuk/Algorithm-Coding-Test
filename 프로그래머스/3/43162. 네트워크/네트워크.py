def solution(n, computers):
    visited = set()
    connection = 0
    # 모든 노드를 대상으로 연결된 커넥션을 탐색
    for i in range(n):
        if i not in visited:
            visited |= getConnection(i, computers)
            connection += 1
    # 커넥션 개수 리턴
    return connection

# 선입선출 큐 자료구조 사용
from collections import deque

# node와 연결된 모든 노드를 담은 집합 리턴
def getConnection(node, graph):
    visited = set([node])
    q = deque([node])
    while len(q) > 0:   # BFS 알고리즘
        now = q.popleft()
        for i in range(len(graph[now])):
            if graph[now][i] == 1 and i not in visited:
                visited.add(i)
                q.append(i)
    return visited