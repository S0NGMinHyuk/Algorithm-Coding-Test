# 탐욕 알고리즘 사용
def solution(name):
    answer = 0
    move = len(name) - 1
    for i, eng in enumerate(name):
        answer += min([ord(eng) - ord("A"), ord("Z") - ord(eng) + 1])

        nextA = i+1
        while nextA < len(name) and name[nextA] == "A":
            nextA += 1
        
        # 현재값, 오른쪽>왼쪽, 왼쪽>오른쪽 중 최소 무빙 횟수 저장
        move = min([move, 2*i + len(name) - nextA, 2*(len(name) - nextA) + i])

    return answer + move