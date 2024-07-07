def solution(people, limit):  
    people.sort()   # 몸무게 기준 내림차순 정렬
    left, right = 0, len(people)-1 # 투포인터 사용
    boat = 0        # 필요한 보트 개수
    while left <= right:
        # 2명을 태우는 경우
        if people[right] + people[left] <= limit:   
            right -= 1
            left += 1
        # 1명만 태우는 경우
        else:                                      
            right -= 1
        boat += 1
    return boat