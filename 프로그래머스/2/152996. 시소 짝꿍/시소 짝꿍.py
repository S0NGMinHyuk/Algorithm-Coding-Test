def solution(weights):
    # 각 몸무게를 가진 사람이 몇명인지 딕셔너리 자료형에 저장
    man_dict = dict()
    for w in weights:
        man_dict[w] = 1 if w not in man_dict else man_dict[w]+1
    
    duo = 0                         # 시소 짝꿍 개수
    available = [3/2, 4/2, 4/3]     # 나보다 무거운 사람 중 나와 짝이 될 수 있는 비율
    
    # 가벼운 사람부터 시작해서 시소 짝궁 찾기
    for man in sorted(man_dict.keys()): 
        if man_dict[man] > 1:   # 나와 같은 몸무게가 2명 이상인 경우
            duo += man_dict[man] * (man_dict[man]-1) / 2
        
        for av in available:    # 시소 거리에 따라 짝이 될 수 있는 사람이 있는 경우
            if man*av in man_dict:
                duo += man_dict[man*av] * man_dict[man]
    
    return duo
    