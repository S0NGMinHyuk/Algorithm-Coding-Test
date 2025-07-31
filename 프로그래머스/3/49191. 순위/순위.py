from collections import deque


def solution(n, results):
    answer = 0
    table = getTable(results)   # 승부 결과를 딕셔너리로 변환
    for i in range(1, n+1):     # 각 선수별로 순위를 알 수 있는지 검사
        if promissing(i, n, table):
            answer += 1
    return answer


def getTable(results):  # 각 선수별 [[나를 이긴 선수], [내가 이긴 선수]] 형태로 결과 저장
    table = dict()
    for w, l in results:
        if w not in table:
            table[w] = [[], [l]]
        else:
            table[w][1].append(l)
        if l not in table:
            table[l] = [[w], []]
        else:
            table[l][0].append(w)
    return table


def promissing(me, n, table):  # 내가 순위를 정확히 알 수 있는지 리턴
    matcher = [0] * (n+1)
    matcher[me] = 1
    
    q = deque([me])
    while q:    # 자신을 이긴 선수들을 계속 타고 올라가기
        man = q.popleft()
        if man not in table:
            continue
        for enemy in table[man][0]:
            if matcher[enemy] == 0:
                matcher[enemy] = 1
                q.append(enemy)
    
    q = deque([me])
    while q:    # 자신이 이긴 선수들을 계속 타고 내려가기
        man = q.popleft()
        if man not in table:
            continue
        for enemy in table[man][1]:
            if matcher[enemy] == 0:
                matcher[enemy] = 1
                q.append(enemy)
    return sum(matcher) == n    # 내가 모든 선수와 매치 결과를 아는지 리턴