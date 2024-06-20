import heapq    # 힙 자료구조 사용

def solution(n, works):
    answer = 0
    heap = []
    for work in works:  # works 리스트를 힙 자료구조에 저장
        heapq.heappush(heap, work*-1)
    
    for _ in range(n):  # 가장 작업량이 큰 일을 1시간만큼 처리 <- n번 반복
        work = heapq.heappop(heap)
        work += 1
        heapq.heappush(heap, work)
    
    for i in heap:      # 남은 작업량에 대해 야근지수 계산
        if i < 0:
            answer += i**2
    
    return answer