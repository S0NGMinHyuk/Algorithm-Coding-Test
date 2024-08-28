def solution(tickets):
    data = makeGraph(tickets)
    result = dfs(data, ["ICN"], len(tickets))
    return sorted(result)[0]    # 여행 동선 중 알파벳 순서가 앞서는 경로 반환


def dfs(data, travel, n):
    # 모든 항공권을 사용한 경우 / Base Case
    if len(travel) > n: 
        return [travel]
    
    # 여행 가능한 동선을 저장하는 리스트
    result = []                 
    
    # 현재 출발지에서 갈 수 있는 도착지 정보를 담은 리스트
    backup = data[travel[-1]] if travel[-1] in data else []   
    
    for i in range(len(backup)):
        data[travel[-1]] = backup[:i] + backup[i+1:]    # i번째 도착지로 향하는 티켓 삭제
        result += dfs(data, travel+[backup[i]], n)      # i번째 도착지를 출발지로 재귀 호출
        data[travel[-1]] = backup                       # i번째 도착지로 향하는 티켓 복구
        
    return result   # 여행 가능한 동선을 리턴


# key = 출발지, value = [도착지,] 형태의 딕셔너리 생성 함수
def makeGraph(tickets):
    graph = dict()
    for a, b in tickets:
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
    return graph