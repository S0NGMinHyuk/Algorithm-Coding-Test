import sys

def solution():
    # 초기 입력값 저장
    target, cities = map(int, sys.stdin.readline().split())
    cost_data = []
    for _ in range(cities):
        cost_data.append(list(map(int, sys.stdin.readline().split())))

    # 배열의 길이를 알 수 없어 딕셔너리 사용
    data = {}
    answer = None

    for cost, customer in cost_data:
        i = cost
        while 1:
            # DP에 사용할 값이 없다면 0으로 생성
            if i not in data:
                data[i] = 0
            if i-cost not in data:
                data[i-cost] = 0

            # DP 로직으로 i 만큼 돈을 쓸 때 최대로 홍보할 수 있는 사람 수 갱신
            data[i] = max(data[i], data[i-cost] + customer)
            
            # 원하는 사람 이상 홍보했다면 answer 갱신 후 while문 탈출
            if data[i] >= target:
                if answer == None or i < answer:
                    answer = i
                break

            # cost 1씩 증가
            i += 1
        
    return answer

print(solution())