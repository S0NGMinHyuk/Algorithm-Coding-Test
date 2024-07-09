from collections import deque

def solution(n, edge):
    # 노드와 엣지 정보를 담은 딕셔너리 생성
    graph = {i: [] for i in range(n)}
    for a, b in edge:
        a -= 1; b -= 1
        graph[a].append(b)
        graph[b].append(a)
    
    answer = 0          # 최대 거리에 있는 노드 개수
    maxDistance = 0     # 최대 거리
    visited = set([0])  # 이미 방문한 노드 집합
    q = deque([[0, 0]]) # [노드 번호, 1번 노드부터의 거리]
    while len(q) > 0:   # BFS 알고리즘 사용
        now, distance = q.popleft()
        if distance > maxDistance:  # 최대 거리보다 더 먼 거리인 경우
            maxDistance = distance  # 최대 거리 갱신
            answer = 1              # 최대 거리에 있는 노드는 now 1개
        elif distance == maxDistance:   # 최대 거리에 있는 또다른 노드인 경우
            answer += 1                 # 최대 거리에 있는 노드 개수 증가
        
        # 현재 노드와 이어진 다른 노드 중 미방문 노드를 q에 추가
        for i in graph[now]:
            if i not in visited:
                visited.add(i)
                q.append([i, distance+1])
    return answer        