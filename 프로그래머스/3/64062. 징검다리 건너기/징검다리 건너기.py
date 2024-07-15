# 이분 탐색 알고리즘
def solution(stones, k):
    # 징검다리 숫자 중 k칸만큼 뛰며 넘어갈 수 있는 가장 큰 숫자를 이분탐색을 통해 찾는다.
    # 이분탐색을 사용하는 근거는 stones 배열 내 원소 크기가 최대 2천만이기 때문 (매우 크다)
    start = 0
    end = max(stones)

    while start <= end:
        # 이분탐색 알고리즘의 중앙값, mid명만큼 지나가는 게 최대라는 가정
        mid = (start+end) // 2  
        count = 0               # 한 번에 건너뛰는 징검다리 수

        for i in stones:
            if count < k:
                if i-mid > 0:   # 가라앉지 않는 징검다리
                    count = 0
                else:           # 가라앉는 징검다리
                    count += 1 
            else:
                break

        if count < k:   # 무사히 건넌 경우
            start = mid+1
        else:           # mid명 만큼 못 건넌 경우
            end = mid-1
    
    return start