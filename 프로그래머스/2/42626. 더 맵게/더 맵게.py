# 힙 자료구조 사용
from heapq import heappush, heappop, heapify

def solution(scoville, K):
    # scoville 리스트를 힙 리스트로 변환
    heapify(scoville)
    
    cooking = 0
    # 가장 덜 매운 음식의 스코빌 지수가 K 미만이면 새 요리 생성
    while scoville[0] < K:
        if len(scoville) == 1:  # 새 요리를 만들지 못하는 경우
            return -1
        first = heappop(scoville)
        second = heappop(scoville)
        heappush(scoville, first+second*2)
        cooking += 1 # 요리 생성 횟수 1 증가
    
    return cooking