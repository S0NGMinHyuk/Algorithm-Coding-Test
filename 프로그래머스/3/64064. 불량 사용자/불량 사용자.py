def solution(user_id, banned_id):
    # dfs 알고리즘 사용
    answer = dfs(user_id, banned_id, 0, set())
    return len(answer)

# banned_id를 만족하는 조합을 찾는 dfs 함수
def dfs(user_id, banned_id, index, union):
    # union이 banned_id를 만족하는 조합인 경우, (base case)
    # 조합을 담은 집합 리턴. (중복 방지를 위해 정렬하고 리턴)
    if index == len(banned_id):
        return {tuple(list(sorted(union)))} 
    
    answer = set()
    # 모든 user_id에 대해 banned_id[index]에 적합하고 기존 union에 없었다면,
    # union에 추가 후 dfs 재귀호출
    for i in range(len(user_id)):
        if i not in union and len(user_id[i]) == len(banned_id[index]):
            for u, b in zip(user_id[i], banned_id[index]):
                if b != "*" and u != b:
                    break
            else:
                union.add(i)
                # dfs 결과 집합을 answer에 추가
                answer |= dfs(user_id, banned_id, index+1, union)
                union.discard(i)
                
    # 결과집합 리턴
    return answer
                
        