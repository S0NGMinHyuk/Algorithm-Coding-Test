def solution(skill, skill_trees):
    answer = 0 
    # key는 스킬 이름, value는 배우는 레벨을 가진 딕셔너리 생성
    skill_level = {s: i for i, s in enumerate(skill)}
    skill = set(skill)
    
    for tree in skill_trees:
        level = 0   # 현재 레벨
        for s in tree:
            if s in skill_level:    # 스킬트리의 스킬이 나왔을 때
                if level >= skill_level[s]: # 배울 수 있다면 레벨 1 증가
                    level += 1
                else:               # 배울 수 없다면 break
                    break
        else:   # 모든 스킬을 배운 경우 answer 1 증가
            answer += 1       
    
    return answer