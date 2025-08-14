import sys
sys.setrecursionlimit(10**6)

def solution(a, edges):
    def createGraph(): # 트리 생성 함수
        graph = dict()
        for a, b in edges:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
        return graph
    
    def dfs(node, parent):
        global turn
        
        # 리프노드인 경우, 자신의 가중치를 부모에게 더하기 (base case)
        if len(graph[node]) == 1 and graph[node][0] == parent:
            turn += abs(a[node])
            a[parent] += a[node]
            return
        
        # 중간노드인 경우, 자식노드로 dfs 호출
        for child in graph[node]:
            if child != parent:
                dfs(child, node)
        
        # 자신의 가중치를 부모에게 더하기
        turn += abs(a[node])
        if parent != None:
            a[parent] += a[node]
        return
    
    graph = createGraph()
    global turn
    turn = 0
    root = 0
    dfs(root, None)
    return turn if a[root] == 0 else -1 # root 노드의 가중치가 0이면 모든 정점의 가중치가 0이다.