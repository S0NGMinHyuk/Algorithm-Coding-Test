from collections import deque

def getParent(union, i):
    while union[i] != i:
        i = union[i]
    return i

def getMSTtree(n, paths, union, gSet, sSet):
    tree = { i:[] for i in range(1, n+1) }
    edges = 0

    for a, b, w in paths:
        if edges == n-1: break
        elif a in gSet and b in gSet: continue
        elif a in sSet and b in sSet: continue
        
        pA = getParent(union, a)
        pB = getParent(union, b)

        if pA == pB:  continue
        elif pA < pB: union[pB] = pA
        elif pA > pB: union[pA] = pB
        
        # a와 b에게 각각 모서리 정보 추가
        tree[a].append([b, w])
        tree[b].append([a, w])
        edges += 1
    
    return tree


def getAnswerByBFS(start, tree, answer, startSet, endSet):
    q = deque([[start, 0]])
    visited = set()
    while len(q) > 0:
        node, weight = q.popleft()
        visited.add(node)
        if node in endSet:
            if weight < answer[1]:
                answer = [node, weight]
            elif node < answer[0] and weight == answer[1]:
                answer = [node, weight]
        else:
            for nexthop in tree[node]:
                if nexthop[0] in visited or nexthop[0] in startSet:
                    continue
                weight = max(weight, nexthop[1])
                q.append([nexthop[0], weight])
    return answer


def solution(n, paths, gates, summits):
    # 크루스칼 알고리즘 사용
    union = { i : i for i in range(1, n+1) }
    paths.sort(key=lambda x: x[2])
    gateSet = set(gates)
    summitSet = set(summits)
    
    tree = getMSTtree(n, paths, union, gateSet, summitSet)       
    
    answer = [50000, 10000000]
    for g in gates:
        answer = getAnswerByBFS(g, tree, answer, gateSet, summitSet)
    
    return answer