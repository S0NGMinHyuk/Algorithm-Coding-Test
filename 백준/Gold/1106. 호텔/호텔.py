import sys

def solution():
    target, cities = map(int, sys.stdin.readline().split())
    cost_data = []
    for _ in range(cities):
        cost_data.append(list(map(int, sys.stdin.readline().split())))
    
    cost_data.sort(key=lambda x: x[1])

    result = {}
    answer = None

    for cost, customer in cost_data:
        i = cost
        while 1:
            if i not in result:
                result[i] = 0
            if i-cost not in result:
                result[i-cost] = 0

            result[i] = max(result[i], result[i-cost] + customer)
            if result[i] >= target:
                if answer == None or i < answer:
                    answer = i
                break
            i += 1
        
    return answer

print(solution())