def solution(friends, gifts):
    # 친구 이름을 숫자로 변경
    dict = {}
    for i in range(len(friends)):
        dict[friends[i]] = [i, 0]

    # 선물을 준 기록을 2차원 배열로 정리
    table = [[0] * len(friends) for _ in range(len(friends))]
    for gift in gifts:
        a, b = gift.split()
        table[dict[a][0]][dict[b][0]] += 1

        # 선물지수 갱신
        dict[a][1] += 1
        dict[b][1] -= 1
    
    # 각 friend마다 다음달에 받을 선물 개수(cnt)를 계산
    answer = 0
    for a in friends:
        cnt = 0
        for b in friends:
            if a == b : continue
            elif table[dict[a][0]][dict[b][0]] > table[dict[b][0]][dict[a][0]]:
                cnt += 1
            elif table[dict[a][0]][dict[b][0]] == table[dict[b][0]][dict[a][0]]:
                if dict[a][1] > dict[b][1]:
                    cnt += 1
        answer = cnt if cnt > answer else answer
    
    return answer