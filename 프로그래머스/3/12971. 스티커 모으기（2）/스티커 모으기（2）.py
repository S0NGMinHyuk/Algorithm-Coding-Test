def solution(sticker):
    # 스티커가 한장일 경우 예외처리
    if len(sticker) == 1:
        return sticker[0]
    
    # 첫 번째 스티커로 시작하는 경우와 두 번째 스티커로 시작하는 경우 중 더 큰 값 리턴
    return max(stickerCollect(sticker[:-1]), stickerCollect(sticker[1:]))

# DP 알고리즘 사용
def stickerCollect(sticker):
    if len(sticker) > 2:
        sticker[2] += sticker[0]
    
    # 현재 인덱스 스티커를 사용하며 만들 수 있는 최대값을 저장
    for i in range(3, len(sticker)):
        sticker[i] += max(sticker[i-2], sticker[i-3])
    
    return max(sticker) # 최대값 리턴