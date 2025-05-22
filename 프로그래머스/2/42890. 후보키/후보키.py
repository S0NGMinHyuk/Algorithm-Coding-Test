from itertools import combinations

def solution(relation):
    answer = []
    l = [n for n in range(len(relation[0]))]
    
    for key_count in range(1, len(relation)+1):
        key = list(combinations(l, key_count))
        
        for k in key:
            unique = True
            for ans in answer:
                cnt = 0
                for i in ans:
                    if i in k:
                        cnt += 1
                if cnt == len(ans):
                    unique = False
            if not unique:
                continue
                
            recordSet = set()
            for r in relation:
                record = []
                for num in k:
                    record.append(r[num])
                recordSet.add(tuple(record))
            if len(recordSet) == len(relation):
                answer.append(k)
    return len(answer)
    