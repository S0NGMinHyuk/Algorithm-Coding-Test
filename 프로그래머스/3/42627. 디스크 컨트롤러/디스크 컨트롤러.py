# 힙 자료구조 사용
from heapq import heappop, heappush

def solution(jobs):
    heap = []
    result, now= 0, 0   # 총 소요시간, 현재시간 변수
    jobs.sort()         # 작업이 요청되는 시간을 기준으로 오름차순 정렬
    
    for job in jobs:
        # 새 작업을 하기 전 시간이 남고 미뤄둔 작업이 있는 경우, 가장 빨리 끝나는 작업을 실행
        while now <= job[0] and heap:
            running, start = heappop(heap)
            now += running
            result += now-start
        # 미뤄둔 작업이 없고, 새 작업을 시작할 수 있으면 실행
        if now <= job[0]:
            now = sum(job)
            result += job[1]
        # 새 작업을 시작할 수 없으면 미루기
        else:
            heappush(heap, job[::-1])
    
    # 미뤄둔 작업을 가장 빨리 끝나는 순서대로 실행
    while len(heap) > 0:
        running, start = heappop(heap)
        now += running
        result += now-start
    
    # 평균 소요시간을 리턴
    return result//len(jobs)
            
    