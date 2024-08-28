# 플루이드 워셜 알고리즘 사용 / 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구하는 알고리즘
def solution(n, s, a, b, fares):
    graph = makeGraph(n, fares)
    result = float("Inf")
    for via in range(1, n+1):
        # s에서 via까지 합승하고, via부터 a, b까지 따로 택시를 탈 때 최소비용을 찾기
        result = min(result, graph[s][via] + graph[via][a] + graph[via][b])
    return result

def makeGraph(n, arr):
    # 가중치가 무한대인 2차원 그래프 생성
    graph = [[float("Inf")]*(n+1) for _ in range(n+1)]
    
    # 자기 자신의 가중치는 0으로 변경
    for i in range(1, n+1):
        graph[i][i] = 0
    
    # 주어진 arr의 가중치를 그래프에 추가
    for a, b, weight in arr:
        graph[a][b] = graph[b][a] = weight
        
    # 플루이드 워셜 알고리즘 사용. 각 지점에서 다른 지점까지의 최소값을 얻는다.
    for via in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = graph[b][a] = min(graph[a][b], graph[a][via]+graph[via][b])
    
    return graph