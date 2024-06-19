# 현재 인덱스를 뺀 3가지 칸 중 가장 큰 경우를 채택. DP..?
# 탐욕 알고리즘이 아니었다.
def solution(land):
    answer = [0, 0, 0, 0]
    for row in land:
        temp = [0, 0, 0, 0]
        for i in range(4):
            temp[i] = row[i] + max_except_me(i, answer)
        answer = list(temp)
    return max(answer)

# lst에서 i번째 값을 제외한 최대값 리턴
def max_except_me(i, lst):
    answer = 0
    for j in range(len(lst)):
        if i == j:
            continue
        answer = lst[j] if lst[j] > answer else answer
    return answer