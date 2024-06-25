import math # 올림 함수 ceil()을 사용하기 위해 호출

def solution(n, words):
    storage = set([words[0]])   # 끝말잇기에 사용된 단어 저장
    for i in range(1, len(words)):
        # 처음 나오는 단어이며 이전 단어와 끝말잇기일 경우
        if words[i] not in storage and words[i][0] == words[i-1][-1]:
            storage.add(words[i])
        else:
            return [i % n + 1, math.ceil((i + 1) / n)]  # 실패한 사람의 번호와 차례 리턴
    else:
        return [0, 0]   # 탈락자가 없다면 [0, 0] 리턴