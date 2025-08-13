from itertools import permutations

def solution(n, weak, dist):
    def createRoad(start):
        left = weak[:start]
        right = weak[start:]
        for i in range(len(left)):
            left[i] += n
        return right + left
    
    def createOrder():
        order = [[]]
        for i in range(1, len(dist)+1):
            order.append(list(permutations(dist, i)))
        return order
    
    answer = len(dist) + 1
    order = createOrder() # 1명부터 모든 친구를 쓰는 순서를 담은 배열
    for start in range(len(weak)):
        road = createRoad(start) # start 인덱스부터 출발하는 길을 만드는 함수
        for using in range(1, len(order)):  # using 만큼 친구를 쓰는 경우
            for friends in order[using]:    # 특정 배열의 경우
                index = 0    # friends 내 친구 인덱스
                position = 0 # 현재 취약점 위치
                ability = friends[index] # 현재 친구가 갈 수 있는 거리
                while position < len(road)-1:
                    if road[position+1] - road[position] <= ability: # 현재 친구가 갈 수 있는 경우
                        ability -= road[position+1] - road[position]
                    else:   # 현재 친구가 못가는 경우, 다음 친구로 변경
                        index += 1
                        if index == len(friends): # 남은 친구가 없는 경우
                            break
                        ability = friends[index]
                    position += 1 # 다음 외벽으로 이동

                if position == len(road) - 1:   # 취약 지점을 모두 검사한 경우
                    answer = min(answer, using) # answer 갱신
        
    return -1 if answer > len(dist) else answer