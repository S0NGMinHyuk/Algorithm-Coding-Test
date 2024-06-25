from collections import deque   # 큐 자료구조 사용

def solution(cacheSize, cities):
    # 캐시사이즈가 0일 경우 예외처리
    if cacheSize == 0:
        return len(cities) * 5
    
    answer = 0
    cache = deque([])
    for city in cities:
        city = city.upper()             # 모든 도시 이름을 대문자로 통일
        if city not in cache:           # city가 cache에 없을 경우
            answer += 5
            if len(cache) == cacheSize: # cache가 꽉 찬 경우 가장 오래된 city 제거
                cache.popleft()
            cache.append(city)          # cache에 현재 city 추가
        else:
            answer += 1
            cache.remove(city)          # cache에 있는 기존 city 제거
            cache.append(city)          # cache의 맨 뒤에 다시 city 추가

    return answer
    # 이거 효율성테스트 괜찮나...?