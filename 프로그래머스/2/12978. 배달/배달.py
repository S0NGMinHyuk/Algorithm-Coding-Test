# BFS 알고리즘을 위한 큐 호출
from collections import deque

def solution(N, road, K):
    # 각 노드의 연결을 2차원 리스트에 저장. 중복 간선은 최소값을 저장
    table = [[0]*N for _ in range(N)]
    for a, b, weight in road:
        a -= 1 ; b -= 1
        if table[a][b] == 0 or weight < table[a][b]:
            table[a][b] = weight
        if table[b][a] == 0 or weight < table[b][a]:
            table[b][a] = weight
    
    # 1번 노드에서 배달 소요시간을 담을 리스트
    lst = [float("inf")]*N
    lst[0] = 0
    
    # BFS 알고리즘 사용
    q = deque([0])
    while len(q) > 0:
        start = q.popleft()
        for i in range(N):
            # 현재 위치에서 배달 가능한 노드 중 현재 위치에서 배달하는 게 최소 소요시간인 경우
            if table[start][i] > 0 and lst[start] + table[start][i] < lst[i]:
                lst[i] = lst[start] + table[start][i]   # 배달 소요시간 갱신
                q.append(i)                             # 도착지를 큐에 추가
    
    # 모든 노드 중 K시간 이내에 배달할 수 있는 노드를 세고 출력
    answer = 0
    for i in range(N):
        if lst[i] <= K:
            answer += 1
    
    return answer