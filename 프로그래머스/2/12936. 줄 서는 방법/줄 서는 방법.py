def solution(n, k):
    lineup = set()  # 이미 줄에 선 사람 집합. (검색 시간복잡도 O(1))
    answer = [0]*n  # 정답 배열 생성
    for index in range(n):
        amount = factorial(n-index-1)   # 현재 인덱스 이후 인덱스 자리에 올 수 있는 경우의 수
        for man in range(1, n+1):
            if man not in lineup:       # 줄 서지 않은 사람 중 탐색
                if k > amount:          
                    k -= amount
                else:
                    answer[index] = man
                    lineup.add(man)
                    break
    return answer

# 팩토리얼 계산 함수
def factorial(n):
    answer = 1
    for i in range(1, n+1):
        answer*= i
    return answer