# 다익스트라 알고리즘(2차원 배열 생성) 방식도 시간초과가 날 수 있다.
# 그럴 땐 2차원 배열 대신 딕셔너리를 사용하자.
from collections import deque

def solution(n, roads, sources, destination):
    # 각 마을에서 이어진 마을의 정보를 담은 딕셔너리 생성
    graph = dict()
    for a, b in roads:
        graph[a] = [b] if a not in graph else graph[a] + [b]
        graph[b] = [a] if b not in graph else graph[b] + [a]
    
    # 목적지에서 각 마을까지 소요되는 시간을 distance 배열에 저장
    distance = [-1] * (n+1)
    distance[destination] = 0
    
    # BFS 알고리즘 사용
    q = deque([destination])
    while len(q) > 0:
        curr = q.popleft()
        for i in graph[curr]:
            if distance[i] == -1:
                distance[i] = distance[curr] + 1
                q.append(i)
    
    # 각 마을에서 목적지까지 걸리는 시간을 배열로 리턴
    return [distance[i] for i in sources]
        
        