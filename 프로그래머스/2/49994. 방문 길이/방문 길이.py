def solution(dirs):
    answer = set()
    pos = [0, 0]        # 현재 위치의 x좌표, y좌표
    for move in dirs:   # dirs의 방향대로 움직이기
        if move == "L" and pos[0] > -5:
            # 양 방향의 진행을 모두 answer에 추가
            answer.add((pos[0], pos[1], pos[0]-1, pos[1]))
            answer.add((pos[0]-1, pos[1], pos[0], pos[1]))
            pos[0] -= 1
        elif move == "R" and pos[0] < 5:
            answer.add((pos[0], pos[1], pos[0]+1, pos[1]))
            answer.add((pos[0]+1, pos[1], pos[0], pos[1]))
            pos[0] += 1
        elif move == "U" and pos[1] < 5:
            answer.add((pos[0], pos[1], pos[0], pos[1]+1))
            answer.add((pos[0], pos[1]+1, pos[0], pos[1]))
            pos[1] += 1
        elif move == "D" and pos[1] > -5:
            answer.add((pos[0], pos[1], pos[0], pos[1]-1))
            answer.add((pos[0], pos[1]-1, pos[0], pos[1]))
            pos[1] -= 1
            
    return len(answer)//2   # answer 집합의 요소 개수 리턴 (양방향이 모두 있으니 2로 나누기)