def solution(k, tangerine):
    # 각 사이즈의 귤이 몇개씩 있는지 저장하는 딕셔너리 자료형 생성
    quantity = dict()
    for i in tangerine:
        if i in quantity:
            quantity[i] += 1
        else:
            quantity[i] = 1
    
    # 가장 많이 있는 사이즈부터 상자에 담으며 k개 이상 담으면 사이즈 개수 리턴
    for i, num in enumerate(sorted(quantity.values(), reverse=True)):
        k -= num
        if k <= 0:
            return i + 1
    else:
        return len(quantity.keys())