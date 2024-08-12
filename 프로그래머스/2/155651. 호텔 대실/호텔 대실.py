def solution(book_time):
    # 힙 자료구조 사용
    from heapq import heappush, heappop
    
    book_time.sort()    # 예약 순서를 오름차순으로 정렬
    maxlen = 0          # 필요한 방의 개수
    rooms = []          # 현재 고객이 사용중인 방의 종료시간을 담은 배열
    
    for booking in book_time:
        # HH:MM 시간을 분으로 변경
        start, end = convertTime(booking[0]), convertTime(booking[1])
        
        # 사용이 종료된 방은 rooms에서 제거
        while len(rooms) > 0 and rooms[0] + 10 <= start:
            heappop(rooms)
        
        # 현재 고객을 rooms에 추가 및 필요한 방의 개수 갱신
        heappush(rooms, end)
        maxlen = max(maxlen, len(rooms))
    
    return maxlen
 
# HH:MM 시간을 분으로 변경하는 함수
def convertTime(time):
    time = list(map(int, time.split(":")))
    return time[0]*60 + time[1]