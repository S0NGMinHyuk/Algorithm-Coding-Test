def solution(n, costs):
    answer = 0                      # 총 건설 비용
    costs.sort(key=lambda x: x[2])  # 건설 비용을 기준으로 오름차순 정렬
    
    linked = 0      # 다리가 생긴 섬 개수
    group = set()   # 연결된 섬 집합
    for info in costs:
        a = getGroup(info[0], group)
        b = getGroup(info[1], group)
        if a == None and b == None:         # 두 섬이 모두 다리가 없다면 두 섬을 집합으로 추가
            group.add((info[0], info[1]))
            linked += 2
        elif a != None and b == None:       # 한 섬에 다리가 있다면 해당 섬의 집합에 다른 섬 추가
            group.remove(a)
            group.add(a + tuple([info[1]]))
            linked += 1
        elif a == None and b != None:       # 한 섬에 다리가 있다면 해당 섬의 집합에 다른 섬 추가
            group.remove(b)
            group.add(b + tuple([info[0]]))
            linked += 1
        else:                               # 양쪽 섬 모두 다리가 있는 경우
            if a == b:                      # 이미 서로 연결된 섬이라면 continue
                continue
            group.remove(a)                 # 서로 연결된 섬이 아니었다면 두 섬의 집합을 합치기
            group.remove(b)
            group.add(a+b)
        answer += info[2]                   # 다리 건설비용 추가
        if linked == n and len(group) == 1: # 모든 섬이 연결되고 한 집합으로 모인 경우
            break
            
    return answer

# group 집합에 target 섬이 있으면 해당 집합을 리턴하는 함수
def getGroup(target, group):
    for g in group:
        if target in g:
            return g
    return None