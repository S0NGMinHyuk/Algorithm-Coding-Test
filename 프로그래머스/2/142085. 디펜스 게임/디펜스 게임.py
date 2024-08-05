# 힙 자료구조 사용
from heapq import heappush, heappop

def solution(n, k, enemy):
    clear = []  # 클리어한 스테이지 배열
    
    for stage in range(len(enemy)):
        # 라운드를 무적권 없이 클리어하기
        heappush(clear, -enemy[stage])
        n -= enemy[stage]
        
        if n < 0:           # 모든 병사를 다 쓴 경우
            if k > 0:       # 클리어한 스테이지 중 적이 가장 많았던 스테이지를 무적권 사용
                n -= heappop(clear)
                k -= 1
            else:           # 무적권이 없다면 종료
                return stage
    # 모든 스테이지를 통과한 경우
    else:
        return len(enemy)