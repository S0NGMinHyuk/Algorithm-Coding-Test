def solution(keymap, targets):
    # 각 알파벳 별 최소 클릭 횟수를 가지는 해시테이블 생성
    hashTable = {}
    for key in keymap:
        for i, alphabet in enumerate(key):
            if alphabet not in hashTable:   # 처음 나오는 알파벳인 경우
                hashTable[alphabet] = i+1
            else:                           # 이미 있는 알파벳인 경우
                if hashTable[alphabet] > i+1:
                    hashTable[alphabet] = i+1
    
    # targets 문자열을 몇 번 눌러야 하는지 검사
    result = []
    for target in targets:
        cnt = 0
        for alphabet in target:
            if alphabet in hashTable:   # 해시테이블에 있는 알파벳인 경우
                cnt += hashTable[alphabet]
            else:                       # 해시테이블에 없는 알파벳인 경우
                result.append(-1)
                break
        else:                           # 모든 알파벳이 해시테이블에 있는 경우
            result.append(cnt)
    
    return result