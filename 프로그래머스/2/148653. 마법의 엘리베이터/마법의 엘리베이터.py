def solution(storey):
    # 버튼 클릭 횟수
    stone = 0    
    
    # 1의 자리 수가 4 이하면 내려가고, 6 이상이면 올라가기
    while storey > 0:
        storey, layer = divmod(storey, 10)
        if layer < 5:
            stone += layer
        elif layer > 5:
            stone += 10 - layer
            storey += 1
        else:   # 1의 자리 수가 5인 경우, 십의 자리 수가 5 이상이면 올리기
            stone += layer
            if storey % 10 >= 5:
                storey += 1
    
    # 버튼 클릭 횟수 리턴
    return stone