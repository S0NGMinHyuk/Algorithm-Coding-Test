from collections import deque

n = int(input())
card = deque(list(range(1, n+1)))   # 카드뭉치 생성

toggle = True           # true 일때 윗장 버리기, false 일 떄 윗장 아래로 내리기
while len(card) > 1:    # 한 장이 남을 때까지 실행
    if toggle:          
        card.popleft()  # 윗장 제거
    else:
        card.append(card.popleft()) # 윗장 아래로 내리기

    toggle = False if toggle else True  # 토글 값 변경

print(card[0])