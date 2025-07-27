def solution(cap, n, deliveries, pickups):
    answer = 0
    deli_head = getHead(deliveries, len(deliveries)-1)  # 가장 먼 배달, 수거 좌표 저장
    pick_head = getHead(pickups, len(pickups)-1)
    
    while deli_head != -1 or pick_head != -1:            # 모든 배달과 수거를 완료할때까지
        answer += (max(deli_head, pick_head) + 1) * 2    # 이동거리는 둘 중 더 먼곳x2
        deliveries = process(deliveries, cap, deli_head) # 가장 먼 곳부터 배달 및 수거하기
        pickups = process(pickups, cap, pick_head)
        
        deli_head = getHead(deliveries, deli_head)  # 가장 먼 배달, 수거 좌표 갱신
        pick_head = getHead(pickups, pick_head)
        
    return answer


def getHead(arr, index):
    for i in range(index, -1, -1):  # 가장 먼 곳부터 배달, 수거하며
        if arr[i] > 0:
            return i
    return -1


def process(arr, cap, index):
    for i in range(index, -1, -1):
        if cap == 0:
            break
        
        if arr[i] > cap:
            arr[i] -= cap
            cap = 0
        else:
            cap -= arr[i]
            arr[i] = 0
            
    return arr