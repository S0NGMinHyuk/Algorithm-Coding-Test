def solution(genres, plays):
    dict = {}
    # dict[장르 이름] = [전체 재생횟수, [곡 번호, 재생횟수], [곡 번호, 재생횟수]...] 형태로 저장
    for i in range(len(plays)):
        if genres[i] not in dict:
            dict[genres[i]] = [plays[i], [[i, plays[i]]]]
        else:
            dict[genres[i]][0] += plays[i]
            dict[genres[i]][1].append([i, plays[i]])
    
    # 가장 많이 들은 장르 순으로 정렬
    value = sorted(dict.values(), key = lambda x : -x[0])  

    # 해당 장르의 가장 많이 들은 곡 최대 2개를 answer에 추가
    answer = []
    for trash, lst in value:
        if len(lst) == 1:                   # 장르의 곡이 1개면 1개만 추가
            answer.append(lst[0][0])
            continue
        lst.sort(key = lambda x : -x[1])    # 많이 들은 순서대로 재정렬 후 2개 추가
        for i in range(2):
            answer.append(lst[i][0])
    
    return answer
    
