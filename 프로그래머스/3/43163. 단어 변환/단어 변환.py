# 선입선출 큐 자료구조 사용
from collections import deque

def solution(begin, target, words):
    answer = 0
    used = {begin: 0}
    q = deque([begin])
    
    while len(q) > 0:   # BFS 알고리즘
        now = q.popleft()
        if now == target:
            answer = used[now]
            break
        
        for word in words:
            # 아직 사용하지 않았고, now에서 변환이 가능한 word라면 q에 추가
            if word not in used and isConvertable(now, word):
                used[word] = used[now] + 1
                q.append(word)
    
    return answer

# word1에서 word2로 변환이 가능한지 검사하는 함수
def isConvertable(word1, word2):
    chance = 1
    for a, b in zip(word1, word2):
        if a != b:
            if chance > 0:
                chance -= 1
            else:
                return False
    return True