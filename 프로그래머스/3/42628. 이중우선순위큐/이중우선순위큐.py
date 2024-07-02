# 힙 자료구조 사용
from heapq import heappush, heappop

def solution(operations):
    # 현재 남은 숫자를 저장할 집합과 오름차순, 내림차순 큐 선언
    numbers = set()
    heap_small, heap_big = [], []
    
    for op in operations:
        command, n = op.split(" ")
        # 삭제 명령어이며 삭제할 숫자가 있는 경우
        if command == "D" and len(numbers) > 0:
            if n == "1":
                while 1:
                    # 최대값 삭제
                    check = heappop(heap_big) * (-1)
                    if check in numbers:
                        numbers.discard(check)
                        break
            elif n == "-1":
                while 1:
                    # 최소값 삭제
                    check = heappop(heap_small)
                    if check in numbers:
                        numbers.discard(check)
                        break
        # 힙과 집합에 숫자 추가
        elif command == "I":
            n = int(n)
            numbers.add(n)
            heappush(heap_small, n)
            heappush(heap_big, n*(-1))
    
    # 집합의 최대, 최소값 리턴. 집합이 비어있다면 [0, 0] 리턴
    return [max(numbers), min(numbers)] if len(numbers) > 0 else [0,0]