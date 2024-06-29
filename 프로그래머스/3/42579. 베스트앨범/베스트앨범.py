def solution(genres, plays):
    dict = {}
    for i in range(len(plays)):
        if genres[i] not in dict:
            dict[genres[i]] = [plays[i], [[i, plays[i]]]]
        else:
            dict[genres[i]][0] += plays[i]
            dict[genres[i]][1].append([i, plays[i]])
    
    answer= []
    value = sorted(dict.values(), key = lambda x : -x[0])
    for trash, lst in value:
        if len(lst) == 1:
            answer.append(lst[0][0])
            continue
        lst.sort(key = lambda x : -x[1])
        for i in range(2):
            answer.append(lst[i][0])
    
    return answer
    