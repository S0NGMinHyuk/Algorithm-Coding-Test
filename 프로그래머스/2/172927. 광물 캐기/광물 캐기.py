def solution(picks, minerals):
    return dfs(picks, minerals)


def dfs(picks, minerals):
    # 모든 광물을 캤거나 곡괭이를 다 쓴 경우
    if len(minerals) == 0 or sum(picks) == 0:
        return 0
    
    answer = []
    for i in range(3):
        # 각 곡괭이를 사용한 경우를 재귀호출 (완전탐색)
        if picks[i] > 0:
            picks[i] -= 1
            answer.append(dfs(picks, minerals[5:]) + getWork(i, minerals[:5]))
            picks[i] += 1
    
    return min(answer)

# arr 배열을 i 곡괭이로 캘 때 피로도를 리턴하는 함수
def getWork(i, arr):
    # 다이아곡괭이
    if i == 0:              
        work = len(arr)
    # 철곡괭이
    elif i == 1:
        work = 0
        for mineral in arr:
            work += 5 if mineral == "diamond" else 1
    # 돌곡괭이
    else:
        work = 0
        for mineral in arr:
            if mineral == "diamond": 
                work += 25
            elif mineral == "iron":
                work += 5
            else:
                work += 1
    
    return work        