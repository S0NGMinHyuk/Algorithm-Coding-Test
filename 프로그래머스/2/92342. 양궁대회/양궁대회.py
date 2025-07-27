def solution(n, info):
    answer = backtracking(n, info, [])
    return answer[0] if answer[1] > 0 else [-1]


def backtracking(arrow, enemy, me): # 백트래킹으로 최적의 경우 찾기
    if len(me) == 11:   # base case
        me[-1] = arrow  # 남은 화살 다 털고,
        return [me, getScore(me, enemy)]    # 현재 점수판과 점수차이를 리턴
    
    if arrow > enemy[len(me)]: # 이길 수 있는 경우 중 
        use = enemy[len(me)] + 1
        win = backtracking(arrow - use, enemy, me + [use])  # 이기는 경우
        lose = backtracking(arrow, enemy, me + [0])         # 지는 경우
        result = compare(win, lose) # 둘 중 최적의 경우를 result로 선정
    else:
        result = backtracking(arrow, enemy, me + [0])       # 지는 경우
    
    return result


def getScore(me, enemy):    # 어피치와의 점수차이 리턴
    score = 0
    for i in range(11):
        if me[i] > enemy[i]:
            score += 10 - i
        elif me[i] < enemy[i]:
            score -= 10 - i
    return score


def compare(a, b):  # a 기록과 b 기록 중 더 나은 것을 리턴
    if a[1] > b[1]:
        return a
    elif a[1] < b[1]:
        return b
    else:
        for i in range(10, -1, -1):
            if a[0][i] > b[0][i]:
                return a
            elif a[0][i] < b[0][i]:
                return b