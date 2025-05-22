from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    l = [i for i in range(1, n+1)]
    candidate = list(combinations(l, 5))    # 가능한 모든 조합 생성
    
    for c in candidate:                     # 하나씩 대조해보기
        for i in range(len(q)):
            c = set(c)
            cnt = 0
            for n in q[i]:
                if n in c:
                    cnt += 1
            if cnt != ans[i]:   # 일치하는 개수가 틀린 경우
                break
        else:   # 모든 조건을 만족한 경우 (정답 조합)
            answer += 1        
    
    return answer 