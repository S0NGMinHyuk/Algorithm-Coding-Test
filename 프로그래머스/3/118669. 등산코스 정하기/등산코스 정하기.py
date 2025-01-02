from collections import deque


# 연결된 조합의 부모 노드를 리턴하는 함수
def getParent(union, i):
    while union[i] != i:
        i = union[i]
    return i


# paths 정보에서 최소신장트리를 구성하는 모서리 정보를 반환하는 함수
# by 크루스칼 알고리즘
def getMSTtree(n, paths, gSet, sSet):
    union = { i : i for i in range(1, n+1) }    # 연결된 노드들의 정보를 저장
    tree = { i:[] for i in range(1, n+1) }      # 반환할 모서리의 정보를 저장
    edges = 0                                   # 연결된 모서리의 개수

    # 모서리를 가중치 기준 오름차순으로 정렬 후 순차 탐색
    paths.sort(key=lambda x: x[2])
    for a, b, w in paths:
        if edges == n-1: break                  # 이미 최소신장트리가 완성된 경우
        elif a in gSet and b in gSet: continue  # 봉우리와 봉우리 혹은 입구와 입구가
        elif a in sSet and b in sSet: continue  # 연결된 모서리는 사용하지 못하기 때문에 skip
        
        pA = getParent(union, a)        # a와 b가 속한 조합의 루트노드값 저장
        pB = getParent(union, b)

        if pA == pB:  continue          # 같은 조합인 경우는 skip
        elif pA < pB: union[pB] = pA    # 다른 조합인 경우는 루트노드가
        elif pA > pB: union[pA] = pB    # 더 작은 쪽으로 합병한다.
        
        tree[a].append([b, w])      # a와 b에게 
        tree[b].append([a, w])      # 각각 모서리 정보 추가 
        edges += 1                  # + 모서리 개수 증가
    
    # 최소신장트리 반환
    return tree


# BFS 알고리즘을 통해 start 지점에서 endSet까지의 
# intensity를 찾고 answer 값을 갱신하는 함수
def getAnswerByBFS(start, tree, answer, startSet, endSet):
    q = deque([[start, 0]])
    visited = set()         # 무한루프를 방지하기 위해 방문 정보 저장

    while len(q) > 0:
        node, weight = q.popleft()  # 큐에서 현재 위치 가져오기
        visited.add(node)           # 방문 정보에 현재 위치 추가

        # 현재 위치가 종료지점인 경우, answer 갱신
        if node in endSet:
            if weight < answer[1]:
                answer = [node, weight]
            elif node < answer[0] and weight == answer[1]:
                answer = [node, weight]
        # 현재 위치가 쉼터인 경우
        else:
            for nexthop in tree[node]:                              # 다음 모서리 정보를 가져오고
                if nexthop[0] in visited or nexthop[0] in startSet: # 다음 노드가 방문했거나 출발지역이면
                    continue                                        # skip 한다.
                
                weight = max(weight, nexthop[1])    # intensity 값을 갱신 후
                q.append([nexthop[0], weight])      # 큐에 다음 위치 정보 추가
    
    # 결과 반환
    return answer


def solution(n, paths, gates, summits):
    gateSet = set(gates)
    summitSet = set(summits)
    answer = [50000, 10000000]
    
    # 최소신장트리 get
    tree = getMSTtree(n, paths, gateSet, summitSet)       
    
    # 모든 출발지에 따른 answer값 갱신
    for g in gates:
        answer = getAnswerByBFS(g, tree, answer, gateSet, summitSet)
    
    return answer